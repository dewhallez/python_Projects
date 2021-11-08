import os

# define the ping function
def pingComputer():
    # Get hostname Ip address
    hostname = input("Enter the ip address: ")
    # ping host for response
    response = os.system("Ping -c 2 " + hostname)

    if response == 0:
        print(f'{hostname} is up')
    else:
        print(f'{hostname} is down')

if __name__ == "__main__":
    pingComputer()
