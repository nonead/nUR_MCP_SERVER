from enum import Enum
import json
from time import sleep
from typing import Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from mcp.shared.exceptions import McpError

from pydantic import BaseModel

import URBasic
from URBasic import RobotModel, DashBoard

import sys

sys.stdout.reconfigure(encoding='utf-8')


class URTools(str, Enum):
    SCAN = "scan_ur"
    CONNECT = "connect_ur"
    DISCONNECT = "disconnect_ur"
    GET_TIME = "get_time"
    GET_SERIAL_NUMBER = "get_serial_number"
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
    SEND_PROGRAM_SCRIPT = "send_program_script"


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
        self.link_check(ip)

        return CommandResult(
            txt=f"{self.robotModle[ip].RobotTimestamp():.2f}"
        )

    def movej(self, ip, q, a=1, v=1, t=0, r=0):
        """发送新的关节姿态到UR机器人"""
        self.link_check(ip)
        cmd = f"movej({q},{a},{v},{t},{r})"

        self.robot[ip].movej(q, a, v, t, r)
        return CommandResult(
            txt=f"Command {cmd} has been sent to UR robot."
        )

    def load_urp(self, ip, name):
        """加载指定UR程序"""
        self.link_check(ip)
        cmd = f"{name}.urp"
        self.robot[ip].robotConnector.DashboardClient.ur_load(cmd)
        return CommandResult(
            txt=self.robot[ip].robotConnector.DashboardClient.last_respond
        )

    def start_ur(self, ip, name):
        """加载并执行指定UR程序"""
        self.link_check(ip)
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
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_stop()
        return CommandResult(
            txt=self.robot[ip].robotConnector.DashboardClient.last_respond
        )

    def pause_ur(self, ip):
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_pause()
        return CommandResult(
            txt=self.robot[ip].robotConnector.DashboardClient.last_respond
        )

    def movel(self, ip, pose, a=1, v=1, t=0, r=0):
        """直线移动"""
        self.link_check(ip)
        cmd = f"movel({pose},{a},{v},{t},{r})"

        self.robot[ip].movel(pose, a, v, t, r)
        return CommandResult(
            txt=f"Command {cmd} has been sent to UR robot."
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

        return CommandResult(
            txt=f"连接成功。IP:{host}"
        )

    def get_actual_tcp_pose(self, ip):
        """获取当前TCP位置"""
        self.link_check(ip)

        return CommandResult(
            txt=f"当前TCP姿态： {self.robot[ip].get_actual_tcp_pose()}"
        )

    def get_actual_joint_pose(self, ip):
        """获取当前关节角度"""
        self.link_check(ip)
        return CommandResult(
            txt=f"当前关节姿态 {self.robot[ip].get_actual_joint_positions()}"
        )

    def movel_x(self, ip, distance):
        """命令TCP沿X轴方向移动"""
        self.link_check(ip)
        pose = self.robot[ip].get_actual_tcp_pose()

        pose[0] = pose[0] + distance
        self.robot[ip].movel(pose)
        # result = self.movelConfirm(ip, pose)
        # while not result:
        #     result = self.movelConfirm(ip, pose)
        #     sleep(1)

        cmd = f"movel({pose},0.5,0.25,0,0)"
        return CommandResult(
            txt=f"命令 {cmd} 已发送"
        )

    def get_serial_number(self, ip):
        """获取机器人序列号"""
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_serial_number()
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的序列号为： {self.robot[ip].robotConnector.DashboardClient.last_respond}"
        )

    def movel_y(self, ip, distance):
        """命令TCP沿Y轴方向移动"""
        self.link_check(ip)
        pose = self.robot[ip].get_actual_tcp_pose()
        pose[1] = pose[1] + distance

        self.robot[ip].movel(pose)
        cmd = f"movel({pose},0.5,0.25,0,0)"
        return CommandResult(
            txt=f"命令 {cmd} 已发送"
        )

    def movel_z(self, ip, distance):
        """命令TCP沿Z轴方向移动"""
        self.link_check(ip)
        pose = self.robot[ip].get_actual_tcp_pose()
        pose[2] = pose[2] + distance
        self.robot[ip].movel(pose)
        cmd = f"movel({pose},0.5,0.25,0,0)"
        return CommandResult(
            txt=f"命令 {cmd} 已发送"
        )

    def get_output_int_register(self, ip, index):
        """获取Int寄存器的值"""
        self.link_check(ip)
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
        self.link_check(ip)
        return CommandResult(
            txt=f"{self.robotModle[ip].OutputDoubleRegister(index)}"
        )

    def get_output_bit_register(self, ip, index):
        """获取Bool寄存器的值"""
        self.link_check(ip)
        bits = self.robotModle[ip].OutputBitRegister()
        return CommandResult(
            txt=f"{bits[index]}"
        )

    def scan_ur(self, ip):
        """扫描网段内的所有UR机器人"""
        ip_pre = remove_last_part(ip)
        result = []
        for i in range(173, 175):
            robotModel = RobotModel()
            robotModel.ipAddress = f"{ip_pre}.{i}"
            # self._logger.info(f'{robotModel.ipAddress}====start')
            dashboard = DashBoard(robotModel)
            dashboard.ur_polyscopeVersion()

            res = dashboard.last_respond
            if res is not None and "URSoftware" in res:
                result.append(robotModel.ipAddress)

            dashboard.close()
            self._logger.info(f'q{result}')

        self._logger.info(f'w{result}')
        self._logger.info(len(result))
        if result is None or len(result) == 0:
            # self._logger.info(f'e{result}')
            return CommandResult(
                txt=f"未发现UR。"
            )
        self._logger.info(f'r{result}')
        separator = '-'
        result_string = separator.join(result)
        self._logger.info(f't{result_string}')
        return CommandResult(
            txt=result_string
        )
        # try:
        #     index = 0
        #     for i in range(2):
        #         sleep(1)
        #         self._logger.info(f'q{index}')
        #         index = index + 1
        #     self._logger.info(f't{index}')
        #     return CommandResult(
        #         txt=str(index)
        #     )
        # except Exception as e:
        #     self._logger.info(e)

    def get_actual_robot_voltage(self, ip):
        """获取机器人电压"""
        self.link_check(ip)
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualRobotVoltage()}（伏特）"
        )

    def get_actual_robot_current(self, ip):
        self.link_check(ip)
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualRobotCurrent()}（安培）"
        )

    def get_actual_joint_voltage(self, ip):
        self.link_check(ip)
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualJointVoltage()}（伏特）"
        )

    def get_actual_joint_current(self, ip):
        self.link_check(ip)
        return CommandResult(
            txt=f"{self.robotModle[ip].ActualJointVoltage()}（安培）"
        )

    def get_joint_temperatures(self, ip):
        self.link_check(ip)
        return CommandResult(
            txt=f"{self.robotModle[ip].JointTemperatures()}（摄氏度）"
        )

    def get_robot_mode(self, ip):
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_robotmode()
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的运行状态为： {self.robot[ip].robotConnector.DashboardClient.last_respond}"
        )

    def get_program_state(self, ip):
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_get_loaded_program()
        prog_name = self.robot[ip].robotConnector.DashboardClient.last_respond
        self.robot[ip].robotConnector.DashboardClient.ur_programState()
        prog_state = self.robot[ip].robotConnector.DashboardClient.last_respond
        self.robot[ip].robotConnector.DashboardClient.ur_isProgramSaved()
        flg = self.robot[ip].robotConnector.DashboardClient.last_respond
        prog_saved = ''
        if flg.startswith("false"):
            prog_saved = '程序未保存，请及时保存或备份正在编辑的程序。'
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人当前加载的程序是：{prog_name}，程序的执行状态是：{prog_state}。{prog_saved}"
        )

    def get_ur_software_version(self, ip):
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_polyscopeVersion()
        result = self.robot[ip].robotConnector.DashboardClient.last_respond
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的软件版本是{result}"
        )

    def get_safety_mode(self, ip):
        self.link_check(ip)
        self.robot[ip].robotConnector.DashboardClient.ur_safetymode()
        result = self.robot[ip].robotConnector.DashboardClient.last_respond
        return CommandResult(
            txt=f"IP为{ip}的优傲机器人的安全模式是{result}"
        )

    def send_program_script(self, ip, script):
        self.link_check(ip)
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
        2：未产生移动
        3：发生移动，但是位置不准确
        '''
        current_pose = self.round_pose(self.robot[ip].get_actual_tcp_pose())

        if current_pose[0] == pose[0] and current_pose[1] == pose[1] and current_pose[2] == pose[2]:
            return 1
        else:
            loop_flg = True
            sleep(1)
            count = 0
            while loop_flg:
                current_pose_1 = self.round_pose(self.robot[ip].get_actual_tcp_pose())
                if current_pose[0] == current_pose_1[0] and current_pose[1] == current_pose_1[1] and current_pose[2] == current_pose_1[2]:
                    count = count + 1
                    if count > 30:
                        return 2
                    continue
                else:
                    current_pose = current_pose_1
                    if current_pose[0] == pose[0] and current_pose[1] == pose[1] and current_pose[2] == pose[2]:
                        return 1
        return 1

    def round_pose(self, pose):
        '''给坐标取近似值，精确到三位小数'''
        pose[0] = round(pose[0], 3)
        pose[1] = round(pose[1], 3)
        pose[2] = round(pose[2], 3)
        pose[2] = round(pose[3], 3)
        pose[4] = round(pose[4], 3)
        pose[5] = round(pose[5], 3)
        return pose


async def serve():
    """启动mcp服务"""
    server = Server("nUR-MCP-SERVER")
    ur_server = URServer()

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """接口列表."""
        return [
            Tool(
                name=URTools.SCAN.value,
                description="根据用户提供的IP，扫描该IP同一网段内的UR机器人。执行失败时停止动作。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "ip": {
                            "type": "string",
                            "description": f"机器人同网段的IP",
                        }
                    },
                    "required": ["ip"],
                },
            ),
            Tool(
                name=URTools.CONNECT.value,
                description="连接UR机器人，连接成功之后才可以发送其它命令。执行失败时停止动作。",
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
                description="断开与当前UR机器人的连接。执行失败时停止动作。",
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
                description="获取UR机器人的开机时长。执行失败时停止动作。",
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
                description="获取UR机器人的Int寄存器输出。Int类型输出共24个，地址分别为0~23，从0开始。执行失败时停止动作。",
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
                description="获取UR机器人的Double寄存器输出。Double类型输出共24个，地址分别为0~23，从0开始。执行失败时停止动作。",
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
                description="获取UR机器人的Double寄存器输出。Double类型输出共32个，地址分别为0~31，从0开始。执行失败时停止动作。",
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
                description="获取UR机器人的序列号。执行失败时停止动作。",
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
                description="获取UR机器人的实时TCP坐标。执行失败时停止动作。",
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
                description="获取UR机器人的实时关节角度。执行失败时停止动作。",
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
                description="发送一个关节姿态给UR，使UR移动到这个姿态位置。执行失败时停止动作。",
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
                description="发送一个TCP位置给UR，使UR的TCP沿直线移动到这个位置。执行失败时停止动作。",
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
                description="沿X轴方向，直线移动一段距离。执行失败时停止动作。",
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
                description="沿Y轴方向，直线移动一段距离。执行失败时停止动作。",
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
                description="沿Z轴方向，直线移动一段距离。执行失败时停止动作。",
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
                description="加载UR程序。执行失败时停止动作。",
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
                description="加载UR程序并且执行。执行失败时停止动作。",
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
                description="命令UR机器人停止执行当前程序。执行失败时停止动作。",
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
                description="命令UR机器人暂停执行当前程序。执行失败时停止动作。",
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
                description="获取UR机器人的当前电压。执行失败时停止动作。",
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
                description="获取UR机器人的当前电流。执行失败时停止动作。",
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
                description="获取UR机器人各个关节的当前电压。执行失败时停止动作。",
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
                description="获取UR机器人各个关节的当前电流。执行失败时停止动作。",
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
                description="获取UR机器人各个关节的当前温度。执行失败时停止动作。",
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
                description="获取UR机器人当前运行状态。执行失败时停止动作。",
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
                description="获取UR机器人的程序执行状态。执行失败时停止动作。",
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
                description="获取UR机器人的软件版本。执行失败时停止动作。",
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
                description="获取UR机器人的安全模式。执行失败时停止动作。",
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
                name=URTools.SEND_PROGRAM_SCRIPT.value,
                description="向UR机器人发送程序脚本。执行失败时停止动作。",
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
        ]

    @server.call_tool()
    async def call_tool(
            name: str, arguments: dict
    ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
        """接口调用"""
        try:
            match name:

                case URTools.GET_TIME.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_time(arguments["ip"])
                case URTools.GET_SERIAL_NUMBER.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_serial_number(arguments["ip"])
                case URTools.CONNECT.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.connect_ur(arguments["ip"])
                case URTools.DISCONNECT.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.disconnect_ur(arguments["ip"])
                case URTools.GET_ACTUAL_TCP_POSE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_tcp_pose(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_POSE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_joint_pose(arguments["ip"])
                case URTools.MOVEJ.value:
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
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")

                    result = ur_server.stop_ur(
                        arguments["ip"]
                    )
                case URTools.PAUSE_UR.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.stop_ur(
                        arguments["ip"]
                    )
                case URTools.GET_OUTPUT_INT_REGISTER.value:
                    if not all(
                            k in arguments
                            for k in ["ip", "index"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_output_int_register(arguments["ip"], arguments["index"])
                case URTools.GET_OUTPUT_DOUBLE_REGISTER.value:
                    if not all(
                            k in arguments
                            for k in ["ip", "index"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_output_double_register(arguments["index"])
                case URTools.GET_OUTPUT_BIT_REGISTER.value:
                    if not all(
                            k in arguments
                            for k in ["ip", "index"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_output_bit_register(arguments["ip"], arguments["index"])
                case URTools.GET_ACTUAL_ROBOT_VOLTAGE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_robot_voltage(arguments["ip"])
                case URTools.GET_ACTUAL_ROBOT_CURRENT.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_robot_current(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_VOLTAGE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_joint_voltage(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_CURRENT.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_actual_joint_current(arguments["ip"])
                case URTools.GET_ACTUAL_JOINT_TEMPERATURES.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_joint_temperatures(arguments["ip"])
                case URTools.GET_ROBOT_MODE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_robot_mode(arguments["ip"])
                case URTools.GET_PROGRAM_STATE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_program_state(arguments["ip"])
                case URTools.GET_UR_SOFTWARE_VERSION.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_ur_software_version(arguments["ip"])
                case URTools.GET_SAFETY_MODE.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.get_safety_mode(arguments["ip"])
                case URTools.SEND_PROGRAM_SCRIPT.value:
                    if not all(
                            k in arguments
                            for k in ["ip", "script"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.send_program_script(arguments["ip"], arguments["script"])
                case URTools.SCAN.value:
                    if not all(
                            k in arguments
                            for k in ["ip"]
                    ):
                        raise ValueError("Missing required arguments")
                    result = ur_server.scan_ur(arguments["ip"])
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
