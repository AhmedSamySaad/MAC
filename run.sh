# !/bin/bash
cd "${0%/*}"
source MAC_venv/bin/activate
export FLASK_APP=app.py
python -m flask run