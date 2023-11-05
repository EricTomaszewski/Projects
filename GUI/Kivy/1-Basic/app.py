import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

class MyApp(App):
    def build(self):
        self.input_text = TextInput()
        self.output_label = Label()
        self.slider_value = Label()
        
        slider = Slider(min=0, max=1, value=0, step=0.1)
        slider.bind(value=self.on_slider_value_change)
        
        button = Button(text='Translate')
        button.bind(on_release=self.on_button_release)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.input_text)
        layout.add_widget(slider)
        layout.add_widget(self.slider_value)
        layout.add_widget(button)
        layout.add_widget(self.output_label)
        
        return layout
    
    def on_slider_value_change(self, instance, value):    
        # Show only the first decimal number.
        value = '{:.1f}'.format(value)
        self.slider_value.text = str(value)
        
    def on_button_release(self, instance):
        # Translate the input text to another language
        translated_text = translate(self.input_text.text, 'en', 'es')
        
        self.output_label.text = translated_text
        
if __name__ == '__main__':
    MyApp().run()
        