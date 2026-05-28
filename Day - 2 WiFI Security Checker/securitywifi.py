import subprocess

print("=" * 50)
print("      Wi-Fi Security Checker")
print("=" * 50)

try:
    ssid = subprocess.check_output(
        "iwgetid -r", shell=True
    ).decode().strip()

    signal = subprocess.check_output(
        "iwconfig 2>/dev/null | grep 'Signal level'",
        shell=True
    ).decode()

    encryption = subprocess.check_output(
        "nmcli -t -f active,ssid,security dev wifi | egrep '^yes'",
        shell=True
    ).decode()

    print(f"\nConnected Wi-Fi : {ssid}")

    print("\nEncryption Details:")
    print(encryption)

    print("\nSignal Information:")
    print(signal)

    print("\nSecurity Status:")

    if "WPA2" in encryption:
        print("[+] WPA2 detected")
    elif "WPA3" in encryption:
        print("[+] WPA3 detected")
    else:
        print("[!] Weak or Unknown Encryption")

except Exception as e:
    print(f"Error: {e}")
