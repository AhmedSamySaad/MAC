# !/bin/bash
cd "${0%/*}"
conda activate mac
export FLASK_APP=app.py
python -m flask run