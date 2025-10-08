from tkinter import *
import tkinter as tk  

def _on_hover(event, used_color: str, used_font: tuple = ("Freestyle Script", 48)) -> None:
    """
    Apply a small animation when the mouse hovers a widget.
    """
    event.widget["foreground"] = used_color
    event.widget["font"] = used_font
    return None
    
def _on_default(event, used_color : str, used_font : tuple = ("Freestyle Script", 48)) -> None:
    """
    Apply a small animation when the mouse is no longer hovering a widget.
    """
    event.widget["foreground"] = used_color
    event.widget["font"] = used_font

    return None