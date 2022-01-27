# !/bin/bash
conda activate
conda config --append channels conda-forge
cd "${0%/*}"
conda env create -f environment.yml
echo Installed the environment successfully!
read -rsp $'Press any key to continue...\n' -n1 key