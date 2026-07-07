# 🌐 Python Subdomain Scanner (Beginner Friendly)

> A simple Python script that checks whether common subdomains of a website exist by resolving their IP addresses.

---

# 📖 What is this project?

Imagine you have a house.

The house address is:

```
example.com
```

Now imagine the house has many different rooms.

Those rooms might be:

```
www.example.com
mail.example.com
api.example.com
blog.example.com
```

These are called **subdomains**.

This script simply asks:

> "Do these rooms exist?"

If they do, Python tells us their IP Address.

---

# 🎯 What does this script do?

The script:

* Takes a domain name from the user
* Tries several common subdomains
* Checks if each one exists
* Prints the IP Address
* Saves all discovered subdomains into a text file
* Shows how long the scan took

Example

```
Enter Domain:

google.com
```

Output

```
[+] Found: www.google.com          -> 142.250.183.68
[+] Found: mail.google.com         -> 142.250.183.17
```

---

# 📂 Project Structure

```
project/

│
├── scanner.py
├── subdomain_results.txt
└── README.md
```

---

# 🧠 Python Modules Used

## socket

```
import socket
```

This module lets Python communicate over a network.

Think of it like a telephone.

Python can ask another computer:

> "Hello, what is the IP Address of [www.example.com](http://www.example.com)?"

The computer replies with something like

```
192.168.1.10
```

---

## time

```
import time
```

Used for measuring how long the scan takes.

Example

```
Start Scan

↓

3 seconds later

↓

End Scan
```

Python calculates

```
End - Start
```

to know the total scan time.

---

## concurrent.futures

```
from concurrent.futures import ThreadPoolExecutor
```

This is used for **multithreading**.

Without multithreading

```
Check www

↓

Wait

↓

Check mail

↓

Wait

↓

Check api

↓

Wait
```

One at a time.

With multithreading

```
www

mail

api

blog

admin

test

```

All start almost together.

This makes scanning much faster.

---

# 📋 Step 1

```
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
```

This is simply a Python List.

Think of a shopping list.

```
Milk

Bread

Eggs
```

Here our list is

```
www

mail

api

blog

...
```

Python will check every item.

---

# 📋 Step 2

```
results = []
```

Creates an empty list.

At first

```
[]
```

Nothing is inside.

Whenever a subdomain is found

```
("www.example.com", "93.184.216.34")
```

gets added.

Eventually it becomes

```
[
 ("www.example.com","93.184.216.34"),
 ("mail.example.com","93.184.216.35")
]
```

---

# 📋 Step 3

```
def scan_subdomain(sub, domain):
```

This creates a **Function**.

A function is simply a reusable machine.

Imagine a juice machine.

You put fruit in.

The machine makes juice.

Every time you want juice,

you press the button instead of rebuilding the machine.

Functions work exactly the same way.

---

# 📋 Step 4

```
target = f"{sub}.{domain}"
```

This is called an **f-string**.

If

```
sub = "www"

domain = "google.com"
```

Python combines them.

Result

```
www.google.com
```

Very simple.

---

# 📋 Step 5

```
socket.gethostbyname(target)
```

This is the most important line.

Python asks DNS

> "What is the IP Address of this website?"

Example

```
www.google.com
```

might return

```
142.250.183.68
```

If the subdomain does not exist,

Python cannot find an IP.

It throws an error.

---

# 📋 Step 6

```
try:
```

Means

> "Try this code."

If everything works,

continue.

---

# 📋 Step 7

```
except socket.gaierror:
```

Sometimes

```
dev.example.com
```

doesn't exist.

Instead of crashing,

Python says

```
No problem.

Move on.
```

This is why the program continues scanning.

---

# 📋 Step 8

```
results.append((target, ip))
```

Imagine you have a notebook.

Whenever you find something interesting,

you write it down.

Python does exactly that.

Before

```
[]
```

After

```
[
 ("www.example.com","93.184.216.34")
]
```

---

# 📋 Step 9

```
ThreadPoolExecutor(max_workers=20)
```

This creates 20 workers.

Imagine one student searching a library.

```
One student

↓

100 books

↓

Very slow
```

Now imagine

20 students searching together.

```
20 students

↓

100 books

↓

Much faster
```

That is exactly what multithreading does.

---

# 📋 Step 10

```
executor.submit(...)
```

This gives work to a thread.

Like saying

```
Worker 1

Check www

Worker 2

Check mail

Worker 3

Check api
```

Everyone starts working together.

---

# 📋 Step 11

```
time.time()
```

Returns the current time.

Example

Start

```
10.25 seconds
```

Finish

```
14.80 seconds
```

Difference

```
4.55 seconds
```

The scan took

```
4.55 seconds
```

---

# 📋 Step 12

```
with open(...)
```

Creates a text file.

Instead of only printing results,

Python saves them.

Example

```
www.google.com

142.250.183.68
```

gets written into

```
subdomain_results.txt
```

---

# 📋 Step 13

```
if __name__ == "__main__":
```

This is a Python standard.

It means

> "Only start the program if this file is executed directly."

If another Python program imports this file,

the scan won't automatically run.

---

# 🔄 Program Flow

```
User enters domain

        │

        ▼

Python loads subdomain list

        │

        ▼

Multiple threads start

        │

        ▼

Each thread checks one subdomain

        │

        ▼

DNS returns IP?

      /     \

    Yes      No

    │         │

Store Result  Ignore

     │

     ▼

Save Results

     │

     ▼

Display Summary
```

---

# 📁 Example Output File

```
Subdomain Enumeration Results

=======================================

www.google.com               142.250.183.68
mail.google.com              142.250.183.17
api.google.com               142.250.183.19
```

---

# 🚀 Improvements Made

Compared to the original version, this script includes:

* ✅ Better code organization using functions
* ✅ Faster scanning with multithreading
* ✅ Cleaner exception handling
* ✅ Automatic result storage
* ✅ Scan duration measurement
* ✅ Results saved to a text file
* ✅ Simple summary after scanning

---

# 📚 Concepts Learned

By building this project, you practice:

* Variables
* Lists
* Functions
* Loops
* String formatting (f-strings)
* Exception handling
* DNS lookups
* Multithreading
* File handling
* Time measurement
* Basic networking

---

# 🎓 Beginner Analogy

Imagine you're looking for different departments in a company.

The company is:

```
example.com
```

Departments might be:

```
HR

IT

Accounts

Reception
```

Instead of walking to each room yourself,

you send **20 helpers**.

Each helper checks one room.

Whenever a room exists,

they write its location in your notebook.

When everyone finishes,

you have a complete list of all the departments that exist.

That is exactly how this Python Subdomain Scanner works.

---

# ❤️ Final Thoughts

This project is intentionally simple, making it an excellent exercise for beginners. It introduces core Python programming concepts and basic networking without requiring external libraries. From here, you can gradually enhance it by reading subdomains from a wordlist, adding command-line arguments, scanning thousands of names, or integrating additional DNS record lookups.
