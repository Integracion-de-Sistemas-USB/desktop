import tkinter as tk
from tkinter import ttk
from .entry_module import create_name_entry_frame
from .radio_button_module import create_radio_button_frame
from .drop_menu_module import create_drop_menu_frame
from .button_module import create_button_frame
import json
from .text_constants import (
    BOLD, 
    ENVIRONMENT, 
    ENVIRONMENT_LABEL, 
    FORM_TITLE, 
    HELVETICA, 
    PHYSICS, 
    PHYSICS_LABEL, 
    SCENARY_LABEL, 
    STRESS_LABEL, 
    STYLE
)

def build_form(callback):
    root = tk.Tk()
    root.title(FORM_TITLE)

    style = ttk.Style()
    style.theme_use(STYLE)

    def create_title_label(parent, text, row, column=0):
        label = tk.Label(parent, text=text, font=(HELVETICA, 12, BOLD))
        label.grid(row=row, column=column, columnspan=2, pady=(10, 5), sticky=tk.W)
        return label

    create_title_label(root, PHYSICS_LABEL, row=0)

    with open('config.json', 'r') as json_file:
        config_data = json.load(json_file)

    physics = config_data[PHYSICS]
    name_entries_physics = []
    for i, entry in enumerate(physics, start=1):
        name_entry_label = f"{entry}:"
        name_entry_frame, name_entry = create_name_entry_frame(root, label_text=name_entry_label)
        name_entry_frame.grid(row=i, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        name_entries_physics.append((name_entry_label, name_entry))

    create_title_label(root, ENVIRONMENT_LABEL, row=len(physics) + 1)

    environment = config_data[ENVIRONMENT]
    name_entries_environment = []
    for i, entry in enumerate(environment, start=len(physics) + 2):
        name_entry_label = f"{entry}:"
        name_entry_frame, name_entry = create_name_entry_frame(root, label_text=name_entry_label)
        name_entry_frame.grid(row=i, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        name_entries_environment.append((name_entry_label, name_entry))

    create_title_label(root, SCENARY_LABEL, row=0, column=1)
    radio_button_frame, option = create_radio_button_frame(root)
    radio_button_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), rowspan=len(physics))

    create_title_label(root, STRESS_LABEL, row=len(physics) + 1, column=1)
    drop_menu_frame, percentage_var = create_drop_menu_frame(root)
    drop_menu_frame.grid(row=len(physics) + 2, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), rowspan=len(environment))

    button_frame = create_button_frame(root, name_entries_physics + name_entries_environment, option, percentage_var, callback)
    button_frame.grid(row=len(physics) + len(environment) + 2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.mainloop()
