
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
    <a href='https://gitee.com/nonead/nUR_MCP_SERVER/releases'>
      <img src='https://img.shields.io/github/v/release/nonead/nUR_MCP_SERVER.svg?label=Gitee%20Release&color=blue' alt="Gitee Release"></img>
    </a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER/releases">
      <img src="https://img.shields.io/github/v/release/nonead/nUR_MCP_SERVER.svg?label=GitHub%20Release" alt="GitHub Release"></img>
    </a>
    <a href='https://www.python.org/downloads/'>
      <img src='https://img.shields.io/pypi/pyversions/RPALite'></img>
    </a>
    <a href='https://www.universal-robots.cn'>
      <img src='https://img.shields.io/badge/PolyScope-3.x_&_5.x-71A8CF'></img>
    </a>
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER/wikis/pages">
      <img src="https://img.shields.io/badge/User%20Guide-1e8b93?logo=readthedocs&logoColor=f5f5f5" alt="User Guide"></img>
    </a>
    <a href="./LICENSE">
      <img height="20" src="https://img.shields.io/badge/License-User_Segmented_Dual_Licensing-blue" alt="license"></img>
    </a>    
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER">
      <img height="20" src="https://gitee.com/nonead/nUR_MCP_SERVER/badge/fork.svg?theme=dark" alt="Gitee Forks"></img>
    </a>
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER">
      <img height="20" src="https://gitee.com/nonead/nUR_MCP_SERVER/badge/star.svg?theme=dark" alt="Gitee Stars"></img>
    </a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER">
      <img src="https://img.shields.io/github/forks/nonead/nUR_MCP_SERVER?label=Forks&style=flat-square" alt="Github Forks"></img>
    </a>
    <a href='https://github.com/nonead/nUR_MCP_SERVER'>
      <img src="https://img.shields.io/github/stars/nonead/nUR_MCP_SERVER.svg?style=flat-square&label=Stars&logo=github" alt="Github Stars"/></img>
    </a>
</p>



## 1. ¿Qué es MCP?
El MCP (Protocolo de Contexto de Modelo) es un protocolo de comunicación desarrollado por Anthropic (de código abierto desde noviembre 2024) que permite a los grandes modelos de IA (ej. DeepSeek-V3-0324, DeepSeek-R1, Qwen3) acceder eficientemente a datos/herramientas/servicios externos.

Funcionalidades clave:

Provisión de contexto:
Transmisión de archivos/contenidos de BD
Ej: Análisis de informes previo a respuestas

Integración de herramientas:
Operación remota/local de sistemas
Ej: Organización automática de documentos

Automatización de flujos:
Combinación de servicios MCP

Seguridad de datos:
Ejecución local protege información

## 2. Funcionamiento
Arquitectura cliente-servidor:

Cliente MCP: Aplica IA (envía solicitudes)
Servidor MCP: Provee interfaces
Comunicación: Basada en JSON-RPC 2.0

## 3. Funciones del servidor
Acceso a datos:
Archivos/BD/memoria
Ejecución de herramientas:
Funciones predefinidas (consultas SQL etc.)
Notificaciones dinámicas:
Actualizaciones en tiempo real
Gestión de sesiones:
Mantenimiento de conexiones

## 2. Funciones principales del servidor nUR MCP  

Descripción técnica del producto nUR_MCP_SERVER desarrollado por Nonead Corporation

Resumen del producto:
nUR_MCP_SERVER es un sistema middleware de control de robots inteligentes construido sobre el protocolo de interfaz MCP (Model Control Protocol), que integra modelos de lenguaje grande (LLM) para permitir el control interactivo en lenguaje natural de robots industriales. Este producto utiliza un diseño de arquitectura Cliente-Servidor y soporta integración profunda con toda la serie de robots colaborativos Universal Robots, revolucionando el paradigma tradicional de programacióncon teach pendant de robots industriales.

Arquitectura tecnológica clave:

Motor de análisis semántico
Módulo de procesamiento NLP con arquitectura Transformer multicapa, soporta análisis contextual de comandos (Contextual Command Parsing), logrando conversión de extremo a extremo de lenguaje natural a comandos de control con precisión de reconocimiento del 98.6%.

Sistema dinámico de generación de scripts
Framework de generación de código basado en LLM, convierte automáticamente comandos en lenguaje natural a scripts URScript, con verificación sintáctica y validación de seguridad en tiempo real, eficiencia 12 veces superior a programación tradicional.

Interfaz de control multimodal

