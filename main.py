from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
import random

class F100_Striker(App):
    def build(self):
        Window.fullscreen = 'auto'
        Window.bind(on_keyboard=self.on_key)
        self.time_left = 24 * 3600 
        self.active = True
        self.root = FloatLayout()

        # العنوان
        self.title = Label(text="TEAM_F100💻", font_size='45sp', bold=True,
                          color=get_color_from_hex('#FF0000'), pos_hint={'center_x': 0.5, 'center_y': 0.85})
        
        # التايمر
        self.timer_label = Label(text="24:00:00", font_size='60sp', pos_hint={'center_x': 0.5, 'center_y': 0.7})
        
        # التهديد
        self.warning = Label(text="ila briti lcode doz telegram [@f100_teamm]\n9bl madouz lmoda ila dazt radi ytfa lk tilfon\nmayx3alx!!",
                            halign='center', font_size='15sp', pos_hint={'center_x': 0.5, 'center_y': 0.55})
        
        # الثمن
        self.price = Label(text="taman lcode: 30dh💵", font_size='22sp', bold=True,
                          color=get_color_from_hex('#00FF00'), pos_hint={'center_x': 0.5, 'center_y': 0.45})
        
        # الإدخال والزر
        self.input_code = TextInput(hint_text="ENTER CODE", password=True, size_hint=(0.8, 0.08),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.35}, halign='center')
        self.btn_unlock = Button(text="UNLOCK DEVICE", size_hint=(0.6, 0.1), background_color=(1,0,0,1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.btn_unlock.bind(on_press=self.check_unlock)

        self.root.add_widget(self.title); self.root.add_widget(self.timer_label)
        self.root.add_widget(self.warning); self.root.add_widget(self.price)
        self.root.add_widget(self.input_code); self.root.add_widget(self.btn_unlock)

        Clock.schedule_interval(self.update_timer, 1)
        return self.root

    def on_key(self, window, key, *args): return True # بلوك زر الرجوع

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            h, m, s = self.time_left // 3600, (self.time_left % 3600) // 60, self.time_left % 60
            self.timer_label.text = f"{h:02d}:{m:02d}:{s:02d}"
        else:
            if self.active: self.trigger_virus()

    def check_unlock(self, instance):
        if self.input_code.text == "JACK_F100": self.stop()
        else:
            self.time_left = max(0, self.time_left - 3600)
            self.input_code.text = ""; self.title.text = "WRONG CODE! -1h"

    def trigger_virus(self):
        self.active = False; self.root.clear_widgets()
        self.final_label = Label(text="SYSTEM DESTROYED", font_size='35sp', color=(1,0,0,1))
        self.root.add_widget(self.final_label)
        Clock.schedule_interval(self.stress_test, 0.05)

    def stress_test(self, dt):
        Window.clearcolor = (random.random(), 0, 0, 1)
        self.final_label.text = f"WIPING SYSTEM...\nError_Code: {random.randint(100,999)}"

if __name__ == "__main__":
    F100_Striker().run()