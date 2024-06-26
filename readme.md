# Desktop Microservice

This microservice contains the form, peripheral and simulation modules

## Installation Ubuntu

1. Clone this repository: https://github.com/Integracion-de-Sistemas-USB/desktop
2. Create a virtual environment: `python3 -m venv simulation`
3. Activate the virtual environment: `source simulation/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Rename ".env.example" to ".env"
5. Start the program: `python3 main.py`
6. Close the virtual environment: `deactivate`

## Run Tests in Ubuntu

1. Activate the virtual environment: `source simulation/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Move to the request folder: `cd request`
4. Run the tests: `python3 -m pytest test.py`
5. Check the results

## Installation Windows 11

1. Clone this repository: https://github.com/Integracion-de-Sistemas-USB/desktop
2. Create a virtual environment: `python.exe -m venv simulation`
3. Activate the virtual environment: `.\simulation\Scripts\activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`
5. Rename ".env.example" to ".env"
5. Start the program: `python.exe .\main.py`
6. Close the virtual environment: `deactivate`

## Run Tests in Windows 11

1. Activate the virtual environment: `.\simulation\Scripts\activate.ps1`
2. Install dependencies: `pip install -r requirements.txt`
3. Move to the request folder: `cd request`
4. Run the tests: `python.exe -m pytest test.py`
5. Check the results
