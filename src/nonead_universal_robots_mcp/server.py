import time

from mcp.server.fastmcp import FastMCP
import json
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import paramiko
import URBasic

# Configure logging
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)
handler = RotatingFileHandler(
    log_dir / "server.log",
    maxBytes=1024 * 1024,  # 1MB
    backupCount=3,  # 保留 3 个旧日志
    encoding="utf-8"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

mcp = FastMCP(
    "nUR_MCP_SERVER",
    description="Control UR robots through the Model Context Protocol"
)

robot_list = None
robotModle_list = None


def set_robot_list():
    global robot_list, robotModle_list
    robot_list = dict()
    robotModle_list = dict()


def link_check(ip):
    """检查连接状态，若连接断开或不存在，则建立连接"""
    if robot_list.get(ip, "unknown") == "unknown" or not robot_list[
        ip].robotConnector.RTDE.isRunning():
        return connect_ur(ip)
    return '连接成功'


def return_msg(txt: str):
    return json.dumps(txt, indent=2, ensure_ascii=False)


def right_pose_joint(current_pose, q):
    """关节的弧度验证，允许0.1的误差,按角度计算大约5度"""
    if q[0] + 0.1 >= current_pose[0] >= q[0] - 0.1:
        if q[1] + 0.1 >= current_pose[1] >= q[1] - 0.1:
            if q[2] + 0.1 >= current_pose[2] >= q[2] - 0.1:
                if q[3] + 0.1 >= current_pose[3] >= q[3] - 0.1:
                    if q[4] + 0.1 >= current_pose[4] >= q[4] - 0.1:
                        if q[5] + 0.1 >= current_pose[5] >= q[5] - 0.1:
                            return True
    return False


def round_pose(pose):
    """给坐标取近似值，精确到三位小数"""
    pose[0] = round(pose[0], 3)
    pose[1] = round(pose[1], 3)
    pose[2] = round(pose[2], 3)
    pose[3] = round(pose[3], 3)
    pose[4] = round(pose[4], 3)
    pose[5] = round(pose[5], 3)
    return pose


def movejConfirm(ip, q):
    """
    movej移动的结果确认
    1：移动到位
    2：移动结束，但是位置不准确
    """
    loop_flg = True
    count = 0
    while loop_flg:
        time.sleep(1)
        current_pose = round_pose(robot_list[ip].get_actual_joint_positions())
        if right_pose_joint(current_pose, q):
            robot_list[ip].robotConnector.DashboardClient.ur_running()
            running = robot_list[ip].robotConnector.DashboardClient.last_respond
            if running == 'Program running: false':
                return 1
        else:
            robot_list[ip].robotConnector.DashboardClient.ur_running()
            running = robot_list[ip].robotConnector.DashboardClient.last_respond

            if running == 'Program running: true':
                # 尚未移动完成
                continue
            else:
                # 移动完成
                count = count + 1
                if count > 5:
                    return 2


def right_pose_tcp(current_pose_1, pose):
    """tcp位置是否一致的校验，这里允许10mm的误差"""
    if pose[0] + 0.010 >= current_pose_1[0] >= pose[0] - 0.010:
        if pose[1] + 0.010 >= current_pose_1[1] >= pose[1] - 0.010:
            if pose[2] + 0.010 >= current_pose_1[2] >= pose[2] - 0.010:
                return True

    return False


def movelConfirm(ip, pose):
    """
    movel移动的结果确认
    1：移动到位
    2：移动结束，但是位置不准确
    """
    loop_flg = True
    count = 0
    while loop_flg:
        time.sleep(1)
        current_pose = round_pose(robot_list[ip].get_actual_tcp_pose())
        if right_pose_tcp(current_pose, pose):
            robot_list[ip].robotConnector.DashboardClient.ur_running()
            running = robot_list[ip].robotConnector.DashboardClient.last_respond
            if running == 'Program running: false':
                return 1
        else:
            robot_list[ip].robotConnector.DashboardClient.ur_running()
            running = robot_list[ip].robotConnector.DashboardClient.last_respond

            if running == 'Program running: true':
                '''尚未移动完成'''
                continue
            else:
                '''移动完成'''
                count = count + 1
                if count > 5:
                    return 2


@mcp.tool()
def connect_ur(ip: str):
    """根据用户提供的IP连接UR
    IP：机器人地址"""
    try:
        host = ip
        global robot_list, robotModle_list

        if robot_list.get(ip, "unknown") != "unknown":
            robot_list[ip].robotConnector.close()
            return return_msg(f"优傲机器人连接失败: {ip}")

        robotModle = URBasic.robotModel.RobotModel()
        robot = URBasic.urScriptExt.UrScriptExt(host=host, robotModel=robotModle)
        robot_list[ip] = robot
        robotModle_list[ip] = robotModle

        if robot_list.get(ip, "unknown") == "unknown" or not robot_list[
            ip].robotConnector.RTDE.isRunning():
            return return_msg(f"优傲机器人连接失败: {ip}")
        robot_list[ip].robotConnector.DashboardClient.ur_is_remote_control()
        remote = robot_list[ip].robotConnector.DashboardClient.last_respond.lower()
        print(f"remote:{remote}")
        if remote != 'true' and not remote.startswith('could not understand'):
            disconnect_ur(ip)
            return return_msg(f"请检查机器人是否处于远程控制模式。IP:{host}")

        return return_msg(f"连接成功。IP:{host}")
    except Exception as e:
        logger.error(f"优傲机器人连接失败: {str(e)}")
        return return_msg(f"优傲机器人连接失败: {str(e)}")


@mcp.tool()
def disconnect_ur(ip: str):
    """根据用户提供的IP，断开与UR机器人的连接
    IP：机器人地址"""
    try:
        if robot_list.get(ip, "unknown") == "unknown":
            return return_msg("连接不存在")
        robot_list[ip].close()
        return return_msg("连接已断开。")
    except Exception as e:
        logger.error(f"连接断开失败: {str(e)}")
        return return_msg(f"连接断开失败: {str(e)}")


@mcp.tool()
def get_serial_number(ip: str):
    """获取指定IP机器人的序列号
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        robot_list[ip].robotConnector.DashboardClient.ur_serial_number()
        return return_msg(
            f"IP为{ip}的优傲机器人的序列号为： {robot_list[ip].robotConnector.DashboardClient.last_respond}")
    except Exception as e:
        logger.error(f"获取序列号失败: {str(e)}")
        return return_msg(f"获取序列号失败: {str(e)}")


@mcp.tool()
def get_time(ip: str) -> str:
    """根据用户提供的IP，获取指定机器人的开机时长(秒)
    IP：机器人地址"""
    try:
        if '连接成功' not in link_check(ip):
            return return_msg(f"与机器人的连接已断开。IP:{ip}")

        return return_msg(f"{robotModle_list[ip].RobotTimestamp():.2f}")
    except Exception as e:
        logger.error(f"获取开机时长失败: {str(e)}")
        return return_msg(f"获取开机时长失败: {str(e)}")


@mcp.tool()
def get_ur_software_version(ip: str):
    """根据用户提供的IP，获取指定机器人的软件版本
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        robot_list[ip].robotConnector.DashboardClient.ur_polyscopeVersion()
        result = robot_list[ip].robotConnector.DashboardClient.last_respond
        return return_msg(f"IP为{ip}的优傲机器人的软件版本是{result}")
    except Exception as e:
        logger.error(f"软件版本获取失败: {str(e)}")
        return return_msg(f"软件版本获取失败: {str(e)}")


@mcp.tool()
def get_robot_model(ip: str):
    """获取指定IP的机器人型号
    IP：机器人地址"""
    try:
        robot_list[ip].robotConnector.DashboardClient.ur_get_robot_model()
        model = robot_list[ip].robotConnector.DashboardClient.last_respond
        robot_list[ip].robotConnector.DashboardClient.ur_is_remote_control()
        e = robot_list[ip].robotConnector.DashboardClient.last_respond.lower()
        if e == 'true' or e == 'false':
            model = f"{model}e"
        return return_msg(model)
    except Exception as e:
        logger.error(f"获取机器人型号失败: {str(e)}")
        return return_msg(f"获取机器人型号失败: {str(e)}")


@mcp.tool()
def get_safety_mode(ip: str):
    """获取指定IP机器人的安全模式
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        robot_list[ip].robotConnector.DashboardClient.ur_safetymode()
        result = robot_list[ip].robotConnector.DashboardClient.last_respond
        return return_msg(f"IP为{ip}的优傲机器人的安全模式是{result}")
    except Exception as e:
        logger.error(f"安全模式获取失败: {str(e)}")
        return return_msg(f"安全模式获取失败: {str(e)}")


@mcp.tool()
def get_robot_mode(ip: str):
    """获取指定IP机器人的运行状态
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        robot_list[ip].robotConnector.DashboardClient.ur_robotmode()
        return return_msg(
            f"IP为{ip}的优傲机器人的运行状态为： {robot_list[ip].robotConnector.DashboardClient.last_respond}")
    except Exception as e:
        logger.error(f"运行状态获取失败: {str(e)}")
        return return_msg(f"运行状态获取失败: {str(e)}")


@mcp.tool()
def get_program_state(ip: str):
    """获取指定IP机器人的程序执行状态
        IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")

        robot_list[ip].robotConnector.DashboardClient.ur_get_loaded_program()
        prog_name = robot_list[ip].robotConnector.DashboardClient.last_respond
        robot_list[ip].robotConnector.DashboardClient.ur_programState()
        prog_state = robot_list[ip].robotConnector.DashboardClient.last_respond
        robot_list[ip].robotConnector.DashboardClient.ur_isProgramSaved()
        flg = robot_list[ip].robotConnector.DashboardClient.last_respond
        robot_list[ip].robotConnector.DashboardClient.ur_running()
        running = robot_list[ip].robotConnector.DashboardClient.last_respond

        prog_saved = ''
        prog_running = ''
        if flg.startswith("false"):
            prog_saved = '程序未保存，请及时保存或备份正在编辑的程序。'
        if running == 'Program running: true':
            prog_running = '机械臂正在动作。'
        return return_msg(
            f"IP为{ip}的优傲机器人当前加载的程序是：{prog_name}，程序的执行状态是：{prog_state}。{prog_saved}。{prog_running}")
    except Exception as e:
        logger.error(f"程序的执行状态获取失败: {str(e)}")
        return return_msg(f"程序的执行状态获取失败: {str(e)}")


@mcp.tool()
def get_actual_tcp_pose(ip: str):
    """获取指定IP机器人的当前TCP位置
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")

        return return_msg(f"当前TCP位置： {robot_list[ip].get_actual_tcp_pose()}")
    except Exception as e:
        logger.error(f"TCP位置获取失败: {str(e)}")
        return return_msg(f"TCP位置获取失败: {str(e)}")


@mcp.tool()
def get_actual_joint_pose(ip: str):
    """获取指定IP机器人的当前关节角度
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"当前关节姿态 {robot_list[ip].get_actual_joint_positions()}")
    except Exception as e:
        logger.error(f"TCP位置获取失败: {str(e)}")
        return return_msg(f"TCP位置获取失败: {str(e)}")


@mcp.tool()
def get_output_int_register(ip: str, index: int):
    """获取指定IP机器人Int寄存器的值,
    IP：机器人地址
    index：寄存器下标，范围是[0，23]"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].OutputIntRegister(index)}")
    except Exception as e:
        logger.error(f"Int寄存器的值获取失败: {str(e)}")
        return return_msg(f"Int寄存器的值获取失败: {str(e)}")


