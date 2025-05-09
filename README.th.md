
<div align="center">
<a href="https://www.nonead.com">
<img src="https://www.nonead.com/assets/img/vi/NONEAD_ai.png" width="300" alt="nonead logo">
</a>
</div>

<p align="center">
  <a href="./README.en.md">English</a> |
  <a href="./README.md">简体中文</a> |
  <a href="./README.jp.md">日本語</a> |
  <a href="./README.ko.md">한국어</a> |
  <a href="./README.de.md">Deutsch</a> |
  <a href="./README.fr.md">Français</a> |
  <a href="./README.ru.md">Русский язык</a> |
  <a href="./README.th.md">ภาษาไทย</a> |
  <a href="./README.es.md">Español</a> |
  <a href="./README.ar.md">العربية</a> |
  <a href="./README.da.md">dansk</a>  
</p>
<p align="center">
    <a href='https://gitee.com/nonead/nUR_MCP_SERVER'><img src='https://img.shields.io/github/v/release/nonead/nUR_MCP_Server?color=green&label=Latest%20Release' alt="Latest Release"></a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER/releases/latest"><img src="https://img.shields.io/github/v/release/nonead/nUR_MCP_Server?color=blue&label=Latest%20Release" alt="Latest Release"></a>
    <a href='https://www.python.org/downloads/'><img src='https://img.shields.io/pypi/pyversions/RPALite'></img></a>
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER/wikis/pages">
        <img src="https://img.shields.io/badge/User%20Guide-1e8b93?logo=readthedocs&logoColor=f5f5f5" alt="User Guide"></a>
    <a href="https://www.apache.org/licenses/LICENSE-2.0"><img height="21" src="https://img.shields.io/badge/License-Apache--2.0-ffffff?labelColor=d4eaf7&color=2e6cc4" alt="license"></a>
     <a href='https://gitee.com/nonead/nUR_MCP_SERVER/stargazers'><img src='https://gitee.com/nonead/nUR_MCP_SERVER/badge/star.svg?theme=dark' alt='star'></img></a>

</p>

## 1. MCP คืออะไร?
MCP (โปรโตคอลบริบทแบบจำลอง) คือโปรโตคอลสื่อสารที่พัฒนาโดย Anthropic (เปิดตัวเป็นโอเพนซอร์สพฤศจิกายน 2024) ช่วยให้โมเดลภาษาใหญ่ (เช่น DeepSeek-V3-0324, DeepSeek-R1, Qwen3) เข้าถึงข้อมูล/เครื่องมือ/บริการภายนอกได้อย่างมีประสิทธิภาพ

ความสามารถหลัก:

การให้บริบท:
ส่งไฟล์/ข้อมูลฐานข้อมูลเสริม
ตัวอย่าง: วิเคราะห์รายงานก่อนตอบคำถาม

การเชื่อมต่อเครื่องมือ:
ควบคุมระบบท้องถิ่น/ระยะไกลโดยตรง
ตัวอย่าง: จัดระเบียบเอกสารอัตโนมัติ

สร้างเวิร์กโฟลว์อัจฉริยะ:
รวมบริการ MCP หลายรายการ

ความปลอดภัยข้อมูล:
ทำงานในสภาพแวดล้อมท้องถิ่น

## 2. วิธีการทำงาน
สถาปัตยกรรมไคลเอนต์-เซิร์ฟเวอร์:

ไคลเอนต์ MCP: แอปพลิเคชัน AI (ส่งคำขอ)
เซิร์ฟเวอร์ MCP: ให้อินเทอร์เฟซข้อมูล
การสื่อสาร: ใช้มาตรฐาน JSON-RPC 2.0

## 3. หน้าที่หลักของเซิร์ฟเวอร์
การเข้าถึงข้อมูล:
ไฟล์/ฐานข้อมูล/หน่วยความจำ

การดำเนินการ:
ฟังก์ชันที่กำหนดไว้ (เช่น คิวรี SQL)

การแจ้งเตือนแบบไดนามิก:
อัปเดตข้อมูลแบบเรียลไทม์

การจัดการเซสชัน:
ดูแลการเชื่อมต่อ

## 2. ฟังก์ชันหลักของเซิร์ฟเวอร์ nUR MCP  

