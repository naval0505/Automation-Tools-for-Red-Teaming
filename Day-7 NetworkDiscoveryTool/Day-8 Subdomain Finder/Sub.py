import socket
import time
from concurrent.futures import ThreadPoolExecutor

subdomains = [
    "www",
    "mail",
    "api",
    "blog",
    "dev",
    "test",
    "admin",
    "portal"
]

results = []


def scan_subdomain(sub, domain):
    target = f"{sub}.{domain}"

    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Found: {target:<30} -> {ip}")
        results.append((target, ip))
    except socket.gaierror:
        pass


def main():
    domain = input("Enter Domain (example.com): ").strip()

    print("\n[*] Scanning Subdomains...\n")

    start = time.time()

    with ThreadPoolExecutor(max_workers=20) as executor:
        for sub in subdomains:
            executor.submit(scan_subdomain, sub, domain)

    end = time.time()

    with open("subdomain_results.txt", "w") as file:
        file.write("Subdomain Enumeration Results\n")
        file.write("=" * 45 + "\n\n")

        if results:
            for host, ip in results:
                file.write(f"{host:<35} {ip}\n")
        else:
            file.write("No subdomains found.\n")

    print("\n" + "=" * 45)
    print("Scan Complete")
    print("=" * 45)
    print(f"Subdomains Found : {len(results)}")
    print(f"Time Taken       : {end - start:.2f} seconds")
    print("Results Saved    : subdomain_results.txt")


if __name__ == "__main__":
    main()