@mcp.tool()
def get_output_double_register(ip: str, index: int):
    """获取指定IP机器人Double寄存器的值,
    IP：机器人地址
    index：寄存器下标，范围是[0，23]"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].OutputDoubleRegister(index)}")
    except Exception as e:
        logger.error(f"Double寄存器的值获取失败: {str(e)}")
        return return_msg(f"Double寄存器的值获取失败: {str(e)}")


@mcp.tool()
def get_output_bit_register(ip: str, index: int):
    """获取指定IP机器人Bool寄存器的值,
    IP：机器人地址
    index：寄存器下标，范围是[0，23]"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        bits = robotModle_list[ip].OutputBitRegister()
        return return_msg(f"{bits[index]}")
    except Exception as e:
        logger.error(f"Bool寄存器的值获取失败: {str(e)}")
        return return_msg(f"Bool寄存器的值获取失败: {str(e)}")


@mcp.tool()
def get_actual_robot_voltage(ip: str):
    """获取指定IP机器人的电压（伏特）
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].ActualRobotVoltage()}（伏特）")
    except Exception as e:
        logger.error(f"机器人的电压获取失败: {str(e)}")
        return return_msg(f"机器人的电压获取失败: {str(e)}")


@mcp.tool()
def get_actual_robot_current(ip: str):
    """获取指定IP机器人的电流（安培）
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].ActualRobotCurrent()}（安培）")
    except Exception as e:
        logger.error(f"机器人的电流获取失败: {str(e)}")
        return return_msg(f"机器人的电流获取失败: {str(e)}")


