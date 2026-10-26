from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image

# These KivyMD imports are necessary for the KV string to be parsed correctly.
# Kivy's Builder needs to know about these classes, even if they are not
# directly referenced in the Python code below.
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton

# KV string for the login screen layout
KV = '''
<LoginScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        
        Image:
            # Assumes you have an 'assets' folder in your project root
            # with the logo inside.
            source: 'main/assets/logo.png'
            size_hint_y: 0.3
            pos_hint: {'center_x': 0.5}
            
        MDCard:
            orientation: 'vertical'
            # Allow the card to set its own height based on its content
            size_hint_y: None
            height: self.minimum_height
            width: "280dp"
            pos_hint: {"center_x": .5}
            padding: "25dp"
            spacing: "20dp"
            elevation: 3
            radius: [15]
            
            MDLabel:
                text: "Login"
                type_style: "headline-small"
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]
                
            MDTextField:
                id: username
                hint_text: "Username"
                icon_right: "account"
                size_hint_y: None
                helper_text: "Enter your username"
                helper_text_mode: "on_focus"
            
            MDTextField:
                id: password
                hint_text: "Password"
                icon_right: "key-variant"
                password: True
                size_hint_y: None
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
            
            MDButton:
                style: "filled"
                text: "LOGIN"
                pos_hint: {"center_x": .5}
                size_hint_y: None # All children need a defined height
                height: "48dp"
                md_bg_color: (0.85, 0.85, 0.85, 1) # A light grey
                on_release: root.login()
            
            MDButton:
                style: "text"
                text: "[u]Continue as Guest[/u]"
                markup: True
                theme_text_color: "Custom"
                text_color: (0.4, 0.4, 0.4, 1) # A medium-dark grey
                size_hint_y: None
                height: "36dp"
                pos_hint: {"center_x": .5}
                on_release: root.guest_login()
                
            MDButton:
                style: "text"
                text: "[u]Sign Up[/u]"
                markup: True
                theme_text_color: "Custom"
                text_color: (0.4, 0.4, 0.4, 1) # A medium-dark grey
                size_hint_y: None
                height: "36dp"
                pos_hint: {"center_x": .5}
                on_release: root.signup()
'''

# Load the KV string
Builder.load_string(KV)

class LoginScreen(MDScreen):
    def login(self):
        """Handle login button click"""
        username = self.ids.username.text
        password = self.ids.password.text
        
        # Here you would implement actual authentication logic
        print(f"Login attempt: {username} / {password}")
        # To switch screens: self.manager.current = "main_app_screen"
        
    def guest_login(self):
        """Handle guest login"""
        print("Continuing as guest")
        # Navigate to main app screen without authentication
        # To switch screens: self.manager.current = "main_app_screen"
        
    def signup(self):
        """Handle signup request"""
        print("Navigate to signup screen")
        # Navigate to registration screen
        # To switch screens: self.manager.current = "signup"