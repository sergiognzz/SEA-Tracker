#! /usr/bin/env python3
import os
import methods as m
from termcolor import colored
import sys
from pathlib import Path

def parameters():
    try:
        target = sys.argv[1]
    except:
        return 0

    if len(sys.argv) == 0:
        return 0
    elif len(target)<=2:
        return None
    else:
        return target



def helpPanel():
    print(colored("HELP PANEL - Sea Tracker", "cyan"))
    print("")
    print(colored("If you dont have a tool instelled in the system","yellow"))
    print(colored("Usage: python3 sea_tracker.py <target>", "green"))
    print(colored("Example:","yellow")+colored(" python3 sea_tracker.py 8.8.8.8 (ip tracker)", "cyan"))
    print(colored("Example:","yellow")+colored(" python3 sea_tracker.py +34123456789 (phone tracker)", "cyan"))
    print(colored("Example:","yellow")+colored(" python3 sea_tracker.py seergiognzz (user tracker)", "cyan"))
    print("")
    print("")
    print(colored("If you have a tool instelled in the system","yellow"))
    print(colored("Usage: sea-tracker <target>", "green"))
    print(colored("Example:","yellow")+colored(" sea_tracker 8.8.8.8 (ip tracker)", "cyan"))
    print(colored("Example:","yellow")+colored(" sea_tracker +34123456789 (phone tracker)", "cyan"))
    print(colored("Example:","yellow")+colored(" sea_tracker seergiognzz (user tracker)", "cyan"))
    print("")


if __name__ == "__main__":
        targetTracked = parameters()
        if targetTracked == 0:
            m.locate_welcomer()
            m.main(targetTracked,False)
        elif targetTracked is None:
            print(colored("[!] No valid target provided. Please provide a target as a command-line argument.", "red"))
            print("")
            helpPanel()
            sys.exit(1)
        else:  
            m.locate_welcomer()
            print("")
            m.main(targetTracked,True)
    