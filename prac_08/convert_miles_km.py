"""
CP1404/CP5632 Practical 08
Estimate: 15 min
Actual: 20 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Convert miles to kilometres with live updating."""
    km_text = StringProperty("0.0")

    def build(self):
        self.title = "Miles ⇢ Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Update km_text based on current input."""
        self.km_text = str(self.get_validated_miles() * MILES_TO_KM)

    def handle_increment(self, change):
        """Increment or decrement the miles value, then recalculate."""
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """Return the current miles value as float or 0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


if __name__ == '__main__':
    MilesConverterApp().run()
