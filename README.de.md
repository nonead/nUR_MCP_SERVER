
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
    <a href='https://gitee.com/nonead/nUR_MCP_SERVER/releases/tag/nUR_MCP_Server_0.1.1'><img src='https://img.shields.io/static/v1?label=Gitee%20Latest%20Release&message=0.1.1&color=Blue' alt="Latest Release"></a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER/releases/latest"><img src="https://img.shields.io/static/v1?label=GitHub%20Latest%20Release&message=0.1.1&color=Green" alt="Latest Release"></a>
    <a href='https://www.python.org/downloads/'><img src='https://img.shields.io/pypi/pyversions/RPALite'></img></a>
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER/wikis/pages">
        <img src="https://img.shields.io/badge/User%20Guide-1e8b93?logo=readthedocs&logoColor=f5f5f5" alt="User Guide"></a>
    <a href="./LICENSE"><img height="21" src="https://img.shields.io/static/v1?label=License&message=User-Segmented Dual Licensing&color=blue" alt="license"></a>
     <a href='https://gitee.com/nonead/nUR_MCP_SERVER/stargazers'><img src='https://gitee.com/nonead/nUR_MCP_SERVER/badge/star.svg?theme=dark' alt='star'></img></a>
</p>

## 1. Was ist MCP?
Das MCP (Model Context Protocol) ist ein von Anthropic entwickeltes Kommunikationsprotokoll (Open Source ab November 2024), das Großsprachmodellen (wie DeepSeek-V3-0324, DeepSeek-R1, Qwen3 etc.) den effizienten Zugriff auf externe Daten/Tools/Dienste ermöglicht.

Hauptfunktionen:

Kontextbereitstellung:
Übermittlung von Dateien/Datenbankinhalten
Beispiel: Berichtsanalyse vor Antwort

Externe Tool-Nutzung:
Direkte Steuerung lokaler/entfernter Funktionen
Beispiel: Automatische Dokumentenorganisation

Workflow-Automatisierung:
Kombination mehrerer MCP-Dienste

Datensicherheit:
Lokale Ausführung schützt sensible Daten

## 2. Funktionsweise
Client-Server-Architektur:

MCP-Client: KI-Anwendung (sendet Anfragen)
MCP-Server: Stellt Schnittstellen bereit
Kommunikation: JSON-RPC 2.0 Standard

## 3. Serverfunktionen
Datenzugriff:
Dateien/Datenbanken/Arbeitsspeicher

Tool-Bereitstellung:
Vordefinierte Funktionen (SQL-Abfragen etc.)

Echtzeit-Updates:
Automatische Benachrichtigungen

Sitzungsverwaltung:
Verbindungsmanagement

## 2. nUR MCP Server Kernfunktionen  

### 2.1 Abrufen aller Hardware-Daten von UR-Robotern  
**Netzwerk-Scan-Funktion**  
fY6gJ6KcwVqfiiUFO-ogx1: Scannt einen bestimmten IP-Bereich für UR-Roboter  

**Verbindungsverwaltung**  
fCf-PPsfx_yD_iZLURtGTV: Verbindung zu einem UR-Roboter mit bestimmter IP herstellen  
fEd1Yp4RD3kiUSxqQlK1Va: Verbindung zu einem UR-Roboter trennen  

**Grundlegende Informationen**  
fmMqIRbJZ4qRGJtRd59OJ-: Seriennummer des Roboters abrufen  
f1ITpGFuwNDVfGfkNJzG2z: Softwareversion abrufen  
f8RnXWPeoSCCCvW3FuF_vS: Betriebszeit abrufen  
fl_BhgXwRaQ8nzexSGjwa7: Sicherheitsmodus abrufen  

**Registerdaten**  
fRRbXKNWy6vXbSrRPmFLJa: Int-Registerwerte abrufen (0-23)  
fRjcTzBeNogyaJtYvJ7_E2: Double-Registerwerte abrufen (0-23)  
fJ_s1E0ywr6t9rkMOBWiq6: Double-Registerwerte abrufen (0-31)  

