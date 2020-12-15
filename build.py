import sys, os, threading, subprocess

def launcher(target, args):
    thread = threading.Thread(target=target, args=args)
    thread.start()

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize build on base path {path}...\n')
    
    os.chdir(f'{path}/Client')
    os.system('yarn install')
    os.system('yarn build')
    os.system('yarn start')

    os.chdir(f'{path}/Services')
    launcher(os.system, (f'dotnet build',))

    os.chdir(f'{path}/Services/Services')
    launcher(os.system, (f'dotnet run --project Services.csproj',))

main()