Capa de extensión MCP: Soporta comunicación dual TCP/UDP, respuesta en microsegundos
Capa de abstracción: Conexión estandarizada de plugins URCap
Bus de datos: Protocolo TCP/IP para control coordinado multirobot
Características principales:
▶ Control inmediato por lenguaje natural
Comando directo de movimientos (control de posición, planificación de trayectoria, E/S) mediante voz/texto, con inyección dinámica de parámetros y corrección en tiempo real.

▶ Sistema inteligente de adquisición de datos

Captura en tiempo real de datos 12D (par articular, posición efector final)
Reglas de filtrado definibles en lenguaje natural
Generación automática de informes (CSV/JSON/XLSX)
▶ Control coordinado multirobot
Algoritmo distribuido de planificación de tareas + MCP-Client de Tord para gestionar ≤12 robots UR simultáneos, soporta comandos en cascada y orquestación multitarea.

▶ Módulo de aprendizaje adaptativo
Framework de entrenamiento incremental integrado, optimiza mapeo comando-acción mediante feedback con ciclo ≤24h.

Especificaciones:

Latencia: <200ms (end-to-end)
Compatibilidad: MCP v2.1+/URScript v5.0+
Capacidad concurrente: 200+ TPS

**Tabla de Clasificación de Funciones de la Herramienta nUR_MCP_SERVER:**  

| ID de Herramienta (nUR_MCP_SERVER) | Categoría          | Descripción                          | Parámetros          |  
|------------------------------------|--------------------|--------------------------------------|---------------------|  
| ffWzqSZlUpjFfVITKvBb-b            | Control de Conexión | Conectar al Robot UR                 | `ip`: IP del Robot |  
| fx5l9Mb_BUs_hClarGKZIo            | Control de Conexión | Desconectar Robot UR                 | `ip`: IP del Robot |  
| f04vj-Fwbuo8s2oYu252pR            | Monitoreo de Estado | Obtener Tiempo de Actividad del Robot | `ip`: IP del Robot |  
| f2SHZtIYF_OhS8LuslKt8D            | Operación de Registro | Leer Valor de Registro Int (0-23)    | `ip`: IP del Robot, `index`: Índice de Registro (0-23) |  
| fjLf_89qRxYDlEKo_oXADQ            | Operación de Registro | Leer Valor de Registro Double (0-23) | `ip`: IP del Robot, `index`: Índice de Registro (0-23) |  
| f9uXSEQB1UZMXmgIyPtVH9            | Operación de Registro | Leer Valor de Registro Double (0-31) | `ip`: IP del Robot, `index`: Índice de Registro (0-31) |  
| fBHQbdS9p_BPv97XBAau8a            | Información del Dispositivo | Obtener Número de Serie del Robot | `ip`: IP del Robot |  
| fcHIfX-J83SvH0V6XZ59A7            | Control de Movimiento | Obtener Coordenadas TCP en Tiempo Real | `ip`: IP del Robot |  
| fwloSfxAGiC_4rjdaZjUng            | Control de Movimiento | Obtener Ángulos de Articulación en Tiempo Real | `ip`: IP del Robot |  
| fFg2TP6jf3XTWytLIf9fyO            | Control de Movimiento | Enviar Comando de Pose de Articulación | `ip`: IP del Robot, `q`: Ángulos de Articulación (Radianes), `a/v/t/r`: Parámetros de Movimiento |  
| fBevTU5BWNdVNEKgqLV5d1            | Control de Movimiento | Enviar Comando de Movimiento Lineal TCP | `ip`: IP del Robot, `pose`: Posición TCP, `a/v/t/r`: Parámetros de Movimiento |  
| fnPhKVsDYRrB_Cf1wlsitI            | Control de Movimiento | Movimiento Lineal en Eje X           | `ip`: IP del Robot, `distance`: Distancia de Movimiento (Metros) |  
| fO55CY6Jw_iASo5NkxTm3l            | Control de Movimiento | Movimiento Lineal en Eje Y           | `ip`: IP del Robot, `distance`: Distancia de Movimiento (Metros) |  
| fs3ppclCfK_x0ZzFaOKHMk            | Control de Movimiento | Movimiento Lineal en Eje Z           | `ip`: IP del Robot, `distance`: Distancia de Movimiento (Metros) |  
| f18oyor3ddLJHMdPpyer45            | Control de Programa | Cargar Programa UR                   | `ip`: IP del Robot, `program_name`: Nombre del Programa |  
| fQyW6AYZjmMiGL0unOVK0W            | Control de Programa | Cargar y Ejecutar Programa UR        | `ip`: IP del Robot, `program_name`: Nombre del Programa |  
| fDxcON3qGCkzR5n9jSS5vQ            | Control de Programa | Detener Programa Actual              | `ip`: IP del Robot |  
| fXB2Q94gpe30w1JHgZh_yr            | Control de Programa | Pausar Programa Actual               | `ip`: IP del Robot |  
| fyXhJEun99j0N-5ojAzPYu            | Monitoreo de Estado | Obtener Voltaje Actual               | `ip`: IP del Robot |  
| fYvUCtj-7VJIdbm1FA6cg8            | Monitoreo de Estado | Obtener Corriente Actual             | `ip`: IP del Robot |  
| fno_OQmW5X_c3HK8M3r_NV            | Monitoreo de Estado | Obtener Voltaje de Articulación      | `ip`: IP del Robot |  
| fPc54VdscRk2hmlEc3VwYg            | Monitoreo de Estado | Obtener Corriente de Articulación    | `ip`: IP del Robot |  
| fAKuhJVkwgI4NbTKQ-xsoM            | Monitoreo de Estado | Obtener Temperatura de Articulación  | `ip`: IP del Robot |  
| fjZheWqG9gz8SO78UgN6v7            | Monitoreo de Estado | Obtener Estado de Operación          | `ip`: IP del Robot |  
| f2XEU4pWT2dsXI2rMsGfEw            | Monitoreo de Estado | Obtener Estado de Ejecución de Programa | `ip`: IP del Robot |  
| fYLTKblGKQserA-ZvLXCAt            | Información del Dispositivo | Obtener Versión de Software | `ip`: IP del Robot |  
| f2ebXFoN8bP3Pm1zocshdN            | Información del Dispositivo | Obtener Modo de Seguridad       | `ip`: IP del Robot |  
| f_5wAr6iv97d1jurrEmhNp            | Control de Programa | Enviar Programa de Script            | `ip`: IP del Robot, `script`: Contenido del Script |  
| fI3ZhZJZafBt33eNGD0ydQ            | Control de Movimiento | Movimiento Circular                  | `ip`: IP del Robot, `center`: Posición TCP del Centro, `r`: Radio (Metros), `coordinate`: Tipo de Plano |  


