
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

## 1. ما هو MCP؟
بروتوكول سياق النموذج (MCP) هو بروتوكول اتصالات طورته Anthropic (مفتوح المصدر نوفمبر 2024)، يمكّن نماذج الذكاء الاصطناعي الكبيرة (مثل DeepSeek-V3-0324، DeepSeek-R1، Qwen3) من الوصول الفعال إلى البيانات/الأدوات/الخدمات الخارجية.

الميزات الرئيسية:

توفير السياق:
نقل الملفات/محتوى قواعد البيانات
مثال: تحليل التقارير قبل الإجابة

دمج الأدوات:
التحكم في الأنظمة المحلية/البعيدة
مثال: تنظيم المستندات آليًا

أتمتة العمليات:
دمج خدمات MCP المتعددة

حماية البيانات:
التنفيذ المحلي يحمي المعلومات

## 2. آلية العمل
هندسة خادم-عميل:

عميل MCP: تطبيق الذكاء الاصطناعي (يرسل الطلبات)
خادم MCP: يوفر واجهات البيانات
التواصل: وفق معيار JSON-RPC 2.0

## 3. وظائف الخادم
الوصول للبيانات:
الملفات/قواعد البيانات/الذاكرة

تنفيذ العمليات:
وظائف محددة مسبقًا (استعلامات SQL إلخ)

الإشعارات الديناميكية:
تحديثات فورية

إدارة الجلسات:
الحفاظ على الاتصالات

## 2. نواة خادم nUR MCP الأساسية  

### 2.1 الحصول على جميع بيانات أجهزة روبوتات UR  
**ميزة المسح الشبكي**  
fY6gJ6KcwVqfiiUFO-ogx1: مسح نطاق IP محدد للروبوتات UR  

**إدارة الاتصالات**  
fCf-PPsfx_yD_iZLURtGTV: الاتصال بروبوت UR بعنوان IP محدد  
fEd1Yp4RD3kiUSxqQlK1Va: قطع الاتصال بروبوت UR  

**الحصول على المعلومات الأساسية**  
fmMqIRbJZ4qRGJtRd59OJ-: الحصول على الرقم التسلسلي للروبوت  
f1ITpGFuwNDVfGfkNJzG2z: الحصول على إصدار البرنامج  
f8RnXWPeoSCCCvW3FuF_vS: الحصول على مدة التشغيل  
fl_BhgXwRaQ8nzexSGjwa7: الحصول على وضع الأمان  

**الحصول على بيانات السجلات**  
fRRbXKNWy6vXbSrRPmFLJa: الحصول على قيم سجلات Int (0-23)  
fRjcTzBeNogyaJtYvJ7_E2: الحصول على قيم سجلات Double (0-23)  
fJ_s1E0ywr6t9rkMOBWiq6: الحصول على قيم سجلات Double (0-31)  

**مراقبة الحالة**  
fVYZ0ocbfuml1VpA5JSNRo: الحصول على إحداثيات TCP في الوقت الحقيقي  
fts21SISQrnyp_mb3jJy91: الحصول على زوايا المفاصل في الوقت الحقيقي  
fmjZNwC7zxju_tLjiM8w4A: الحصول على حالة التشغيل  
fy5NIEBXN7Kqecb1RkPhZN: الحصول على حالة تنفيذ البرنامج  

**مراقبة المعايير الكهربائية**  
fGU3ubp1fmrw-zPE2pyNDI: الحصول على الجهد الحالي  
fl--FA0LvH9LBjXjVB0gGD: الحصول على التيار الحالي  
fb3HhLwWUa8s49OXpU5Iq8: الحصول على جهد كل مفصل  
frGKnkZFPFesyEXdGAxpD9: الحصول على تيار كل مفصل  
fzVxBGVvO7T3n3JbmAmvqB: الحصول على درجة حرارة كل مفصل  

### 2.2 تنفيذ أوامر فردية لروبوتات UR  
**وظائف التحكم في الحركة**  
ffoF99tQZ6vcEqHQplHTjv: إرسال أوامر وضع المفاصل (movej)  
fiF4Pmxs7LQTrG7hY4sQV8: إرسال أوامر حركة TCP الخطية (movel)  
fOyQY2wR6xzOZP3NxjpLjK: الحركة الخطية على طول محور X  
fCV_0M8pdPIVJs3nMGo6XS: الحركة الخطية على طول محور Y  
fWkTyW-C5rxUPe3U0WGSsm: الحركة الخطية على طول محور Z  

