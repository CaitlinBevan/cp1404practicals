"""
CP1404 Practical
Kivy GUI program to convert m to km
"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMtoKm(App):
    """ConvertMtoKm is a Kivy App for to convert miles to kilometres."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label widget."""
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)


ConvertMtoKm().run()
