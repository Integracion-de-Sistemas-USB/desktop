import tkinter as tk
from tkinter import ttk
import threading

form_built_flag = threading.Event()

def create_button_frame(parent_frame, name_entries, option, percentage_var, callback):
    frame = ttk.Frame(parent_frame, padding="10")

    def submit_form():
        form_data = {}
        for name_label, name_entry in name_entries:
            name = name_entry.get()
            form_data[name_label[:-1]] = name

        form_data["Selected Option"] = option.get()
        form_data["Selected Percentage"] = percentage_var.get()

        form_built_flag.set()
        parent_frame.destroy()

        callback(form_data)
        return form_data

    submit_button = ttk.Button(frame, text="OK", command=submit_form)
    submit_button.grid(row=0, column=0, columnspan=2, pady=5)

    return frame
