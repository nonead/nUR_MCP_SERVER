
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

Nonead Corporationが独自開発したnUR_MCP_SERVER製品の技術説明書

製品概要:
nUR_MCP_SERVERはMCP(Model Control Protocol)インターフェースプロトコルを基に構築されたインテリジェントロボット制御ミドルウェアシステムで、大規模言語モデル(LLM)を統合し産業用ロボットの自然言語インタラクティブ制御を実現します。本製品はClient-Serverアーキテクチャ設計を採用し、ユニバーサルロボッツ(Universal Robots)全シリーズ協働ロボットとの深い統合をサポートし、従来のティーチペンダントプログラミングによる産業用ロボット操作パラダイムを革新します。

中核技術アーキテクチャ:
1. 意味解析エンジン
多層TransformerアーキテクチャのNLP処理モジュールを搭載、文脈認識型コマンド解析(Contextual Command Parsing)をサポートし、自然言語からロボット制御コマンドへのエンドツーエンド変換を実現、コマンド認識精度98.6%を達成

2. 動的スクリプト生成システム
LLMベースのコード生成フレームワークにより、自然言語コマンドをURScriptロボット制御スクリプトに自動変換、リアルタイム構文チェックと安全性検証をサポートし、生成効率は従来プログラミング比12倍向上

3. マルチモーダル制御インターフェース
- MCPプロトコル拡張層: TCP/UDPデュアルモード通信をサポート、マイクロ秒級コマンド応答を提供
- デバイス抽象化層: URCapプラグインの標準化接続を実現
- データバス: TCP/IPイーサネットプロトコルベースで多機協調制御を実現

中核機能特性:
▶ 自然言語即時制御
音声/テキストコマンドで直接ロボット動作を駆動(姿勢制御、軌道計画、IO操作)、動的パラメータ注入とリアルタイム運動修正をサポート

▶ インテリジェントデータ収集システム
- 関節トルク、エンドエフェクタ姿勢等12次元状態データをリアルタイム収集
- 自然言語定義データフィルタリングルールをサポート
- 構造化データレポートを自動生成(CSV/JSON/XLSX)

▶ 多機協調制御
分散タスクスケジューリングアルゴリズムに基づき、Tord開発のMCP-Clientと連携して≤12台URロボットクラスターを同時管理可能、音声カスケードコマンドとクロスデバイスタスクオーケストレーションをサポート

▶ 適応型学習モジュール
内蔵インクリメンタル学習フレームワークにより、ユーザーフィードバックを通じてコマンド-動作マッピング関係を継続的に最適化、システム反復学習サイクル≤24時間

技術仕様:
- コマンド応答遅延: <200ms(エンドツーエンド)
- プロトコル互換性: MCP v2.1+ / URScript v5.0+
- 並列処理能力: 200+ TPS

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

本プロジェクトはユーザー区分型デュアルライセンス（User-Segmented Dual Licensing）モデルを採用しています。

**基本原則**
* 個人ユーザー及び10人以下の企業/組織：デフォルトでGNU Affero 一般公衆ライセンスv3.0（AGPLv3）が適用されます
* 10人を超える企業/組織：商用ライセンス（Commercial License）の取得が必須です

「10人以下」の定義：
貴組織（会社、非営利団体、政府機関、教育機関等のあらゆる法人を含む）において、本ソフトウェア（nUR_MCP_SERVER）の機能にアクセス、使用、または何らかの形で直接的・間接的に利益を得る個人の総数が10人を超えない場合を指します。これには開発者、テスター、運用者、エンドユーザー、統合システムを介した間接利用者等が含まれますが、これらに限定されません。

### 10.1 オープンソースライセンス（Open Source License）：AGPLv3 - 個人及び10人以下の組織向け
* 貴方が個人ユーザー、または貴組織が上記「10人以下」の定義に該当する場合、AGPLv3の条件下でnUR_MCP_SERVERを自由に使用、改変、配布できます。AGPLv3の全文はhttps://www.gnu.org/licenses/agpl-3.0.htmlで確認できます。
* **主要義務：** AGPLv3の重要な要件として、nUR_MCP_Serverを改変してネットワークサービスとして提供、または改変版を配布する場合、受領者に対しAGPLv3ライセンスに基づく完全なソースコードを提供する義務があります。「10人以下」基準に該当する場合でも、このソースコード公開義務を回避したい場合は、商用ライセンス（下記参照）の取得を検討する必要があります。
* 使用前に必ずAGPLv3の全条項を精読し理解してください。

### 10.2 商用ライセンス（Commercial License） - 10人超の組織またはAGPLv3義務を回避したいユーザー向け
* **必須要件：** 貴組織が上記「10人以下」定義に**該当しない**（即ち11人以上が本ソフトウェアにアクセス/使用/利益を得る）場合、nUR_MCP_SERVER使用前に当社に連絡し商用ライセンスを締結する必要があります。
* **任意選択：** 貴組織が「10人以下」条件に該当する場合でも、使用シナリオが**AGPLv3条項を満たせない**（特にソースコード公開義務）場合、またはAGPLv3が**提供しない**特定の商用条項（保証、賠償、Copyleft制限なし等）が必要な場合にも商用ライセンス締結が必須です。
* **商用ライセンスが必要な一般的なケース（以下に限定されません）：**
  * 組織規模が10人を超える場合
  * （組織規模不問）改変したnUR_MCP_SERVER版を配布するが、AGPLv3に基づく改変部分のソースコード公開を望まない場合
  * （組織規模不問）改変したnUR_MCP_SERVERを基にネットワークサービス（SaaS）を提供するが、サービス利用者に改変ソースコードを提供したくない場合
  * （組織規模不問）会社方針、顧客契約またはプロジェクト要件上、AGPLv3ライセンスソフトの使用が不可、またはクローズド配布・機密保持が必要な場合
* **商用ライセンス取得：** nUR_MCP_SERVER開発チームへservice@nonead.comまでご連絡ください。

### 10.3 貢献（Contributions）
* nUR_MCP_SERVERへのコミュニティ貢献を歓迎します。本プロジェクトに提出される全ての貢献はAGPLv3ライセンス下で提供されたものとみなされます。
* 本プロジェクトへ貢献（例：Pull Request）を提出することで、貴方のコードがAGPLv3ライセンスで本プロジェクト及び全ての後続利用者（最終的にAGPLv3または商用ライセンスを選択するか否かに関わらず）に提供されることに同意したものとみなします。
* また、貴方の貢献が商用ライセンス下で配布されるnUR_MCP_SERVER版に含まれる可能性があることを理解し同意するものとします。

### 10.4 その他の条項（Other Terms）
* 商用ライセンスの具体的条件は締結された正式な商用ライセンス契約に準じます。
* プロジェクトメンテナーは必要に応じて本ライセンスポリシー（ユーザー規模定義及び閾値を含む）を更新する権利を留保します。関連する更新はプロジェクト公式チャネル（コードリポジトリ、公式ウェブサイト等）で通知されます。


## 11. 開発 コアチーム

蘇州拓徳ロボット科技有限公司 MCP Server 開発チーム

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>