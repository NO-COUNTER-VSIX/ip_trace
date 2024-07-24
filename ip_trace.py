import os
import requests
from termcolor import colored
import re

def clear_screen():
    os.system('clear')

def display_banner():
    print(colored('''
        =====================================================================
       |   ____    _    _     _       __  __ _____  __     ______ ____   __  |
       |  / ___|  / \  | |   | |     |  \/  | ____| \ \   / / ___|_ _\ \/ /  |
       | | |     / _ \ | |   | |     | |\/| |  _|    \ \ / /\___ \| | \  /   |
       | | |___ / ___ \| |___| |___  | |  | | |___    \ V /  ___) | | /  \   |
       |  \____/_/   \_\_____|_____| |_|  |_|_____|    \_/  |____/___/_/\_\  |
       |                                                                     |
        ====================================================================
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                ||||||||||||||||||||||||||||||||||||||||||||||||||||
                          |||||||||||||||||||||||||||||||
                           +++++++++++++++++++++++++++++

    ''', 'red'))
    print('                      To get the IP of target ')
    print('                      Go to this link & Sign up')
    print('                      https://pipedream.com')
    print('''                      And Enter Project & 
                      enter new workflow & 
                      create project & 
                      add Trigger & 
                      copy the link & 
                      send to target  

    ''')

def get_target_ip():
    return input(colored('     Enter Target [IP] >>', 'green'))

def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

def get_ip_info(ip):
    api_key = '4e93f13af3f843f29af000304627df8a'
    url = f'https://api.ipgeolocation.io/ipgeo?ip={ip}&apiKey={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(colored(f'Error fetching IP information: {e}', 'red'))
        return

def print_ip_info(info):
    if not info:
        return
    
    fields = [
        'ip', 'continent_name', 'country_name', 'country_code2', 'state_prov', 'city', 'zipcode',
        'latitude', 'longitude', 'isp', 'organization', 'asn', 'currency', 'currency_name',
        'country_tld', 'calling_code', 'languages', 'country_flag', 'geoname_id', 'time_zone'
    ]
    
    print(colored('\nIP Information:', 'cyan'))
    for field in fields:
        if field in info:
            print(colored(f'{field.replace("_", " ").title()}: ', 'yellow') + f'{info[field]}')

def main():
    clear_screen()
    display_banner()
    
    target_ip = get_target_ip()
    if is_valid_ip(target_ip):
        ip_info = get_ip_info(target_ip)
        if ip_info:
            print_ip_info(ip_info)
    else:
        print(colored('Please enter a valid IP address.', 'red'))

if __name__ == '__main__':
    main()
