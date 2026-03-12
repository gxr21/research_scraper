import json
import os

def export_problems():
    # 1. إعداد المسارات
    input_path = os.path.join('data', 'scraped_data.json')
    output_folder = 'problems_search'
    output_file = os.path.join(output_folder, 'problems_for_thesis.txt')

    # 2. التأكد من وجود مجلد المخرجات
    os.makedirs(output_folder, exist_ok=True)

    try:
        # 3. تحميل البيانات من مجلد data
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 4. معالجة وحفظ النصوص في مجلد problems_search
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("===============================================\n")
            f_out.write("   RESEARCH EVIDENCE: DETAILED SECURITY ISSUES \n")
            f_out.write("===============================================\n\n")
            
            count = 0
            for index, item in enumerate(data, 1):
                desc = item.get('description', '').strip()
                
                # تصفية النصوص (جلب القصص والمشاكل الحقيقية فقط)
                if len(desc) > 100: 
                    count += 1
                    f_out.write(f"CASE STUDY ({count}):\n")
                    f_out.write(f"SOURCE: {item.get('source', 'N/A')}\n")
                    f_out.write(f"DETAILS: {desc}\n")
                    f_out.write("-" * 60 + "\n")
            
        print(f"✅ تم استخراج {count} حالة بنجاح في: {output_file}")
        
    except FileNotFoundError:
        print(f"❌ خطأ: لم يتم العثور على {input_path}. تأكد من وجود ملف البيانات أولاً.")
    except Exception as e:
        print(f"⚠️ حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    export_problems()