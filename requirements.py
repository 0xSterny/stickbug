import os

# Importing of Hoaxshell requirement
def hoaxshell():
    os.system("git clone https://github.com/t3l3machus/hoaxshell.git")
    os.system("pip3 install -r hoaxshell/requirements.txt")
    os.system("chmod +x hoaxshell/hoaxshell.py")

def netifaces():
    os.system("pip install netifaces")

if __name__ == "__main__":
    hoaxshell()
    netifaces()