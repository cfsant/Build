import sys, os, threading

def launcher(target, args):
    thread = threading.Thread(target=target, args=args)
    thread.start()

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize build on base path {path}...\n')
    
    launcher(os.system, (f'dotnet build {path}/Services',))
    launcher(os.system, (f'dotnet run --project {path}/Services/Services/Services.csproj',))

    os.chdir(f'{path}/Client')
    launcher(os.system, ('yarn build | yarn start',))

main()