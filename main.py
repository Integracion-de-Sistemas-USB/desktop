# main.py
from simulator.simulator import simulator
from form.form_module import build_form

data = {}

def handle_form_data(form_data):
    global data
    data = form_data

if __name__ == "__main__":
    build_form(callback=handle_form_data)
    simulator(data)
