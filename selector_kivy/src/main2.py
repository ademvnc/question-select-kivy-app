from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

class QuestionSelector(BoxLayout):
    def __init__(self, **kwargs):
        super(QuestionSelector, self).__init__(**kwargs)

        # Dikey bir düzen oluşturun
        self.orientation = 'vertical'

        # Sol taraftaki düzen
        left_layout = BoxLayout(orientation='horizontal', spacing=10, padding=3,size_hint=(1, None), height=100)

        # Değer girişi için metin giriş kutusu
        self.num_input = TextInput(hint_text='Kaç adet öğrenci seçilecek?',
                                    multiline=False,
                                    input_type='number',
                                    input_filter='int', size_hint=(None, None), size=(400, 75))

        # Soruları oluştur butonu
        self.generate_button = Button(text='Soruları Oluştur', background_color=(2.5, 0, 1.5, 1) , size_hint=(None, None), size=(200, 75))
        self.generate_button.bind(on_press=self.generate_questions)
        
        # Çıkış butonu
        self.exit_button = Button(text='Çıkış', background_color=(2.5, 0, 0, 1), size_hint=(None, None), size=(200, 75))
        self.exit_button.bind(on_press=self.exit_app)

        # Sol taraftaki widget'ları düzene ekleyin
        left_layout.add_widget(self.num_input)
        left_layout.add_widget(self.generate_button)
        left_layout.add_widget(self.exit_button)

        # Sağ taraftaki düzen
        self.right_layout = GridLayout(cols=2, spacing=15, padding=15)

        # Sol ve sağ taraftaki düzenleri ana düzene ekleyin
        self.add_widget(left_layout)
        self.add_widget(self.right_layout)

    def generate_questions(self, instance):
        try:
            num = int(self.num_input.text)
            if num == 0:
                self.show_popup("Lütfen geçerli bir sayı giriniz.")
                return
            
            if num < 0:
                self.show_popup("Lütfen pozitif bir sayı giriniz.")
                return

            questions = ['Was?', 'Wo?', 'Wann?', 'Wie?', 'Warum?', 'Wer?']
            selected_questions = random.choices(questions, k=num*3)  # Her öğrenci için 3 soru seçildiği için num*3
            
            # Sağ taraftaki düzeni temizle
            self.right_layout.clear_widgets()

            for i in range(num):
                student_questions = selected_questions[i*3 : (i+1)*3]  # Her öğrenci için 3 soru seç
                student_questions_text = ", ".join(student_questions)  # Soruları virgülle ayırarak birleştir
                self.right_layout.add_widget(Label(text=f"{i + 1}. Öğrenci: {student_questions_text}", color=(1, 1, 0, 1), font_size='25sp'))
                
        except ValueError:
            self.show_popup("Geçerli bir sayı giriniz.")

    def exit_app(self, instance):
        self.show_popup("Çıkış yapılıyor...")

    def show_popup(self, content):
        # Popup içeriğini ayarla
        popup = Popup(title='Uyarı', content=Label(text=content), size_hint=(None, None), size=(400, 200))
        # Popup'ı göster
        popup.open()
        # Çıkış popup'ı kapatıldıktan sonra uygulamayı kapatmak için 1 saniye bekleyin
        if content == "Çıkış yapılıyor...":
            Clock.schedule_once(self.close_app, 1)

    def close_app(self, *args):
        App.get_running_app().stop()

class QuestionApp(App):
    def build(self):
        return QuestionSelector()

if __name__ == "__main__":
    QuestionApp().run()
