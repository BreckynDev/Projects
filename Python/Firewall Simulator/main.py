import random

def introduction():
    
    amount = 30

    for i in range(amount):
        print("-", end="")
    print()
    print("Welcome to Firewall Simulator")
    for i in range(amount):
        print("-", end="")
    print()

def ip_generator():
    random_num = random.randint(1, 15)
    network_ID = "192.169.10."
    ip_address = network_ID + str(random_num)
    return ip_address

def ip_banning():
    banned_ips = [
        "192.169.10.0", "192.169.10.1", 
        "192.169.10.3", "192.169.10.5", 
        "192.169.10.6", "192.169.10.8",]
    return banned_ips

def main():

    introduction()

    running = True
    while running == True:

        trafic_amount = input("Enter amount of users on network: ")
        trafic_amount = int(trafic_amount)

        ip_list = []

        for i in range(trafic_amount):
            ip_address = ip_generator()
            print("User", (i + 1),":",ip_address)
            ip_list.append(ip_address)

        banned_ips = ip_banning()
        
        rejected = []
        rejected_users = []

        for i in range(len(ip_list)):
            ip = ip_list[i]

            for x in range(len(banned_ips)):
                if ip == banned_ips[x]:
                    rejected.append(ip)
                    rejected_users.append(i + 1)

        print("\nThe following users have IP addresses")
        print("that are banned and thus rejected: \n")

        for i in range(len(rejected_users)):
            print("User ", rejected_users[i], end = "")
            print()
        print()

        user_input = input("Would you like to run the simulator again (y/n): ")
        if user_input == "y" or user_input == "Y":
            running = True
        else:
            print("Quitting Program")
            running = False

if __name__ == '__main__':
    main()