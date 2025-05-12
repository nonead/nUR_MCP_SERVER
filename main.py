from mcp.types import TextContent
import json
from URBasic import RobotModel, DashBoard
from server import serve, URServer

if __name__ == '__main__':
    import asyncio
    asyncio.run(serve())
    # a=dict()
    # a[1]="q"
    # a[2]="w"
    # print(a.values())
    # my_list = ['apple', 'banana', 'cherry']
    # separator = ', '
    # result_string = separator.join(my_list)
    # print(result_string)
    # ur = URServer()
    #
    # print([
    #     TextContent(type="text", text=json.dumps(ur.scan_ur("192.168.1.174").model_dump(), indent=2))
    # ])
    # ur.connect_ur("192.168.1.174")
    # ur.get_program_state("192.168.1.174")

    # gbk_string = "Connected: Universal Robots Dashboard Server\nURSoftware 5.13.1.1131001 (äº\x94æ\x9c\x88 04 2023)".encode('gbk')  # 模拟一个 GBK 编码的字符串
    # # # 先将 gbk 字节对象解码为字符串
    # unicode_string = gbk_string.decode('gbk')
    # # # 再将字符串编码为 utf-8 字节对象
    # utf8_string = unicode_string.encode('utf-8')
    # print("转换后的 UTF-8 字符串:", utf8_string.decode('utf-8'))