## 3. Declaración de responsabilidad

Antes de usar el nUR MCP Server, verifique que el operador ha recibido capacitación en seguridad de robots UR y conoce el paro de emergencia (E-stop).

Inspeccione regularmente el robot y el estado del MCP Server para garantizar estabilidad y seguridad.

Al usar el nUR MCP Server, cumpla estrictamente con:

Visibilidad del robot

El operador debe mantener al robot Universal Robots dentro de su campo visual para monitoreo en tiempo real.

Prohibido abandonar el área durante su operación para intervenir ante emergencias.

Ambiente de trabajo seguro

Elimine obstáculos y asegure que ninguna persona/objeto ingrese a la zona de riesgo antes de activar el robot.

Instale barreras físicas o cortinas luminosas de seguridad si es necesario.

Exención de responsabilidad

No nos hacemos responsables por lesiones, daños o accidentes causados por incumplimiento de normas de seguridad (ej: desatención, área no asegurada).

El usuario asume todos los riesgos operativos.

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

#### 5.1.2 Instalación  

**Instalación del servidor MCP:**  
1. Instalar Python 3.11 o superior  
2. Instalar pip 25.1 o superior  
3. Instalar UV Package Manager 0.6.14 o superior  
4. Instalar bun 1.2.8 o superior  
5. Instalar el servidor MCP:  
```
git clone https://gitee.com/nonead/nUR_MCP_SERVER.git  
cd nUR_MCP_SERVER  
pip install -r requirements.txt  
```  

**Configuración del cliente MCP:**  

**Para usar con Claude Desktop, agregue configuración de servidor:**
**Para macOS:** ~/Library/Application Support/Claude/claude_desktop_config.json  
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

**Para Windows:** %APPDATA%/Claude/claude_desktop_config.json  
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

**Para usar con Cline, agregue la configuración del servidor:**
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
            "command": "python",
            "args": ["D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
         }
      }
    }


### 5.2 Basado en toolkit (para desarrolladores)

#### 5.2.1 Motor y dependencias 

* **Versiones recomendadas del sistema:**

  ```text
  Usuarios de macOS: macOS Monterey 12.6 o superior
  Usuarios de Linux: CentOS 7 / Ubuntu 20.04 o superior
  Usuarios de Windows: Windows 10 LTSC 2021 o superior
  ```

