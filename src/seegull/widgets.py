import tkinter as tk
from tkinter import ttk
from typing import Union


class BaseWidget:
    def set_parent(self, parent: Union[ttk.Frame, tk.Tk]):
        self.parent = parent

    def create(self):
        pass


class Page(BaseWidget):
    pass


class Output(BaseWidget):
    pass
