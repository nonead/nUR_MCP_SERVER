
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

## 1. Что такое MCP?
MCP (Протокол контекста модели) - коммуникационный протокол, разработанный Anthropic (открытый код с ноября 2024), позволяющий большим языковым моделям (DeepSeek-V3-0324, DeepSeek-R1, Qwen3 и др.) эффективно взаимодействовать с внешними данными/инструментами/сервисами.

Основные функции:

Предоставление контекста:
Передача файлов/данных из БД
Пример: Анализ отчетов перед ответом

Интеграция инструментов:
Управление локальными/удаленными системами
Пример: Автоматизация документов

Автоматизация процессов:
Комбинация сервисов MCP

Защита данных:
Локальное выполнение операций

## 2. Принцип работы
Клиент-серверная архитектура:

Клиент MCP: ИИ-приложение
Сервер MCP: Предоставляет интерфейсы
Связь: JSON-RPC 2.0

## 3. Функции сервера
Доступ к данным:
Файлы/БД/память

Выполнение операций:
Предопределенные функции (SQL и др.)

Динамические уведомления:
Обновления в реальном времени

Управление сессиями:
Поддержка соединений

## 2. Основные функции сервера nUR MCP  

### 2.1 Получение всех аппаратных данных роботов UR  
**Функция сетевого сканирования**  
fY6gJ6KcwVqfiiUFO-ogx1: Сканирование указанного диапазона IP-адресов для роботов UR  

**Управление подключениями**  
fCf-PPsfx_yD_iZLURtGTV: Подключение к роботу UR по указанному IP-адресу  
fEd1Yp4RD3kiUSxqQlK1Va: Отключение от робота UR  

**Получение основной информации**  
fmMqIRbJZ4qRGJtRd59OJ-: Получение серийного номера робота  
f1ITpGFuwNDVfGfkNJzG2z: Получение версии ПО  
f8RnXWPeoSCCCvW3FuF_vS: Получение времени работы  
fl_BhgXwRaQ8nzexSGjwa7: Получение режима безопасности  

**Получение данных регистров**  
fRRbXKNWy6vXbSrRPmFLJa: Получение значений регистров Int (0-23)  
fRjcTzBeNogyaJtYvJ7_E2: Получение значений регистров Double (0-23)  
fJ_s1E0ywr6t9rkMOBWiq6: Получение значений регистров Double (0-31)  

**Мониторинг состояния**  
fVYZ0ocbfuml1VpA5JSNRo: Получение координат TCP в реальном времени  
fts21SISQrnyp_mb3jJy91: Получение углов сочленений в реальном времени  
fmjZNwC7zxju_tLjiM8w4A: Получение состояния работы  
fy5NIEBXN7Kqecb1RkPhZN: Получение состояния выполнения программы  

**Электрические параметры**  
fGU3ubp1fmrw-zPE2pyNDI: Получение текущего напряжения  
fl--FA0LvH9LBjXjVB0gGD: Получение текущего тока  
fb3HhLwWUa8s49OXpU5Iq8: Получение напряжений сочленений  
frGKnkZFPFesyEXdGAxpD9: Получение токов сочленений  
fzVxBGVvO7T3n3JbmAmvqB: Получение температур сочленений  

### 2.2 Выполнение отдельных команд для роботов UR  
**Управление движением**  
ffoF99tQZ6vcEqHQplHTjv: Отправка команды положения сочленений (movej)  
fiF4Pmxs7LQTrG7hY4sQV8: Отправка команды линейного движения TCP (movel)  
fOyQY2wR6xzOZP3NxjpLjK: Линейное движение по оси X  
fCV_0M8pdPIVJs3nMGo6XS: Линейное движение по оси Y  
fWkTyW-C5rxUPe3U0WGSsm: Линейное движение по оси Z  

### 2.3 Написание программ для роботов UR с помощью больших языковых моделей и их выполнение  

### 2.4 Запуск встроенных программ роботов UR  
**Управление программами**  
fE0WxXcDh3ENo8Q3fYul5K: Загрузка программы UR  
fDqpZeOA1_KF8ixwndRP8-: Загрузка и выполнение программы UR  
fH1AYKDXPCcGU1q3Ndrnwt: Остановка текущей программы  
fVwECQj8_p85mT6KaggA-N: Пауза текущей программы  
f4cp0iAFlVXMWqz51ylP4Z: Отправка скрипта программы  

### 2.5 Координация нескольких роботов UR  


## 3. Отказ от ответственности

Перед использованием nUR MCP Server убедитесь, что операторы прошли обучение безопасности UR и знакомы с аварийной остановкой (E-stop).

Регулярно проверяйте состояние робота и сервера для обеспечения безопасности.

