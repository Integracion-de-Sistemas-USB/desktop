import json
import tkinter as tk
from tkinter import ttk

from form.text_constants import STRESS

def create_drop_menu_frame(parent_frame, options, title, default):
    frame = ttk.Frame(parent_frame, padding="10")

    percentage_label = ttk.Label(frame, text=title)
    percentage_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    percentage_var = tk.StringVar(value=default)

    percentage_combobox = ttk.Combobox(frame, state="readonly", values=options, textvariable=percentage_var)
    percentage_combobox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    return frame, percentage_var
