import asyncio
from playwright.async_api import async_playwright
import json
from bs4 import BeautifulSoup
import os 
class SecurityIssueScraper:
    def __init__(self):
        self.results = []

    async def scrape_site(self, url):
        async with async_playwright() as p:
            # إضافة User-Agent لكي يبدو المتصفح كأنه مستخدم حقيقي
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            
            print(f"جاري الدخول إلى: {url}")
            try:
                # تغيير wait_until وزيادة المهلة لـ 60 ثانية
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                
                # انتظار إضافي بسيط للتأكد من ظهور المحتوى
                await page.wait_for_timeout(5000) 

                for _ in range(2):
                    await page.mouse.wheel(0, 1000)
                    await asyncio.sleep(2)

                content = await page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # استخراج البيانات (نفس المنطق السابق)
                articles = soup.find_all(['div', 'article', 'h3']) 
                for item in articles :
                    text = item.get_text().strip()
                    text = " ".join(text.split()) # إزالة المسافات الزائدة
                    if len(text) > 60 and "reddit" not in text.lower(): # جلب النصوص الطويلة فقط (المشاكل)
                        self.results.append({
                            "description": text,
                            "source": url
                        })

            except Exception as e:
                print(f"⚠️ حدث خطأ أثناء تحميل {url}: {e}")
            
            finally:
                await browser.close()
    def save_to_json(self, filename="scraped_data.json"):
        # 1. تحديد اسم المجلد
        folder_name = "data"
        
        # 2. التأكد من وجود المجلد، وإنشاؤه إذا لم يكن موجوداً
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"📁 تم إنشاء المجلد: {folder_name}")

        # 3. دمج المسار (Path) للمجلد مع اسم الملف
        filepath = os.path.join(folder_name, filename)

        # 4. حفظ البيانات
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
            
        print(f"✅ تم حفظ {len(self.results)} سجل بنجاح في: {filepath}")
async def main():
    scraper = SecurityIssueScraper()
    
    # يمكنك إضافة روابط البحث هنا (مثلاً من Reddit أو مدونات أمنية)
    search_urls = [
        # "https://www.reddit.com/r/cybersecurity/search/?q=data+breach+cloud",
        "https://www.bleepingcomputer.com/search/?q=leak",
        "https://www.darkreading.com/search?q=cloud+security",
        "https://www.securityweek.com/search?q=cloud+security",
        "https://www.theregister.com/search?q=cloud+security",
        "https://www.wired.com/search?q=cloud+security",
        "https://www.zdnet.com/search/?q=cloud+security",
        "https://krebsonsecurity.com/?s=cloud+leak",
        "https://www.cvedetails.com/google-search-results.php?q=cloud+storage",
        "https://cloudsecurityalliance.org/search?q=top+threats",
        "https://www.bleepingcomputer.com/search/?q=cloud+storage+leak"
    ]
    
    for url in search_urls:
        await scraper.scrape_site(url)
    
    scraper.save_to_json()

if __name__ == "__main__":
    asyncio.run(main())