### 2.1 การดึงข้อมูลฮาร์ดแวร์ทั้งหมดจากหุ่นยนต์ UR  
**ฟังก์ชันการสแกนเครือข่าย**  
fY6gJ6KcwVqfiiUFO-ogx1: สแกนช่วง IP ที่กำหนดเพื่อค้นหาหุ่นยนต์ UR  

**การจัดการการเชื่อมต่อ**  
fCf-PPsfx_yD_iZLURtGTV: เชื่อมต่อกับหุ่นยนต์ UR ที่มี IP เฉพาะ  
fEd1Yp4RD3kiUSxqQlK1Va: ตัดการเชื่อมต่อจากหุ่นยนต์ UR  

**ข้อมูลพื้นฐาน**  
fmMqIRbJZ4qRGJtRd59OJ-: ดึงหมายเลขซีเรียลของหุ่นยนต์  
f1ITpGFuwNDVfGfkNJzG2z: ดึงเวอร์ชันซอฟต์แวร์  
f8RnXWPeoSCCCvW3FuF_vS: ดึงเวลาการทำงาน  
fl_BhgXwRaQ8nzexSGjwa7: ดึงโหมดความปลอดภัย  

**ข้อมูลรีจิสเตอร์**  
fRRbXKNWy6vXbSrRPmFLJa: ดึงค่าตัวแปร Int (0-23)  
fRjcTzBeNogyaJtYvJ7_E2: ดึงค่าตัวแปร Double (0-23)  
fJ_s1E0ywr6t9rkMOBWiq6: ดึงค่าตัวแปร Double (0-31)  

**การตรวจสอบสถานะ**  
fVYZ0ocbfuml1VpA5JSNRo: ดึงพิกัด TCP แบบเรียลไทม์  
fts21SISQrnyp_mb3jJy91: ดึงมุมข้อต่อแบบเรียลไทม์  
fmjZNwC7zxju_tLjiM8w4A: ดึงสถานะการทำงาน  
fy5NIEBXN7Kqecb1RkPhZN: ดึงสถานะการทำงานของโปรแกรม  

**พารามิเตอร์ไฟฟ้า**  
fGU3ubp1fmrw-zPE2pyNDI: ดึงแรงดันไฟฟ้าปัจจุบัน  
fl--FA0LvH9LBjXjVB0gGD: ดึงกระแสไฟฟ้าปัจจุบัน  
fb3HhLwWUa8s49OXpU5Iq8: ดึงแรงดันข้อต่อ  
frGKnkZFPFesyEXdGAxpD9: ดึงกระแสข้อต่อ  
fzVxBGVvO7T3n3JbmAmvqB: ดึงอุณหภูมิข้อต่อ  

### 2.2 การสั่งงานคำสั่งเดี่ยวให้หุ่นยนต์ UR  
**การควบคุมการเคลื่อนไหว**  
ffoF99tQZ6vcEqHQplHTjv: ส่งคำสั่งตำแหน่งข้อต่อ (movej)  
fiF4Pmxs7LQTrG7hY4sQV8: ส่งคำสั่งเคลื่อนที่เชิงเส้น TCP (movel)  
fOyQY2wR6xzOZP3NxjpLjK: การเคลื่อนที่เชิงเส้นตามแกน X  
fCV_0M8pdPIVJs3nMGo6XS: การเคลื่อนที่เชิงเส้นตามแกน Y  
fWkTyW-C5rxUPe3U0WGSsm: การเคลื่อนที่เชิงเส้นตามแกน Z  

### 2.3 การเขียนโปรแกรมหุ่นยนต์ UR ด้วยโมเดลภาษาขนาดใหญ่และการทำงาน  

### 2.4 การทำงานโปรแกรมในตัวของหุ่นยนต์ UR  
**การควบคุมโปรแกรม**  
fE0WxXcDh3ENo8Q3fYul5K: โหลดโปรแกรม UR  
fDqpZeOA1_KF8ixwndRP8-: โหลดและรันโปรแกรม UR  
fH1AYKDXPCcGU1q3Ndrnwt: หยุดโปรแกรมปัจจุบัน  
fVwECQj8_p85mT6KaggA-N: ระงับโปรแกรมปัจจุบัน  
f4cp0iAFlVXMWqz51ylP4Z: ส่งสคริปต์โปรแกรม  

### 2.5 การประสานงานหุ่นยนต์ UR หลายตัว  


