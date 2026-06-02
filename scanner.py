import socket
import time
import json
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

init()

targets = input("Enter target IPs separated by commas: ").split(",")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

results = []

start_time = time.time()

print(Fore.CYAN + "\n[+] Starting network scan...\n")


def grab_banner(ip, port):

    try:
        s = socket.socket()
        s.settimeout(2)

        s.connect((ip, port))

        banner = s.recv(1024).decode().strip()

        return banner

    except:
        return "No banner"


def scan_port(target, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        banner = grab_banner(target, port)

        print(Fore.GREEN + f"[OPEN] {target}:{port} -> {service}")
        print(Fore.YELLOW + f"Banner: {banner}\n")

        results.append({
            "target": target,
            "port": port,
            "service": service,
            "banner": banner
        })

    s.close()


for target in targets:

    target = target.strip()

    print(Fore.CYAN + f"\n[+] Scanning target: {target}\n")

    with ThreadPoolExecutor(max_workers=50) as executor:

        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)


with open("scan_results.json", "w") as file:
    json.dump(results, file, indent=4)

end_time = time.time()

print(Fore.CYAN + f"\nScan completed in {round(end_time - start_time, 2)} seconds.")