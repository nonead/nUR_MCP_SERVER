
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
      <img height="20" src="https://gitee.com/nonead/nUR_MCP_SERVER/badge/star.svg?theme=dark" alt="Gitee Stars"></img>
    </a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER">
      <img src="https://img.shields.io/github/forks/nonead/nUR_MCP_SERVER?label=Forks&style=flat-square" alt="Github Forks"></img>
    </a>
    <a href='https://github.com/nonead/nUR_MCP_SERVER'>
      <img src="https://img.shields.io/github/stars/nonead/nUR_MCP_SERVER.svg?style=flat-square&label=Stars&logo=github" alt="Github Stars"/></img>
    </a>
</p>

## 1.Hvad er MCP?
MCP (Model Context Protocol) er en forbindelsesprotokol udviklet af firmen Anthropic og gendanneval som open source i november 2024. Den bruges til at gøre store AI-\Vasker (som DeepSeek-V3-0324, DeepSeek-R1 og Qwen3) mere effektive ved at give dem adgang til eksterne data, værktøjer og serviicer. Derved kan den give mere præcis og intelligente svar.
Hvad kan MCP gøre?

Nuværten af kontekst information:

Anvendelsprogrammer kan overføre filer, databaseinhalte osv. til AI, hvilket hjælper det til at forstå problemet bedre.

For eksempel: Lå AI læse en rapport og svar derefter baseret på rapportens indhold.

Udførelse af handlinger:

AI kan via MCP direkte operere lokale eller distancered funktionaliteter, som leje/værdi filer, forefrage databaser, oprette API-anrop osv., og kontrollere hardvardekstrukturer.

For eksempel: Lå AI automatisere dokumentoverblikket eller extrahere data fra en database til rapportgenerering.

Opret af intelligente workflow:

Udviklere kan kombinere flere MCP-servicer, så AI kan udføre mere komplekse opgaver, som automatiseret datanalys og intelligent kundeservice.

Beskyttelse af dataetsIntegritet:

MCP kører lokalt, hvilket forhæmmes følsomt data fra at blive uploadet til cloud, og beskytter den personlighed.

## 2.Hvordan fungerer MCP?
MCP bruger en kundebeskrivelse-Serverarkitektur (Client-Server):
MCP-kundebeskrivelse:

Dette er typisk en AI-anvendelse (som Claude eller andre LLM-verk), der sender anmodninger til Server.

MCP-Server:

Kører lokalt eller distanceret og levererer data eller værktøj-intfacer til AI kan forenqværdi.

Forbindelses_måde:

Baseret på JSON-RPC 2.0 (en standard forbindelse_format), der understøtter anmodninger, svar og i-tidshitsnotifikationer.

## 3. Hovedfunktioner i MCP-serveren  

MCP-serveren fungerer som AI's "assistent" og kan levere følgende support:  

**Adgang til data (Resource Exposure)**  
Giver adgang til filer, databaser, hukommelsesdata osv., f.eks.:  
- `file:///docs/report.pdf` (læser lokal fil)  
- `db://sales/records` (søger i database)  

**Udførelse af handlinger (Tool Provisioning)**  
Tilbyder funktioner, der kan kaldes, f.eks.:  
- `search_database(sql_query)` (udfører SQL-forespørgsel)  
- `save_file(path, content)` (gemmer fil)  

**Realtidsoppdateringer (Dynamic Notification)**  
Når data ændres, kan serveren aktivt underrette AI'en for at sikre, at informationen er ajour.  

**Sessionstyring (Session Management)**  
Håndterer forbindelsen mellem AI'en og serveren for at sikre stabil kommunikation.

## 2. nUR MCP Server kernefunktioner  

Teknisk beskrivelse af nUR_MCP_SERVER-produktet udviklet af Nonead Corporation

Produktoversigt:
nUR_MCP_SERVER er en intelligent robotstyringsmiddleware bygget på MCP-protokollen (Model Control Protocol) med LLM-integration til naturlig sproglig interaktion med industrierobotter. Client-Server-arkitekturen understøtter dyb integration med Universal Robots' hele serie og transformerer traditionel teach pendant-programmering.