@mcp.tool()
def get_actual_joint_voltage(ip: str):
    """获取指定IP机器人的各关节电压（伏特）
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].ActualJointVoltage()}（伏特）")
    except Exception as e:
        logger.error(f"机器人的关节电压获取失败: {str(e)}")
        return return_msg(f"机器人的关节电压获取失败: {str(e)}")


@mcp.tool()
def get_actual_joint_current(ip: str):
    """获取指定IP机器人各关节的电流（安培）
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].ActualJointVoltage()}（安培）")
    except Exception as e:
        logger.error(f"机器人各关节的电流获取失败: {str(e)}")
        return return_msg(f"机器人各关节的电流获取失败: {str(e)}")


@mcp.tool()
def get_joint_temperatures(ip: str):
    """获取指定IP机器人各关节的温度（摄氏度）。
    IP：机器人地址"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        return return_msg(f"{robotModle_list[ip].JointTemperatures()}（摄氏度）")
    except Exception as e:
        logger.error(f"机器人各关节的温度获取失败: {str(e)}")
        return return_msg(f"机器人各关节的温度获取失败: {str(e)}")


@mcp.tool()
def get_programs(ip: str, username='root', password='easybot'):
    """获取指定IP机器人的所有程序。
    IP：机器人地址
    username：ssh账号
    password：ssh密码
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=22, username=username, password=password)
        # 创建交互式 shell
        shell = ssh.invoke_shell()
        # 执行多个命令
        shell.send('cd /programs\n')
        shell.send('ls -1\n')
        # 获取输出
        import time
        time.sleep(1)  # 等待命令执行
        output = shell.recv(65535).decode()
        ssh.close()
        files = []
        for file in output.split('\n'):
            name = file.replace(' ', '').replace('\r', '')
            if name.endswith('.urp'):
                files.append(name)
        return return_msg(f"命令已发送：{str(files)}")
    except Exception as e:
        return return_msg(f"程序列表获取失败。{str(e)}")