При использовании nUR MCP Server строго соблюдайте:

Видимость робота

Оператор должен всегда видеть робота Universal Robots для мониторинга в реальном времени.

Запрещено покидать зону работы во время эксплуатации.

Безопасная среда

Уберите препятствия и исключите нахождение людей/объектов в опасной зоне.

При необходимости установите защитные ограждения или световые завесы.

Освобождение от ответственности

При несоблюдении требований (например, отсутствие контроля), мы не несем ответственности за травмы, поломки или аварии.

Все риски несет пользователь.

## 4. Выпуск версий

### 4.1 Последние обновления

* 15.05.2025 : Первый выпуск nUR_MCP_SERVER

### 4.2 Планы на будущее

* Поддержка эксклюзивного MCP Client для nUR MCP Server, усиление функций безопасности исполнительных устройств.
* Добавление записи логов роботов UR
* Резервное копирование и загрузка программ роботов UR

## 5. Быстрый старт

### 5.1 На основе продукта (для обычных пользователей)

#### 5.1.1 Движок и зависимости

* **Рекомендуемые версии системы:**

  ```text
  Пользователи macOS: macOS Monterey 12.6 или новее
  Пользователи Linux: CentOS 7 / Ubuntu 20.04 или новее
  Пользователи Windows: Windows 10 LTSC 2021 или новее
  ```

* **Требования к программному обеспечению:**

  Серверная среда MCP

  ```text
  Python 3.11 или новее     
  pip 25.1 или новее
  UV Package Manager 0.6.14 или новее  
  bun 1.2.8 или новее
  ```

  MCP клиент

  ```text
   Claude Desktop 3.7.0 или новее
   Cherry Studio 1.2.10 или новее
   Cline 3.14.1 или новее

   ClaudeMind, Cursor, NextChat, ChatMCP, Copilot-MCP, Continue, Dolphin-MCP, Goose не тестировались.
  ```

   LLM большая языковая модель

  ```text
  DeepSeek-V3-0324 или новее
  DeepSeek-R1-671b  или новее 
  Qwen3-235b-a22b или новее
  
  Обычно поддерживаются большие языковые модели с MCP, модели вне списка не тестировались
  Модели, развернутые через Ollama, пока не могут вызывать Tool, проблема решается...
  ```

#### 5.1.2 Установка

**Установка MCP сервера:**
1. Установите Python 3.11 или новее.
2. Установите pip 25.1 или новее.
3. Установите UV Package Manager 0.6.14 или новее.
4. Установите bun 1.2.8 или новее.
5. Установите MCP Server:
```
     git clone https://gitee.com/nonead/nUR_MCP_SERVER.git
     cd nUR_MCP_SERVER
     pip install -r requirements.txt
```

**Настройка MCP клиента:**

**Для работы с Claude Desktop, добавьте конфигурацию сервера:**
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

**Для работы с Cherry Studio，добавьте конфигурацию сервера：**  

**Для macOS & Linux:**   
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

**Для Windows:**  
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

**Для использования с Cline добавьте конфигурацию сервера:**
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


### 5.2 На основе инструментария (для разработчиков)

#### 5.2.1 Движок и зависимости 

* **Рекомендуемые версии системы:**

  ```text
  Пользователи macOS: macOS Monterey 12.6 или новее
  Пользователи Linux: CentOS 7 / Ubuntu 20.04 или новее
  Пользователи Windows: Windows 10 LTSC 2021 или новее
  ```

* **Программные требования:**

  Серверная среда MCP

  ```text
  Python 3.11 или новее     
  pip 25.1 или новее
  UV Package Manager 0.6.14 или новее  
  bun 1.2.8 или новее
  ```
  Большие языковые модели LLM

  ```text
  DeepSeek-V3-0324 или новее
  DeepSeek-R1-671b или новее 
  Qwen3-235b-a22b или новее
  
  Обычно большие языковые модели, поддерживающие MCP, пригодны к использованию. Неперечисленные модели не тестировались
  Модели, развернутые через Ollama, в настоящее время не могут вызывать инструменты. В процессе решения...
  ```

#### 5.2.2 Установка

**Для разработчиков на macOS/Linux/Windows**

```text
Python 3.11 или новее
pip 25.1 или новее
Менеджер пакетов UV 0.6.14 или новее
bun 1.2.8 или новее
``` 

#### 5.2.3 Использование

Примеры задач для выполнения большими языковыми моделями:

