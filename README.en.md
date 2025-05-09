
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

## 1. What is MCP?
MCP (Model Context Protocol) is a communication protocol developed by Anthropic (open-sourced in November 2024) that enables large language models (e.g. DeepSeek-V3-0324, DeepSeek-R1, Qwen3) to efficiently access external data/tools/services for delivering more accurate and intelligent responses.

Key Capabilities:

Context Provisioning:
Deliver files/database contents as supplementary context
Example: Analyzing reports before answering

External Tool Integration:
Directly operate local/remote systems (files, APIs, hardware)
Example: Automated document organization

Workflow Automation:
Combine multiple MCP services for complex tasks

Data Security:
Local execution protects sensitive information

## 2. How MCP Works
Client-Server Architecture:

MCP Client: AI application (initiates requests)
MCP Server: Provides data/tool interfaces
Communication: JSON-RPC 2.0 compliant

## 3. Server Functions
Data Access:
Files/databases/memory resources

Tool Execution:
Predefined functions (SQL queries, file ops)

Real-time Updates:
Push notifications for data changes

Session Management:
Connection maintenance

## 2. Core Functions of nUR MCP Server  

### 2.1 Acquiring All Hardware Data of UR Robots  

**Network Scanning Function**  
fY6gJ6KcwVqfiiUFO-ogx1: Scan UR robots within a specified IP range  

**Connection Management Function**  
fCf-PPsfx_yD_iZLURtGTV: Connect to a UR robot at a specified IP  
fEd1Yp4RD3kiUSxqQlK1Va: Disconnect from a UR robot  

**Basic Information Retrieval**  
fmMqIRbJZ4qRGJtRd59OJ-: Retrieve robot serial number  
f1ITpGFuwNDVfGfkNJzG2z: Retrieve software version  
f8RnXWPeoSCCCvW3FuF_vS: Retrieve uptime  
fl_BhgXwRaQ8nzexSGjwa7: Retrieve safety mode  

**Register Data Retrieval**  
fRRbXKNWy6vXbSrRPmFLJa: Retrieve Int register values (0-23)  
fRjcTzBeNogyaJtYvJ7_E2: Retrieve Double register values (0-23)  
fJ_s1E0ywr6t9rkMOBWiq6: Retrieve Double register values (0-31)  

**Status Monitoring**  
fVYZ0ocbfuml1VpA5JSNRo: Retrieve real-time TCP coordinates  
fts21SISQrnyp_mb3jJy91: Retrieve real-time joint angles  
fmjZNwC7zxju_tLjiM8w4A: Retrieve operating status  
fy5NIEBXN7Kqecb1RkPhZN: Retrieve program execution status  

**Electrical Parameter Monitoring**  
fGU3ubp1fmrw-zPE2pyNDI: Retrieve current voltage  
fl--FA0LvH9LBjXjVB0gGD: Retrieve current current  
fb3HhLwWUa8s49OXpU5Iq8: Retrieve joint voltages  
frGKnkZFPFesyEXdGAxpD9: Retrieve joint currents  
fzVxBGVvO7T3n3JbmAmvqB: Retrieve joint temperatures  

### 2.2 Executing Single-Command Instructions for UR Robots  

**Motion Control Function**  
ffoF99tQZ6vcEqHQplHTjv: Send joint pose command (movej)  
fiF4Pmxs7LQTrG7hY4sQV8: Send TCP linear movement command (movel)  
fOyQY2wR6xzOZP3NxjpLjK: Linear movement along the X-axis  
fCV_0M8pdPIVJs3nMGo6XS: Linear movement along the Y-axis  
fWkTyW-C5rxUPe3U0WGSsm: Linear movement along the Z-axis  

### 2.3 Using Large Language Models to Write and Execute UR Robot Script Programs  

### 2.4 Running Built-in Programs of UR Robots  

**Program Control**  
fE0WxXcDh3ENo8Q3fYul5K: Load a UR program  
fDqpZeOA1_KF8ixwndRP8-: Load and execute a UR program  
fH1AYKDXPCcGU1q3Ndrnwt: Stop the current program  
fVwECQj8_p85mT6KaggA-N: Pause the current program  
f4cp0iAFlVXMWqz51ylP4Z: Send a program script  

### 2.5 Coordinated Operation of Multiple UR Robots


## 3. Disclaimer

Before using the nUR MCP Server, ensure that operators have completed UR robot safety training and are familiar with emergency stop (E-stop) procedures.

Regularly inspect the robot and MCP Server's operational status to maintain system stability and safety.

The following safety protocols must be strictly adhered to when using the nUR MCP Server:

Robot Visibility

Operators shall keep Universal Robots within direct line of sight for real-time monitoring.

Leaving the operating area during robot operation is prohibited to ensure immediate response to emergencies.

Secure Work Environment

Clear obstacles and ensure no personnel/objects enter the hazard zone before robot activation.

Install physical barriers or safety light curtains if necessary to prevent unauthorized access.