@mcp.tool()
def send_program_script(ip: str, script: str):
    """发送脚本到指定IP的机器人。
    IP：机器人地址
    script：脚本内容"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        robot_list[ip].robotConnector.RealTimeClient.SendProgram(script)
        return return_msg(f"脚本程序已发送，请确认执行结果。")
    except Exception as e:
        logger.error(f"发送脚本失败: {str(e)}")
        return return_msg(f"发送脚本失败: {str(e)}")


@mcp.tool()
def movej(ip: str, q: dict, a=1, v=1, t=0, r=0):
    """发送新的关节姿态到指定IP的机器人，使每个关节都旋转至指定弧度。
    IP：机器人地址
    q：各关节角度
    a：加速度（米每平方秒）
    v：速度（米每秒）
    t：移动时长（秒）
    r：交融半径（米）"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")

        cmd = f"movej({q},{a},{v},{t},{r})"
        robot_list[ip].movej(q, a, v, t, r)
        result = movejConfirm(ip, q)
        if result == 1:
            return return_msg(f"命令 {cmd} 已发送，移动完成。")
        else:
            return return_msg(f"命令 {cmd} 已发送，移动失败。")
    except Exception as e:
        logger.error(f"发送新的关节姿态到UR机器人失败: {str(e)}")
        return return_msg(f"发送新的关节姿态到UR机器人: {str(e)}")


