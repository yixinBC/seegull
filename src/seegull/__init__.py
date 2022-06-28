import tkinter as tk
from typing import List
from . import widgets


class App:
    def __init__(self, base_program: str):
        self.base_program = base_program
        self.root = tk.Tk()


    def run(self):
        self.root.title(self.base_program)
        self.root.mainloop()

    
    def set_output(self, output: widgets.Output):
        self.output = output


class SinglePageApp(App):
    """
    a single page app is used to create a program that has a single page.
    """
    def __init__(self, base_program: str):
        super().__init__(base_program)
        self.widgets : List[widgets.BaseWidget]= []


    def add_widget(self, widget: widgets.BaseWidget):
        self.widgets.append(widget)
        widget.set_parent(self.root)


    def create_widgets(self):
        for widget in self.widgets:
            widget.create()


class MultiPageApp(App):
    """
    a multi page app is used to create a program that has multiple pages.
    """
    def __init__(self, base_program: str):
        super().__init__(base_program)
        self.pages : List[widgets.Page]= []


    def add_page(self, page: widgets.Page):
        self.pages.append(page)
        page.set_parent(self.root)


    def create_pages(self):
        for page in self.pages:
            page.create()