**Statusüberwachung**  
fVYZ0ocbfuml1VpA5JSNRo: Echtzeit-TCP-Koordinaten abrufen  
fts21SISQrnyp_mb3jJy91: Echtzeit-Gelenkwinkel abrufen  
fmjZNwC7zxju_tLjiM8w4A: Betriebsstatus abrufen  
fy5NIEBXN7Kqecb1RkPhZN: Programmausführungsstatus abrufen  

**Elektrische Parameter**  
fGU3ubp1fmrw-zPE2pyNDI: Aktuelle Spannung abrufen  
fl--FA0LvH9LBjXjVB0gGD: Aktuellen Strom abrufen  
fb3HhLwWUa8s49OXpU5Iq8: Gelenkspannungen abrufen  
frGKnkZFPFesyEXdGAxpD9: Gelenkströme abrufen  
fzVxBGVvO7T3n3JbmAmvqB: Gelenktemperaturen abrufen  

### 2.2 Einzelbefehle für UR-Roboter ausführen  
**Bewegungssteuerung**  
ffoF99tQZ6vcEqHQplHTjv: Gelenkpositionsbefehl senden (movej)  
fiF4Pmxs7LQTrG7hY4sQV8: TCP-Linearbewegungsbefehl senden (movel)  
fOyQY2wR6xzOZP3NxjpLjK: Linearbewegung entlang der X-Achse  
fCV_0M8pdPIVJs3nMGo6XS: Linearbewegung entlang der Y-Achse  
fWkTyW-C5rxUPe3U0WGSsm: Linearbewegung entlang der Z-Achse  

### 2.3 UR-Roboterprogramme mit großen Sprachmodellen schreiben und ausführen  

### 2.4 Integrierte UR-Roboterprogramme ausführen  
**Programmsteuerung**  
fE0WxXcDh3ENo8Q3fYul5K: UR-Programm laden  
fDqpZeOA1_KF8ixwndRP8-: UR-Programm laden und ausführen  
fH1AYKDXPCcGU1q3Ndrnwt: Aktuelles Programm stoppen  
fVwECQj8_p85mT6KaggA-N: Aktuelles Programm pausieren  
f4cp0iAFlVXMWqz51ylP4Z: Programmscript senden  

### 2.5 Koordination mehrerer UR-Roboter  


## 3. Haftungsausschluss

Stellen Sie vor der Nutzung des nUR MCP Server sicher, dass das Bedienpersonal eine UR-Robotersicherheitsschulung absolviert hat und mit Not-Aus (E-Stop) vertraut ist.

Führen Sie regelmäßige Inspektionen des Roboters und des MCP Server durch, um Systemstabilität und Sicherheit zu gewährleisten.

Bei der Nutzung des nUR MCP Server sind folgende Sicherheitsvorschriften zwingend einzuhalten:

Sichtbereich des Roboters

Der Bediener muss den Universal Robots-Roboter stets im Sichtfeld behalten, um den Betriebszustand in Echtzeit überwachen zu können.

Verlassen des Arbeitsbereichs während des Betriebs ist verboten, um bei Notfällen eingreifen zu können.

Sichere Arbeitsumgebung

Vor dem Start sind Hindernisse zu beseitigen und sicherzustellen, dass sich keine Personen/Objekte im Gefahrenbereich befinden.

Bei Bedarf sind physische Schutzzäune oder Sicherheitslichtvorhänge zu installieren.

Haftungsfreistellung bei Verstößen

Bei Verletzungen, Geräteschäden oder Produktionsstörungen aufgrund von Sicherheitsverstößen (z.B. fehlende Überwachung, ungesicherter Arbeitsbereich) übernehmen wir keine rechtliche Haftung oder Entschädigungspflicht.

Alle Betriebsrisiken und Folgen trägt der Anwender.

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

**MCP-Server-Installation:**  
1. Python 3.11 oder höher installieren  
2. pip 25.1 oder höher installieren  
3. UV Package Manager 0.6.14 oder höher installieren  
4. bun 1.2.8 oder höher installieren  
5. MCP-Server installieren:  
```
git clone https://gitee.com/nonead/nUR_MCP_SERVER.git  
cd nUR_MCP_SERVER  
pip install -r requirements.txt  
```  

