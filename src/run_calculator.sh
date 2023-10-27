#!/bin/bash

pip install colorama 
python3 -m venv .venv
source .venv/bin/activate
python3 calorie_calculator.py
