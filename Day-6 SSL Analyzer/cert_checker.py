import ssl
import socket
from datetime import datetime

domain = input("Enter Domain: ")

try:
    context = ssl.create_default_context()

    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            cert = ssock.getpeercert()

            issuer = dict(x[0] for x in cert['issuer'])
            subject = dict(x[0] for x in cert['subject'])

            valid_from = cert['notBefore']
            valid_until = cert['notAfter']

            expiry_date = datetime.strptime(
                valid_until,
                "%b %d %H:%M:%S %Y %Z"
            )

            days_remaining = (
                expiry_date - datetime.utcnow()
            ).days

            if days_remaining < 0:
                cert_status = "Expired"
            elif days_remaining <= 30:
                cert_status = "Expiring Soon"
            else:
                cert_status = "Valid"

            print("\nCertificate Information\n")

            print("Issuer:")
            print(issuer.get('organizationName', 'Unknown'))

            print("\nSubject:")
            print(subject.get('commonName', 'Unknown'))

            print("\nValid From:")
            print(valid_from)

            print("\nValid Until:")
            print(valid_until)

            print("\nDays Remaining:")
            print(days_remaining)

            print("\nCertificate Status:")
            print(cert_status)

            if days_remaining <= 30:
                print("\nWARNING: Certificate expires within 30 days.")

except Exception as e:
    print(f"Error: {e}")