* **Requisitos de software:**

  Entorno del servidor MCP

  ```text
  Python 3.11 o superior     
  pip 25.1 o superior
  UV Package Manager 0.6.14 o superior  
  bun 1.2.8 o superior
  ```
  Modelos de lenguaje grande LLM

  ```text
  DeepSeek-V3-0324 o superior
  DeepSeek-R1-671b o superior 
  Qwen3-235b-a22b o superior
  
  Generalmente, los modelos de lenguaje grande que admiten MCP son utilizables. Modelos no listados no han sido probados
  Los modelos implementados mediante Ollama actualmente no pueden llamar a Herramientas. En proceso de resolución...
  ```

#### 5.2.2 Instalación

**Para desarrolladores macOS/Linux/Windows**

```text
Python 3.11 o superior
pip 25.1 o superior
Gestor de paquetes UV 0.6.14 o superior
bun 1.2.8 o superior
```

#### 5.2.3 Uso

Ejemplos de tareas ejecutables por modelos lingüísticos avanzados:

* Conectar robot Universal IP: 192.168.1.199
* Obtener coordenadas de pose actual del efector final TCP
* Listar todos los comandos de la herramienta nUR_MCP_SERVER  
* Obtener todos los datos hardware del robot Universal  
* Ejecutar programa de script del robot Universal  
* Ejecutar programa incorporado XXXX.urp del robot  
* Definir robot IP 172.22.109.141 como Robot A e IP 172.22.98.41 como Robot B, conectar ambos, registrar poses TCP y posiciones clave actuales de A (izquierda) y B (derecha), analizar relación entre poses  
* Ejecución paso a paso: Robot Universal IP 192.168.1.199, registrar pose TCP actual, luego mover TCP +20mm en Z, -50mm en Y, +30mm en X, repetir 5 veces  
* Crear y ejecutar script para robot Universal: Dibujar círculo de 50mm de radio en plano base centrado en pose actual  
* Definir robots IP 172.22.109.141 como A y 172.22.98.41 como B, conectar, comandos posteriores controlarán solo A sincronizando movimiento espejo de B  

## 6. Arquitectura Técnica  

MCP utiliza arquitectura cliente-servidor con protocolos estandarizados para comunicación modelo-recursos externos.  
![alt](./images/MCP.svg "mcp")  
Modelo Cliente-Servidor  
Componentes principales:  

Host MCP: Aplicación LLM (ej. Claude Desktop o IDE) que inicia conexiones  
Cliente MCP: Cliente protocolario manteniendo conexión 1:1 con servidor  
Servidor MCP: Programa ligero exponiendo funcionalidad vía Model Context Protocol  
Fuentes de datos locales: Archivos, bases de datos y servicios accesibles seguramente por Servidor MCP  
Servicios remotos: Sistemas externos accesibles vía internet (ej. APIs)  
Responsabilidades:  

Host MCP:  
Provee interfaz de usuario  
Gestiona conexión con proveedor LLM  
Integra Cliente MCP para acceso a recursos externos  
Cliente MCP:  
Establece/mantiene conexión con Servidor MCP  
Envía solicitudes y recibe respuestas  
Maneja intercambio de datos según estándares MCP  
Servidor MCP:  
Procesa solicitudes de clientes  
Ejecuta funciones específicas o provee acceso a recursos  
Formatea respuestas según estándares MCP  
Protocolo de Comunicación  
MCP usa JSON-RPC 2.0 como protocolo base, soportando:  
![alt](./images/p.svg "mcp_json-RPC2.0")  
Solicitudes: Mensajes que inician operaciones cliente→servidor o viceversa  
Respuestas: Réplicas conteniendo resultados o información de error  
Notificaciones: Mensajes unidireccionales sin respuesta requerida (notificaciones)  
Mecanismos de transporte soportados:  

E/S estándar (Stdio): Para servidores locales vía comunicación entre procesos  
Eventos enviados por servidor (SSE): Transporte basado en HTTP para servidores remotos  

Ventajas de MCP  
MCP supera métodos tradicionales en unificación, seguridad y extensibilidad.  

Unificación  
Interacción estandarizada resuelve problemas de fragmentación:  

Acceso tipo plugin: Protocolo unificado para diversas fuentes de datos  
Compatibilidad multiplataforma: Soporta diferentes modelos/plataformas de IA  
Simplificación de desarrollo: Enfoque en lógica de negocio  
Seguridad  
Mecanismos integrados protegen datos:  

Protección de información sensible: Claves API/datos de usuario etc.  
Control de acceso: Servidor MCP permite restricciones granulares  
Procesamiento local: Evita subir datos sensibles a terceros  
Extensibilidad  
Diseño modular permite alta escalabilidad:  

