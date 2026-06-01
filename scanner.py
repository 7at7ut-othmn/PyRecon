import socket
import time

target = input("Enter target IP: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

start_time = time.time()

print(f"\n[+] Scanning {target}\n")


def grab_banner(ip, port):

    try:
        s = socket.socket()
        s.settimeout(2)

        s.connect((ip, port))

        banner = s.recv(1024).decode().strip()

        return banner

    except:
        return "No banner"


for port in range(start_port, end_port + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        banner = grab_banner(target, port)

        print(f"[OPEN] Port {port} -> {service}")
        print(f"Banner: {banner}\n")

    s.close()

end_time = time.time()

print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")