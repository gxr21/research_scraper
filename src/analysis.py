import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import os

# 1. إعداد المسارات (Paths) لضمان التنظيم
input_path = os.path.join('data', 'scraped_data.json')
output_folder = 'export'
output_image = os.path.join(output_folder, 'analysis_result.png')

# التأكد من وجود مجلد التصدير
os.makedirs(output_folder, exist_ok=True)

# 2. تحميل البيانات من ملف JSON داخل مجلد data
try:
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✅ تم تحميل البيانات بنجاح من {input_path}")
except FileNotFoundError:
    print(f"❌ خطأ: لم يتم العثور على {input_path}. تأكد من تشغيل السكرابر أولاً.")
    exit()

# 3. تنظيف النصوص وجمع الكلمات
text_pool = " ".join([item['description'].lower() for item in data])
words = re.findall(r'\w+', text_pool)

# 4. تحديد الكلمات المفتاحية
target_keywords = ['leak', 'breach', 'security', 'cloud', 'hacked', 'stolen', 'privacy', 'vulnerability']
filtered_words = [word for word in words if word in target_keywords]

# 5. حساب التكرار
word_counts = Counter(filtered_words)
df = pd.DataFrame(word_counts.items(), columns=['Keyword', 'Frequency']).sort_values(by='Frequency', ascending=False)

# 6. رسم المخطط البياني
plt.figure(figsize=(10, 6))
plt.bar(df['Keyword'], df['Frequency'], color='skyblue')
plt.title('Common Security Issues Found in Web Scraping Analysis')
plt.xlabel('Security Terms')
plt.ylabel('Number of Occurrences')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 7. حفظ الصورة في مجلد export
plt.savefig(output_image)
print(f"✨ تم حفظ المخطط البياني بنجاح في: {output_image}")
plt.show()