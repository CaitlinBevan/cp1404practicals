"""
CP1404 Practical
Kivy GUI program to convert m to km
"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMtoKm(App):
    """ConvertMtoKm is a Kivy App for to convert miles to kilometres."""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root


ConvertMtoKm().run()
