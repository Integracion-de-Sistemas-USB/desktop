import asyncio
from tkinter import Tk, Label, Frame
from simulator.simulator import simulator
from form.form_module import build_form

data = {}

def handle_form_data(form_data):
    global data
    data = form_data

def show_results(scores):
    win = Tk()
    win.title("Results")

    label_title = Label(win, text="Your Results:\n")
    label_title.pack()

    for i in range(len(scores)):
        label = Label(win, text=f"Shoot {i + 1}:\t{scores[i]}")
        label.pack()

    win_width = 240
    win_height = 60 + len(scores) * 20
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - win_width) // 2
    y = (screen_height - win_height) // 2
    win.geometry(f"{win_width}x{win_height}+{x}+{y}")

    win.mainloop()

async def main():
    build_form(callback=handle_form_data)
    scores = await simulator(data)
    print(scores)
    show_results(scores)

if __name__ == "__main__":
    asyncio.run(main())
