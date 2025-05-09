
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

## 1. MCPとは？
MCP（モデルコンテキストプロトコル）はAnthropic社が開発した通信プロトコル（2024年11月オープンソース化）で、AI大規模言語モデル（DeepSeek-V3-0324、DeepSeek-R1、Qwen3など）が外部データ・ツール・サービスに効率的にアクセスし、より正確で知的な回答を提供するために使用されます。

MCPの主な機能

コンテキスト情報提供：
アプリケーションがファイルやデータベース内容などの追加情報をAIに渡し、問題理解を支援
例：レポートをAIに読ませた上で内容に基づく回答

外部ツール連携：
AIがMCP経由でローカル/リモート機能（ファイル操作、DB問合せ、API呼出、ハードウェア制御など）を直接操作
例：文書自動整理やDBデータからのレポート自動作成

インテリジェントワークフロー構築：
開発者が複数MCPサービスを組み合わせ、データ分析自動化やインテリジェントカスタマーサポートなど複雑タスクを実現

データセキュリティ保障：
MCPはローカル環境で動作するため、機密データのクラウドアップロードを防止

## 2. MCPの動作原理
クライアント・サーバーアーキテクチャを採用

MCPクライアント：ClaudeなどのAIアプリケーション（リクエスト送信側）
MCPサーバー：ローカル/リモートで動作（データ・ツールインタフェース提供）
通信方式：JSON-RPC 2.0準拠（要求・応答・リアルタイム通知対応）

## 3. MCPサーバーの主要機能
AIの「アシスタント」として以下を提供：

データアクセス（リソース公開）
・file:///docs/report.pdf（ローカルファイル読込）
・db://sales/records（データベース問合せ）

操作実行（ツール提供）
・search_database(sql_query)（SQL実行）
・save_file(path, content)（ファイル保存）

リアルタイム更新（動的通知）
データ変更時にAIへ自動通知

セッション管理
AIとサーバーの接続を管理

## 2. nUR MCPサーバーの主要機能  

### 2.1 URロボットの全ハードウェアデータ取得  
**ネットワークスキャン機能**  
fY6gJ6KcwVqfiiUFO-ogx1: 指定IP範囲のURロボットをスキャン  

**接続管理機能**  
fCf-PPsfx_yD_iZLURtGTV: 指定IPのURロボットに接続  
fEd1Yp4RD3kiUSxqQlK1Va: URロボットから切断  

**基本情報取得**  
fmMqIRbJZ4qRGJtRd59OJ-: ロボットのシリアル番号を取得  
f1ITpGFuwNDVfGfkNJzG2z: ソフトウェアバージョンを取得  
f8RnXWPeoSCCCvW3FuF_vS: 稼働時間を取得  
fl_BhgXwRaQ8nzexSGjwa7: セーフティモードを取得  

**レジスタデータ取得**  
fRRbXKNWy6vXbSrRPmFLJa: Intレジスタ値(0-23)を取得  
fRjcTzBeNogyaJtYvJ7_E2: Doubleレジスタ値(0-23)を取得  
fJ_s1E0ywr6t9rkMOBWiq6: Doubleレジスタ値(0-31)を取得  

**状態監視**  
fVYZ0ocbfuml1VpA5JSNRo: リアルタイムTCP座標を取得  
fts21SISQrnyp_mb3jJy91: リアルタイム関節角度を取得  
fmjZNwC7zxju_tLjiM8w4A: 動作状態を取得  
fy5NIEBXN7Kqecb1RkPhZN: プログラム実行状態を取得  

**電気パラメータ監視**  
fGU3ubp1fmrw-zPE2pyNDI: 現在の電圧を取得  
fl--FA0LvH9LBjXjVB0gGD: 現在の電流を取得  
fb3HhLwWUa8s49OXpU5Iq8: 各関節の電圧を取得  
frGKnkZFPFesyEXdGAxpD9: 各関節の電流を取得  
fzVxBGVvO7T3n3JbmAmvqB: 各関節の温度を取得  

### 2.2 URロボットの単一コマンド実行  
**動作制御機能**  
ffoF99tQZ6vcEqHQplHTjv: 関節姿勢コマンドを送信(movej)  
fiF4Pmxs7LQTrG7hY4sQV8: TCP直線移動コマンドを送信(movel)  
fOyQY2wR6xzOZP3NxjpLjK: X軸に沿った直線移動  
fCV_0M8pdPIVJs3nMGo6XS: Y軸に沿った直線移動  
fWkTyW-C5rxUPe3U0WGSsm: Z軸に沿った直線移動  

### 2.3 大規模言語モデルによるURロボットスクリプトプログラムの作成と実行  

### 2.4 URロボット組み込みプログラムの実行  
**プログラム制御**  
fE0WxXcDh3ENo8Q3fYul5K: URプログラムをロード  
fDqpZeOA1_KF8ixwndRP8-: URプログラムをロードして実行  
fH1AYKDXPCcGU1q3Ndrnwt: 現在のプログラムを停止  
fVwECQj8_p85mT6KaggA-N: 現在のプログラムを一時停止  
f4cp0iAFlVXMWqz51ylP4Z: プログラムスクリプトを送信  