@mcp.tool()
def movel(ip: str, pose: dict, a=1, v=1, t=0, r=0):
    """发送新的TCP位置到指定IP的机器人，使TCP移动到指定位置，移动期间TCP作直线移动。
    IP：机器人地址
    pose：TCP位置
    a：加速度（米每平方秒）
    v：速度（米每秒）
    t：移动时长（秒）
    r：交融半径（米）"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")

        robot_list[ip].movel(pose, a, v, t, r)
        result = movelConfirm(ip, pose)
        cmd = f"movel(p{pose},{a},{v},{t},{r})"
        if result == 1:
            return return_msg(f"命令 {cmd} 已发送，移动完成。")
        else:
            return return_msg(f"命令 {cmd} 已发送，移动失败。")
    except Exception as e:
        logger.error(f"发送新的TCP位置到指定IP的机器人失败: {str(e)}")
        return return_msg(f"发送新的TCP位置到指定IP的机器人: {str(e)}")


@mcp.tool()
def movel_x(ip: str, distance: float):
    """命令指定IP机器人的TCP沿X轴方向移动
    IP：机器人地址
    distance：移动距离（米）"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        pose = robot_list[ip].get_actual_tcp_pose()
        pose[0] = pose[0] + distance
        robot_list[ip].movel(pose)
        result = movelConfirm(ip, pose)
        cmd = f"movel(p[{'{:.4f}'.format(pose[0])},{'{:.4f}'.format(pose[1])},{'{:.4f}'.format(pose[2])},{'{:.4f}'.format(pose[3])},{'{:.4f}'.format(pose[4])},{'{:.4f}'.format(pose[5])},],0.5,0.25,0,0)"
        if result == 1:
            return return_msg(f"命令 {cmd} 已发送，移动完成。")
        else:
            return return_msg(f"命令 {cmd} 已发送，移动失败。")
    except Exception as e:
        logger.error(f"移动失败: {str(e)}")
        return return_msg(f"移动失败: {str(e)}")


@mcp.tool()
def movel_y(ip: str, distance: float):
    """命令指定IP机器人的TCP沿Y轴方向移动
    IP：机器人地址
    distance：移动距离（米）"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        pose = robot_list[ip].get_actual_tcp_pose()
        pose[1] = pose[1] + distance

        robot_list[ip].movel(pose)
        result = movelConfirm(ip, pose)
        cmd = f"movel(p[{'{:.4f}'.format(pose[0])},{'{:.4f}'.format(pose[1])},{'{:.4f}'.format(pose[2])},{'{:.4f}'.format(pose[3])},{'{:.4f}'.format(pose[4])},{'{:.4f}'.format(pose[5])},],0.5,0.25,0,0)"
        if result == 1:
            return return_msg(f"命令 {cmd} 已发送，移动完成。")
        else:
            return return_msg(f"命令 {cmd} 已发送，移动失败。")
    except Exception as e:
        logger.error(f"移动失败: {str(e)}")
        return return_msg(f"移动失败: {str(e)}")


@mcp.tool()
def movel_z(ip: str, distance: float):
    """命令指定IP机器人的TCP沿Y轴方向移动
    IP：机器人地址
    distance：移动距离（米）"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        pose = robot_list[ip].get_actual_tcp_pose()
        pose[2] = pose[2] + distance
        robot_list[ip].movel(pose)
        result = movelConfirm(ip, pose)
        cmd = f"movel(p[{'{:.4f}'.format(pose[0])},{'{:.4f}'.format(pose[1])},{'{:.4f}'.format(pose[2])},{'{:.4f}'.format(pose[3])},{'{:.4f}'.format(pose[4])},{'{:.4f}'.format(pose[5])},],0.5,0.25,0,0)"
        if result == 1:
            return return_msg(f"命令 {cmd} 已发送，移动完成。")
        else:
            return return_msg(f"命令 {cmd} 已发送，移动失败。")
    except Exception as e:
        logger.error(f"移动失败: {str(e)}")
        return return_msg(f"移动失败: {str(e)}")


@mcp.tool()
def draw_circle(ip: str, center: dict, r: float, coordinate="z"):
    """命令指定IP的机器人，给定圆心位置和半径，在水平或竖直方向画一个圆
        center：圆心的TCP位置
        r：半径（米）
        coordinate：圆所在的平面。z：圆形所在的平面与基座所在平面垂直,其它：圆形所在的平面与基座所在平面平行。默认值：z。"""
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        wp_1 = [center[0], center[1], center[2], center[3], center[4], center[5]]
        wp_2 = [center[0], center[1], center[2], center[3], center[4], center[5]]
        wp_3 = [center[0], center[1], center[2], center[3], center[4], center[5]]
        wp_4 = [center[0], center[1], center[2], center[3], center[4], center[5]]
        cmd = ''
        if coordinate.lower() == "z":
            wp_1[2] = wp_1[2] + r

            wp_2[1] = wp_2[1] + r

            wp_3[2] = wp_3[2] - r

            wp_4[1] = wp_4[1] - r
        else:
            wp_1[0] = wp_1[0] - r

            wp_2[1] = wp_2[1] + r

            wp_3[0] = wp_3[0] + r

            wp_4[1] = wp_4[1] - r

        cmd = (f"movep(p{str(wp_1)}, a=1, v=0.25, r=0.025)\nmovec(p{str(wp_2)}, p{str(wp_3)}, a=1, v=0.25, "
               f"r=0.025, mode=0)\nmovec(p{str(wp_4)}, p{str(wp_1)}, a=1, v=0.25, r=0.025, mode=0)")

        robot_list[ip].robotConnector.RealTimeClient.SendProgram(cmd)
        return return_msg(f"命令已发送：{cmd}")
    except Exception as e:
        logger.error(f"命令发送失败: {str(e)}")
        return return_msg(f"命令发送失败: {str(e)}")


