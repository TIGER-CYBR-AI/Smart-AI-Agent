import os
import requests

# السيرفر المفتوح والمقاوم للحظر الجغرافي
API_URL = "https://pollinations.ai"

def call_ai(prompt):
    """دالة اتصال مباشرة وخفيفة جداً تتوافق مع السيرفر الجديد"""
    try:
        # إرسال النص مباشرة في الرابط بطريقة الـ GET السريعة
        query_url = f"{API_URL}{requests.utils.quote(prompt)}"
        response = requests.get(query_url)
        if response.status_code == 200:
            return response.text
        else:
            return f"خطأ في الاتصال: {response.status_code}"
    except Exception as e:
        return f"فشل الاتصال: {str(e)}"

def coder_agent(task_description):
    """الوكيل الأول: المبرمج"""
    prompt = f"Write a secure, clean Python code for the following task. Provide ONLY the raw code without code blocks or markdown, no explanation:\nTask: {task_description}"
    return call_ai(prompt)

def auditor_agent(generated_code):
    """الوكيل الثاني: المدقق الأمني"""
    prompt = f"Analyze this Python code for any logic flaws or bugs. If it is 100% safe, reply ONLY with 'PASSED'. If there are bugs, list them shortly:\nCode:\n{generated_code}"
    return call_ai(prompt)

def run_development_cycle(task):
    """حلقة التصحيح الذاتي والنقاش"""
    print(f"\n[+] بدء العمل على: {task}")
    
    print("[*] المبرمج يصيغ الكود...")
    current_code = coder_agent(task)
    
    max_attempts = 2
    for attempt in range(1, max_attempts + 1):
        print(f"[*] محاولة {attempt}: المدقق الأمني يفحص الكود...")
        audit_report = auditor_agent(current_code)
        
        if "PASSED" in audit_report.upper():
            print("[+] نجاح! الكود سليم بنسبة 100%.")
            return current_code, audit_report
        else:
            print(f"[!] ملاحظات أمنية:\n{audit_report}")
            print("[*] إعادة الإصلاح...")
            fix_prompt = f"Fix this Python code based on this report. Return ONLY corrected code:\nCode:\n{current_code}\nReport:\n{audit_report}"
            current_code = call_ai(fix_prompt)
            
    return current_code, audit_report

if __name__ == "__main__":
    task = "Write a function to read a file safely without path traversal"
    final_code, final_report = run_development_cycle(task)
    print("\n================== النسخة الآمنة النهائية ==================")
    print(final_code)