### 2.5 複数URロボットの連動  

## 3. 免責事項

nUR MCP Serverをご使用前に、操作担当者がURロボットの安全トレーニングを受講し、緊急停止（E-stop）などの安全操作に精通していることを確認してください。

ロボットおよびMCP Serverの稼働状態を定期的に点検し、システムの安定性と安全性を確保することを推奨します。

nUR MCP Server使用時は、以下の安全規範を厳守してください：

ロボットの可視範囲内での稼働

操作者は常にユニバーサルロボットを視界内に配置し、リアルタイムで動作状態を監視できるようにする必要があります。

不測の事態に対応できないリスクを避けるため、ロボット動作中の操作区域離脱を禁止します。

作業環境の安全性確保

ロボット稼働前に周辺の障害物を点検・除去し、危険区域に人員・設備・その他物体が侵入しないことを確認してください。

必要に応じて物理防護柵または安全光線を設置し、許可のない者の作業区域への立ち入りを防止します。

安全規範違反時の責任免除

上記の安全要件（監視離脱、作業区域未整理など）を遵守しなかったことにより、人身傷害、設備損傷または生産事故が発生した場合、当方は一切の法的責任及び賠償義務を負いません。

全ての操作リスク及び結果は使用者側に帰属します。

## 4. バージョンリリース

### 4.1 最近の更新

* 2025.05.15 : nUR_MCP_SERVER 初回リリース

### 4.2 今後の計画

* nUR MCP Server専用のMCP Clientをサポート、エグゼキュータのセキュリティ機能を強化
* URロボットのログ記録を追加
* URロボットプログラムのバックアップとアップロード

## 5. クイックスタート

### 5.1 製品ベース（一般ユーザー向け）

#### 5.1.1 エンジン＆依存関係

* **推奨システムバージョン:**

  ```text
  macOSユーザー: macOS Monterey 12.6 以降
  Linuxユーザー: CentOS 7 / Ubuntu 20.04 以降
  Windowsユーザー: Windows 10 LTSC 2021 以降
  ```

* **ソフトウェア要件:**

  MCPサーバー環境

  ```text
  Python 3.11 以降     
  pip 25.1 以降
  UV Package Manager 0.6.14 以降  
  bun 1.2.8 以降
  ```

  MCPクライアント

  ```text
   Claude Desktop 3.7.0 以降
   Cherry Studio 1.2.10 以降
   Cline 3.14.1 以降

   ClaudeMind、Cursor、NextChat、ChatMCP、Copilot-MCP、Continue、Dolphin-MCP、Gooseは未テストです。
  ```

   LLM大規模言語モデル

  ```text
  DeepSeek-V3-0324 以降
  DeepSeek-R1-671b  以降 
  Qwen3-235b-a22b 以降
  
  一般的にMCPをサポートする大規模言語モデルは使用可能、リスト外のモデルは未テストです
  Ollamaでデプロイされたモデルは現在Tool呼び出し不可、解決中です...
  ```

#### 5.1.2 インストール

**MCPサーバーインストール:**
1. Python 3.11以降をインストール
2. pip 25.1以降をインストール
3. UV Package Manager 0.6.14以降をインストール
4. bun 1.2.8以降をインストール
5. MCP Serverをインストール:
```
     git clone https://gitee.com/nonead/nUR_MCP_SERVER.git
     cd nUR_MCP_SERVER
     pip install -r requirements.txt
```

**MCPクライアント設定:**

**Claude Desktopと連携するには、サーバー設定を追加してください:**
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
          "command": "python",
          "args": ["D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
        }
      }
    }

**Cherry Studioと連携するには、サーバー設定を追加してください：**  

**macOS & Linux向け:**   
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

**Windows向け:**  
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

**Clineと連携するには、サーバー設定を追加してください：**
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


### 5.2 ツールキットベース（開発者向け）

#### 5.2.1 エンジン＆依存関係 

* **推奨システムバージョン：**

  ```text
  macOSユーザー：macOS Monterey 12.6 以降
  Linuxユーザー：CentOS 7 / Ubuntu 20.04 以降
  Windowsユーザー：Windows 10 LTSC 2021 以降
  ```

* **ソフトウェア要件：**

  MCPサーバー環境

  ```text
  Python 3.11 以降     
  pip 25.1 以降
  UV Package Manager 0.6.14 以降  
  bun 1.2.8 以降
  ```
  LLM 大規模言語モデル

  ```text
  DeepSeek-V3-0324 以降
  DeepSeek-R1-671b  以降 
  Qwen3-235b-a22b 以降
  
  MCPをサポートする一般的な大規模言語モデルは使用可能です。リスト外のモデルはテストされていません
  Ollamaでデプロイされたモデルは現在Toolを呼び出せません。解決中です...
  ```

#### 5.2.2 インストール

**macOS/Linux/Windows開発者向け**

```text
Python 3.11 以降
pip 25.1 以降
UVパッケージマネージャ 0.6.14 以降
bun 1.2.8 以降
```

#### 5.2.3 使用方法

以下は大規模言語モデルに実行させることができるタスクの例です：