**MCP-Client-Konfiguration:**  

**Für die Verwendung mit Claude Desktop Serverkonfiguration hinzufügen:**
**Für macOS:** ~/Library/Application Support/Claude/claude_desktop_config.json  
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

**Für Windows:** %APPDATA%/Claude/claude_desktop_config.json  
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

**Zur Verwendung mit Cline fügen Sie die Serverkonfiguration hinzu:**
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


### 5.2 Toolkit-basiert (für Entwickler)

#### 5.2.1 Engine & Abhängigkeiten 

* **Empfohlene Systemversionen:**

  ```text
  macOS-Benutzer: macOS Monterey 12.6 oder neuer
  Linux-Benutzer: CentOS 7 / Ubuntu 20.04 oder neuer
  Windows-Benutzer: Windows 10 LTSC 2021 oder neuer
  ```

* **Softwareanforderungen:**

  MCP-Serverumgebung

  ```text
  Python 3.11 oder neuer     
  pip 25.1 oder neuer
  UV Package Manager 0.6.14 oder neuer  
  bun 1.2.8 oder neuer
  ```
  LLM-Großsprachmodelle

  ```text
  DeepSeek-V3-0324 oder neuer
  DeepSeek-R1-671b oder neuer 
  Qwen3-235b-a22b oder neuer
  
  Allgemein sind Großsprachmodelle, die MCP unterstützen, verwendbar. Nicht aufgeführte Modelle wurden nicht getestet
  Mit Ollama bereitgestellte Modelle können derzeit keine Tools aufrufen. Wird bearbeitet...
  ```

#### 5.2.2 Installation

**Für macOS/Linux/Windows-Entwickler**

```text
Python 3.11 oder neuer
pip 25.1 oder neuer
UV Paketmanager 0.6.14 oder neuer
bun 1.2.8 oder neuer
```

#### 5.2.3 Verwendung

Beispiele für Aufgaben, die von großen Sprachmodellen ausgeführt werden können:

* Universal-Roboter-IP verbinden: 192.168.1.199  
* Aktuelle TCP-Endeffektor-Position des Universal-Roboters abrufen  
* Alle Befehle des nUR_MCP_SERVER-Tools auflisten  
* Alle Hardware-Daten des Universal-Roboters abrufen  
* Skriptprogramm des Universal-Roboters ausführen  
* Integriertes Programm XXXX.urp des Roboters ausführen  
* Roboter mit IP 172.22.109.141 als A und IP 172.22.98.41 als B definieren, verbinden, aktuelle TCP-Positionen und Schlüsselpositionen von A (links) und B (rechts) aufzeichnen, Positionsbeziehung analysieren  
* Schrittweise Ausführung: Universal-Roboter IP 192.168.1.199, aktuelle TCP-Position aufzeichnen, dann TCP um +20mm in Z, -50mm in Y, +30mm in X bewegen, 5 Mal wiederholen  
* Universal-Roboter-Skript erstellen/ausführen: Kreis mit 50mm Radius in Basisebene um aktuelle Position zeichnen  
* Roboter mit IP 172.22.109.141 als A und 172.22.98.41 als B definieren/verbinden, nachfolgende Befehle steuern nur A mit synchroner Spiegelbewegung von B  

## 6. Technische Architektur  

MCP nutzt Client-Server-Architektur mit standardisierten Protokollen für Modell-zu-externen-Ressourcen-Kommunikation.  
![alt](./images/MCP.svg "mcp")  
Client-Server-Modell  
Kernkomponenten:  

MCP-Host: LLM-Anwendung (z.B. Claude Desktop) die Verbindungen initiiert  
MCP-Client: Protokollclient der 1:1 Serververbindung in Host-App verwaltet  
MCP-Server: Leichtgewichtiges Programm das Funktionen via standardisiertes Model Context Protocol bereitstellt  
Lokale Datenquellen: Dateien/Datenbanken/Dienste sicher zugänglich für MCP-Server  
Remote-Dienste: Externe Systeme via Internet erreichbar (z.B. APIs)  
Zuständigkeiten:  

