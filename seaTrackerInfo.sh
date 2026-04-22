#!/bin/bash
# ---- COLORES ----
GREEN="\e[32m"
CYAN="\e[36m"
WHITE="\e[97m"
clear
# Info del sistema
USER_NAME=$(whoami)
HOST=$(hostname)
KERNEL=$(uname -r)
UPTIME=$(uptime -p | sed 's/up //')
DISTRO=$(grep '^PRETTY_NAME' /etc/os-release | cut -d= -f2 | tr -d '"')
IP=$(/usr/bin/ip a | grep ens33 | tail -n 1 | awk '{print $2}' | sed 's/\/24//')
Public_IP=$(curl -s https://api.ipify.org | head -n 1)

echo -e "--------------------------------"
echo -e "         SYSTEM INFO            "
echo -e "--------------------------------"
echo -e "${GREEN}User      ${WHITE}: ${CYAN}$USER_NAME"
echo -e "${GREEN}Host      ${WHITE}: ${CYAN}$HOST"
echo -e "${GREEN}OS        ${WHITE}: ${CYAN}$DISTRO"
echo -e "${GREEN}Kernel    ${WHITE}: ${CYAN}$KERNEL"
echo -e "${GREEN}Uptime    ${WHITE}: ${CYAN}$UPTIME"
echo -e "${GREEN}IP        ${WHITE}: ${CYAN}$IP"
echo -e "${GREEN}Public IP ${WHITE}: ${CYAN}$Public_IP"


