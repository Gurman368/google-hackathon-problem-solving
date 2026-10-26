from kivy.uix.screen import Screen
from kivy.lang import Builder

# The Lottie widget needs to be imported so the KV parser recognizes it.
from GLLottie.gleslottie import Lottie

KV = '''
<LoadingScreen>:
    Lottie:
        source: 'main/assets/Material wave loading.json'
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint: None, None
        size: "200dp", "200dp"
        loop: True
        # The animation will play automatically when the widget is visible
'''

Builder.load_string(KV)

class LoadingScreen(Screen):
    pass