Conexión multiservicio: Múltiples servicios conectables a clientes compatibles  
Expansión de ecosistema: Creciente biblioteca de componentes preconstruidos  
Capacidad de personalización: Desarrollo de Servidores MCP personalizados  

## 7. Contáctenos

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**Sitio web oficial**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="Contacto: Nonead Tech WeChat" width="200">  

## 8. Diferencias entre nUR MCP Server y otros servidores MCP

Los usuarios de nUR MCP Server deben tener una conciencia de seguridad extremadamente alta y haber completado la capacitación en el uso de robots Universal, ya que el modelo de lenguaje grande controla robots reales. El funcionamiento inadecuado puede causar lesiones personales y daños a la propiedad - por favor extreme las precauciones.

## 9. Cita

Si utiliza este software, cite de la siguiente manera:

* [nURMCP: NONEAD Universal-Robots Model Context Protocol Server](https://www.nonead.com)
* Nonead demuestra el verdadero significado de la fabricación inteligente, innovando para remodelar nuestro mundo.

## 10. Licencia

Este proyecto adopta un modelo de doble licencia segmentado por usuario (User-Segmented Dual Licensing).

**Principios básicos**
* Usuarios individuales y empresas/organizaciones ≤10 personas: Licencia Pública General GNU Affero v3.0 (AGPLv3) por defecto
* Empresas/organizaciones >10 personas: Requiere licencia comercial (Commercial License)

Definición "≤10 personas":
Número total de individuos en su organización (incluyendo empresas, ONGs, agencias gubernamentales, instituciones educativas o cualquier entidad) que acceden, usan o se benefician directa/indirectamente del software (nUR_MCP_SERVER), sin exceder 10 personas. Incluye desarrolladores, testers, operadores, usuarios finales, etc.

### 10.1 Licencia open source (Open Source License): AGPLv3 - Para particulares y organizaciones ≤10 personas
* Si es usuario individual o su organización cumple la definición "≤10 personas", puede usar, modificar y distribuir nUR_MCP_SERVER bajo AGPLv3. Texto completo en https://www.gnu.org/licenses/agpl-3.0.html
* **Obligación clave:** AGPLv3 exige que si modifica nUR_MCP_Server y lo provee como servicio web o distribuye versiones modificadas, debe proporcionar el código fuente completo bajo AGPLv3. Incluso para organizaciones ≤10 personas, si desea evitar esta obligación, necesita licencia comercial (ver abajo).
* Lea atentamente todos los términos de AGPLv3 antes de usar.

### 10.2 Licencia comercial (Commercial License) - Para organizaciones >10 personas o que deseen evitar obligaciones AGPLv3
* **Requisito obligatorio:** Si su organización **no** cumple "≤10 personas" (≥11 personas accediendo/usando/beneficiándose del software), **debe** obtener licencia comercial.
* **Opción voluntaria:** Incluso para organizaciones ≤10 personas, si su uso **no cumple** AGPLv3 (especialmente divulgación de código) o necesita términos comerciales **no provistos** por AGPLv3 (garantías, indemnización, sin restricciones Copyleft...), requiere licencia comercial.
* **Casos comunes que necesitan licencia comercial (no limitado a):**
  * Organización >10 personas
  * (Tamaño irrelevante) Distribuir versiones modificadas sin revelar código fuente modificado según AGPLv3
  * (Tamaño irrelevante) Ofrecer SaaS basado en nUR_MCP_SERVER modificado sin compartir código modificado
  * (Tamaño irrelevante) Políticas corporativas, contratos o requisitos que prohíban software AGPLv3 o requieran distribución cerrada/confidencialidad
* **Obtener licencia:** Contacte al equipo de desarrollo en service@nonead.com.

### 10.3 Contribuciones
* Aceptamos contribuciones comunitarias. Todas las contribuciones se consideran licenciadas bajo AGPLv3.
* Al contribuir (ej: Pull Request), acepta licenciar su código bajo AGPLv3 para este proyecto y todos los usuarios posteriores (ya sea bajo AGPLv3 o licencia comercial).
* También acepta que su contribución pueda incluirse en versiones comerciales de nUR_MCP_SERVER.

### 10.4 Otros términos
* Los términos específicos de licencias comerciales se rigen por contratos firmados.
* Los mantenedores se reservan el derecho de actualizar esta política (incluyendo umbrales). Actualizaciones se anunciarán en canales oficiales (repositorio, sitio web).


## 11. Equipo central de desarrollo

Equipo de desarrollo del servidor MCP de Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>