## 3. ข้อปฏิเสธความรับผิดชอบ

ก่อนใช้ nUR MCP Server ต้องตรวจสอบว่าผู้ปฏิบัติงานผ่านการอบรมความปลอดภัยหุ่นยนต์ UR และรู้จักการใช้ปุ่มหยุดฉุกเฉิน (E-stop)

ตรวจสอบสภาพหุ่นยนต์และเซิร์ฟเวอร์อย่างสม่ำเสมอเพื่อความปลอดภัย

ข้อกำหนดความปลอดภัยที่ต้องปฏิบัติตาม:

การมองเห็นหุ่นยนต์

ผู้ควบคุมต้องมองเห็นหุ่นยนต์ Universal Robots ตลอดเวลาเพื่อตรวจสอบสถานะ

ห้ามออกจากพื้นที่ขณะหุ่นยนต์ทำงาน

สภาพแวดล้อมปลอดภัย

ล้างสิ่งกีดขวางและตรวจสอบให้แน่ใจว่าไม่มีบุคคล/วัตถุในเขตอันตราย

ติดตั้งรั้วกายภาพหรือม่านแสงความปลอดภัยหากจำเป็น

การละเมิดกฎความปลอดภัย

หากเกิดความเสียหายจากความไม่ปฏิบัติตาม (เช่น ไม่เฝ้าดู ไม่เคลียร์พื้นที่) ทางเราไม่รับผิดชอบ

ความเสี่ยงทั้งหมดเป็นของผู้ใช้งาน

## 4. การเผยแพร่เวอร์ชัน

### 4.1 อัปเดตล่าสุด

* 2025.05.15 : เปิดตัว nUR_MCP_SERVER เป็นครั้งแรก

### 4.2 แผนในอนาคต

* พัฒนา MCP Client เฉพาะสำหรับ nUR MCP Server เพื่อเพิ่มความปลอดภัยของแอคชูเอเตอร์
* เพิ่มการบันทึก Log ของหุ่นยนต์ UR
* การสำรองข้อมูลและอัปโหลดโปรแกรมหุ่นยนต์ UR

## 5. เริ่มต้นใช้งานอย่างรวดเร็ว

### 5.1 สำหรับผู้ใช้ทั่วไป

#### 5.1.1 ข้อกำหนดระบบ

* **รุ่นระบบปฏิบัติการที่แนะนำ:**

  ```text
  macOS: macOS Monterey 12.6 หรือใหม่กว่า
  Linux: CentOS 7 / Ubuntu 20.04 หรือใหม่กว่า
  Windows: Windows 10 LTSC 2021 หรือใหม่กว่า
  ```

* **ข้อกำหนดซอฟต์แวร์:**

  สภาพแวดล้อมเซิร์ฟเวอร์ MCP

  ```text
  Python 3.11 หรือใหม่กว่า     
  pip 25.1 หรือใหม่กว่า
  UV Package Manager 0.6.14 หรือใหม่กว่า  
  bun 1.2.8 หรือใหม่กว่า
  ```

  ไคลเอนต์ MCP

  ```text
   Claude Desktop 3.7.0 หรือใหม่กว่า
   Cherry Studio 1.2.10 หรือใหม่กว่า
   Cline 3.14.1 หรือใหม่กว่า

   ClaudeMind, Cursor, NextChat, ChatMCP, Copilot-MCP, Continue, Dolphin-MCP, Goose ยังไม่ผ่านการทดสอบ
  ```

   LLM โมเดลภาษาขนาดใหญ่

  ```text
  DeepSeek-V3-0324 หรือใหม่กว่า
  DeepSeek-R1-671b หรือใหม่กว่า 
  Qwen3-235b-a22b หรือใหม่กว่า
  
  โดยทั่วไปโมเดลภาษาที่รองรับ MCP สามารถใช้งานได้ โมเดลนอกเหนือจากรายการยังไม่ผ่านการทดสอบ
  โมเดลที่ใช้งานผ่าน Ollama ยังไม่สามารถเรียกใช้ Tool ได้ กำลังแก้ไขปัญหา...
  ```

#### 5.1.2 การติดตั้ง