Liability Waiver for Non-Compliance

We shall not be held liable for injuries, equipment damage, or production accidents caused by failure to comply with safety requirements (e.g., unattended operation, uncleared work areas).

All operational risks and consequences are borne by the user.

## 4. Version Releases  

### 4.1 Recent Updates  

* **2025.05.15**: Initial release of nUR_MCP_SERVER  

### 4.2 Future Plans  

* Develop a dedicated MCP Client for nUR MCP Server to enhance actuator safety features.  
* Add UR robot log recording functionality.  
* Enable backup and upload of UR robot programs.  

## 5. Quick Start  

### 5.1 Product-Based (For General Users)  

#### 5.1.1 Engine & Dependencies  

* **Recommended System Versions:**  

  ```text  
  macOS Users: macOS Monterey 12.6 or later  
  Linux Users: CentOS 7 / Ubuntu 20.04 or later  
  Windows Users: Windows 10 LTSC 2021 or later  
  ```  

* **Software Requirements:**  

  **MCP Server Environment**  

  ```text  
  Python 3.11 or later  
  pip 25.1 or later  
  UV Package Manager 0.6.14 or later  
  bun 1.2.8 or later  
  ```  

  **MCP Client**  

  ```text  
  Claude Desktop 3.7.0 or later  
  Cherry Studio 1.2.10 or later  
  Cline 3.14.1 or later  

  ClaudeMind, Cursor, NextChat, ChatMCP, Copilot-MCP, Continue, Dolphin-MCP, Goose - Not tested.  
  ```  

  **LLM Large Language Models**  

  ```text  
  DeepSeek-V3-0324 or later  
  DeepSeek-R1-671b or later  
  Qwen3-235b-a22b or later  

  Generally, any MCP-supported LLM can be used. Models not listed here have not been tested.  
  Ollama-deployed models currently cannot invoke Tools (under resolution)...  
  ```

#### 5.1.2 Installation  

**MCP Server Installation:**  
1. Install Python 3.11 or later.  
2. Install pip 25.1 or later.  
3. Install UV Package Manager 0.6.14 or later.  
4. Install bun 1.2.8 or later.  
5. Install MCP Server:  
```
git clone https://gitee.com/nonead/nUR_MCP_SERVER.git  
cd nUR_MCP_SERVER  
pip install -r requirements.txt  
```  

**MCP Client Configuration:**  

**To use with Claude Desktop, add server configuration:**
**For macOS:**  ~/Library/Application Support/Claude/claude_desktop_config.json  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "command": "python",
      "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
    }
  }
}
```

**For Windows:**  %APPDATA%/Claude/claude_desktop_config.json  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "command": "cmd",
      "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
    }
  }
}
```

**To use with Cherry Studio, add server configuration:**  

**For macOS & Linux:**  
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

**For Windows:**  
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

**To use with Cline, add server configuration:**  

**For macOS & Linux:**  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "command": "python",
      "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
    }
  }
}
```

**For Windows:**  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "command": "cmd",
      "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
    }
  }
}
```

### 5.2 Toolkit-Based (For Developers)  

#### 5.2.1 Engine & Dependencies  

* **Recommended System Versions:**  

  ```text  
  macOS Users: macOS Monterey 12.6 or later  
  Linux Users: CentOS 7 / Ubuntu 20.04 or later  
  Windows Users: Windows 10 LTSC 2021 or later  
  ```  

* **Software Requirements:**  

  **MCP Server Environment**  

  ```text  
  Python 3.11 or later  
  pip 25.1 or later  
  UV Package Manager 0.6.14 or later  
  bun 1.2.8 or later  
  ```  

  **LLM Large Language Models**  

  ```text  
  DeepSeek-V3-0324 or later  
  DeepSeek-R1-671b or later  
  Qwen3-235b-a22b or later  

  Generally, any LLM supporting MCP is usable. Untested models are not guaranteed.  
  Ollama-deployed models currently cannot invoke Tools (under resolution)...  
  ```  

#### 5.2.2 Installation  

**For macOS / Linux / Windows Developers**  

```text  
  Python 3.11 or later  
  pip 25.1 or later  
  UV Package Manager 0.6.14 or later  
  bun 1.2.8 or later  
```  

#### 5.2.3 Usage  

Here are some example tasks you can instruct the LLM to execute:  

* Connect to UR robot at IP: 192.168.1.199  
* Get the current TCP end-effector pose coordinates of the UR robot  
* List all commands of the nUR_MCP_SERVER tool  
* Retrieve all hardware data of the UR robot  
* Execute a script program on the UR robot  
* Run the UR robot's built-in program XXXX.urp  
* Assign the UR robot at 172.22.109.141 as "Robot A" and the one at 172.22.98.41 as "Robot B". Connect both robots, record their current TCP poses and key positions (Robot A on the left, Robot B on the right), and analyze their spatial relationship.  
* Execute step-by-step instructions for UR robot at 192.168.1.199: Record current TCP pose, then move TCP +20mm in Z, -50mm in Y, +30mm in X, repeating for 5 cycles.  
* Program and execute a UR script to draw a 50mm-radius circle in the base plane centered at the current pose.  
* Assign the UR robot at 172.22.109.141 as "Robot A" and the one at 172.22.98.41 as "Robot B". Connect both robots, then synchronize Robot B to mirror Robot A's movements in subsequent commands.

