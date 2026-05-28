import re

def check_password(password):
    # Your original strength checking logic
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
        feedback.append("[+] Minimum length verified")
    else:
        feedback.append("[-] Password too short")

    if re.search(r"[A-Z]", password):
        strength += 1
        feedback.append("[+] Uppercase letter detected")

    if re.search(r"[a-z]", password):
        strength += 1
        feedback.append("[+] Lowercase letter detected")

    if re.search(r"[0-9]", password):
        strength += 1
        feedback.append("[+] Number detected")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
        feedback.append("[+] Special character detected")

    # Determine strength label
    if strength == 5:
        label = "STRONG"
    elif strength >= 3:
        label = "MEDIUM"
    else:
        label = "WEAK"

    return feedback, label


# This is where the password takes the input from and if the password is all small caps it quits the progeram
while True:
    password = input("\nEnter Password (or type 'quit' to exit): ")
    if password.lower() == 'quit':
        break

    feedback, label = check_password(password)

    for line in feedback:
        print(line)

    print(f"Password Strength: {label}")
