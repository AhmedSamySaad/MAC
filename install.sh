# !/bin/bash
pip install virtualenv
cd "${0%/*}"
virtualenv MAC_venv
source MAC_venv/bin/activate
pip install -r requirements.txt
echo Installed the environment successfully!
read -rsp $'Press any key to continue...\n' -n1 key