**การติดตั้งเซิร์ฟเวอร์ MCP:**
1. ติดตั้ง Python 3.11 หรือใหม่กว่า
2. ติดตั้ง pip 25.1 หรือใหม่กว่า
3. ติดตั้ง UV Package Manager 0.6.14 หรือใหม่กว่า
4. ติดตั้ง bun 1.2.8 หรือใหม่กว่า
5. ติดตั้ง MCP Server:
```
     git clone https://gitee.com/nonead/nUR_MCP_SERVER.git
     cd nUR_MCP_SERVER
     pip install -r requirements.txt
```

**การกำหนดค่าไคลเอนต์ MCP:**

**สำหรับใช้งานกับ Claude Desktop ให้เพิ่มการกำหนดค่าเซิร์ฟเวอร์:**
MacOS: ~/Library/Application Support/Claude/claude_desktop_config.json  

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
          "command": "python",
          "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
        }
      }
    }

Windows: %APPDATA%/Claude/claude_desktop_config.json  

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
          "command": "cmd",
          "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
        }
      }
    }

**สำหรับใช้งานกับ Cherry Studio ให้เพิ่มการกำหนดค่าเซิร์ฟเวอร์:**

**สำหรับ macOS & Linux:**  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "name": "nUR_MCP_Server",
      "type": "stdio",
      "description": "NONEAD Universal-Robots MCP Server",
      "isActive": true,
      "provider": "NONEAD Corporation",
      "providerUrl": "https://www.nonead.com",
      "logoUrl": "https://www.nonead.com/assets/img/vi/5.png",
      "tags": [
        "NONEAD",
        "nUR_MCP_Server",
        "Universal-Robots"
      ],
      "command": "python",
      "args": [
        "/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"
      ]
    }
  }
}
```

**สำหรับ Windows:**  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "name": "nUR_MCP_Server",
      "type": "stdio",
      "description": "NONEAD Universal-Robots MCP Server",
      "isActive": true,
      "provider": "NONEAD Corporation",
      "providerUrl": "https://www.nonead.com",
      "logoUrl": "https://www.nonead.com/assets/img/vi/5.png",
      "tags": [
        "NONEAD",
        "nUR_MCP_Server",
        "Universal-Robots"
      ],
      "command": "cmd",
      "args": [
        "/c",
        "python",
        "D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"
      ]
    }
  }
}
```

**เพื่อใช้งานร่วมกับ Cline ให้เพิ่มการกำหนดค่าเซิร์ฟเวอร์:**
MacOS & Linux:

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
            "command": "python",
            "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
         }
      }
    }

Windows:

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
            "command": "cmd",
            "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
         }
      }
    }


### 5.2 ใช้ชุดเครื่องมือ (สำหรับนักพัฒนา)

#### 5.2.1 เครื่องมือและส่วนประกอบ 

* **รุ่นระบบที่แนะนำ:**

  ```text
  ผู้ใช้ macOS: macOS Monterey 12.6 หรือใหม่กว่า
  ผู้ใช้ Linux: CentOS 7 / Ubuntu 20.04 หรือใหม่กว่า
  ผู้ใช้ Windows: Windows 10 LTSC 2021 หรือใหม่กว่า
  ```

* **ความต้องการด้านซอฟต์แวร์:**

  สภาพแวดล้อมเซิร์ฟเวอร์ MCP

  ```text
  Python 3.11 หรือใหม่กว่า     
  pip 25.1 หรือใหม่กว่า
  UV Package Manager 0.6.14 หรือใหม่กว่า  
  bun 1.2.8 หรือใหม่กว่า
  ```
  แบบจำลองภาษาขนาดใหญ่ LLM

  ```text
  DeepSeek-V3-0324 หรือใหม่กว่า
  DeepSeek-R1-671b หรือใหม่กว่า 
  Qwen3-235b-a22b หรือใหม่กว่า
  
  โดยทั่วไปแบบจำลองภาษาขนาดใหญ่ที่รองรับ MCP สามารถใช้งานได้ แบบจำลองที่ไม่ได้ระบุไว้ยังไม่ได้รับการทดสอบ
  แบบจำลองที่ติดตั้งผ่าน Ollama ปัจจุบันไม่สามารถเรียกใช้เครื่องมือได้ กำลังแก้ไข...
  ```

#### 5.2.2 การติดตั้ง

**สำหรับนักพัฒนา macOS/Linux/Windows**

