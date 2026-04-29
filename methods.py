from termcolor import colored
import requests
import json
import time
import os
from phonenumbers import geocoder, carrier, timezone
import phonenumbers
import subprocess
import socket
from urllib.parse import urlparse

def IP_Track(ip):
    print(colored("=============", "blue") + colored("IP Tracker", "green") + colored("=============", "blue"))
    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = json.loads(req_api.text)

    time.sleep(2)

    print(colored("\n [+] IP target       :", "blue"), colored(ip, "green"))
    print(colored(" [+] Type IP         :", "blue"), colored(ip_data["type"], "green"))
    print(colored(" [+] Country         :", "blue"), colored(ip_data["country"], "green"))
    print(colored(" [+] Country Code    :", "blue"), colored(ip_data["country_code"], "green"))
    print(colored(" [+] City            :", "blue"), colored(ip_data["city"], "green"))
    print(colored(" [+] Continent       :", "blue"), colored(ip_data["continent"], "green"))
    print(colored(" [+] Continent Code  :", "blue"), colored(ip_data["continent_code"], "green"))
    print(colored(" [+] Region          :", "blue"), colored(ip_data["region"], "green"))
    print(colored(" [+] Region Code     :", "blue"), colored(ip_data["region_code"], "green"))
    print(colored(" [+] Latitude        :", "blue"), colored(ip_data["latitude"], "green"))
    print(colored(" [+] Longitude       :", "blue"), colored(ip_data["longitude"], "green"))

    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])

    print(colored(" [+] Maps            :", "blue"), colored(f"https://www.google.com/maps/@{lat},{lon},8z", "green"))
    print(colored(" [+] EU              :", "blue"), colored(ip_data["is_eu"], "green"))
    print(colored(" [+] Postal          :", "blue"), colored(ip_data["postal"], "green"))
    print(colored(" [+] Calling Code    :", "blue"), colored(ip_data["calling_code"], "green"))
    print(colored(" [+] Capital         :", "blue"), colored(ip_data["capital"], "green"))
    print(colored(" [+] Borders         :", "blue"), colored(ip_data["borders"], "green"))
    print(colored(" [+] Country Flag    :", "blue"), colored(ip_data["flag"]["emoji"], "green"))
    print(colored(" [+] ASN             :", "blue"), colored(ip_data["connection"]["asn"], "green"))
    print(colored(" [+] ORG             :", "blue"), colored(ip_data["connection"]["org"], "green"))
    print(colored(" [+] ISP             :", "blue"), colored(ip_data["connection"]["isp"], "green"))
    print(colored(" [+] Domain          :", "blue"), colored(ip_data["connection"]["domain"], "green"))
    print(colored(" [+] ID              :", "blue"), colored(ip_data["timezone"]["id"], "green"))
    print(colored(" [+] ABBR            :", "blue"), colored(ip_data["timezone"]["abbr"], "green"))
    print(colored(" [+] DST             :", "blue"), colored(ip_data["timezone"]["is_dst"], "green"))
    print(colored(" [+] Offset          :", "blue"), colored(ip_data["timezone"]["offset"], "green"))
    print(colored(" [+] UTC             :", "blue"), colored(ip_data["timezone"]["utc"], "green"))
    print(colored(" [+] Current Time    :", "blue"), colored(ip_data["timezone"]["current_time"], "green"))


def menu_options():
    print(colored("Welcome to the Sea Tracker by Sergio González Sabucedo!", "cyan"))
    print(colored("Please select an option:", "yellow"))
    print(colored("1. Ip tracker", "green"))
    print(colored("2. Phone tracker", "green"))
    print(colored("3. User tracker", "green"))
    print(colored("4. Show pc info", "green"))
    print(colored("5. Insert target manually", "green"))
    print(colored("6. Track IP by URL", "green"))
    print(colored("7. App settings","magenta"))
    print(colored("8. Exit", "red"))


