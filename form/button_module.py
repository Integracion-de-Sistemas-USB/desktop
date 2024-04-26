import tkinter as tk
from tkinter import ttk
from .text_constants import SELECTED_OPTION, SELECTED_PERCENTAGE, NAME, CODE

def create_button_frame(parent_frame, name_entries, option, percentage_var, user_entry, code_entry, weapon_type, callback):
    frame = ttk.Frame(parent_frame, padding="10")

    def submit_form():
        form_data = {}
        for name_label, name_entry in name_entries:
            name = name_entry.get()
            form_data[name_label[:-1]] = name

        form_data[SELECTED_OPTION] = option.get()
        form_data[SELECTED_PERCENTAGE] = percentage_var.get()
        form_data[NAME] = user_entry.get()
        form_data[CODE] = code_entry.get()
        form_data["Selected Type"] = weapon_type.get()
        parent_frame.destroy()

        callback(form_data)
        return form_data

    submit_button = ttk.Button(frame, text="OK", command=submit_form)
    submit_button.grid(row=0, column=0, columnspan=2, pady=5)

    return frame
