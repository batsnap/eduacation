from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class HomeScreen(Screen):
   pass

class SettingsScreen(Screen):
   pass
GUI=Builder.load_string('''
#: import ScreenManager kivy.uix.screenmanager.ScreenManager
#: import Screen kivy.uix.screenmanager.ScreenManager
#: import SettingsScreen screen

GridLayout:
   cols:1
   ScreenManager:
      id: screen_manager
      HomeScreen:
         name:"home_screen"
         id:home_screen
      SettingsScreen:
         name:"settings_screen"
         id:"settings_screen"
<HomeScreen>:
   BoxLayout:
      GridLayout:
         cols:3
         Button:
            text:"e"
         Button:
            text:"и"
         Button:
            text:"смена экрана"
            on_release:app.change_screen("settings_screen")
<SettingsScreen>:
   Button:
      text:"you are at home screen"
      on_release:app.change_screen("home_screen")
''')



class MainApp(App):
   def build(self):
      return GUI
   def change_screen(self,screen_name):
      screen_manager=self.root.ids['screen_manager']
      screen_manager.current=screen_name
MainApp().run()