MCP-Host:  
Stellt Benutzeroberfläche bereit  
Verwaltet LLM-Anbieterverbindung  
Integriert MCP-Client für externen Ressourcenzugriff  
MCP-Client:  
Stellt/erhält MCP-Serververbindung aufrecht  
Sendet Anfragen/empfängt Antworten  
Verarbeitet Datenaustausch gemäß MCP-Standards  
MCP-Server:  
Verarbeitet Clientanfragen  
Führt spezifische Funktionen aus oder ermöglicht Ressourcenzugriff  
Formatiert Antworten gemäß MCP-Protokollstandards  
Kommunikationsprotokoll  
MCP verwendet JSON-RPC 2.0 als Basisprotokoll, unterstützt:  
![alt](./images/p.svg "mcp_json-RPC2.0")  
Anfragen: Nachrichten die Operationen von Client→Server oder umgekehrt initiieren  
Antworten: Rückmeldungen zu Anfragen mit Ergebnissen/Fehlerinformationen  
Benachrichtigungen: Einweg-Nachrichten ohne Antwort (typisch für Ereignismeldungen)  
Unterstützte Transportmechanismen:  

Standard-E/A (Stdio): Für lokale Server via Prozesskommunikation  
Server-Sent Events (SSE): HTTP-basierter Transport für Remote-Server  

MCP-Vorteile  
MCP übertrifft traditionelle Methoden in Einheitlichkeit, Sicherheit und Erweiterbarkeit.  

Einheitlichkeit  
Standardisierte Interaktion löst Fragmentierungsprobleme:  

Plugin-artiger Zugang: Einheitliches Protokoll für diverse Datenquellen  
Plattformübergreifende Kompatibilität: Unterstützt verschiedene KI-Modelle/Plattformen  
Entwicklungsvereinfachung: Fokus auf Geschäftslogik  
Sicherheit  
Integrierte Sicherheitsmechanismen schützen Daten:  

Sensible Informationssicherung: API-Schlüssel/Benutzerdaten etc.  
Zugriffskontrolle: MCP-Server ermöglicht granulare Zugriffsbeschränkungen  
Lokale Verarbeitung: Vermeidet Upload sensibler Daten zu Dritten  
Erweiterbarkeit  
Modulares Design ermöglicht hohe Skalierbarkeit:  

Multi-Service-Verbindung: Mehrere Dienste mit kompatiblen Clients verbindbar  
Ökosystemerweiterung: Wachsende Bibliothek vorgefertigter Komponenten  
Anpassungsfähigkeit: Entwicklung benutzerdefinierter MCP-Server möglich  

## 7. Kontakt

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**Offizielle Website**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="Kontakt: Nonead Tech WeChat" width="200">  

## 8. Unterschiede zwischen nUR MCP Server und anderen MCP Servern

Benutzer des nUR MCP Servers müssen ein sehr hohes Sicherheitsbewusstsein haben und eine Schulung zur Verwendung von Universal Robots absolviert haben, da das große Sprachmodell echte Roboter steuert. Fehlbedienungen können zu Personenschäden und Sachschäden führen. Bitte seien Sie äußerst vorsichtig.

## 9. Zitierung

Wenn Sie diese Software verwenden, zitieren Sie bitte wie folgt:

* [nURMCP: NONEAD Uninversal-Robots Model Context Protocol Server](https://www.nonead.com)
* Nonead zeigt die wahre Bedeutung der intelligenten Fertigung und führt Innovationen an, die unsere Welt verändern. <br>
  Nonead demonstrates the true meaning of intelligent manufacturing, pioneering innovations that reshape our world.

## 10. Lizenz

Dieses Projekt verwendet ein benutzersegmentiertes Dual-Lizenzmodell (User-Segmented Dual Licensing).

**Grundprinzipien**
* Privatnutzer und Unternehmen/Organisationen mit ≤10 Personen: Standardmäßig GNU Affero General Public License v3.0 (AGPLv3)
* Unternehmen/Organisationen mit >10 Personen: Erfordert eine kommerzielle Lizenz (Commercial License)

Definition "≤10 Personen":
Die Gesamtzahl der Personen in Ihrer Organisation (einschließlich Unternehmen, NGOs, Regierungsbehörden, Bildungseinrichtungen oder anderen Entitäten), die direkt/indirekt auf die Software (nUR_MCP_SERVER) zugreifen, sie nutzen oder davon profitieren, darf 10 Personen nicht überschreiten. Dies umfasst Entwickler, Tester, Betreiber, Endnutzer etc.

### 10.1 Open-Source-Lizenz (AGPLv3) - Für Privatpersonen und Organisationen mit ≤10 Personen
* Wenn Sie Privatnutzer sind oder Ihre Organisation die "≤10 Personen"-Definition erfüllt, können Sie nUR_MCP_SERVER unter AGPLv3 nutzen, modifizieren und verteilen. Vollständiger Text unter https://www.gnu.org/licenses/agpl-3.0.html
* **Schlüsselverpflichtung:** AGPLv3 verlangt, dass bei Modifikationen von nUR_MCP_Server und Bereitstellung als Webdienst oder Verteilung modifizierter Versionen der vollständige Quellcode unter AGPLv3 bereitgestellt werden muss. Selbst für Organisationen mit ≤10 Personen gilt: Falls Sie diese Verpflichtung umgehen möchten, benötigen Sie eine kommerzielle Lizenz (siehe unten).
* Lesen Sie alle AGPLv3-Bedingungen sorgfältig vor der Nutzung.

### 10.2 Kommerzielle Lizenz - Für Organisationen mit >10 Personen oder zur Umgehung von AGPLv3-Verpflichtungen
* **Zwingende Voraussetzung:** Wenn Ihre Organisation **nicht** "≤10 Personen" erfüllt (≥11 Personen mit Zugriff/Nutzung/Profit von der Software), **müssen** Sie eine kommerzielle Lizenz erwerben.
* **Freiwillige Option:** Selbst für Organisationen mit ≤10 Personen: Falls Ihre Nutzung **nicht** AGPLv3 entspricht (insbesondere Quellcode-Offenlegung) oder Sie kommerzielle Bedingungen benötigen, die **nicht** durch AGPLv3 abgedeckt sind (Garantien, Entschädigung, keine Copyleft-Beschränkungen...), ist eine kommerzielle Lizenz erforderlich.
* **Häufige Fälle, die eine kommerzielle Lizenz erfordern (nicht abschließend):**
  * Organisation mit >10 Personen
  * (Größe irrelevant) Verteilung modifizierter Versionen ohne Offenlegung des modifizierten Quellcodes gemäß AGPLv3
  * (Größe irrelevant) Bereitstellung von SaaS basierend auf modifiziertem nUR_MCP_SERVER ohne Weitergabe des modifizierten Codes
  * (Größe irrelevant) Unternehmensrichtlinien, Verträge oder Anforderungen, die AGPLv3-Software verbieten oder geschlossene Vertraulichkeit verlangen
* **Lizenzierung:** Kontaktieren Sie das Entwicklungsteam unter service@nonead.com.

### 10.3 Beiträge
* Community-Beiträge sind willkommen. Alle Beiträge gelten als unter AGPLv3 lizenziert.
* Durch Beitragseinreichung (z.B. Pull Request) erklären Sie sich damit einverstanden, Ihren Code unter AGPLv3 für dieses Projekt und alle zukünftigen Nutzer (ob unter AGPLv3 oder kommerzieller Lizenz) zu lizenzieren.
* Sie akzeptieren auch, dass Ihr Beitrag in kommerziellen Versionen von nUR_MCP_SERVER enthalten sein kann.

### 10.4 Weitere Bedingungen
* Spezifische Bedingungen kommerzieller Lizenzen unterliegen den unterzeichneten Verträgen.
* Die Projektbetreuer behalten sich das Recht vor, diese Richtlinie (einschließlich Schwellenwerten) zu aktualisieren. Änderungen werden über offizielle Kanäle (Repository, Website) bekannt gegeben.

## 11. Entwicklung Kernteam

MCP Server Entwicklungsteam der Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>