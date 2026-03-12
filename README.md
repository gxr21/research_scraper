# 🛡️ Cyber-Insight: Web Scraping & AI Classifier Pipeline

**Automated Security Threat Intelligence Gathering and Classification**

---

# 🌐 English Version

## 📝 Description

**Cyber-Insight** is a powerful Python-based pipeline designed for researchers and developers in the cybersecurity field. It automates the process of collecting real-time security data from multiple technical news sources and uses State-of-the-Art Natural Language Processing (NLP) to classify threats into actionable categories.

## 🚀 Key Features

* **Intelligent Scraping:** Targeted extraction of security news from top-tier sources such as BleepingComputer and ZDNet.
* **AI-Powered Classification:** Utilizes the `facebook/bart-large-mnli` model for Zero-shot classification.
* **Smart Filtering:** Automated noise reduction (removes irrelevant content, short snippets, and specific platform noise).
* **Data Categorization:** Automatically groups findings into:

1. Technical Vulnerabilities & Exploits
2. Financial Loss & Economic Impact
3. Public Opinion & Reputation Damage

* **Research-Ready Output:** Generates structured CSV files compatible with Excel and Google Sheets for statistical analysis.

## 🎓 For Researchers & Developers

### Researchers

Use this tool to justify **Problem Statements** with real-world data and identify emerging threat trends such as Zero-day exploits.

### Developers

Build datasets for training security models or understand common software vulnerabilities to improve defensive coding practices.

---

# 🌍 النسخة العربية

## 📝 وصف الأداة

**Cyber-Insight** هي أداة برمجية متكاملة مبنية بلغة بايثون مخصصة للباحثين والمطورين في مجال الأمن السيبراني. تقوم الأداة بأتمتة عملية جمع البيانات الأمنية اللحظية من مصادر إخبارية تقنية متعددة، ثم تستخدم نماذج معالجة اللغات الطبيعية (NLP) المتقدمة لتصنيف هذه التهديدات إلى فئات محددة بدقة.

## 🚀 المميزات الرئيسية

* **زاحف ويب ذكي (Scraper):** استخراج مركز للأخبار الأمنية من أفضل المصادر العالمية.
* **تصنيف بالذكاء الاصطناعي:** استخدام نموذج `BART` المتطور لتصنيف النصوص دون الحاجة لتدريب مسبق.
* **تنظيف تلقائي للبيانات:** فلترة النصوص غير المهمة وحذف الضجيج الرقمي لضمان جودة النتائج.

### تصنيف المشاكل إلى:

1. الثغرات التقنية والبرمجية
2. الأضرار المالية والاقتصادية
3. قضايا الخصوصية والسمعة الرقمية

* **مخرجات جاهزة للبحث:** تصدير النتائج بصيغة CSV لسهولة تحليلها إحصائياً في ملفات الوورد والإكسل.

---

# 🛠️ How to Use / كيفية الاستخدام

## 1️⃣ Install Requirements / تثبيت المتطلبات

```bash
pip install transformers pandas beautifulsoup4 requests tqdm torch
```

## 2️⃣ Run the Pipeline / تشغيل الأداة

* Run `scraper.py` to collect raw data.
  قم بتشغيل سكريبت السحب لجمع البيانات الخام.

* Run `classifier_summarizer.py` to process with AI.
  قم بتشغيل سكريبت التصنيف والتحليل باستخدام الذكاء الاصطناعي.

---

# 👨‍💻 Author

**Ali Jalal**
Information Technology Student
Cybersecurity Researcher