Kernteknologi:
1. Semantisk analyseengine
NLP-modul med multilayer Transformer-arkitektur understøtter kontekstbevidst kommandoparsning (98,6% nøjagtighed) og end-to-end-konvertering af naturligt sprog til robotkommandoer.

2. Dynamisk scriptgenerering
LLM-baseret kodegenerering konverterer automatisk naturlige sprogkommandoer til URScript (12x hurtigere end traditionel programmering) med realtids syntakscheck og sikkerhedsvalidering.

3. Multimodal styringssnitflade
- MCP-protokoludvidelse: Understøtter TCP/UDP dual-mode kommunikation (µs-respons)
- Enhedsabstraktionslag: Standardiseret URCap-plugin-integration
- Databus: TCP/IP-baseret multi-enhedsstyring

Nøglefunktioner:
▶ Naturlig sprogstyring
Direkte bevægelseskontrol (positionsstyring, banegenerering, I/O) via stemme/tekstkommandoer med dynamisk parameterindførsel og realtidsjustering.

▶ Intelligent dataindsamling
- Realtids indsamling af 12D tilstandsdata (ledmoment, endeffektorposition)
- Naturligt sprogdefinerede datafiltreringsregler
- Automatisk rapportgenerering (CSV/JSON/XLSX)

▶ Multi-robotkoordinering
Distribueret opgaveledelsesalgoritme + Tords MCP-Client til styring af ≤12 UR-robotter samtidig med stemmekaskadekommandoer og tværenhedsopgaveorchestering.

▶ Adaptiv læringsmodul
Indbygget inkrementel træningsramme optimerer kommando-handling-mapping via brugerfeedback (læringscyklus ≤24 timer).

Specifikationer:
- Kommandoforsinkelse: <200ms (end-to-end)
- Protokolkompatibilitet: MCP v2.1+/URScript 5.0+
- Samtidig kapacitet: 200+ TPS

### **2.1 Netværk og Forbindelseshåndtering**  
- **fifQB5xNlEkpHGCAPl4DuR**  
  ▸ Funktion: Scan UR-robotter i samme netværk  
  ▸ Parametre: `ip` (IP i samme netværk)  

- **fE5gA9T733lcQ8Hd_MLP82**  
  ▸ Funktion: Opret forbindelse til UR-robot  
  ▸ Parametre: `ip` (robot-IP)  

- **fsX43cYxV0PI4evuVyUBQb**  
  ▸ Funktion: Afbryd forbindelse til UR-robot  
  ▸ Parametre: `ip` (robot-IP)  

---  

### **2.2 Robotstatusovervågning**  
- **fOIkmMPGlGGxwyw-3P9PLw**  
  ▸ Funktion: Hent opetid  
  ▸ Parametre: `ip`  

- **fwyyKaqkrt6NBWXlSqhla2**  
  ▸ Funktion: Hent serienummer  
  ▸ Parametre: `ip`  

- **f6sWepY5YsPIqDuVllQixz**  
  ▸ Funktion: Hent softwareversion  
  ▸ Parametre: `ip`  

- **fJmgMj32RjjCxzg3n-OmKs**  
  ▸ Funktion: Hent sikkerhedstilstand  
  ▸ Parametre: `ip`  

- **fAJNyeIvDxM49kypgXs9xx**  
  ▸ Funktion: Hent køretilstand  
  ▸ Parametre: `ip`  

- **frXKuqREVTmRygel-MDG11**  
  ▸ Funktion: Hent programudførelsestilstand  
  ▸ Parametre: `ip`  

---  

### **2.3 Register- og dataaflæsning**  
- **fOXjbOy_B40SqwczE0zRRx**  
  ▸ Funktion: Læs Int-register (0~23)  
  ▸ Parametre: `ip`, `index` (0-23)  

- **ftWfHugqIFU3zE1k4szoST**  
  ▸ Funktion: Læs Double-register (0~23)  
  ▸ Parametre: `ip`, `index` (0-23)  

- **f-CXiO_NaDsWiwltfrDhks**  
  ▸ Funktion: Læs Double-register (0~31)  
  ▸ Parametre: `ip`, `index` (0-31)  

---  

