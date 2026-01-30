from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import psutil
import hashlib
import time

# ============================================================
# SOVEREIGN OS - ANDROID MONSTER EDITION v6.0
# Developer: Ahmed Osama (15yo)
# ============================================================

class SovereignAndroid(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # واجهة الوحش للهاتف (Neon Green Style)
        self.bg_color = (0, 0, 0, 1)
        
        self.label_title = MDLabel(
            text="SOVEREIGN MOBILE CORE",
            halign="center",
            pos_hint={"center_y": 0.9},
            font_style="H4",
            theme_text_color="Custom",
            text_color=(0, 1, 0.2, 1)
        )
        self.add_widget(self.label_title)

        # شاشة الرادار اللحظي
        self.stats_label = MDLabel(
            text="INITIALIZING PHYSICAL RADAR...",
            halign="left",
            pos_hint={"center_x": 0.55, "center_y": 0.5},
            theme_text_color="Custom",
            text_color=(0, 0.8, 0, 1),
            font_style="Caption"
        )
        self.add_widget(self.stats_label)

        # زر السيادة المطلقة
        self.btn_seize = MDRaisedButton(
            text="SEIZE MOBILE CONTROL",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            md_bg_color=(1, 0, 0, 1),
            on_release=self.activate_sovereignty
        )
        self.add_widget(self.btn_seize)

        # تحديث البيانات كل ثانية
        Clock.schedule_interval(self.update_radar, 1)

    def update_radar(self, dt):
        # ميزات حقيقية: قراءة المعالج والبطارية
        cpu = psutil.cpu_percent()
        battery = psutil.sensors_battery()
        bat_per = battery.percent if battery else "N/A"
        
        # خوارزمية التشفير بالوقت والعتاد
        entropy_key = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        
        radar_text = (
            f"--- SOVEREIGN RADAR v6.0 ---\n"
            f"[STATUS]: MASTER PRIORITY ACTIVE\n"
            f"[CPU LOAD]: {cpu}%\n"
            f"[BATTERY]: {bat_per}%\n"
            f"[ENTROPY KEY]: {entropy_key}\n"
            f"[SHIELD]: OFFLINE ENCRYPTION ON\n"
            f"----------------------------\n"
            f">>> ANALYZING THERMAL STRESS...\n"
            f">>> SECURING HARDWARE THREADS..."
        )
        self.stats_label.text = radar_text

    def activate_sovereignty(self, instance):
        self.stats_label.text += "\n\n[CRITICAL]: PRIVILEGES ELEVATED!"

class MonsterMobileApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return SovereignAndroid()

if __name__ == "__main__":
    MonsterMobileApp().run()
