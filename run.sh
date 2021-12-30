pip install virtualenv
cd "${0%/*}"
virtualenv MAC_venv
source MAC_venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
python -m flask run