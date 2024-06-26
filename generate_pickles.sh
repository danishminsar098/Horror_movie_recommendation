#!/bin/bash
python -m nbconvert --to script Model.ipynb
python Model.py