```text
Python 3.11 หรือใหม่กว่า
pip 25.1 หรือใหม่กว่า
ตัวจัดการแพ็คเกจ UV 0.6.14 หรือใหม่กว่า
bun 1.2.8 หรือใหม่กว่า
```

#### 5.2.3 การใช้งาน

ตัวอย่างงานที่โมเดลภาษาขนาดใหญ่สามารถดำเนินการได้:

* เชื่อมต่อหุ่นยนต์ Universal IP: 192.168.1.199  
* รับพิกัดท่าปัจจุบันของ TCP end effector  
* แสดงรายการคำสั่งทั้งหมดของเครื่องมือ nUR_MCP_SERVER  
* ดึงข้อมูลฮาร์ดแวร์ทั้งหมดของหุ่นยนต์ Universal  
* ประมวลผลสคริปต์โปรแกรมของหุ่นยนต์  
* เรียกใช้โปรแกรมในตัว XXXX.urp  
* กำหนดหุ่นยนต์ IP 172.22.109.141 เป็น A และ IP 172.22.98.41 เป็น B เชื่อมต่อทั้งคู่ บันทึกท่า TCP และตำแหน่งหลักของ A (ซ้าย) และ B (ขวา) วิเคราะห์ความสัมพันธ์ระหว่างท่า  
* ดำเนินการเป็นขั้นตอน: หุ่นยนต์ Universal IP 192.168.1.199 บันทึกท่า TCP ปัจจุบัน แล้วเคลื่อน TCP +20mm ในแกน Z, -50mm ในแกน Y, +30mm ในแกน X ทำซ้ำ 5 ครั้ง  
* เขียนและดำเนินการสคริปต์หุ่นยนต์: วาดวงกลมรัศมี 50mm ในระนาบฐานโดยมีท่าปัจจุบันเป็นศูนย์กลาง  
* กำหนดหุ่นยนต์ IP 172.22.109.141 เป็น A และ 172.22.98.41 เป็น B เชื่อมต่อ คำสั่งต่อๆ ไปจะควบคุมเฉพาะ A พร้อมซิงค์การเคลื่อนไหวกระจกของ B  

## 6. โครงสร้างทางเทคนิค  

MCP ใช้โครงสร้างแบบ client-server ด้วยโปรโตคอลมาตรฐานสำหรับการสื่อสารระหว่างโมเดลกับทรัพยากรภายนอก  
![alt](./images/MCP.svg "mcp")  
โมเดล Client-Server  
องค์ประกอบหลัก:  

โฮสต์ MCP: แอปพลิเคชัน LLM (เช่น Claude Desktop) ที่เริ่มการเชื่อมต่อ  
ไคลเอนต์ MCP: โปรโตคอลไคลเอนต์ที่รักษาการเชื่อมต่อ 1:1 กับเซิร์ฟเวอร์  
เซิร์ฟเวอร์ MCP: โปรแกรมน้ำหนักเบาที่เปิดเผยฟังก์ชันผ่าน Model Context Protocol มาตรฐาน  
แหล่งข้อมูลท้องถิ่น: ไฟล์/ฐานข้อมูล/บริการที่เซิร์ฟเวอร์เข้าถึงได้อย่างปลอดภัย  
บริการระยะไกล: ระบบภายนอกที่เข้าถึงได้ผ่านอินเทอร์เน็ต (เช่น APIs)  
ความรับผิดชอบ:  

โฮสต์ MCP:  
ให้ส่วนติดต่อผู้ใช้  
จัดการการเชื่อมต่อกับผู้ให้บริการ LLM  
รวมไคลเอนต์ MCP สำหรับการเข้าถึงทรัพยากรภายนอก  
ไคลเอนต์ MCP:  
สร้าง/รักษาการเชื่อมต่อเซิร์ฟเวอร์ MCP  
ส่งคำขอและรับการตอบกลับ  
จัดการการแลกเปลี่ยนข้อมูลตามมาตรฐาน MCP  
เซิร์ฟเวอร์ MCP:  
ประมวลผลคำขอจากไคลเอนต์  
ดำเนินการฟังก์ชันเฉพาะหรือให้เข้าถึงทรัพยากร  
จัดรูปแบบการตอบกลับตามมาตรฐานโปรโตคอล MCP  
โปรโตคอลการสื่อสาร  
MCP ใช้ JSON-RPC 2.0 เป็นโปรโตคอลพื้นฐาน สนับสนุน:  
![alt](./images/p.svg "mcp_json-RPC2.0")  
คำขอ: ข้อความที่เริ่มการดำเนินการจากไคลเอนต์→เซิร์ฟเวอร์ หรือในทางกลับกัน  
การตอบกลับ: การตอบสนองต่อคำขอที่มีผลลัพธ์หรือข้อมูลข้อผิดพลาด  
การแจ้งเตือน: ข้อความทางเดียวที่ไม่ต้องการการตอบกลับ (มักใช้สำหรับการแจ้งเหตุการณ์)  
กลไกการขนส่งที่สนับสนุน:  

