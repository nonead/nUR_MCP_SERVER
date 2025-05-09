
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

## 1. Qu'est-ce que le MCP ?
Le MCP (Protocole de Contexte Modèle) est un protocole de communication développé par Anthropic (open source en novembre 2024), permettant aux grands modèles d'IA (comme DeepSeek-V3-0324, DeepSeek-R1, Qwen3, etc.) d'accéder efficacement à des données/tools/services externes pour fournir des réponses plus précises et intelligentes.

Fonctionnalités principales :

Fourniture de contexte :
Transmission de fichiers/contenus de base de données
Ex : Analyse de rapports avant réponse

Appel d'outils externes :
Interaction avec systèmes locaux/distance (fichiers, API, matériel)
Ex : Organisation automatique de documents

Création de flux de travail :
Combinaison de services MCP pour des tâches complexes

Sécurité des données :
Exécution locale protégeant la confidentialité

## 2. Fonctionnement du MCP
Architecture client-serveur :

Client MCP : Application IA (émet des requêtes)
Serveur MCP : Fournit des interfaces
Communication : Basée sur JSON-RPC 2.0

## 3. Fonctions du serveur MCP
Accès aux données :
Fichiers/BDD/mémoire

Exécution d'opérations :
Fonctions prédéfinies (SQL, sauvegarde)

Notifications dynamiques :
Mises à jour en temps réel

Gestion de session :
Maintenance des connexions

## 2. Fonctions principales du serveur nUR MCP  

### 2.1 Obtenir toutes les données matérielles des robots UR  
**Fonction de scan réseau**  
fY6gJ6KcwVqfiiUFO-ogx1: Scanner une plage IP spécifique pour les robots UR  

**Gestion des connexions**  
fCf-PPsfx_yD_iZLURtGTV: Se connecter à un robot UR avec une IP spécifique  
fEd1Yp4RD3kiUSxqQlK1Va: Déconnecter d'un robot UR  

**Informations de base**  
fmMqIRbJZ4qRGJtRd59OJ-: Obtenir le numéro de série du robot  
f1ITpGFuwNDVfGfkNJzG2z: Obtenir la version du logiciel  
f8RnXWPeoSCCCvW3FuF_vS: Obtenir la durée de fonctionnement  
fl_BhgXwRaQ8nzexSGjwa7: Obtenir le mode de sécurité  

**Données des registres**  
fRRbXKNWy6vXbSrRPmFLJa: Obtenir les valeurs des registres Int (0-23)  
fRjcTzBeNogyaJtYvJ7_E2: Obtenir les valeurs des registres Double (0-23)  
fJ_s1E0ywr6t9rkMOBWiq6: Obtenir les valeurs des registres Double (0-31)  

**Surveillance d'état**  
fVYZ0ocbfuml1VpA5JSNRo: Obtenir les coordonnées TCP en temps réel  
fts21SISQrnyp_mb3jJy91: Obtenir les angles des articulations en temps réel  
fmjZNwC7zxju_tLjiM8w4A: Obtenir l'état de fonctionnement  
fy5NIEBXN7Kqecb1RkPhZN: Obtenir l'état d'exécution du programme  

**Paramètres électriques**  
fGU3ubp1fmrw-zPE2pyNDI: Obtenir la tension actuelle  
fl--FA0LvH9LBjXjVB0gGD: Obtenir le courant actuel  
fb3HhLwWUa8s49OXpU5Iq8: Obtenir les tensions des articulations  
frGKnkZFPFesyEXdGAxpD9: Obtenir les courants des articulations  
fzVxBGVvO7T3n3JbmAmvqB: Obtenir les températures des articulations  

### 2.2 Exécuter des commandes individuelles pour robots UR  
**Contrôle de mouvement**  
ffoF99tQZ6vcEqHQplHTjv: Envoyer une commande de position articulaire (movej)  
fiF4Pmxs7LQTrG7hY4sQV8: Envoyer une commande de mouvement linéaire TCP (movel)  
fOyQY2wR6xzOZP3NxjpLjK: Mouvement linéaire le long de l'axe X  
fCV_0M8pdPIVJs3nMGo6XS: Mouvement linéaire le long de l'axe Y  
fWkTyW-C5rxUPe3U0WGSsm: Mouvement linéaire le long de l'axe Z  

### 2.3 Écrire des programmes pour robots UR avec des modèles de langage avancés et les exécuter  

### 2.4 Exécuter les programmes intégrés des robots UR  
**Contrôle de programme**  
fE0WxXcDh3ENo8Q3fYul5K: Charger un programme UR  
fDqpZeOA1_KF8ixwndRP8-: Charger et exécuter un programme UR  
fH1AYKDXPCcGU1q3Ndrnwt: Arrêter le programme actuel  
fVwECQj8_p85mT6KaggA-N: Mettre en pause le programme actuel  
f4cp0iAFlVXMWqz51ylP4Z: Envoyer un script de programme  