## 6. Technical Architecture  

MCP adopts a client-server architecture, enabling standardized communication between models and external resources.
![pic alt](./images/MCP.svg "mcp")
### Client-Server Model  
The MCP architecture consists of the following core components:  

- **MCP Host**: The LLM application (e.g., Claude Desktop or IDE) that initiates connections and seeks to access data via MCP.  
- **MCP Client**: A protocol client embedded within the host application, maintaining a 1:1 connection with the server.  
- **MCP Server**: A lightweight program that exposes specific functionalities through the standardized Model Context Protocol.  
- **Local Data Sources**: Computer files, databases, and services that the MCP server can securely access.  
- **Remote Services**: External systems (e.g., APIs) accessible via the internet that the MCP server can connect to.  

### Core Responsibilities  
In the MCP architecture, each component has the following responsibilities:  

**MCP Host:**  
- Provides the user interface  
- Manages connections with LLM providers  
- Integrates the MCP client to access external resources  

**MCP Client:**  
- Establishes and maintains connections with the MCP server  
- Sends requests and receives responses  
- Handles data exchange in compliance with the MCP protocol standards  

**MCP Server:**  
- Processes requests from clients  
- Executes specific functions or provides access to resources  
- Formats responses according to the MCP protocol standards  

### Communication Protocol  
MCP uses **JSON-RPC 2.0** as its foundational communication protocol, supporting the following message types:  

- **Requests**: Messages sent from the client to the server (or vice versa) to initiate operations.  
- **Responses**: Replies to requests, containing either results or error information.  
- **Notifications**: One-way messages that do not require responses, typically used for event notifications.  

MCP supports multiple transport mechanisms, including:  
- **Standard Input/Output (Stdio)**: Suitable for local servers, enabling inter-process communication.  
- **Server-Sent Events (SSE)**: An HTTP-based transport mechanism for remote servers.  
![pic alt](./images/p.svg "mcp_json-RPC2.0")  
**Requests**: Messages initiating operations sent from client to server or vice versa.  
**Responses**: Replies to requests containing either results or error information.  
**Notifications**: One-way messages requiring no response, typically used for event notifications.  

MCP supports multiple transport mechanisms, including:  
- **Standard Input/Output (Stdio)**: Suitable for local servers, implemented via inter-process communication.  
- **Server-Sent Events (SSE)**: An HTTP-based transport mechanism for remote servers.  

### Advantages of MCP  
MCP offers significant advantages over traditional integration methods, particularly in standardization, security, and scalability.  

**Standardization**  
MCP addresses fragmentation in traditional integration by standardizing interactions between AI systems and external data sources:  
- **Plug-and-play connectivity**: Unified protocol enables seamless integration of diverse data sources without custom coding.  
- **Cross-platform compatibility**: Supports different AI models and platforms, enhancing interoperability.  
- **Simplified development**: Reduces complexity, allowing developers to focus on business logic rather than underlying integrations.  

**Security**  
MCP incorporates built-in security mechanisms to safeguard data during transmission and processing:  
- **Sensitive data protection**: Ensures secure handling of confidential information (e.g., API keys, user data).  
- **Access control**: MCP servers implement granular permissions to validate request authorization.  
- **Local processing**: Keeps sensitive data on-premises, eliminating third-party exposure risks.  

**Scalability**  
MCP's modular design delivers exceptional extensibility:  
- **Multi-service connectivity**: Supports standardized resource/tool sharing across compatible clients.  
- **Ecosystem growth**: Developers gain access to expanding libraries of pre-built components.  
- **Customization**: Enables creation of specialized MCP servers to extend system capabilities.  

---  

## 7. Contact Us  

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**Gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**Official Website**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="Contact: Nonead Tech WeChat" width="200">  

## 8. Differences Between nUR MCP Server and Other MCP Servers  

Users of nUR MCP Server **must** possess advanced safety awareness and complete UR robot operation training, as LLMs directly control physical robots. Improper operation may cause personal injury or property damage.  

## 9. Citation  

If using this software, please cite as follows:  
* [nURMCP: NONEAD Uninversal-Robots Model Context Protocol Server](https://www.nonead.com)
* 拓德诠释智造之韵，创新引领世界之变 <br>
  Nonead demonstrates the true meaning of intelligent manufacturing, pioneering innovations that reshape our world.

## 10. License  

[Apache License 2.0](LICENSE)  

## 11. Core Development Team  

MCP Server Development Team, Suzhou Nonead Robotics Technology Co., Ltd.  

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>