def phone_tracker(telephone_number):
    default_region = "ID"
    parsed_number = phonenumbers.parse(telephone_number, default_region)
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
        parsed_number, default_region, with_formatting=True
    )
    number_type = phonenumbers.number_type(parsed_number)
    timezoneF = ', '.join(timezone.time_zones_for_number(parsed_number))

    print(colored("=============", "blue") + colored("Phone Tracker", "green") + colored("=============", "blue"))

    print(colored("\n Location             :", "blue"), colored(location, "green"))
    print(colored(" Region Code          :", "blue"), colored(region_code, "green"))
    print(colored(" Timezone             :", "blue"), colored(timezoneF, "green"))
    print(colored(" Operator             :", "blue"), colored(jenis_provider, "green"))
    print(colored(" Valid number         :", "blue"), colored(is_valid_number, "green"))
    print(colored(" Possible number      :", "blue"), colored(is_possible_number, "green"))
    print(colored(" International format :", "blue"), colored(formatted_number, "green"))
    print(colored(" Mobile format        :", "blue"), colored(formatted_number_for_mobile, "green"))
    print(colored(" Original number      :", "blue"), colored(parsed_number.national_number, "green"))
    print(
        colored(" E.164 format         :", "blue"),
        colored(phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164), "green")
    )
    print(colored(" Country code         :", "blue"), colored(parsed_number.country_code, "green"))
    print(colored(" Local number         :", "blue"), colored(parsed_number.national_number, "green"))

    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(colored(" Type                 :", "blue"), colored("This is a mobile number", "green"))
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(colored(" Type                 :", "blue"), colored("This is a fixed-line number", "green"))
    else:
        print(colored(" Type                 :", "blue"), colored("This is another type of number", "green"))

def user_tracker(username):
    try:
        results = {}

        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "YouTube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://t.me/{}", "name": "Telegram"},
            {"url": "https://weheartit.com/{}", "name": "We Heart It"},
            {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
            {"url": "https://www.roblox.com/user.aspx?username={}", "name": "Roblox"},
            {"url": "https://open.spotify.com/user/{}", "name": "Spotify"},
            {"url": "https://www.deviantart.com/{}", "name": "DeviantArt"},
            {"url": "https://www.vk.com/{}", "name": "VK"},
            {"url": "https://www.xing.com/profile/{}", "name": "Xing"},
            {"url": "https://www.kaggle.com/{}", "name": "Kaggle"},
            {"url": "https://www.codecademy.com/profiles/{}", "name": "Codecademy"},
            {"url": "https://www.hackerone.com/{}", "name": "HackerOne"},
            {"url": "https://tryhackme.com/p/{}", "name": "TryHackMe"},
            {"url": "https://keybase.io/{}", "name": "Keybase"},
            {"url": "https://about.me/{}", "name": "About.me"},
            {"url": "https://angel.co/u/{}", "name": "AngelList"},
            {"url": "https://www.last.fm/user/{}", "name": "Last.fm"},
            {"url": "https://www.mixcloud.com/{}", "name": "Mixcloud"},
        ]

        for site in social_media:
            url = site['url'].format(username)
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    results[site['name']] = colored(url, "green")
                else:
                    results[site['name']] = colored("Not Found", "red")
            except:
                results[site['name']] = colored("Error", "yellow")

    except Exception as e:
        print(colored(f"Error: {e}", "red"))
        return

    print(colored("\n========== USER TRACKER ==========\n", "cyan", attrs=["bold"]))

    for site, url in results.items():
        print(f"{colored('[+]', 'blue')} {colored(site, 'white')}: {url}")


def personal_information():
    try:
        locate_info()
    except Exception as e:
        print(colored(f"Error: {e}", "red"))

def locate_info():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "seaTrackerInfo.sh")
    os.system(f"bash {script_path}")

def locate_installer():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir,"install.sh")
    os.system(f"chmod +x {script_path}")
    os.system(f"bash {script_path}")

def locate_unistaller():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir,"unistaller.sh")
    os.system(f"chmod +x {script_path}")
    os.system(f"bash {script_path}")
    
def locate_welcomer():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "animationStart.sh")
    os.system(f"bash {script_path}")

def HelpPanelInsert():
    print(colored("Help panel to insert targets", "cyan"))
    print("")
    print(colored("Example: 8.8.8.8 (IP Tracker)","yellow"))
    print(colored("Example: +34123456789 (Phone Tracker)","yellow"))
    print(colored("Example: seergiognzz (User Tracker)","yellow"))
    print(colored("Example: https://www.google.com (Track IP by URL)","yellow"))
    print("")

def get_ip_from_url(url):
    try:
        dominio = urlparse(url).hostname
        ip = socket.gethostbyname(dominio)
        print(colored(f"IP address for ", "blue") + colored(url, "cyan") + colored(" -> ", "blue") + colored(ip, "yellow"))
    except:
        print(colored(f"Could not resolve IP address for {url}", "red"))