### **2.4 Bevægelseskontrol**  
- **fq5lK3nuHMu6AR1AOolkVT**  
  ▸ Funktion: Bevægelse i ledrum  
  ▸ Parametre: `ip`, `q` (ledvinkler), `a`/`v`/`t`/`r` (valgfrit)  

- **fepruq4N7v4MBNqsiIvLRc**  
  ▸ Funktion: TCP-lineær bevægelse  
  ▸ Parametre: `ip`, `pose` (TCP-position), `a`/`v`/`t`/`r` (valgfrit)  

- **fcKCrZ2H_lwnAe4P2uTJ4L**  
  ▸ Funktion: Lineær bevægelse langs X-aksen  
  ▸ Parametre: `ip`, `distance` (meter)  

- **f77gv6fXQGTSKbsgemu8Np**  
  ▸ Funktion: Lineær bevægelse langs Y-aksen  
  ▸ Parametre: `ip`, `distance`  

- **f-bIJDZENUgzPrLJqOFvIs**  
  ▸ Funktion: Lineær bevægelse langs Z-aksen  
  ▸ Parametre: `ip`, `distance`  

---  

### **2.5 Programhåndtering**  
- **ftdgwJLZQ2dYp2mB1ZtRPD**  
  ▸ Funktion: Indlæs program  
  ▸ Parametre: `ip`, `program_name`  

- **fl1XHdiQ-GgEJPB7rlMaHU**  
  ▸ Funktion: Indlæs og udfør program  
  ▸ Parametre: `ip`, `program_name`  

- **fL8CYEkias2SbMtv0S7s-N**  
  ▸ Funktion: Stop nuværende program  
  ▸ Parametre: `ip`  

- **fkS98Mpak4obl30wTves1K**  
  ▸ Funktion: Paus nuværende program  
  ▸ Parametre: `ip`  

- **fV_tezoVRKYr9IiYnl2ezU**  
  ▸ Funktion: Send scriptprogram  
  ▸ Parametre: `ip`, `script`  

---  

### **2.6 Sensor- og strømovervågning**  
- **fW18vf-tvLsFR-8coc2e5U**  
  ▸ Funktion: Hent nuværende spænding  
  ▸ Parametre: `ip`  

- **fEK48x3yHMxEx14KQsVzjZ**  
  ▸ Funktion: Hent nuværende strøm  
  ▸ Parametre: `ip`  

- **fEh1yfbkyrh-kr2PDF7XI5**  
  ▸ Funktion: Hent ledspænding  
  ▸ Parametre: `ip`  

- **fsmxaF8Agn8NF0mMegv3_f**  
  ▸ Funktion: Hent ledstrøm  
  ▸ Parametre: `ip`  

- **fdGsS6kwiGlY_zybhYQWrS**  
  ▸ Funktion: Hent ledtemperatur  
  ▸ Parametre: `ip`  

---  

### **2.7 Realtidsdatafeedback**  
- **f6danXc2Pz98ilo5gMNc44**  
  ▸ Funktion: Hent realtids TCP-koordinater  
  ▸ Parametre: `ip`  

- **fwHgxwtA4blZuetfmJ3OiK**  
  ▸ Funktion: Hent realtids ledvinkler  
  ▸ Parametre: `ip`  

---  

## 3. Ansvarsfraskrivelse

Før brug af nUR MCP Server skal operatører gennemføre UR-robotsikkerhedstræning og kunne håndtere nødstop (E-stop).

Kontroller regelmæssigt robot og MCP Server for at sikre systemstabilitet.

Følgende sikkerhedsregler skal overholdes:

Robottens synsfelt

Operatøren skal altid holde Universal Robots-robotten inden for synsvidde for realtidskontrol.

Forlad ikke arbejdsområdet under drift for at forebygge uheld.

Sikker arbejdszone

Fjern forhindringer og sikr, at ingen personer/objekter er i farezonen før aktivering.

Installer fysiske barrierer eller sikkerhedsgitter ved behov.

Ansvarsbegrænsning

Vi påtager os ikke ansvar for personskader, udstyrsfejl eller produktionsincidenter forårsaget af sikkerhedsbrist (f.eks. uovervåget drift).

Brugeren bærer alle operationelle risici.

