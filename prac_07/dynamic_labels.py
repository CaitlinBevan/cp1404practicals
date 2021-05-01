"""
CP1404 Practical
Kivy GUI program for dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def create_labels(self):
        """Create labels from dictionary entries."""
        for name in self.name_to_phone:
            temp_label = Button(text=name)
            temp_label.bind()
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
