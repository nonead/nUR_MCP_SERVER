
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
    <a href='https://gitee.com/nonead/nUR_MCP_SERVER/releases/latest'><img src='https://img.shields.io/static/v1?label=Gitee.Com&message=Latest%20Release&color=Blue' alt="Latest Release"></a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER/releases/latest"><img src="https://img.shields.io/static/v1?label=GitHub.Com&message=Latest%20Release&color=Green" alt="Latest Release"></a>
    <a href='https://www.python.org/downloads/'><img src='https://img.shields.io/pypi/pyversions/RPALite'></img></a>
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER/wikis/pages">
        <img src="https://img.shields.io/badge/User%20Guide-1e8b93?logo=readthedocs&logoColor=f5f5f5" alt="User Guide"></a>
    <a href="./LICENSE"><img height="21" src="https://img.shields.io/static/v1?label=License&message=User-Segmented Dual Licensing&color=blue" alt="license"></a>
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

Technical Specification of Tuode Technology's Self-developed nUR_MCP_SERVER Product  

Product Overview:  
The nUR_MCP_SERVER is an intelligent robot control middleware system built on the MCP (Model Control Protocol) interface, enabling natural language interactive control of industrial robots through integration with large language models (LLMs). Designed with a Client-Server architecture, it supports deep integration with Universal Robots' full range of collaborative robots, revolutionizing the traditional teach pendant programming paradigm for industrial robots.  

Core Technical Architecture:  
1. Semantic Parsing Engine  
Equipped with a multi-layer Transformer-based NLP processing module, it supports context-aware command parsing (Contextual Command Parsing), achieving end-to-end conversion from natural language to robot control commands with a command recognition accuracy of 98.6%.  

2. Dynamic Script Generation System  
An LLM-based code generation framework that automatically converts natural language commands into URScript robot control scripts. It supports real-time syntax validation and safety verification, improving generation efficiency by 12x compared to traditional programming.  

3. Multimodal Control Interface  
- MCP Protocol Extension Layer: Supports dual-mode TCP/UDP communication with µs-level command response.  
- Device Abstraction Layer: Standardizes URCap plugin integration.  
- Data Bus: Enables multi-robot collaborative control via TCP/IP Ethernet protocol.  

Core Features:  
▶ Natural Language Real-Time Control  
Directly drives robot motion (pose control, trajectory planning, I/O operations) via voice/text commands, supporting dynamic parameter injection and real-time motion adjustments.  

▶ Intelligent Data Acquisition System  
- Real-time collection of 12-dimensional state data (joint torque, end-effector pose, etc.).  
- Supports natural language-defined data filtering rules.  
- Automatically generates structured data reports (CSV/JSON/XLSX).  

▶ Multi-Robot Collaborative Control  
Based on a distributed task scheduling algorithm, it can manage ≤12 UR robots simultaneously when paired with Tuode's MCP-Client, supporting voice cascading commands and cross-device task orchestration.  

▶ Adaptive Learning Module  
Features an incremental training framework that continuously optimizes command-action mapping through user feedback, with a system iteration cycle of ≤24h.  

Technical Specifications:  
- Command Response Latency: <200ms (end-to-end).  
- Protocol Compatibility: MCP v2.1+ / URScript v5.0+.  
- Concurrent Processing Capacity: 200+ TPS.

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
      "command": "python",
      "args": ["D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
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
      "command": "python",
      "args": [
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
      "command": "python",
      "args": ["D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
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

This project adopts a User-Segmented Dual Licensing model.

**Basic Principles**
* Individual users and organizations/companies with ≤10 people: AGPLv3 license applies automatically
* Organizations/companies with >10 people: Commercial license required

Definition of "≤10 people":
This refers to situations where the total number of individuals in your organization (including companies, non-profits, government agencies, educational institutions, etc.) who directly or indirectly access, use, or benefit from nUR_MCP_SERVER does not exceed 10. This includes but is not limited to developers, testers, operators, end-users, and users through integrated systems.

### 10.1 Open Source License (AGPLv3) - For individuals and organizations with ≤10 people
* If you're an individual user or your organization meets the "≤10 people" definition, you may freely use, modify, and redistribute nUR_MCP_SERVER under AGPLv3 terms. The full AGPLv3 license can be found at https://www.gnu.org/licenses/agpl-3.0.html.
* **Key obligations:** As a core requirement of AGPLv3, you must provide recipients with complete source code under AGPLv3 if you distribute modified versions of nUR_MCP_Server or offer it as a network service. Even if your organization meets the "≤10 people" criteria, you should consider a commercial license (see below) if you wish to avoid this source code disclosure requirement.
* Read and understand all AGPLv3 terms thoroughly before use.

### 10.2 Commercial License - For organizations with >10 people or users wishing to avoid AGPLv3 obligations
* **Mandatory requirement:** If your organization doesn't meet the "≤10 people" definition (i.e., 11+ people access/use/benefit from the software), you must enter a commercial license agreement with us before using nUR_MCP_SERVER.
* **Optional application:** Even if your organization meets the "≤10 people" criteria, a commercial license is required if your usage scenario doesn't comply with AGPLv3 terms (especially source code disclosure requirements) or if you need specific commercial provisions (such as warranties, indemnification, or absence of Copyleft restrictions) not offered under AGPLv3.
* **Common cases requiring commercial license (non-exhaustive):**
  * Organizations with >10 people
  * (Regardless of size) Distributing modified versions of nUR_MCP_SERVER without disclosing source code as required by AGPLv3
  * (Regardless of size) Offering nUR_MCP_SERVER as a network service (SaaS) without providing users access to modified source code
  * (Regardless of size) When company policies, customer contracts, or project requirements prohibit use of AGPLv3-licensed software or require closed distribution/confidentiality
* **Obtaining commercial license:** Contact nUR_MCP_SERVER development team at service@nonead.com.

### 10.3 Contributions
* We welcome community contributions to nUR_MCP_SERVER. All contributions to the project are considered made under AGPLv3 license.
* By submitting a contribution (e.g., a Pull Request), you agree that your code will be made available to the project and all future users (regardless of whether they choose AGPLv3 or commercial license) under AGPLv3 terms.
* You also agree that your contribution may be included in versions of nUR_MCP_SERVER distributed under a commercial license.

### 10.4 Other Terms
* Specific commercial license terms are established in the formal commercial license agreement.
* Project maintainers reserve the right to update this license policy (including user size definitions and thresholds) as needed. Any updates will be announced via the project's official channels (code repository, website, etc.).


## 11. Core Development Team  

MCP Server Development Team, Suzhou Nonead Robotics Technology Co., Ltd.  

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>