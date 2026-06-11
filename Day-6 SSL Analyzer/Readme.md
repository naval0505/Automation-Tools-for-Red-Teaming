# SSL Certificate Checker

A simple Python script that retrieves and displays SSL/TLS certificate information for a given domain.

## Features

* Retrieves SSL/TLS certificate details from a website
* Displays certificate issuer information
* Displays certificate subject/common name
* Shows certificate validity period
* Calculates remaining days before certificate expiration
* Indicates certificate status:

  * Valid
  * Expiring Soon
  * Expired
* Provides expiry warnings for certificates nearing expiration

## Requirements

* Python 3.x
* Internet connection

## Usage

```bash
python3 cert_checker.py
```

Enter a domain name when prompted:

```text
Enter Domain: google.com
```

## Example Output

```text
Certificate Information

Issuer:
Google Trust Services

Subject:
google.com

Valid From:
Jun 16 08:33:42 2026 GMT

Valid Until:
Sep 08 08:33:41 2026 GMT

Days Remaining:
84

Certificate Status:
Valid
```

## Learning Objectives

This project demonstrates:

* Python networking with `socket`
* SSL/TLS certificate handling using `ssl`
* Date and time calculations
* Exception handling
* Dictionary manipulation
* Basic cybersecurity automation

```
Developed as part of a cybersecurity internship learning exercise.
```