@mcp.tool()
def draw_square(ip: str, origin: dict, border: float, coordinate="z"):
    """给定起点位置和边长，在水平或竖直方向画一个正方形
        origin：画正方形时TCP的起点位置
        border：边长（米）
        coordinate：圆所在的平面。z：圆形所在的平面与基座所在平面垂直,其它：圆形所在的平面与基座所在平面平行。默认值：z。
        """
    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        wp_1 = [origin[0], origin[1], origin[2], origin[3], origin[4], origin[5]]
        wp_2 = [origin[0], origin[1], origin[2], origin[3], origin[4], origin[5]]
        wp_3 = [origin[0], origin[1], origin[2], origin[3], origin[4], origin[5]]
        if coordinate.lower() == "z":
            wp_1[1] = wp_1[1] + border

            wp_2[1] = wp_2[1] + border
            wp_2[3] = wp_2[3] - border

            wp_3[3] = wp_3[3] - border

        else:
            wp_1[1] = wp_1[1] + border

            wp_2[1] = wp_2[1] + border
            wp_2[0] = wp_2[0] + border

            wp_3[0] = wp_3[0] + border

        cmd = (f"movel(p{str(origin)}, a=1, v=0.25)\nmovel(p{str(wp_1)}, a=1, v=0.25)\n"
               f"movel(p{str(wp_2)}, a=1, v=0.25)\nmovel(p{str(wp_3)}, a=1, v=0.25)\n"
               f"movel(p{str(origin)}, a=1, v=0.25)")
        robot_list[ip].robotConnector.RealTimeClient.SendProgram(cmd)
        return return_msg(f"命令已发送：{cmd}")
    except Exception as e:
        logger.error(f"命令发送失败: {str(e)}")
        return return_msg(f"命令发送失败: {str(e)}")


@mcp.tool()
def draw_rectangle(ip: str, origin: dict, width: float, height: float, coordinate="z"):
    """给定起点位置和边长，在水平或竖直方向画一个正方形
            origin：画长方形时TCP的起点位置
            width：长（米）
            height：宽（米）
            coordinate：圆所在的平面。z：圆形所在的平面与基座所在平面垂直,其它：圆形所在的平面与基座所在平面平行。默认值：z。"""

    try:
        if '连接失败' in link_check(ip):
            return return_msg(f"与机器人的连接已断开。")
        wp_1 = [origin[0], origin[1], origin[2], origin[3], origin[4], origin[5]]
        wp_2 = [origin[0], origin[1], origin[2], origin[3], origin[4], origin[5]]
        wp_3 = [origin[0], origin[1], origin[2], origin[3], origin[4], origin[5]]
        if coordinate.lower() == "z":
            wp_1[1] = wp_1[1] + width

            wp_2[1] = wp_2[1] + width
            wp_2[3] = wp_2[3] - height

            wp_3[3] = wp_3[3] - height

        else:
            wp_1[1] = wp_1[1] + width

            wp_2[1] = wp_2[1] + width
            wp_2[0] = wp_2[0] + height

            wp_3[0] = wp_3[0] + height

        cmd = (f"movel(p{str(origin)}, a=1, v=0.25)\nmovel(p{str(wp_1)}, a=1, v=0.25)\n"
               f"movel(p{str(wp_2)}, a=1, v=0.25)\nmovel(p{str(wp_3)}, a=1, v=0.25)\n"
               f"movel(p{str(origin)}, a=1, v=0.25)")
        robot_list[ip].robotConnector.RealTimeClient.SendProgram(cmd)
        return return_msg(f"命令已发送：{cmd}")
    except Exception as e:
        logger.error(f"命令发送失败: {str(e)}")
        return return_msg(f"命令发送失败: {str(e)}")


# Main execution

def main():
    """Run the MCP server"""
    logger.info("Nonead-Universal-Robots-MCP  启动")
    set_robot_list()
    mcp.run()


if __name__ == "__main__":
    main()
