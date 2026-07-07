import subprocess
import socket
import time
from concurrent.futures import ThreadPoolExecutor

results = []


def scan_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown"

            print(f"[+] {ip} ({hostname})")

            results.append((ip, hostname))

    except Exception:
        pass


def main():
    network = input("Enter Network Prefix (e.g. 192.168.1): ").strip()

    print("\n[*] Scanning Network...\n")

    start = time.time()

    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(1, 255):
            ip = f"{network}.{i}"
            executor.submit(scan_host, ip)

    end = time.time()

    with open("scan_results.txt", "w") as file:
        file.write("Network Scan Results\n")
        file.write("=" * 40 + "\n\n")

        for ip, hostname in results:
            file.write(f"IP Address : {ip}\n")
            file.write(f"Hostname   : {hostname}\n")
            file.write("-" * 30 + "\n")

    print("\n" + "=" * 40)
    print("Scan Complete")
    print("=" * 40)
    print(f"Devices Found : {len(results)}")
    print(f"Time Taken    : {end - start:.2f} seconds")
    print("Results Saved : scan_results.txt")


if __name__ == "__main__":
    main()
