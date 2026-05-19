# Simple TCP Port Scanner

A basic, easy-to-understand TCP port scanner written in Python.  
Designed for learning network programming, purple teaming, and security fundamentals.

## Overview

This script asks the user for a target IP/domain and a port range, then attempts a TCP connection to each port. If a port responds, it is marked as `OPEN`. The scan uses a 0.5‑second timeout, making it fast enough for internal networks while remaining simple to study and modify.

**Use cases:**
- Learning Python’s `socket` module
- Understanding the TCP three-way handshake
- Reconnaissance during authorized penetration testing or purple team exercises
- Baseline network audits

## Features

- Plain Python – no external libraries required.
- User‑friendly interactive prompts.
- Lightweight and easy to extend (banner grabbing, threading, Nmap comparison, etc.).

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository or download the `scanner.py` file.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows

3. No extra dependencies needed.

Usage
Run the script from the terminal:

bash
python scanner.py
Follow the prompts:

text
Enter Target IP/Domain: scanme.nmap.org
Enter Start Port: 20
Enter End Port: 100
Example output:

text
Scanning Target: scanme.nmap.org
----------------------------------------
[+] Port 22 is OPEN
[+] Port 80 is OPEN

Scan Completed.   