## 4. Versioner og udgivelser

### 4.1 Seneste opdateringer

* **2025.05.15**: Første udgivelse af nUR_MCP_SERVER

### 4.2 Fremtidige planer

* Udvikle en dedikeret MCP-klient til nUR MCP-server for at forbedre aktuatorens sikkerhedsfunktioner
* Tilføje logføringsfunktionalitet for UR-robotter
* Muliggøre backup og upload af UR-robotprogrammer

## 5. Hurtig start

### 5.1 Produktbaseret (til almindelige brugere)

#### 5.1.1 Motor og afhængigheder

* **Anbefalede systemversioner:**

  ```text
  macOS-brugere: macOS Monterey 12.6 eller nyere
  Linux-brugere: CentOS 7 / Ubuntu 20.04 eller nyere
  Windows-brugere: Windows 10 LTSC 2021 eller nyere
  ```

* **Softwarekrav:**

  **MCP-servermiljø**

  ```text
  Python 3.11 eller nyere
  pip 25.1 eller nyere
  UV Package Manager 0.6.14 eller nyere
  bun 1.2.8 eller nyere
  ```

  **MCP-klient**

  ```text
  Claude Desktop 3.7.0 eller nyere
  Cherry Studio 1.2.10 eller nyere
  Cline 3.14.1 eller nyere

  ClaudeMind, Cursor, NextChat, ChatMCP, Copilot-MCP, Continue, Dolphin-MCP, Goose - Ikke testet.
  ```

  **LLM store sprogmodeller**

  ```text
  DeepSeek-V3-0324 eller nyere
  DeepSeek-R1-671b eller nyere
  Qwen3-235b-a22b eller nyere

  Generelt kan enhver MCP-understøttet LLM bruges. Modeller ikke nævnt her er ikke testet.
  Ollama-implementerede modeller kan i øjeblikket ikke aktivere Tools (under løsning)...
  ```

#### 5.1.2 Installation  

**Installation af MCP-server:**  
1. Installer Python 3.11 eller nyere  
2. Installer pip 25.1 eller nyere  
3. Installer UV Package Manager 0.6.14 eller nyere  
4. Installer bun 1.2.8 eller nyere  
5. Installer MCP-server:  
```
git clone https://gitee.com/nonead/nUR_MCP_SERVER.git  
cd nUR_MCP_SERVER  
pip install -r requirements.txt  
```  

**Konfiguration af MCP-klient:**  

**For brug med Claude Desktop, tilføj serverkonfiguration:**
**Til macOS:**  ~/Library/Application Support/Claude/claude_desktop_config.json  
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

**Til Windows:**  %APPDATA%/Claude/claude_desktop_config.json  
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

**For brug med Cherry Studio, tilføj serverkonfiguration:**  

**Til macOS & Linux:**  
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

**Til Windows:**  
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

**For brug med Cline, tilføj serverkonfiguration:**  

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

**Til macOS/Linux/Windows-udviklere**

```text
Python 3.11 eller nyere
pip 25.1 eller nyere
UV Pakkehåndtering 0.6.14 eller nyere
bun 1.2.8 eller nyere
```

#### 5.2.3 Brug

Eksempler på opgaver store sprogmodeller kan udføre:

* Tilslut Universal Robot IP: 192.168.1.199
* Hent aktuel TCP-endeeffektor-pose
* List alle kommandoer i nUR_MCP_SERVER-værktøj
* Hent alle hardware-data fra Universal Robot
* Kør Universal Robot-scriptprogram
* Eksekver indbygget program XXXX.urp
* Definer robot med IP 172.22.109.141 som A og IP 172.22.98.41 som B, tilslut begge, registrer aktuelle TCP-poser og nøglepositioner for A (venstre) og B (højre), analyser pose-forhold
* Trinvis udførelse: Universal Robot IP 192.168.1.199, registrer aktuel TCP-pose, flyt derefter TCP +20mm i Z, -50mm i Y, +30mm i X, gentag 5 gange
* Skriv og eksekver Universal Robot-script: Tegn 50mm radius cirkel i basisplan centreret på aktuel pose
* Definer robotter med IP 172.22.109.141 som A og 172.22.98.41 som B, tilslut, efterfølgende kommandoer kontrollerer kun A mens B synkroniseres spejlet