* ユニバーサルロボットIP接続: 192.168.1.199
* ユニバーサルロボットのTCPエンドエフェクタの現在姿勢座標を取得
* nUR_MCP_SERVERツールの全コマンドをリスト表示
* ユニバーサルロボットの全ハードウェアデータを取得
* ユニバーサルロボットのスクリプトプログラムを実行
* ユニバーサルロボット組み込みプログラムXXXX.urpを実行
* IP172.22.109.141のロボットをA、IP172.22.98.41をBと命名し、両ロボットを接続。A(左)とB(右)の現在TCP姿勢と各キーポジションを記録し、両ロボットの姿勢関係を分析
* 段階的実行：IP192.168.1.199のロボットで現在TCP姿勢を記録後、+Z方向20mm、-Y方向50mm、+X方向30mm移動を5回繰り返し
* ユニバーサルロボットスクリプトを作成・実行：現在姿勢を中心に基部平面で半径50mmの円を描画
* IP172.22.109.141をA、172.22.98.41をBと設定し接続。以降のコマンドはAのみを制御し、Bにミラー動作を同期

## 6. 技術アーキテクチャ

MCPはクライアント-サーバーアーキテクチャを採用し、標準化プロトコルでモデルと外部リソース間通信を実現。  
![pic alt](./images/MCP.svg "mcp")  
クライアント-サーバーモデル
MCPアーキテクチャの主要コンポーネント：

MCPホスト：接続を開始するLLMアプリケーション(Claude DesktopやIDE等)
MCPクライアント：ホストアプリ内でサーバーと1:1接続を維持するプロトコルクライアント
MCPサーバー：標準化Model Context Protocolで特定機能を公開する軽量プログラム
ローカルデータソース：MCPサーバーが安全にアクセス可能なコンピュータファイル/DB/サービス
リモートサービス：MCPサーバーが接続可能なAPI経由の外部システム
主要コンポーネントの責務：

MCPホスト：
UI提供
LLMプロバイダー接続管理
外部リソースアクセスのためのMCPクライアント統合
MCPクライアント：
MCPサーバーとの接続確立・維持
リクエスト送信/レスポンス受信
MCPプロトコル標準に準拠したデータ交換処理
MCPサーバー：
クライアントリクエスト処理
特定機能の実行/リソースアクセス提供
MCPプロトコル標準に準拠したレスポンス整形
通信プロトコル
MCPはJSON-RPC 2.0を基盤通信プロトコルとして採用：  
![pic alt](./images/p.svg "mcp_json-RPC2.0")  
リクエスト：クライアント→サーバー/サーバー→クライアントの操作開始メッセージ
レスポンス：リクエストへの返答（結果/エラー情報含む）
通知：応答不要の一方向メッセージ（主にイベント通知用）
MCPがサポートする伝送機構：

標準入出力(Stdio)：ローカルサーバー向け、プロセス間通信で実現
Server-Sent Events(SSE)：HTTPベースの伝送機構、リモートサーバー向け

MCPの優位性
MCPは従来の統合方法と比べ、統一性・安全性・拡張性で顕著な優位性を有する。

統一性
標準化されたAIシステムと外部データソース間インタラクションにより、従来の断片化問題を解決：

プラグイン式接続：統一プロトコルで各種データソースをプラグイン接続可能
クロスプラットフォーム互換：異なるAIモデル/プラットフォームをサポート
開発簡素化：開発者はビジネスロジックに集中可能
安全性
組み込みセキュリティ機構でデータ伝送/処理過程を保護：

機密情報保護：APIキー/ユーザーデータ等の機密情報を保護
アクセス制御：MCPサーバーで細かなアクセス制御を実現
ローカル処理：機密情報をサードパーティにアップロードせずローカル処理
拡張性
モジュラー設計で高い拡張性を実現：

マルチサービス接続：複数サービスが互換クライアントに接続可能
エコシステム拡大：成熟に伴い利用可能なプリビルドコンポーネントが増加
カスタマイズ能力：開発者は必要に応じてカスタムMCPサーバーを作成可能

## 7. お問い合わせ

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**公式サイト**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="連絡先: Nonead Tech WeChat" width="200">  

## 8. nUR MCP Server と他の MCP Server の違い

nUR MCP Server を使用するユーザーは、非常に高い安全意識を持ち、ユニバーサルロボットの使用トレーニングを受ける必要があります。大規模言語モデルが操作するのは実際のロボットであり、誤った操作は人身事故や財産損失を引き起こす可能性があるため、十分に注意してください。

## 9. 引用

本ソフトウェアを使用する場合は、以下のように引用してください:

* [nURMCP: NONEAD Uninversal-Robots Model Context Protocol Server](https://www.nonead.com)
* 拓徳は知能製造の真髄を解き明かし、革新が世界を変える <br>
  Nonead demonstrates the true meaning of intelligent manufacturing, pioneering innovations that reshape our world.

## 10. ライセンス

[Apache License 2.0](LICENSE)

## 11. 開発 コアチーム

蘇州拓徳ロボット科技有限公司 MCP Server 開発チーム

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>