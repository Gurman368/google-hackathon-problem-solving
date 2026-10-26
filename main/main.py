from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock

# Import screens
from login import LoginScreen
from loading_screen import LoadingScreen
# You would also import SignupScreen once implemented

# Set window size for development purposes
Window.size = (400, 600)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        # Kivy automatically loads a file named after the App class (main.kv).
        # We return the root widget defined in that file.
        return Builder.load_file('main.kv')

    def on_start(self):
        """Called after the build() method is run to schedule the screen transition."""
        # After 3 seconds, switch from the loading screen to the login screen.
        Clock.schedule_once(self.go_to_login, 3)

    def go_to_login(self, *args):
        """Switches to the login screen."""
        # The root widget is the ScreenManager from main.kv
        self.root.current = "login"

if __name__ == "__main__":
    MainApp().run()