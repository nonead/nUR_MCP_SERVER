from enum import Enum
import json
from time import sleep
from typing import Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from mcp.shared.exceptions import McpError
import paramiko
from pydantic import BaseModel
import URBasic
from URBasic import RobotModel, DashBoard

import sys

sys.stdout.reconfigure(encoding='utf-8')


class URTools(str, Enum):
    CONNECT = "connect_ur"
    DISCONNECT = "disconnect_ur"
    GET_TIME = "get_time"
    GET_SERIAL_NUMBER = "get_serial_number"
    GET_ROBOT_MODEL = "get_robot_model"
    GET_ACTUAL_TCP_POSE = "get_actual_tcp_pose"
    GET_ACTUAL_JOINT_POSE = "get_actual_joint_pose"
    MOVEJ = "movej"
    MOVEL = "movel"
    MOVEL_X = "movel_x"
    MOVEL_Y = "movel_y"
    MOVEL_Z = "movel_z"
    LOAD_URP = "load_urp"
    START_UR = "start_ur"
    STOP_UR = "stop_ur"
    PAUSE_UR = "pause_ur"
    GET_OUTPUT_INT_REGISTER = "get_output_int_register"
    GET_OUTPUT_DOUBLE_REGISTER = "get_output_double_register"
    GET_OUTPUT_BIT_REGISTER = "get_output_bit_register"
    GET_ACTUAL_ROBOT_VOLTAGE = "get_actual_robot_voltage"
    GET_ACTUAL_ROBOT_CURRENT = "get_actual_robot_current"
    GET_ACTUAL_JOINT_VOLTAGE = "get_actual_joint_voltage"
    GET_ACTUAL_JOINT_CURRENT = "get_actual_joint_current"
    GET_ACTUAL_JOINT_TEMPERATURES = "get_joint_temperatures"
    GET_ROBOT_MODE = "get_robot_mode"
    GET_PROGRAM_STATE = "get_program_state"
    GET_UR_SOFTWARE_VERSION = "get_ur_software_version"
    GET_SAFETY_MODE = "get_safety_mode"
    GET_PROGRAMS = "get_programs"
    SEND_PROGRAM_SCRIPT = "send_program_script"
    DRAW_CIRCLE = "draw_circle"
    DRAW_SQUARE = "draw_square"
    DRAW_RECTANGLE = "draw_rectangle"


class CommandResult(BaseModel):
    txt: str


class ConnectionState:
    ERROR = 0
    DISCONNECTED = 1
    CONNECTED = 2
    PAUSED = 3
    STARTED = 4