* Подключение робота Universal по IP: 192.168.1.199
* Получение текущих координат позиции TCP-инструмента
* Вывод списка всех команд инструмента nUR_MCP_SERVER
* Получение всех аппаратных данных робота Universal
* Выполнение скриптовой программы робота
* Запуск встроенной программы XXXX.urp
* Определение робота с IP 172.22.109.141 как A и IP 172.22.98.41 как B, подключение обоих, запись текущих позиций TCP и ключевых положений A (слева) и B (справа), анализ взаимного расположения
* Пошаговое выполнение: робот Universal IP 192.168.1.199, запись текущей позиции TCP, затем перемещение +20мм по Z, -50мм по Y, +30мм по X, повторение 5 раз
* Написание и выполнение скрипта для робота: рисование окружности радиусом 50мм в базовой плоскости с центром в текущей позиции
* Определение роботов с IP 172.22.109.141 как A и 172.22.98.41 как B, подключение, последующие команды будут управлять только A с синхронным зеркальным движением B

## 6. Техническая архитектура

MCP использует клиент-серверную архитектуру со стандартизированными протоколами для связи модели с внешними ресурсами.  
![alt](./images/MCP.svg "mcp")  
Клиент-Серверная Модель
Ключевые компоненты:

MCP Хост: LLM-приложение (напр. Claude Desktop), инициирующее подключения
MCP Клиент: Протокольный клиент, поддерживающий 1:1 соединение с сервером
MCP Сервер: Легковесная программа, предоставляющая функционал через стандартизированный Model Context Protocol
Локальные источники данных: Файлы, БД и сервисы, безопасно доступные MCP Серверу
Удаленные сервисы: Внешние системы, доступные через интернет (напр. API)
Обязанности компонентов:

MCP Хост:
Предоставляет интерфейс пользователя
Управляет подключением к провайдеру LLM
Интегрирует MCP Клиент для доступа к внешним ресурсам
MCP Клиент:
Устанавливает/поддерживает соединение с MCP Сервером
Отправляет запросы и получает ответы
Обрабатывает обмен данными согласно стандартам MCP
MCP Сервер:
Обрабатывает запросы клиентов
Выполняет специфичные функции или предоставляет доступ к ресурсам
Форматирует ответы согласно стандартам протокола MCP
Протокол связи
MCP использует JSON-RPC 2.0 как базовый протокол, поддерживая:  
![alt](./images/p.svg "mcp_json-RPC2.0")  
Запросы: Сообщения, инициирующие операции клиент→сервер или сервер→клиент
Ответы: Результаты выполнения запросов или информация об ошибках
Уведомления: Однонаправленные сообщения, не требующие ответа (обычно для оповещений)
Поддерживаемые механизмы передачи:

Стандартный ввод/вывод (Stdio): Для локальных серверов через межпроцессное взаимодействие
Server-Sent Events (SSE): HTTP-механизм для удаленных серверов

Преимущества MCP
MCP превосходит традиционные методы интеграции в унификации, безопасности и расширяемости.

Унификация
Стандартизированное взаимодействие решает проблемы фрагментации:

Подключение по принципу плагинов: Единый протокол для различных источников данных
Кросс-платформенная совместимость: Поддержка разных моделей/платформ ИИ
Упрощение разработки: Концентрация на бизнес-логике
Безопасность
Встроенные механизмы защиты данных:

Защита конфиденциальной информации: API-ключи, пользовательские данные и т.д.
Контроль доступа: MCP Сервер реализует детализированные ограничения доступа
Локальная обработка: Исключает передачу конфиденциальных данных третьим сторонам
Расширяемость
Модульная архитектура обеспечивает масштабируемость:

Подключение множества сервисов: Несколько сервисов могут подключаться к совместимым клиентам
Развитие экосистемы: Растущая библиотека предсобранных компонентов
Гибкость настройки: Возможность создания пользовательских MCP Серверов
## 7. Контакты

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**Официальный сайт**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="Контакт: Nonead Tech WeChat" width="200">  

## 8. Отличия nUR MCP Server от других серверов MCP

Пользователи nUR MCP Server должны обладать чрезвычайно высокой осведомленностью о безопасности и пройти обучение работе с роботами Universal Robots, поскольку большая языковая модель управляет реальными роботами. Неправильная эксплуатация может привести к травмам и материальному ущербу - пожалуйста, соблюдайте максимальную осторожность.

## 9. Цитирование

Если вы используете это программное обеспечение, процитируйте следующим образом:

* [nURMCP: NONEAD Universal-Robots Model Context Protocol Server](https://www.nonead.com)
* Nonead демонстрирует истинное значение интеллектуального производства, являясь первопроходцем инноваций, преобразующих наш мир.

## 10. Лицензия

[Apache License 2.0](LICENSE)

## 11. Основная команда разработчиков

Команда разработчиков MCP Server компании Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>