### 2.3 كتابة برامج روبوتات UR باستخدام نموذج لغوي كبير وتنفيذها  

### 2.4 تشغيل البرامج المدمجة في روبوتات UR  
**التحكم في البرامج**  
fE0WxXcDh3ENo8Q3fYul5K: تحميل برنامج UR  
fDqpZeOA1_KF8ixwndRP8-: تحميل وتنفيذ برنامج UR  
fH1AYKDXPCcGU1q3Ndrnwt: إيقاف البرنامج الحالي  
fVwECQj8_p85mT6KaggA-N: إيقاف البرنامج الحالي مؤقتًا  
f4cp0iAFlVXMWqz51ylP4Z: إرسال نص البرنامج  

### 2.5 التنسيق بين عدة روبوتات UR  


## 3. إخلاء المسؤولية

قبل استخدام nUR MCP Server، تأكد من تدريب المشغلين على سلامة روبوتات UR ومعرفتهم بإيقاف الطوارئ (E-stop).

افحص الروبوت والخوادم بانتظام لضمان الاستقرار.

التزم بالبروتوكولات التالية عند الاستخدام:

الرؤية المباشرة للروبوت

يجب أن يبقى روبوت Universal Robots ضمن مجال رؤية المشغل للمراقبة الفورية.

يُمنع مغادرة المنطقة أثناء التشغيل.

تأمين البيئة

أزل العوائق وتأكد من خلو المنطقة الخطرة من الأشخاص/الأشياء.

ضع حواجز مادية أو ستائر ضوئية عند الحاجة.

تنصل قانوني

نحن غير مسؤولين عن الإصابات أو الأضرار الناجمة عن عدم الامتثال للاشتراطات (مثل الإهمال أو عدم التأمين).

المستخدم يتحمل جميع المخاطر.

## 4. إصدارات النسخ

### 4.1 التحديثات الحديثة

* **2025.05.15**: الإصدار الأولي لـ nUR_MCP_SERVER

### 4.2 الخطط المستقبلية

* تطوير عميل MCP مخصص لخادم nUR MCP لتحسين ميزات أمان المشغلات
* إضافة وظيفة تسجيل سجلات روبوتات UR
* تمكين نسخ احتياطي وتحويل برامج روبوتات UR

## 5. البدء السريع

### 5.1 حسب المنتج (للمستخدمين العاديين)

#### 5.1.1 المحرك والتبعيات

* **إصدارات النظام الموصى بها:**

  ```text
  مستخدمو macOS: macOS Monterey 12.6 أو أحدث
  مستخدمو Linux: CentOS 7 / Ubuntu 20.04 أو أحدث
  مستخدمو Windows: Windows 10 LTSC 2021 أو أحدث
  ```

* **متطلبات البرمجيات:**

  **بيئة خادم MCP**

  ```text
  Python 3.11 أو أحدث
  pip 25.1 أو أحدث
  مدير الحزم UV 0.6.14 أو أحدث
  bun 1.2.8 أو أحدث
  ```

  **عميل MCP**

  ```text
  Claude Desktop 3.7.0 أو أحدث
  Cherry Studio 1.2.10 أو أحدث
  Cline 3.14.1 أو أحدث

  ClaudeMind، Cursor، NextChat، ChatMCP، Copilot-MCP، Continue، Dolphin-MCP، Goose - لم يتم اختبارها.
  ```

  **نماذج اللغة الكبيرة LLM**

  ```text
  DeepSeek-V3-0324 أو أحدث
  DeepSeek-R1-671b أو أحدث
  Qwen3-235b-a22b أو أحدث

  بشكل عام، يمكن استخدام أي نموذج LLM مدعوم من MCP. النماذج غير المدرجة هنا لم يتم اختبارها.
  النماذج المثبتة عبر Ollama لا يمكنها حاليًا استدعاء الأدوات (قيد الحل)...
  ```

#### 5.1.2 التثبيت  

