"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometres(App):
    """MilesToKilometres is a Kivy App for to convert miles to kilometres."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label widget."""
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Handle button press to increase by one or decrease by one."""
        result = 3 + increment
        self.root.ids.input_number.text = str(result)
        self.handle_calculate(result)


MilesToKilometres().run()
