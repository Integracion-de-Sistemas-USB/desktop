import tkinter as tk
from tkinter import ttk

def create_button_frame(parent_frame, name_entries, option, percentage_var):
    frame = ttk.Frame(parent_frame, padding="10")

    def submit_form():
        for name_label, name_entry in name_entries:
            name = name_entry.get()
            print(f"{name_label}", name)

        selected_option = option.get()
        selected_percentage = percentage_var.get()
        print("Selected Option:", selected_option)
        print("Selected Percentage:", selected_percentage)

        parent_frame.destroy()

    submit_button = ttk.Button(frame, text="OK", command=submit_form)
    submit_button.grid(row=0, column=0, columnspan=2, pady=5)

    return frame
