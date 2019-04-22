from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import  Gridlayout
#from kivy.uix.boxlayout import  BoxLayout
#from kivy.uix.textinput import TextInput
class MyApp(App):
   def build(self):
      al= AnchorLayout()
      bl= BoxLayout(orientation='vertical',size_hint=[.4,.4])
      bl.add_widget(TextInput())
      bl.add_widget(TextInput())
      bl.add_widget(Button(text="ГЫ"))
      al.add_widget(bl)
      return al








if __name__=="__main__":
   MyApp().run()