**تثبيت خادم MCP:**  
1. ثبّت بايثون 3.11 أو أحدث  
2. ثبّت pip 25.1 أو أحدث  
3. ثبّت مدير الحزم UV 0.6.14 أو أحدث  
4. ثبّت bun 1.2.8 أو أحدث  
5. ثبّت خادم MCP:  
```
git clone https://gitee.com/nonead/nUR_MCP_SERVER.git  
cd nUR_MCP_SERVER  
pip install -r requirements.txt  
```  

**تهيئة عميل MCP:**  

**لاستخدام مع Claude Desktop، أضف تكوين الخادم:**
**لـ macOS:** ~/Library/Application Support/Claude/claude_desktop_config.json  
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

**لـ Windows:** %APPDATA%/Claude/claude_desktop_config.json  
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

**لاستخدام مع Cherry Studio، أضف تكوين الخادم:**

**لـ macOS وLinux:**
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "name": "nUR_MCP_Server",
      "type": "stdio",
      "description": "خادم NONEAD Universal-Robots MCP",
      "isActive": true,
      "provider": "شركة NONEAD",
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

**لـ Windows:**
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "name": "nUR_MCP_Server",
      "type": "stdio",
      "description": "خادم NONEAD Universal-Robots MCP",
      "isActive": true,
      "provider": "شركة NONEAD",
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

**لاستخدامه مع Cline، أضف تكوين الخادم:**
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


### 5.2 بناءً على مجموعة الأدوات (للمطورين)

#### 5.2.1 المحرك والتبعيات 

* **إصدارات النظام الموصى بها:**

  ```text
  مستخدمو macOS: macOS Monterey 12.6 أو أحدث
  مستخدمو Linux: CentOS 7 / Ubuntu 20.04 أو أحدث
  مستخدمو Windows: Windows 10 LTSC 2021 أو أحدث
  ```

* **متطلبات البرمجيات:**

  بيئة خادم MCP

  ```text
  Python 3.11 أو أحدث     
  pip 25.1 أو أحدث
  UV Package Manager 0.6.14 أو أحدث  
  bun 1.2.8 أو أحدث
  ```
  نماذج اللغة الكبيرة LLM

  ```text
  DeepSeek-V3-0324 أو أحدث
  DeepSeek-R1-671b أو أحدث 
  Qwen3-235b-a22b أو أحدث
  
  عادةً ما تكون نماذج اللغة الكبيرة التي تدعم MCP قابلة للاستخدام. النماذج غير المدرجة لم يتم اختبارها
  النماذج الموزعة عبر Ollama لا يمكنها حاليًا استدعاء الأدوات. قيد الحل...
  ```

#### 5.2.2 التثبيت

**لمطوري macOS/Linux/Windows**

```text
  Python 3.11  أو أحدث     
  pip 25.1  أو أحدث
  UV Package Manager 0.6.14  أو أحدث  
  bun 1.2.8  أو أحدث
```

#### 5.2.3 الاستخدام

أمثلة على مهام يمكن لنماذج اللغة الكبيرة تنفيذها:

* توصيل روبوت يونيفرسال عبر IP: 192.168.1.199
* الحصول على إحداثيات وضعية أداة TCP النهائية الحالية
* سرد جميع أوامر أداة nUR_MCP_SERVER
* استرجاع جميع بيانات أجهزة روبوت يونيفرسال
* تنفيذ برنامج نصي للروبوت
* تشغيل البرنامج المدمج XXXX.urp
* تعريف روبوت IP 172.22.109.141 كـ A وIP 172.22.98.41 كـ B، توصيلهما، تسجيل أوضاع TCP الحالية والمواقع الرئيسية لـ A (يسار) وB (يمين)، تحليل العلاقة بين الأوضاع
* تنفيذ خطوة بخطوة: روبوت يونيفرسال IP 192.168.1.199، تسجيل وضع TCP الحالي، ثم تحريك +20مم في Z، -50مم في Y، +30مم في X، تكرار 5 مرات
* كتابة وتنفيذ سكريبت روبوت: رسم دائرة نصف قطرها 50مم في المستوى الأساسي متمركزة على الوضع الحالي
* تعريف روبوتات IP 172.22.109.141 كـ A و172.22.98.41 كـ B، توصيلهما، الأوامر اللاحقة تتحكم فقط في A مع مزامنة حركة مرآة لـ B

## 6. البنية التقنية

