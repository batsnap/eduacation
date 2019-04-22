from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout




Config.set('graphics','resizable','0')
Config.set('graphics','width','600')
Config.set('graphics','height','480')
class MyApp(App):

   def build(self):
      f1=FloatLayout(size=(300,300))
      f1.add_widget(Button(text="это моя первая кнопка",
      font_size=16,
      on_press=self.btn_press,
      background_color=[1,0,0,1],
      background_normal='',
      size_hint=(.5,.25),
      pos=(160,480/2-(480*.25/2))))
      
      return f1



   def btn_press(self,instance):
      print('кнопка нажата!')
      instance.text='я нажата'
if __name__=="__main__":
   MyApp().run()