def update_repo(path):
    result = subprocess.run(
        ["git", "-C", path, "pull"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        raise Exception(result.stderr)
    
    return result.stdout


def main(target, control):
    
    menu_options()
    while True:
        try:
            opcion = input("Enter your option: ")
        except KeyboardInterrupt:
            print(colored("\n[*] Program interrupted by user.", "yellow"))
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

        try:
            opcionInt = int(opcion)
            match opcionInt:
                case 1:
                    try:
                        if control:
                            os.system("clear")
                            IP_Track(target)
                            print("")
                            menu_options()
                        else:
                            print(colored("[!] No target provided. Please provide a target as a command-line argument.", "red"))
                    except:
                        print(colored("[!] An error occurred while tracking the IP.","red"))
                case 2:
                    try:
                        if control:
                            os.system("clear")
                            phone_tracker(target)
                            print("")
                            menu_options()
                        else:
                            print(colored("[!] No target provided. Please provide a target as a command-line argument.", "red"))
                    except:
                        print(colored("[!] An error occurred while tracking the phone number.","red"))
                case 3:
                    try:
                        if control:
                            os.system("clear")
                            print(colored("[*] Searching user...","cyan"))
                            user_tracker(target)
                            print("")
                            menu_options()
                        else:
                            print(colored("[!] No target provided. Please provide a target as a command-line argument.", "red"))
                    except:
                        print(colored("[!] An error occurred while tracking the user.","red"))
                case 4:
                    try:
                        personal_information()
                        print("")
                        menu_options()
                    except:
                        print(colored("[!] An error occurred while retrieving personal information.","red"))
                case 5:
                    try:
                        os.system("clear")
                        HelpPanelInsert()
                        new_target = input(colored("[+] Enter the new target: ", "yellow")).strip()
                        if len(new_target) <= 2:
                            print(colored("[!] Invalid target. Please provide a valid target.", "red"))
                        else:
                            target = new_target
                            control = True
                            print(colored("[+] Target updated successfully!", "green"))
                    except:
                        print(colored("[!] An error occurred while updating the target.","red"))
                
                case 6:
                    try:
                        if control:
                            os.system("clear")
                            print(colored("[*] Tracking the target...","cyan"))
                            print("")
                            time.sleep(2)
                            get_ip_from_url(target)
                            print("")
                            menu_options()
                        else:
                            print(colored("[!] No target provided. Please provide a target as a command-line argument.", "red"))
                    except:
                        print(colored("[!] An error has occurred while the program is tracking ip of the target url.","red"))
                case 7:
                    os.system("clear")
                    print(colored("-----------------App settings ---------------------","cyan"))
                    print(colored("                 1. Install App                    ","yellow"))
                    print(colored("                 2. Unistall App [!]                   ","red"))
                    print(colored("                 3. Update App                     ","yellow"))
                    print(colored("                 4. Exit Settings                  ","red"))
                    print(colored("---------------------------------------------------","cyan"))
                    while True:
                        opcion = input("Insert the option: ").strip()
                        try:
                            opcionInt = int(opcion)
                            if opcionInt == 1:
                               try:
                                ruta = os.path.expanduser("~/.config/SEA-tracker")
                                if os.path.isdir(ruta):
                                   print(colored("[!] The App is installed","blue"))
                                else:
                                    print(colored("[*] Installing app...","cyan"))
                                    locate_installer()
                               except:
                                   print(colored("[!] An error has occurred while the app was installing","red"))
                            elif opcionInt == 2:
                                try:
                                    ruta = os.path.expanduser("~/.config/SEA-tracker")
                                    if os.path.isdir(ruta):
                                        print(colored("[*] Unistalling app...","cyan"))
                                        locate_unistaller()
                                    else:
                                        print(colored("[!] The App is not installed","red"))
                                except:
                                    print(colored("[!] An error has occurred while the app was unistalling","red"))
                            elif opcionInt == 3:
                                try:
                                    print(colored("[*] Updating app...","cyan"))
                                    base_dir = os.path.dirname(os.path.abspath(__file__))
                                    update_repo(base_dir)
                                except:
                                    print(colored("[!] An error has occurred while the app was updating","red"))
                            elif opcionInt == 4:
                                print(colored("[!] Exiting of Settings...","green"))
                                time.sleep(2)
                                os.system("clear")
                                menu_options()
                                break
                            else:
                                print(colored("[!] Select a valid option","red"))
                        except:
                            print(colored("[!] Insert a valid option -> ex: 1","red"))

                case 8:
                    print(colored("[!] Thank you for using the Sea Tracker by Sergio González Sabucedo!","cyan"))
                    break
                case default:
                    print(colored("[!] Invalid option. Please enter a number between 1 and 6.", "red"))
        except:
            print("Invalid option. Please enter a number.")