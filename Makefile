ifeq ($(OS), Windows_NT)
py_assoc = python
venv_exec = .\venv\Scripts\activate
pip_assoc = pip
else
py_assoc = python3
venv_exec = source ./venv/bin/activate
pip_assoc = pip3
endif

all: setup run
run:
	$(py_assoc) main.py
setup:
	$(py_assoc) -m venv ./venv
	$(venv_exec)
	$(pip_assoc) install -r requirements.txt


.PHONY: all