## 6. Teknisk Arkitektur

MCP bruger klient-server-arkitektur med standardiserede protokoller til model-ekstern ressource kommunikation.  
![alt](./images/MCP.svg "mcp")  
Klient-Server Model
Kernekkomponenter:

MCP Vært: LLM-applikation (f.eks. Claude Desktop) der initierer forbindelser
MCP Klient: Protokolklient der vedligeholder 1:1 serverforbindelse
MCP Server: Letvægtsprogram der eksponerer funktionalitet via standardiseret Model Context Protocol
Lokale datakilder: Filer, databaser og tjenester sikkert tilgængelige for MCP Server
Eksterne tjenester: Systemer tilgængelige via internet (f.eks. APIs)
Ansvarsområder:

MCP Vært:
Tilbyder brugergrænseflade
Håndterer forbindelse til LLM-udbyder
Integrerer MCP Klient til ekstern ressourceadgang
MCP Klient:
Etablerer/vedligeholder serverforbindelse
Sender anmodninger og modtager svar
Håndterer dataudveksling efter MCP-standarder
MCP Server:
Behandler klientanmodninger
Eksekverer specifikke funktioner eller giver ressourceadgang
Formatterer svar efter MCP-protokolstandarder
Kommunikationsprotokol
MCP bruger JSON-RPC 2.0 som basisprotokol, understøtter:  
![alt](./images/p.svg "mcp_json-RPC2.0")  
Anmodninger: Beskeder der initierer operationer klient→server eller omvendt
Svar: Svar på anmodninger med resultater eller fejlinformation
Notifikationer: Envejsbeskeder uden svarkrav (typisk begivenhedsnotifikationer)
Understøttede transportmekanismer:

Standard I/O (Stdio): Til lokale servere via interproceskommunikation
Server-Sent Events (SSE): HTTP-baseret transport til eksterne servere

MCP Fordele
MCP overgår traditionelle integrationsmetoder i ensartethed, sikkerhed og udvidelsesevne.

Ensartethed
Standardiseret interaktion løser fragmenteringsproblemer:

Plugin-style adgang: Ensartet protokol til diverse datakilder
Tværgående kompatibilitet: Understøtter forskellige AI-modeller/platforme
Udviklingsforenkling: Fokus på forretningslogik
Sikkerhed
Indbyggede sikkerhedsmekanismer beskytter data:

Følsom informationsbeskyttelse: API-nøgler/brugerdata etc.
Adgangskontrol: MCP Server muliggør detaljerede restriktioner
Lokal behandling: Undgår upload af følsomme data til tredjeparter
Udvidelsesevne
Moduldesign muliggør høj skalerbarhed:

Multitjenestetilslutning: Flere tjenester kan forbindes til kompatible klienter
Økosystemudvidelse: Voksende bibliotek af præbyggede komponenter
Tilpasningsevne: Udvikling af brugerdefinerede MCP Servere

## 7. Kontakt os

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**Officiel hjemmeside**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="Kontakt: Nonead Tech WeChat" width="200">  

## 8. Forskelle mellem nUR MCP Server og andre MCP-servere

Brugere af nUR MCP Server skal have ekstremt høj sikkerhedsbevidsthed og have gennemført Universal Robots-operationsuddannelse, da den store sprogmodel styrer faktiske robotter. Forkert brug kan forårsage personskade og materiel skade - vær venligst yderst forsigtig.

## 9. Citation

Hvis du bruger denne software, citer venligst som følger:

* [nURMCP: NONEAD Universal-Robots Model Context Protocol Server](https://www.nonead.com)
* Nonead demonstrerer den sande betydning af intelligent produktion, der er foregangsmand for innovationer, der omformer vores verden.

## 10. Licens

Dette projekt anvender en User-Segmented Dual Licensing-model.

**Grundlæggende principper**
* Privatbrugere og organisationer/ virksomheder med ≤10 personer: AGPLv3-licensen gælder automatisk
* Organisationer/ virksomheder med >10 personer: Kommerciel licens kræves

Definition af "≤10 personer":
Dette refererer til situationer, hvor det samlede antal personer i din organisation (inklusiv virksomheder, non-profit organisationer, statslige institutioner, uddannelsesinstitutioner mv.), der direkte eller indirekte får adgang til, bruger eller drager fordel af nUR_MCP_SERVER, ikke overstiger 10. Dette inkluderer men er ikke begrænset til udviklere, testpersonale, operatører, slutbrugere og brugere via integrerede systemer.

### 10.1 Open Source-licens (AGPLv3) - Til privatbrugere og organisationer med ≤10 personer
* Hvis du er privatbruger eller din organisation opfylder "≤10 personer"-definitionen, kan du frit bruge, modificere og redistribuere nUR_MCP_SERVER under AGPLv3-betingelserne. Den fulde AGPLv3-licens kan findes på https://www.gnu.org/licenses/agpl-3.0.html.
* **Vigtigste forpligtelser:** Som et kernekrav i AGPLv3 skal du give modtagerne adgang til den fulde kildekode under AGPLv3, hvis du distribuerer modificerede versioner af nUR_MCP_Server eller tilbyder det som en netværkstjeneste. Selvom din organisation opfylder "≤10 personer"-kriteriet, bør du overveje en kommerciel licens (se nedenfor), hvis du ønsker at undgå denne kildekode-offentliggørelsesforpligtelse.
* Læs og forstå alle AGPLv3-vilkår grundigt før brug.

### 10.2 Kommerciel licens - Til organisationer med >10 personer eller brugere, der ønsker at undgå AGPLv3-forpligtelser
* **Obligatorisk krav:** Hvis din organisation ikke opfylder "≤10 personer"-definitionen (dvs. 11+ personer får adgang til/bruger/drager fordel af softwaren), skal du indgå en kommerciel licensaftale med os før brug af nUR_MCP_SERVER.
* **Valgfri anvendelse:** Selvom din organisation opfylder "≤10 personer"-kriteriet, kræves en kommerciel licens, hvis din brugssituation ikke overholder AGPLv3-vilkår (især kildekode-offentliggørelsesforpligtelsen) eller hvis du har brug for specifikke kommercielle bestemmelser (såsom garanti, erstatning eller fravær af Copyleft-begrænsninger), som ikke tilbydes under AGPLv3.
* **Typiske tilfælde, der kræver kommerciel licens (ikke udtømmende):**
  * Organisationer med >10 personer
  * (Uanset størrelse) Distribution af modificerede versioner af nUR_MCP_SERVER uden at offentliggøre kildekoden som krævet af AGPLv3
  * (Uanset størrelse) Tilbud af nUR_MCP_SERVER som en netværkstjeneste (SaaS) uden at give brugere adgang til modificeret kildekode
  * (Uanset størrelse) Hvis virksomhedspolitikker, kundekontrakter eller projektkrav forbyder brug af AGPLv3-licenseret software eller kræver lukket distribution/fortrolighed
* **Anskaffelse af kommerciel licens:** Kontakt nUR_MCP_SERVER-udviklingsteamet på service@nonead.com.

### 10.3 Bidrag (Contributions)
* Vi byder velkommen til bidrag fra fællesskabet til nUR_MCP_SERVER. Alle bidrag til projektet betragtes som leveret under AGPLv3-licensen.
* Ved at indsende et bidrag (f.eks. en Pull Request) accepterer du, at din kode vil blive gjort tilgængelig for projektet og alle fremtidige brugere (uanset om de vælger AGPLv3 eller kommerciel licens) under AGPLv3-vilkårene.
* Du accepterer også, at dit bidrag kan inkluderes i versioner af nUR_MCP_SERVER, der distribueres under en kommerciel licens.

### 10.4 Andre vilkår
* Specifikke betingelser for den kommercielle licens fastsættes i den formelle kommercielle licensaftale.
* Projektets vedligeholdere forbeholder sig retten til at opdatere denne licenspolitik (inklusive definitioner og tærskler for brugerstørrelse) efter behov. Eventuelle opdateringer vil blive annonceret via projektets officielle kanaler (kodelager, hjemmeside mv.).

## 11. Kerneudviklingsteam

MCP Server-udviklingsteam hos Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>