تستخدم MCP بنية عميل-خادم مع بروتوكولات معيارية للتواصل بين النموذج والموارد الخارجية.  
![alt](./images/MCP.svg "mcp")  
نموذج العميل-الخادم
المكونات الأساسية:

مضيف MCP: تطبيق LLM (مثل Claude Desktop) يبدأ الاتصالات
عميل MCP: عميل بروتوكول يحافظ على اتصال 1:1 مع الخادم
خادم MCP: برنامج خفيف يعرض وظائف عبر Model Context Protocol المعياري
مصادر البيانات المحلية: ملفات/قواعد بيانات/خدمات يصل إليها الخادم بأمان
الخدمات البعيدة: أنظمة خارجية متاحة عبر الإنترنت (مثل APIs)
المسؤوليات:

مضيف MCP:
يوفر واجهة مستخدم
يدير اتصال موفر LLM
يدمج عميل MCP للوصول إلى الموارد الخارجية
عميل MCP:
يؤسس/يحافظ على اتصال خادم MCP
يرسل الطلبات ويتلقى الردود
يتعامل مع تبادل البيانات حسب معايير MCP
خادم MCP:
يعالج طلبات العملاء
ينفذ وظائف محددة أو يوفر وصولاً للموارد
يُنسق الردود حسب معايير بروتوكول MCP
بروتوكول الاتصال
تستخدم MCP JSON-RPC 2.0 كبروتوكول أساسي، تدعم:  
![alt](./images/p.svg "mcp_json-RPC2.0")    
الطلبات: رسائل تبدأ عمليات من العميل→الخادم أو العكس
الردود: إجابات على الطلبات تحتوي نتائج أو معلومات خطأ
الإشعارات: رسائل أحادية الاتجاه لا تتطلب رداً (عادة للإخطارات)
آليات النقل المدعومة:

الإدخال/الإخراج القياسي (Stdio): للخوادم المحلية عبر اتصال بين العمليات
أحداث مرسلة من الخادم (SSE): آلية نقل تعتمد على HTTP للخوادم البعيدة

مزايا MCP
تتفوق MCP على الطرق التقليدية في التوحيد والأمان والقابلية للتوسع.

التوحيد
التفاعل المعياري يحل مشاكل التجزئة:

وصول يشبه الملحق: بروتوكول موحد لمصادر بيانات متنوعة
التوافق عبر المنصات: يدعم نماذج/منصات ذكاء اصطناعي مختلفة
تبسيط التطوير: التركيز على المنطق التجاري
الأمان
آليات أمان مدمجة تحمي البيانات:

حماية المعلومات الحساسة: مفاتيح API/بيانات المستخدم إلخ
تحكم في الوصول: خادم MCP يمكّن قيود وصول مفصلة
المعالجة المحلية: تتجنب تحميل بيانات حساسة لأطراف ثالثة
القابلية للتوسع
التصميم المعياري يمكّن قابلية توسع عالية:

اتصال متعدد الخدمات: خدمات متعددة تتصل بعملاء متوافقين
توسع النظام البيئي: مكتبة متنامية من المكونات الجاهزة
قابلية التخصيص: تطوير خوادم MCP مخصصة

## 7. اتصل بنا

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**الموقع الرسمي**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="للتواصل: Nonead Tech WeChat" width="200">  

## 8. الفرق بين nUR MCP Server وخوادم MCP الأخرى

يجب أن يتمتع مستخدمو nUR MCP Server بوعي أمان عالٍ جدًا وأن يكونوا قد أكملوا تدريب تشغيل روبوتات Universal، حيث يتحكم النموذج اللغوي الكبير في روبوتات فعلية. قد يتسبب التشغيل غير الصحيح في إصابات بشرية وأضرار مادية - يُرجى توخي أقصى درجات الحذر.

## 9. الاقتباس

إذا كنت تستخدم هذا البرنامج، يُرجى الاقتباس على النحو التالي:

* [nURMCP: NONEAD Universal-Robots Model Context Protocol Server](https://www.nonead.com)
* توضح Nonead المعنى الحقيقي للتصنيع الذكي، وتقود الابتكارات التي تعيد تشكيل عالمنا.

## 10. الترخيص

[رخصة Apache 2.0](LICENSE)

## 11. فريق التطوير الأساسي

فريق تطوير خادم MCP في شركة Suzhou Nonead Robot Technology Co., Ltd.

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>