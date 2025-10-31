"""
CP1404/CP5632 Practical 08
Estimate: 15 min
Actual: 15 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically adds labels for a list of names."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))


if __name__ == '__main__':
    DynamicLabelsApp().run()
