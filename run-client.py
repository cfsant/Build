import sys, os, threading, subprocess

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize CLIENT on base path {path}...\n')
    
    os.chdir(f'{path}/Client')
    os.system('yarn install')
    os.system('yarn build')
    os.system('yarn start')

main()