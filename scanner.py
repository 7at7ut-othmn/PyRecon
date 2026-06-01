import socket

target = input("Enter target IP: ")

ports = [21, 22, 80, 443, 3306]

print(f"\n[+] Scanning {target}\n")

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"[OPEN] Port {port} -> {service}")

    s.close()

print("\nScan completed.")