import tkinter as tk
from tkinter import ttk
from .entry_module import create_name_entry_frame
from .radio_button_module import create_radio_button_frame
from .drop_menu_module import create_drop_menu_frame
from .button_module import create_button_frame
import json
from .text_constants import (
    BOLD, 
    FORM_TITLE, 
    HELVETICA, 
    SCENERY_LABEL, 
    STRESS_LABEL, 
    USER_LABEL
)

def build_form(callback):
    root = tk.Tk()
    root.title(FORM_TITLE)

    content_frame = ttk.Frame(root, padding="30 0")
    content_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    style = ttk.Style()

    def create_title_label(parent, text, row, column=0):
        label = tk.Label(parent, text=text, font=(HELVETICA, 12, BOLD))
        label.grid(row=row, column=column, columnspan=2, pady=(10, 5), sticky=tk.W)
        return label

    create_title_label(content_frame, USER_LABEL, row=0)

    user_name_frame, user_name_entry = create_name_entry_frame(content_frame, label_text="Name:")
    user_name_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    user_code_frame, user_code_entry = create_name_entry_frame(content_frame, label_text="Code:")
    user_code_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    create_title_label(content_frame, SCENERY_LABEL, row=3, column=0)
    radio_button_frame, option = create_radio_button_frame(content_frame)
    radio_button_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    create_title_label(content_frame, STRESS_LABEL, row=5, column=0)
    drop_menu_frame, percentage_var = create_drop_menu_frame(content_frame, ["Low", "Medium", "High"], "Level:", "None")
    drop_menu_frame.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    create_title_label(content_frame, "Weapon Type:", row=7, column=0)
    drop_menu_frame_type, weapon_type = create_drop_menu_frame(content_frame, ["glock19", "FNX-45", "desert eagle"], "Type:", "glock19")
    drop_menu_frame_type.grid(row=8, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    button_frame = create_button_frame(root, [], option, percentage_var, user_name_entry, user_code_entry, weapon_type, callback)
    button_frame.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    version_label = tk.Label(root, text="v1.1.2")
    version_label.grid(row=10, column=0, sticky=tk.W, padx=10, pady=10)

    root.mainloop()
