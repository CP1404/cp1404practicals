"""
CP1404/CP5632 Practical 08
Estimate: 15 min
Actual: 18 min
"""


from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """App that greets the user and can clear the screen."""
    def build(self):
        self.title = "Greeter"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display greeting using the name entered."""
        name = self.root.ids.input_name.text.strip()
        self.root.ids.output_label.text = f"Hello {name}" if name else "Hello"

    def handle_clear(self):
        """Clear the input and output fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


if __name__ == '__main__':
    BoxLayoutDemo().run()
