import json
import tkinter as tk
from tkinter import ttk

from form.text_constants import STRESS

def create_drop_menu_frame(parent_frame):
    frame = ttk.Frame(parent_frame, padding="10")

    with open('config.json', 'r') as json_file:
        config_data = json.load(json_file)

    stress_options = config_data[STRESS]

    percentage_label = ttk.Label(frame, text="Percentage:")
    percentage_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    percentage_var = tk.StringVar(value="0%")

    percentage_combobox = ttk.Combobox(frame, values=stress_options, textvariable=percentage_var)
    percentage_combobox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    return frame, percentage_var
