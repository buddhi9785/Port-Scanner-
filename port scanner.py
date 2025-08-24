import socket

# Target IP address or hostname
target = input("Enter target IP or hostname: ")

# Port range
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # 0.5 seconds timeout

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        s.close()
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        break
    except socket.error:
        print("❌ Couldn't connect to server.")
        break
