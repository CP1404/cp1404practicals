"""
CP1404/CP5632 Practical 08
Estimate: 15 min
Actual: 15 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """SquareNumberApp squares a user‑entered number."""
    def build(self):
        Window.size = (300, 120)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) ** 2
        except ValueError:
            result = 0
        self.root.ids.output_label.text = str(result)


if __name__ == '__main__':
    SquareNumberApp().run()
