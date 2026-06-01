import socket

target = input("Enter target IP: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\n[+] Scanning {target}\n")

for port in range(start_port, end_port + 1):

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