class URServer:

    def __init__(self):
        self.robot = dict()
        self.robotModle = dict()
        logger = URBasic.dataLogging.DataLogging()
        name = logger.AddEventLogging(__name__)
        self._logger = logger.__dict__[name]

    def get_time(self, ip) -> CommandResult:
        """获取开机时长"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )

        return CommandResult(
            txt=f"{self.robotModle[ip].RobotTimestamp():.2f}"
        )

    def movej(self, ip, q, a=1, v=1, t=0, r=0):
        """发送新的关节姿态到UR机器人"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        cmd = f"movej({q},{a},{v},{t},{r})"
        self.robot[ip].movej(q, a, v, t, r)
        result = self.movejConfirm(ip, q)
        if result == 1:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动完成。"
            )
        else:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动失败。"
            )

    def load_urp(self, ip, name):
        """加载指定UR程序"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        cmd = f"{name}.urp"
        self.robot[ip].robotConnector.DashboardClient.ur_load(cmd)
        return CommandResult(
            txt=self.robot[ip].robotConnector.DashboardClient.last_respond
        )

    def start_ur(self, ip, name):
        """加载并执行指定UR程序"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        cmd = f"{name}.urp"
        self.robot[ip].robotConnector.DashboardClient.ur_load(cmd)
        result = self.robot[ip].robotConnector.DashboardClient.last_respond
        if result.startswith("Loading program:"):
            self.robot[ip].robotConnector.DashboardClient.ur_play()
            return CommandResult(
                txt=self.robot[ip].robotConnector.DashboardClient.last_respond
            )
        else:
            return CommandResult(
                txt=result
            )

    def stop_ur(self, ip):
        """停止执行"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_stop()
        return CommandResult(
            txt=self.robot[ip].robotConnector.DashboardClient.last_respond
        )

    def pause_ur(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_pause()
        return CommandResult(
            txt=self.robot[ip].robotConnector.DashboardClient.last_respond
        )

    def movel(self, ip, pose, a=1, v=1, t=0, r=0):
        """直线移动"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )

        self.robot[ip].movel(pose, a, v, t, r)
        result = self.movelConfirm(ip, pose)
        cmd = f"movel(p{pose},{a},{v},{t},{r})"
        if result == 1:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动完成。"
            )
        else:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动失败。"
            )

    def connect_ur(self, ip):
        """连接UR"""
        host = ip

        if self.robot is None:
            self.robot = dict()
            self.robotModle = dict()

        if self.robot.get(ip, "unknown") != "unknown":
            self.robot[ip].close()

        robotModle = URBasic.robotModel.RobotModel()
        robot = URBasic.urScriptExt.UrScriptExt(host=host, robotModel=robotModle)
        self.robot[ip] = robot
        self.robotModle[ip] = robotModle

        # if self.robot.get(ip, "unknown") == "unknown" or not self.robot[
        #     ip].robotConnector.RealTimeClient.IsRtcConnected() or self.robot[
        #     ip].robotConnector.DashboardClient.dbs_is_running() or self.robot[
        #     ip].robotConnector.RTDE.isRunning():
        #     return CommandResult(
        #         txt=f"连接失败。IP:{host}"
        #     )
        self.robot[ip].robotConnector.DashboardClient.ur_is_remote_control()
        remote = self.robot[ip].robotConnector.DashboardClient.last_respond.lower()
        print(f"remote:{remote}")
        if remote != 'true' and not remote.startswith('could not understand'):
            self.disconnect_ur(ip)
            return CommandResult(
                txt=f"请检查机器人是否处于远程控制模式。IP:{host}"
            )

        return CommandResult(
            txt=f"连接成功。IP:{host}"
        )

    def get_actual_tcp_pose(self, ip):
        """获取当前TCP位置"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )

        return CommandResult(
            txt=f"当前TCP姿态： {self.robot[ip].get_actual_tcp_pose()}"
        )

    def get_actual_joint_pose(self, ip):
        """获取当前关节角度"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"当前关节姿态 {self.robot[ip].get_actual_joint_positions()}"
        )

    def movel_x(self, ip, distance):
        """命令TCP沿X轴方向移动"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        pose = self.robot[ip].get_actual_tcp_pose()
        pose[0] = pose[0] + distance
        self.robot[ip].movel(pose)
        result = self.movelConfirm(ip, pose)
        cmd = f"movel(p[{'{:.4f}'.format(pose[0])},{'{:.4f}'.format(pose[1])},{'{:.4f}'.format(pose[2])},{'{:.4f}'.format(pose[3])},{'{:.4f}'.format(pose[4])},{'{:.4f}'.format(pose[5])},],0.5,0.25,0,0)"
        if result == 1:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动完成。"
            )
        else:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动失败。"
            )

    def get_serial_number(self, ip):
        """获取机器人序列号"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_serial_number()
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的序列号为： {self.robot[ip].robotConnector.DashboardClient.last_respond}"
        )

    def movel_y(self, ip, distance):
        """命令TCP沿Y轴方向移动"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        pose = self.robot[ip].get_actual_tcp_pose()
        pose[1] = pose[1] + distance

        self.robot[ip].movel(pose)
        result = self.movelConfirm(ip, pose)
        cmd = f"movel(p[{'{:.4f}'.format(pose[0])},{'{:.4f}'.format(pose[1])},{'{:.4f}'.format(pose[2])},{'{:.4f}'.format(pose[3])},{'{:.4f}'.format(pose[4])},{'{:.4f}'.format(pose[5])},],0.5,0.25,0,0)"
        if result == 1:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动完成。"
            )
        else:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动失败。"
            )

    def movel_z(self, ip, distance):
        """命令TCP沿Z轴方向移动"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        pose = self.robot[ip].get_actual_tcp_pose()
        pose[2] = pose[2] + distance
        self.robot[ip].movel(pose)
        result = self.movelConfirm(ip, pose)
        cmd = f"movel(p[{'{:.4f}'.format(pose[0])},{'{:.4f}'.format(pose[1])},{'{:.4f}'.format(pose[2])},{'{:.4f}'.format(pose[3])},{'{:.4f}'.format(pose[4])},{'{:.4f}'.format(pose[5])},],0.5,0.25,0,0)"
        if result == 1:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动完成。"
            )
        else:
            return CommandResult(
                txt=f"命令 {cmd} 已发送，移动失败。"
            )

    def get_output_int_register(self, ip, index):
        """获取Int寄存器的值"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].OutputIntRegister(index)}"
        )

    def disconnect_ur(self, ip):
        """断开与UR机器人的连接"""
        if self.robot.get(ip, "unknown") == "unknown":
            return CommandResult(
                txt=f"连接不存在"
            )
        self.robot[ip].close()
        return CommandResult(
            txt=f"连接已断开。"
        )

    def get_output_double_register(self, ip, index):
        """获取Double寄存器的值"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].OutputDoubleRegister(index)}"
        )

    def get_output_bit_register(self, ip, index):
        """获取Bool寄存器的值"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        bits = self.robotModle[ip].OutputBitRegister()
        return CommandResult(
            txt=f"{bits[index]}"
        )

    def get_actual_robot_voltage(self, ip):
        """获取机器人电压"""
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualRobotVoltage()}（伏特）"
        )

    def get_actual_robot_current(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualRobotCurrent()}（安培）"
        )

    def get_actual_joint_voltage(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualJointVoltage()}（伏特）"
        )

    def get_actual_joint_current(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualJointVoltage()}（安培）"
        )

    def get_joint_temperatures(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        return CommandResult(
            txt=f"{self.robotModle[ip].JointTemperatures()}（摄氏度）"
        )

    def get_robot_mode(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_robotmode()
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的运行状态为： {self.robot[ip].robotConnector.DashboardClient.last_respond}"
        )

    def get_program_state(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_get_loaded_program()
        prog_name = self.robot[ip].robotConnector.DashboardClient.last_respond
        self.robot[ip].robotConnector.DashboardClient.ur_programState()
        prog_state = self.robot[ip].robotConnector.DashboardClient.last_respond
        self.robot[ip].robotConnector.DashboardClient.ur_isProgramSaved()
        flg = self.robot[ip].robotConnector.DashboardClient.last_respond
        self.robot[ip].robotConnector.DashboardClient.ur_running()
        running = self.robot[ip].robotConnector.DashboardClient.last_respond

        prog_saved = ''
        prog_running = ''
        if flg.startswith("false"):
            prog_saved = '程序未保存，请及时保存或备份正在编辑的程序。'
        if running == 'Program running: true':
            prog_running = '机械臂正在动作。'
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人当前加载的程序是：{prog_name}，程序的执行状态是：{prog_state}。{prog_saved}。{prog_running}"
        )

    def get_ur_software_version(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_polyscopeVersion()
        result = self.robot[ip].robotConnector.DashboardClient.last_respond
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的软件版本是{result}"
        )

    def get_safety_mode(self, ip):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.DashboardClient.ur_safetymode()
        result = self.robot[ip].robotConnector.DashboardClient.last_respond
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的安全模式是{result}"
        )

    def send_program_script(self, ip, script):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        self.robot[ip].robotConnector.RealTimeClient.SendProgram(script)

        return CommandResult(
            txt=f"脚本程序已发送。"
        )

    def link_check(self, ip):
        '''检查连接状态，若连接断开或不存在，则建立连接'''
        if self.robot.get(ip, "unknown") == "unknown" or not self.robot[
            ip].robotConnector.RealTimeClient.IsRtcConnected() or self.robot[
            ip].robotConnector.DashboardClient.dbs_is_running() or self.robot[
            ip].robotConnector.RTDE.isRunning():
            self.connect_ur(ip)

    def movelConfirm(self, ip, pose):
        '''
        movel移动的结果确认
        1：移动到位
        2：移动结束，但是位置不准确
        '''
        loop_flg = True
        count = 0
        while loop_flg:
            sleep(1)
            current_pose = self.round_pose(self.robot[ip].get_actual_tcp_pose())
            if self.right_pose_tcp(current_pose, pose):
                self.robot[ip].robotConnector.DashboardClient.ur_running()
                running = self.robot[ip].robotConnector.DashboardClient.last_respond
                if running == 'Program running: false':
                    return 1
            else:
                self.robot[ip].robotConnector.DashboardClient.ur_running()
                running = self.robot[ip].robotConnector.DashboardClient.last_respond

                if running == 'Program running: true':
                    '''尚未移动完成'''
                    continue
                else:
                    '''移动完成'''
                    count = count + 1
                    if count > 5:
                        return 2

    def round_pose(self, pose):
        '''给坐标取近似值，精确到三位小数'''
        pose[0] = round(pose[0], 3)
        pose[1] = round(pose[1], 3)
        pose[2] = round(pose[2], 3)
        pose[3] = round(pose[3], 3)
        pose[4] = round(pose[4], 3)
        pose[5] = round(pose[5], 3)
        return pose

    def right_pose_tcp(self, current_pose_1, pose):
        '''tcp位置是否一致的校验，这里允许10mm的误差'''
        if pose[0] + 0.010 >= current_pose_1[0] >= pose[0] - 0.010:
            if pose[1] + 0.010 >= current_pose_1[1] >= pose[1] - 0.010:
                if pose[2] + 0.010 >= current_pose_1[2] >= pose[2] - 0.010:
                    return True

        return False

    # def ur_is_running(self,ip):
    def movejConfirm(self, ip, q):
        '''
        movej移动的结果确认
        1：移动到位
        2：移动结束，但是位置不准确
        '''
        loop_flg = True
        count = 0
        while loop_flg:
            sleep(1)
            current_pose = self.round_pose(self.robot[ip].get_actual_joint_positions())
            if self.right_pose_joint(current_pose, q):
                self.robot[ip].robotConnector.DashboardClient.ur_running()
                running = self.robot[ip].robotConnector.DashboardClient.last_respond
                if running == 'Program running: false':
                    return 1
            else:
                self.robot[ip].robotConnector.DashboardClient.ur_running()
                running = self.robot[ip].robotConnector.DashboardClient.last_respond

                if running == 'Program running: true':
                    # 尚未移动完成
                    continue
                else:
                    # 移动完成
                    count = count + 1
                    if count > 5:
                        return 2

    def right_pose_joint(self, current_pose, q):
        '''关节的弧度验证，允许0.1的误差,按角度计算大约5度'''
        if q[0] + 0.1 >= current_pose[0] >= q[0] - 0.1:
            if q[1] + 0.1 >= current_pose[1] >= q[1] - 0.1:
                if q[2] + 0.1 >= current_pose[2] >= q[2] - 0.1:
                    if q[3] + 0.1 >= current_pose[3] >= q[3] - 0.1:
                        if q[4] + 0.1 >= current_pose[4] >= q[4] - 0.1:
                            if q[5] + 0.1 >= current_pose[5] >= q[5] - 0.1:
                                return True
        return False

    def draw_circle(self, ip, center, r, coordinate="z"):
        '''给定圆心位置和半径，在水平或竖直方向画一个圆'''
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
        wp_1 = [center[0],center[1],center[2],center[3],center[4],center[5]]
        wp_2 = [center[0],center[1],center[2],center[3],center[4],center[5]]
        wp_3 = [center[0],center[1],center[2],center[3],center[4],center[5]]
        wp_4 = [center[0],center[1],center[2],center[3],center[4],center[5]]
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

        self.robot[ip].robotConnector.RealTimeClient.SendProgram(cmd)
        return CommandResult(
            txt=f"命令已发送：{cmd}"
        )

    def draw_square(self, ip, origin, border, coordinate="z"):
        '''给定起点位置和边长，在水平或竖直方向画一个正方形'''
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
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
        self.robot[ip].robotConnector.RealTimeClient.SendProgram(cmd)
        return CommandResult(
            txt=f"命令已发送：{cmd}"
        )

    def draw_rectangle(self, ip, origin, width,height, coordinate="z"):
        if '连接失败' in self.link_check(ip):
            return CommandResult(
                txt=f"与机器人的连接已断开。"
            )
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
        self.robot[ip].robotConnector.RealTimeClient.SendProgram(cmd)
        return CommandResult(
            txt=f"命令已发送：{cmd}"
        )

    def get_robot_model(self, ip):
        self.robot[ip].robotConnector.DashboardClient.ur_get_robot_model()
        model = self.robot[ip].robotConnector.DashboardClient.last_respond
        self.robot[ip].robotConnector.DashboardClient.ur_is_remote_control()
        e=self.robot[ip].robotConnector.DashboardClient.last_respond.lower()
        if e == 'true' or e == 'false':
            model = f"{model}e"
        return model

    def get_programs(self, ip, username='root', password='easybot'):
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

            return CommandResult(
                txt=f"命令已发送：{str(files)}"
                )
        except Exception as e:
            return CommandResult(
                txt=f"程序列表获取失败。"
            )



async def serve():
    """启动mcp服务"""
    server = Server("nUR-MCP-SERVER")
    ur_server = URServer()

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """接口列表."""
        return [
            Tool(
                name=URTools.CONNECT.value,
                description="连接UR机器人，连接成功之后才可以发送其它命令。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.DISCONNECT.value,
                description="断开与当前UR机器人的连接。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.GET_TIME.value,
                description="获取UR机器人的开机时长（秒）。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.GET_OUTPUT_INT_REGISTER.value,
                description="获取UR机器人的Int寄存器输出。Int类型输出共24个，地址分别为0~23，从0开始。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "index": {
                            "type": "number",
                            "description": f"范围：0~23的整数，包括0和23。",
                        }
                    },
                    "required": ["ip", "index"],
                },
            ),
            Tool(
                name=URTools.GET_OUTPUT_DOUBLE_REGISTER.value,
                description="获取UR机器人的Double寄存器输出。Double类型输出共24个，地址分别为0~23，从0开始。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "index": {
                            "type": "number",
                            "description": f"范围：0~23的整数，包括0和23。",
                        }
                    },
                    "required": ["ip", "index"],
                },
            ),
            Tool(
                name=URTools.GET_OUTPUT_BIT_REGISTER.value,
                description="获取UR机器人的Double寄存器输出。Double类型输出共32个，地址分别为0~31，从0开始。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "index": {
                            "type": "number",
                            "description": f"范围：0~31的整数，包括0和31。",
                        }
                    },
                    "required": ["ip", "index"],
                },
            ),
            Tool(
                name=URTools.GET_SERIAL_NUMBER.value,
                description="获取UR机器人的序列号。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.GET_ROBOT_MODEL.value,
                description="获取UR机器人的型号。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.GET_ACTUAL_TCP_POSE.value,
                description="获取UR机器人的实时TCP坐标。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.GET_ACTUAL_JOINT_POSE.value,
                description="获取UR机器人的实时关节角度。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.MOVEJ.value,
                description="发送一个关节姿态给UR，使UR移动到这个姿态位置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "q": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": f"关节角度（弧度）",
                        },
                        "a": {
                            "type": "number",
                            "description": f"加速度 (米每平方秒)",
                        },
                        "v": {
                            "type": "number",
                            "description": f"速度 (米每秒)",
                        },
                        "t": {
                            "type": "number",
                            "description": f"移动时间 (秒)",
                        },
                        "r": {
                            "type": "number",
                            "description": f"交融半径 （米）",
                        }
                    },
                    "required": ["ip", "q"],
                },
            ), Tool(
                name=URTools.MOVEL.value,
                description="发送一个TCP位置给UR，使UR的TCP沿直线移动到这个位置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "pose": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": f"工具端（TCP）位置",
                        },
                        "a": {
                            "type": "number",
                            "description": f"加速度 (米每平方秒)",
                        },
                        "v": {
                            "type": "number",
                            "description": f"速度 (米每秒)",
                        },
                        "t": {
                            "type": "number",
                            "description": f"移动时间 (秒)",
                        },
                        "r": {
                            "type": "number",
                            "description": f"交融半径 （米）",
                        }
                    },
                    "required": ["ip", "pose"],
                },
            ), Tool(
                name=URTools.MOVEL_X.value,
                description="沿X轴方向，直线移动一段距离。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "distance": {
                            "type": "number",
                            "description": f"移动距离（米）",
                        }
                    },
                    "required": ["ip", "distance"],
                },
            ), Tool(
                name=URTools.MOVEL_Y.value,
                description="沿Y轴方向，直线移动一段距离。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "distance": {
                            "type": "number",
                            "description": f"移动距离（米）",
                        }
                    },
                    "required": ["ip", "distance"],
                },
            ), Tool(
                name=URTools.MOVEL_Z.value,
                description="沿Z轴方向，直线移动一段距离。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "distance": {
                            "type": "number",
                            "description": f"移动距离（米）",
                        }
                    },
                    "required": ["ip", "distance"],
                },
            ), Tool(
                name=URTools.LOAD_URP.value,
                description="加载UR程序。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "program_name": {
                            "type": "string",
                            "description": f"程序名称",
                        }
                    },
                    "required": ["ip", "program_name"]
                },
            ), Tool(
                name=URTools.START_UR.value,
                description="加载UR程序并且执行。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "program_name": {
                            "type": "string",
                            "description": f"程序名称",
                        }
                    },
                    "required": ["ip", "program_name"]
                },
            ), Tool(
                name=URTools.STOP_UR.value,
                description="命令UR机器人停止执行当前程序。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"]
                },
            ), Tool(
                name=URTools.PAUSE_UR.value,
                description="命令UR机器人暂停执行当前程序。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"]
                },
            ), Tool(
                name=URTools.GET_ACTUAL_ROBOT_VOLTAGE.value,
                description="获取UR机器人的当前电压。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_ACTUAL_ROBOT_CURRENT.value,
                description="获取UR机器人的当前电流。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_ACTUAL_JOINT_VOLTAGE.value,
                description="获取UR机器人各个关节的当前电压。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_ACTUAL_JOINT_CURRENT.value,
                description="获取UR机器人各个关节的当前电流。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_ACTUAL_JOINT_TEMPERATURES.value,
                description="获取UR机器人各个关节的当前温度。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_ROBOT_MODE.value,
                description="获取UR机器人当前运行状态。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_PROGRAM_STATE.value,
                description="获取UR机器人的程序执行状态。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_UR_SOFTWARE_VERSION.value,
                description="获取UR机器人的软件版本。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.GET_SAFETY_MODE.value,
                description="获取UR机器人的安全模式。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),Tool(
                name=URTools.GET_PROGRAMS.value,
                description="获取UR机器人的程序列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "username": {
                            "type": "string",
                            "description": f"SSH用户名,默认值：root",
                        },
                        "password": {
                            "type": "string",
                            "description": f"SSH密码，默认值：easybot",
                        }
                    },
                    "required": ["ip"],
                },
            ), Tool(
                name=URTools.SEND_PROGRAM_SCRIPT.value,
                description="向UR机器人发送程序脚本。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "script": {
                            "type": "string",
                            "description": f"脚本内容",
                        }
                    },
                    "required": ["ip", "script"],
                },
            ),
            Tool(
                name=URTools.DRAW_CIRCLE.value,
                description="命令机器人在水平或竖直平面上画圆。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "center": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": f"圆心的TCP位置",
                        },
                        "r": {
                            "type": "number",
                            "description": f"半径（米）",
                        },
                        "coordinate": {
                            "type": "string",
                            "description": f"圆所在的平面。z：圆形所在的平面与基座所在平面垂直,其它：圆形所在的平面与基座所在平面平行。默认值：z。",
                        }
                    },
                    "required": ["ip", "center", "r"],
                },
            ),
            Tool(
                name=URTools.DRAW_SQUARE.value,
                description="命令机器人在水平或竖直平面上画正方形。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "origin": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": f"正方形左上方的顶点，画正方形的起点。",
                        },
                        "border": {
                            "type": "number",
                            "description": f"正方形的边长（米）",
                        },
                        "coordinate": {
                            "type": "string",
                            "description": f"正方形所在的平面。z：正方形所在的平面与基座所在平面垂直,其它：正方形所在的平面与基座所在平面平行。默认值：z。",
                        }
                    },
                    "required": ["ip", "origin", "border"],
                },
            ),
            Tool(
                name=URTools.DRAW_RECTANGLE.value,
                description="命令机器人在水平或竖直平面上画矩形。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人IP",
                        },
                        "origin": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": f"矩形左上方的顶点，画矩形的起点。",
                        },
                        "width": {
                            "type": "number",
                            "description": f"矩形的长（米）",
                        },
                        "height": {
                            "type": "number",
                            "description": f"矩形的宽（米）",
                        },
                        "coordinate": {
                            "type": "string",
                            "description": f"矩形所在的平面。z：矩形所在的平面与基座所在平面垂直,其它：矩形所在的平面与基座所在平面平行。默认值：z。",
                        }
                    },
                    "required": ["ip", "origin", "width", "height"],
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(
            name: str, arguments: dict
    ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
        """接口调用"""
        try:
            match name:

                case URTools.GET_TIME.value:
                    '''时间'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_time(arguments["ip"])
                case URTools.GET_SERIAL_NUMBER.value:
                    '''序列号'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_serial_number(arguments["ip"])
                case URTools.GET_ROBOT_MODEL.value:
                    '''型号'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_robot_model(arguments["ip"])
                case URTools.CONNECT.value:
                    '''连接机器人'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.connect_ur(arguments["ip"])
                case URTools.DISCONNECT.value:
                    '''断开连接'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.disconnect_ur(arguments["ip"])
                case URTools.GET_ACTUAL_TCP_POSE.value:
                    '''获取TCP姿态'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_tcp_pose(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_POSE.value:
                    '''序列号'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_joint_pose(arguments["ip"])
                case URTools.MOVEJ.value:
                    '''MOVEJ'''
                    if not all(
                            k in arguments
                            for k in ["ip", "q"]
                    ):
                        raise ValueError("Missing required arguments")

                    a = 1
                    v = 1
                    t = 0
                    r = 0
                    if "a" in arguments:
                        a = arguments["a"]
                    if "v" in arguments:
                        v = arguments["v"]
                    if "t" in arguments:
                        t = arguments["t"]
                    if "r" in arguments:
                        r = arguments["r"]

                    result = ur_server.movej(
                        arguments["ip"],
                        arguments["q"],
                        a,
                        v,
                        t,
                        r,
                    )

                case URTools.MOVEL.value:
                    '''MOVEL'''
                    if not all(
                            k in arguments
                            for k in ["ip", "pose"]
                    ):
                        raise ValueError("Missing required arguments")

                    a = 1
                    v = 1
                    t = 0
                    r = 0
                    if "a" in arguments:
                        a = arguments["a"]
                    if "v" in arguments:
                        v = arguments["v"]
                    if "t" in arguments:
                        t = arguments["t"]
                    if "r" in arguments:
                        r = arguments["r"]

                    result = ur_server.movel(
                        arguments["ip"],
                        arguments["pose"],
                        a,
                        v,
                        t,
                        r,
                    )

                case URTools.MOVEL_X.value:
                    '''沿X轴方向运动'''
                    if not all(
                            k in arguments
                            for k in ["ip", "distance"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.movel_x(
                        arguments["ip"],
                        arguments["distance"]
                    )
                case URTools.MOVEL_Y.value:
                    '''沿Y轴方向运动'''
                    if not all(
                            k in arguments
                            for k in ["ip", "distance"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.movel_y(
                        arguments["ip"],
                        arguments["distance"]
                    )
                case URTools.MOVEL_Z.value:
                    '''沿Z轴方向运动'''
                    if not all(
                            k in arguments
                            for k in ["ip", "distance"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.movel_z(
                        arguments["ip"],
                        arguments["distance"]
                    )

                case URTools.LOAD_URP.value:
                    '''加载程序'''
                    if not all(
                            k in arguments
                            for k in ["ip", "program_name"]
                    ):
                        raise ValueError("Missing required arguments")

                    result = ur_server.load_urp(
                        arguments["ip"],
                        arguments["program_name"]
                    )

                case URTools.START_UR.value:
                    '''加载并启动'''
                    if not all(
                            k in arguments
                            for k in ["ip", "program_name"]
                    ):
                        raise ValueError("Missing required arguments")

                    result = ur_server.start_ur(
                        arguments["ip"],
                        arguments["program_name"]
                    )

                case URTools.STOP_UR.value:
                    '''停止'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")

                    result = ur_server.stop_ur(
                        arguments["ip"]
                    )
                case URTools.PAUSE_UR.value:
                    '''暂停'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.stop_ur(
                        arguments["ip"]
                    )
                case URTools.GET_OUTPUT_INT_REGISTER.value:
                    '''获取整数寄存器的值'''
                    if not all(
                            k in arguments
                            for k in ["ip", "index"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_output_int_register(arguments["ip"], arguments["index"])
                case URTools.GET_OUTPUT_DOUBLE_REGISTER.value:
                    '''获取浮点寄存器的值'''
                    if not all(
                            k in arguments
                            for k in ["ip", "index"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_output_double_register(arguments["index"])
                case URTools.GET_OUTPUT_BIT_REGISTER.value:
                    '''获取布尔寄存器的值'''
                    if not all(
                            k in arguments
                            for k in ["ip", "index"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_output_bit_register(arguments["ip"], arguments["index"])
                case URTools.GET_ACTUAL_ROBOT_VOLTAGE.value:
                    '''机器人电压'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_robot_voltage(arguments["ip"])
                case URTools.GET_ACTUAL_ROBOT_CURRENT.value:
                    '''机器人电流'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_robot_current(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_VOLTAGE.value:
                    '''关节电压'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_joint_voltage(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_CURRENT.value:
                    '''关节电流'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_joint_current(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_TEMPERATURES.value:
                    '''关节温度'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_joint_temperatures(arguments["ip"])
                case URTools.GET_ROBOT_MODE.value:
                    '''机器人运行状态'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_robot_mode(arguments["ip"])
                case URTools.GET_PROGRAM_STATE.value:
                    '''机器人程序状态'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_program_state(arguments["ip"])
                case URTools.GET_UR_SOFTWARE_VERSION.value:
                    '''机器人软件版本'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_ur_software_version(arguments["ip"])
                case URTools.GET_SAFETY_MODE.value:
                    '''安全模式'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_safety_mode(arguments["ip"])
                case URTools.GET_PROGRAMS.value:
                    '''获取程序列表'''
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_programs(arguments["ip"],arguments["username"],arguments["password"])
                case URTools.SEND_PROGRAM_SCRIPT.value:
                    '''向机器人发送脚本'''
                    if not all(
                            k in arguments
                            for k in ["ip", "script"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.send_program_script(arguments["ip"], arguments["script"])
                case URTools.DRAW_CIRCLE.value:
                    '''画圆'''
                    if not all(
                            k in arguments
                            for k in ["ip", "center", "r"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.draw_circle(arguments["ip"], arguments["center"], arguments["r"]
                                                   , arguments["coordinate"])
                case URTools.DRAW_SQUARE.value:
                    '''画正方形'''
                    if not all(
                            k in arguments
                            for k in ["ip", "origin", "border"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.draw_square(arguments["ip"], arguments["origin"], arguments["border"]
                                                   , arguments["coordinate"])
                case URTools.DRAW_RECTANGLE.value:
                    '''画矩形'''
                    if not all(
                            k in arguments
                            for k in ["ip", "origin", "width","height"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.draw_rectangle(arguments["ip"], arguments["origin"], arguments["width"]
                                                   , arguments["height"], arguments["coordinate"])
                case _:
                    raise ValueError(f"Unknown tool: {name}")

            return [
                TextContent(type="text", text=json.dumps(result.model_dump(), indent=2))
            ]

        except Exception as e:
            raise ValueError(f"Error processing ur-mcp-server query: {str(e)}")

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options)


def remove_last_part(ip):
    '''去掉IP的最后一段'''
    parts = ip.split('.')
    if len(parts) == 4:
        return '.'.join(parts[:-1])
    return ip