มาตรฐาน I/O (Stdio): สำหรับเซิร์ฟเวอร์ท้องถิ่นผ่านการสื่อสารระหว่างกระบวนการ  
Server-Sent Events (SSE): กลไกการขนส่งแบบ HTTP สำหรับเซิร์ฟเวอร์ระยะไกล  

ข้อได้เปรียบของ MCP  
MCP เหนือกว่าวิธีการแบบเดิมในด้านความเป็นหนึ่งเดียว ความปลอดภัย และความสามารถในการขยาย  

ความเป็นหนึ่งเดียว  
การโต้ตอบที่เป็นมาตรฐานแก้ปัญหาการแบ่งส่วน:  

การเข้าถึงแบบปลั๊กอิน: โปรโตคอลรวมศูนย์สำหรับแหล่งข้อมูลที่หลากหลาย  
ความเข้ากันได้ข้ามแพลตฟอร์ม: รองรับโมเดล/แพลตฟอร์ม AI ที่แตกต่างกัน  
การพัฒนาที่ง่ายขึ้น: มุ่งเน้นที่ตรรกะทางธุรกิจ  
ความปลอดภัย  
กลไกความปลอดภัยในตัวปกป้องข้อมูล:  

การปกป้องข้อมูลสำคัญ: คีย์ API/ข้อมูลผู้ใช้ ฯลฯ  
การควบคุมการเข้าถึง: เซิร์ฟเวอร์ MCP เปิดใช้งานข้อจำกัดการเข้าถึงแบบละเอียด  
การประมวลผลในท้องถิ่น: หลีกเลี่ยงการอัปโหลดข้อมูลสำคัญไปยังบุคคลที่สาม  
ความสามารถในการขยาย  
การออกแบบแบบโมดูลาร์ช่วยให้ขยายได้สูง:  

การเชื่อมต่อหลายบริการ: บริการหลายรายการสามารถเชื่อมต่อกับไคลเอนต์ที่เข้ากันได้  
การขยายระบบนิเวศ: ห้องสมุดของส่วนประกอบที่สร้างไว้ล่วงหน้าเพิ่มขึ้น  
ความสามารถในการปรับแต่ง: การพัฒนาเซิร์ฟเวอร์ MCP ที่กำหนดเอง  
## 7. ติดต่อเรา

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**เว็บไซต์ทางการ**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="ติดต่อ: Nonead Tech WeChat" width="200">  

## 8. ความแตกต่างระหว่าง nUR MCP Server กับเซิร์ฟเวอร์ MCP อื่นๆ

ผู้ใช้ nUR MCP Server ต้องมีความตระหนักด้านความปลอดภัยสูงมากและต้องผ่านการฝึกอบรมการใช้งานหุ่นยนต์ Universal Robots เนื่องจากโมเดลภาษาขนาดใหญ่ควบคุมหุ่นยนต์จริง การใช้งานที่ไม่เหมาะสมอาจทำให้เกิดการบาดเจ็บและความเสียหายต่อทรัพย์สิน - โปรดใช้ความระมัดระวังสูงสุด

## 9. การอ้างอิง

หากคุณใช้ซอฟต์แวร์นี้ โปรดอ้างอิงดังนี้:

* [nURMCP: NONEAD Universal-Robots Model Context Protocol Server](https://www.nonead.com)
* Nonead สาธิตความหมายที่แท้จริงของการผลิตอัจฉริยะ นำนวัตกรรมที่เปลี่ยนแปลงโลกของเรา

## 10. ใบอนุญาต

[Apache License 2.0](LICENSE)

## 11. ทีมพัฒนาหลัก

ทีมพัฒนาเซิร์ฟเวอร์ MCP ของบริษัท Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>
