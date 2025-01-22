import argparse
import os
import sys
import subprocess
import platform
import shutil

parser = argparse.ArgumentParser(description="Echoroot Virtual Machine Software")

parser.add_argument('-i', '--init', type=str, help='Set Up Echoroot')
parser.add_argument('-n', '--new', type=str, help='Create a New Echroot')
parser.add_argument('-o', '--open', type=str, help='Open an Echroot')
parser.add_argument('-r', '--remove', type=str, help='Delete an Echroot')

args = parser.parse_args()

if args.init:
    entry = args.init
    os.chdir(os.path.expanduser('~'))
    try:
        os.chdir('echoroot')
        print('Echoroot Is Already Set Up')
    except FileNotFoundError:
        os.mkdir('echoroot')

if args.new:
    entry = args.new
    os.chdir(os.path.expanduser('~'))
    try:
        os.chdir('echoroot')
        try:
            os.chdir(entry)
            print('Echoroot Already Exists')
            sys.exit()
        except FileNotFoundError:
            try:
                os.mkdir(entry)
            except FileExistsError:
                print('Echoroot Already Exists')
    except FileNotFoundError:
        print('Echoroot Is Not Set Up')
    os.chdir(entry)
    os.mkdir('Documents')
    os.mkdir('Applications')
    os.mkdir('Downloads')
    os.mkdir('Pictures')
    os.mkdir('Desktop')

if args.open:

    if platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

    name = args.open

    os.chdir(os.path.expanduser('~'))
    try:
        os.chdir('echoroot')
    except FileNotFoundError:
        print('Echoroot Is Not Set Up')
        sys.exit()
    try:
        os.chdir(name)
    except FileNotFoundError:
        print('Echoroot Does Not Exist')
        sys.exit()

    while True:

        command = input(f'{name}@Echoroot ~ % ')

        if command == 'exit':
            sys.exit()

        elif command == 'pwd':
            pwdpath = os.path.expanduser(os.getcwd())
            printpath = os.path.basename(pwdpath)
            print(f'/Echoroots/{printpath}')

        elif command == 'whoami':
            print(name)

        else:
            os.system(command)

if args.remove:
    name = args.remove
    os.chdir(os.path.expanduser('~'))
    try:
        os.chdir('echoroot')
    except FileNotFoundError:
        print('Echoroot Is Not Set Up')
        sys.exit()
    try:
        shutil.rmtree(name)
    except FileNotFoundError:
        print('Echoroot Does Not Exist')
        sys.exit()
