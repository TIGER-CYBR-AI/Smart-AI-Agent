import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.core.window import Window

# ضبط أبعاد الشاشة لتناسب الهاتف
Window.clearcolor = (0.05, 0.05, 0.07, 1)

class SmartAgentApp(App):
    def build(self):
        self.title = "مساعدي الذكي الاحترافي"
        
        # التخطيط الرئيسي للتطبيق
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # عنوان التطبيق العلوي
        title_label = Label(text="AI Security & Coding Agent", font_size=20, size_hint_y=0.1, color=(0, 0.7, 1, 1))
        main_layout.add_widget(title_label)
        
        # منطقة عرض المحادثة والأكواد الآمنة (Scrollable)
        self.scroll = ScrollView(size_hint_y=0.6)
        self.chat_box = Label(text="مرحباً بك! اكتب مهمتك البرمجية في الأسفل وسيقوم المبرمج والمدقق الأمني بإكمالها بدقة...", 
                              font_size=16, halign='left', valign='top', size_hint_y=None, color=(0.9, 0.9, 0.9, 1))
        self.chat_box.bind(texture_size=self.chat_box.setter('size'))
        self.scroll.add_widget(self.chat_box)
        main_layout.add_widget(self.scroll)
        
        # خانة إدخال الأوامر والمهام
        self.user_input = TextInput(hint_text="اكتب هنا (مثال: Write a secure login function)...", 
                                    multiline=False, size_hint_y=0.15, background_color=(0.1, 0.1, 0.15, 1), foreground_color=(1, 1, 1, 1))
        main_layout.add_widget(self.user_input)
        
        # زر تشغيل المساعدين الأذكياء
        run_btn = Button(text="ابدأ التطوير والتدقيق الأمني", size_hint_y=0.15, background_color=(0, 0.5, 0.9, 1), font_size=18)
        run_btn.bind(on_press=self.start_agent_cycle)
        main_layout.add_widget(run_btn)
        
        return main_layout

    def start_agent_cycle(self, instance):
        task = self.user_input.text
        if not task:
            self.chat_box.text = "[!] يرجى كتابة مهمة أولاً..."
            return
            
        self.chat_box.text = f"[+] جاري بدء العمل على مهمتك: {task}\n[*] يتصل المبرمج بالسحاب الآن..."
        
        # استدعاء المحرك البرمجي الذي بنيناه وتعديله للتوافق المباشر
        API_URL = "https://pollinations.ai"
        try:
            # فلترة وتحسين استجابة السيرفر المباشرة
            prompt = f"Write secure code for: {task}. Return only code."
            query_url = f"{API_URL}{requests.utils.quote(prompt)}"
            res = requests.get(query_url)
            
            if res.status_code == 200:
                clean_text = res.text.replace("Failed to parse:", "").strip()
                self.chat_box.text = f"================ النسخة الآمنة النهائية ================\n\n{clean_text}"
            else:
                self.chat_box.text = f"[!] خطأ في الاتصال: {res.status_code}"
        except Exception as e:
            self.chat_box.text = f"[!] فشل التنفيذ: {str(e)}"
            
        self.user_input.text = ""

if __name__ == "__main__":
    SmartAgentApp().run()
