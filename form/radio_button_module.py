import json
import tkinter as tk
from tkinter import ttk

from form.text_constants import SCENERY

def create_radio_button_frame(parent_frame):
    frame = ttk.Frame(parent_frame, padding="10")

    option = tk.StringVar(value="Option1")

    with open('config.json', 'r') as json_file:
        config_data = json.load(json_file)

    scenery = config_data[SCENERY]

    options = [(scene, scene) for scene in scenery]

    for i, (text, value) in enumerate(options, start=1):
        radio_button = ttk.Radiobutton(frame, text=text, value=value, variable=option)
        radio_button.grid(row=i, column=0, columnspan=2, sticky=tk.W, padx=5)

    return frame, option
