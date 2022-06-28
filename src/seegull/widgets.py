import tkinter as tk
from typing import Union


class BaseWidget(tk.Widget):
    def set_parent(self, parent: Union[tk.Widget, tk.Tk]):
        self.parent = parent

    def create(self):
        pass


class Page(BaseWidget):
    pass


class Output(BaseWidget):
    pass