### 2.5 Coordination de plusieurs robots UR  

## 3. Clause de non-responsabilité

Avant d'utiliser le nUR MCP Server, assurez-vous que les opérateurs ont suivi la formation de sécurité UR et maîtrisent les procédures d'arrêt d'urgence (E-stop).

Il est recommandé d'inspecter régulièrement l'état du robot et du MCP Server pour garantir la stabilité et la sécurité du système.

Lors de l'utilisation du nUR MCP Server, les normes de sécurité suivantes doivent être strictement respectées :

Zone de vision directe du robot

L'opérateur doit toujours maintenir le robot Universal Robots dans son champ de vision pour un contrôle visuel en temps réel.

Il est interdit de quitter la zone d'opération pendant le fonctionnement du robot afin d'intervenir immédiatement en cas d'incident.

Sécurisation de l'environnement

Vérifiez et dégagez les obstacles avant la mise en marche du robot pour éviter toute intrusion de personnel, équipement ou objet dans la zone dangereuse.

Installez si nécessaire des barrières physiques ou des rideaux lumineux de sécurité pour restreindre l'accès non autorisé.

Exemption de responsabilité en cas de non-conformité

En cas de blessure, dommage matériel ou accident dû au non-respect des exigences de sécurité (ex: absence de surveillance, zone non sécurisée), nous déclinons toute responsabilité légale et obligation de compensation.

L'utilisateur assume l'ensemble des risques et conséquences liés à l'opération.

**Pour utiliser avec Cline, ajoutez la configuration du serveur :**
MacOS & Linux :

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
            "command": "python",
            "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
         }
      }
    }

Windows :

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
            "command": "cmd",
            "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
         }
      }
    }


### 5.2 Basé sur la boîte à outils (pour les développeurs)

#### 5.2.1 Moteur & Dépendances 

* **Version système recommandée :**

  ```text
  Utilisateurs macOS : macOS Monterey 12.6 ou version ultérieure
  Utilisateurs Linux : CentOS 7 / Ubuntu 20.04 ou version ultérieure
  Utilisateurs Windows : Windows 10 LTSC 2021 ou version ultérieure
  ```

* **Exigences logicielles :**

  Environnement serveur MCP

  ```text
  Python 3.11 ou version ultérieure     
  pip 25.1 ou version ultérieure
  UV Package Manager 0.6.14 ou version ultérieure  
  bun 1.2.8 ou version ultérieure
  ```
  Modèle de langage large LLM

  ```text
  DeepSeek-V3-0324 ou version ultérieure
  DeepSeek-R1-671b ou version ultérieure 
  Qwen3-235b-a22b ou version ultérieure
  
  Les modèles de langage larges prenant généralement en charge MCP sont utilisables. Les modèles non listés n'ont pas été testés
  Les modèles déployés via Ollama ne peuvent actuellement pas appeler les outils. En cours de résolution...
  ```

#### 5.1.2 Installation  

**Installation du serveur MCP :**  
1. Installez Python 3.11 ou ultérieur  
2. Installez pip 25.1 ou ultérieur  
3. Installez UV Package Manager 0.6.14 ou ultérieur  
4. Installez bun 1.2.8 ou ultérieur  
5. Installez le serveur MCP :  
```
git clone https://gitee.com/nonead/nUR_MCP_SERVER.git  
cd nUR_MCP_SERVER  
pip install -r requirements.txt  
```  

**Configuration du client MCP :**  

**Pour utiliser avec Claude Desktop, ajoutez la configuration serveur :**
**Pour macOS :** ~/Library/Application Support/Claude/claude_desktop_config.json  
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

**Pour Windows :** %APPDATA%/Claude/claude_desktop_config.json  
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

**Pour macOS & Linux :**   
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

**Pour Windows :**  
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

**Pour développeurs macOS/Linux/Windows**

```text
Python 3.11 ou supérieur
pip 25.1 ou supérieur
Gestionnaire de paquets UV 0.6.14 ou supérieur
bun 1.2.8 ou supérieur
```

#### 5.2.3 Utilisation

Voici des exemples de tâches que vous pouvez faire exécuter par un modèle linguistique étendu :

* Connexion du robot Universal IP : 192.168.1.199
* Obtenir les coordonnées de pose actuelles de l'effecteur terminal TCP du robot Universal
* Lister toutes les commandes de l'outil nUR_MCP_SERVER
* Obtenir toutes les données matérielles du robot Universal
* Exécuter un programme de script du robot Universal
* Exécuter le programme intégré XXXX.urp du robot Universal
* Définir le robot Universal avec IP 172.22.109.141 comme robot A et IP 172.22.98.41 comme robot B, les connecter, enregistrer les poses TCP actuelles et positions clés des robots A (gauche) et B (droite), analyser leurs relations de pose.
* Exécution étape par étape : robot Universal IP 192.168.1.199, enregistrer la pose TCP actuelle, puis déplacer TCP de +20mm en Z, -50mm en Y, +30mm en X, répéter 5 fois.
* Écrire et exécuter un script pour robot Universal : dessiner un cercle de 50mm de rayon dans le plan de base centré sur la pose actuelle.
* Définir le robot IP 172.22.109.141 comme A et 172.22.98.41 comme B, les connecter, les commandes suivantes ne contrôleront que A tout en synchronisant le mouvement miroir de B.

