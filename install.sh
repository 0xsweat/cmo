#!/bin/bash
Red='\033[0;30m'
if [[ $EUID -ne 0 ]]; then
   echo -e "${Red}must run as root" 
   exit 1
fi
pip install colorama
mkdir /cmo
cp cmo.py /cmo
echo "alias cmo='python /cmo/cmo.py'" >> ~/.bashrc
echo "alias cmo='python /cmo/cmo.py'" >> ~/.zshrc
Cyan='\033[1;36m'
echo -e "${Cyan}Cmo can now be started with just typing in 'cmo'"
