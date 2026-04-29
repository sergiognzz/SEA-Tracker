# =====================================================
# Network Device Discovery Tool
# Created by Sergio González Sabucedo
# =====================================================

import subprocess
import re
import platform
import csv
import nmap
from termcolor import colored


# ==========================
# MAC ADDRESS
# ==========================
def get_mac(ip):
    system = platform.system()

    if system == "Windows":
        subprocess.call(["ping", "-n", "1", ip], stdout=subprocess.DEVNULL)
        command = ["arp", "-a", ip]
    else:
        subprocess.call(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL)
        command = ["arp", "-n", ip]

    try:
        output = subprocess.check_output(command, text=True)
    except subprocess.CalledProcessError:
        return "Not available"

    mac_regex = r"([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})"
    result = re.search(mac_regex, output)

    return result.group() if result else "Not found"



# ==========================
# TTL USING NMAP
# ==========================
def get_ttl_nmap(ip):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip, arguments="-sn -PE")
        if ip in nm.all_hosts():
            return nm[ip].get("ip", {}).get("ttl")
    except Exception:
        pass
    return None


def interpret_ttl(ttl):
    if ttl is None:
        return "Unknown"

    ttl = int(ttl)
    if ttl <= 64:
        return "Linux / Unix / Android"
    elif ttl <= 128:
        return "Windows"
    elif ttl <= 255:
        return "Router / Network device"
    return "Unknown"


# ==========================
# OPEN PORTS
# ==========================
def get_open_ports(ip):
    nm = nmap.PortScanner()
    results = []
    ports = ""

    try:
        nm.scan(ip, arguments="-sT --top-ports 20 --open")
        if ip in nm.all_hosts():
            for proto in nm[ip].all_protocols():
                for port in nm[ip][proto]:
                    service = nm[ip][proto][port].get("name", "unknown")
                    results.append((port, service))
            for x in  results:
                ports = ""+ports + ","+x

    except Exception as e:
        return [("Error", str(e))]

    return ports


# ==========================
# ROLE INFERENCE
# ==========================
def infer_role(ports):
    port_list = [p[0] for p in ports if isinstance(p[0], int)]

    if 80 in port_list or 443 in port_list:
        return "Web server / Web interface"
    if 22 in port_list:
        return "Linux server / SSH"
    if 3389 in port_list:
        return "Windows system (RDP)"
    if 445 in port_list:
        return "Windows / Samba"
    if 161 in port_list:
        return "Network device (SNMP)"

    return "Role not identified"


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    print(colored("========================================", "cyan"))
    print(colored(" Network Device Discovery Tool", "cyan", attrs=["bold"]))
    print(colored(" Created by Sergio González Sabucedo", "cyan"))
    print(colored("========================================\n", "cyan"))

    ip = input(colored("Enter the IP address: ", "yellow", attrs=["bold"]))

    mac = get_mac(ip)
    vendor = get_vendor(mac)
    ttl = get_ttl_nmap(ip)
    os_guess = interpret_ttl(ttl)
    ports = get_open_ports(ip)
    role = infer_role(ports)

    print(colored("\n===== RESULTS =====", "magenta", attrs=["bold"]))
    print(f"{colored('IP:', 'blue', attrs=['bold'])} {colored(ip, 'yellow')}")
    print(f"{colored('MAC:', 'blue', attrs=['bold'])} {colored(mac, 'green')}")
    print(f"{colored('Vendor:', 'blue', attrs=['bold'])} {colored(vendor, 'cyan')}")
    print(f"{colored('TTL:', 'blue', attrs=['bold'])} {colored(ttl, 'yellow')}")
    print(f"{colored('Probable OS:', 'blue', attrs=['bold'])} {colored(os_guess, 'red')}")

    print(colored("\nOpen ports:", "magenta", attrs=["bold"]))
    if ports:
        for port, service in ports:
            print(f"  - {colored(str(port), 'yellow')}/{colored(service, 'green')}")
    else:
        print(colored("  None detected", "red"))

    print(f"\n{colored('Probable device role:', 'magenta', attrs=['bold'])} {colored(role, 'cyan')}\n")

    print(colored("Tool designer and programming by Sergio González Sabucedo :)", "green", attrs=["bold"]))