## 6. Architecture technique

MCP adopte une architecture client-serveur, implémentant la communication entre modèles et ressources externes via des protocoles standardisés.  
![alt](./images/MCP.svg "mcp")
Modèle client-serveur
Composants clés de l'architecture MCP :

Hôte MCP : Application LLM initiant la connexion (comme Claude Desktop ou IDE)
Client MCP : Client protocolaire maintenant une connexion 1:1 avec le serveur dans l'application hôte
Serveur MCP : Programme léger exposant des fonctionnalités via le Model Context Protocol standardisé
Sources de données locales : Fichiers, bases de données et services accessibles en toute sécurité par le serveur MCP
Services distants : Systèmes externes accessibles via Internet (par exemple via API)
Responsabilités des composants :

Hôte MCP :
Fournir l'interface utilisateur
Gérer la connexion avec le fournisseur LLM
Intégrer le client MCP pour accéder aux ressources externes
Client MCP :
Établir et maintenir la connexion avec le serveur MCP
Envoyer des requêtes et recevoir des réponses
Traiter les échanges de données conformément au protocole MCP
Serveur MCP :
Traiter les requêtes des clients
Exécuter des fonctionnalités spécifiques ou fournir un accès aux ressources
Formater les réponses selon le standard du protocole MCP
Protocole de communication
MCP utilise JSON-RPC 2.0 comme protocole de communication de base, supportant:  
![alt](./images/p.svg "mcp_json-RPC2.0")  
Requêtes : Messages initiant des opérations du client vers le serveur ou vice versa
Réponses : Réponses aux requêtes, contenant résultats ou informations d'erreur
Notifications : Messages unidirectionnels ne nécessitant pas de réponse (généralement pour notifications d'événements)
MCP supporte plusieurs mécanismes de transport :

Entrée/sortie standard (Stdio) : Pour serveurs locaux, via communication inter-processus
Événements envoyés par le serveur (SSE) : Mécanisme de transport basé sur HTTP pour serveurs distants

Avantages de MCP
MCP présente des avantages significatifs par rapport aux méthodes d'intégration traditionnelles, notamment en termes d'uniformité, sécurité et extensibilité.

Uniformité
MCP résout le problème de fragmentation des méthodes d'intégration traditionnelles via une interaction standardisée entre systèmes d'IA et sources de données externes :

Connexion plug-in : Accès unifié à diverses sources de données via un protocole standardisé
Compatibilité multiplateforme : Support de différents modèles et plateformes d'IA
Simplification du développement : Les développeurs peuvent se concentrer sur la logique métier
Sécurité
MCP intègre des mécanismes de sécurité pour protéger les données pendant le transfert et le traitement :

Protection des informations sensibles : Clés API, données utilisateurs, etc.
Contrôle d'accès : Le serveur MCP peut implémenter un contrôle d'accès granulaire
Traitement local : Évite le téléchargement d'informations sensibles vers des plateformes tierces
Extensibilité
La conception modulaire de MCP offre une grande extensibilité :

Connexion multi-services : Plusieurs services peuvent se connecter à tout client compatible
Écosystème extensible : De plus en plus de composants préconstruits disponibles
Capacité de personnalisation : Les développeurs peuvent créer des serveurs MCP personnalisés

## 7. Contact

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**Site officiel**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="Contact: Nonead Tech WeChat" width="200">  

## 8. Différences entre nUR MCP Server et les autres serveurs MCP

Les utilisateurs du serveur nUR MCP doivent avoir une conscience de sécurité très élevée et avoir suivi une formation à l'utilisation des robots Universal Robots, car les modèles linguistiques avancés opèrent sur de vrais robots. Une mauvaise manipulation peut entraîner des blessures corporelles et des dommages matériels, soyez très prudent.

## 9. Citation

Si vous utilisez ce logiciel, veuillez citer comme suit :

* [nURMCP: NONEAD Uninversal-Robots Model Context Protocol Server](https://www.nonead.com)
* Nonead illustre la véritable signification de la fabrication intelligente, en pionnier des innovations qui redéfinissent notre monde. <br>
  Nonead demonstrates the true meaning of intelligent manufacturing, pioneering innovations that reshape our world.

## 10. Licence

[Apache License 2.0](LICENSE)

## 11. Équipe de développement principale

Équipe de développement du serveur MCP de Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>