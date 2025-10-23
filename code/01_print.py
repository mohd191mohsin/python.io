"""
Python Print Master Guide
-------------------------
This script demonstrates almost every way to use Python's print() function.
It covers:
- Basic printing
- Data type printing
- Formatting and styling
- Escapes, Unicode, bytes
- Alignment, precision, and bases
- Printing collections
- File and flush printing
- Pretty printing and text wrapping
- Progress bars and tabular data
"""

# ========== 1️⃣ BASIC PRINTING ==========

# Single-line print
print('Hello World!!!')

# Printing basic data types
print(2)                 # Integer
print(3.5)               # Float
print(True)              # Boolean

# Multi-line string
print("""
This is a multi-line string.
It can span multiple lines.
You can use it to write longer text.
It is useful for documentation or comments.
""")

# Special characters (escaping quotes)
print("He said, \"Hello!\"")

# Escape sequences: \n (newline), \t (tab)
print("First Line\nSecond Line\tTabbed")

# Raw strings: ignore escape sequences
print(r"C:\Users\Name\Documents")

# ========== 2️⃣ VARIABLES AND FORMATTING ==========

name = "Alice"
age = 30

# f-Strings (modern way)
print(f"My name is {name} and I am {age} years old.")

# Using 'end' parameter (avoid automatic newline)
print("Hello,", end=" ")
print("World!")  # Output: Hello, World!

# Using 'sep' parameter (custom separator)
print("Apple", "Banana", "Cherry", sep=" | ")

# Large numbers with underscores
print(1_000_000)  # Output: 1000000

# Complex numbers
print(3 + 4j)

# Unicode characters (☺)
print("Unicode character for smiley face: \u263A")

# Bytes
print(b'Hello Bytes')

# format() method (older but still common)
print("My name is {} and I am {} years old.".format(name, age))

# f-string with expressions
print(f"{name} will be {age + 1} next year.")

# Multi-line formatted string
print(f"""
My name is {name},
I am {age} years old,
My hobbies are playing Cricket and Coding.
""")

# Custom end and sep combined
print("Python", "is", "fun!", sep=" - ", end="\n***\n")

# Flush output immediately (useful for logging or live updates)   
print("This will be printed immediately.", flush=True)

# ========== 3️⃣ PRINTING COLLECTIONS ==========

person = {"name": "Bob", "age": 25}
print(person)  # Dictionary

fruits = ["Apple", "Banana", "Cherry"]
print(fruits)  # List

coordinates = (10, 20)
print(coordinates)  # Tuple

colors = {"Red", "Green", "Blue"}
print(colors)  # Set (unordered)

print(None)  # NoneType

# Joining elements of a list
words = ["Hello", "from", "Python"]
print(" ".join(words))

# ========== 4️⃣ NUMERIC FORMATTING ==========

number = 255
print(f"Decimal: {number}, Hex: {hex(number)}, Oct: {oct(number)}, Bin: {bin(number)}")

# Width and alignment
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")

# Precision formatting
pi = 3.141592653589793
print(f"Pi to 3 decimal places: {pi:.3f}")

# Percentage and padding
score = 0.9876
print(f"Success rate: {score:.2%}")  # 98.76%

# ========== 5️⃣ ADVANCED PRINTING ==========

# Using textwrap for long text
import textwrap
long_string = (
    "This is a very long string that needs to be wrapped "
    "to fit within a certain width for better readability."
)
wrapped_string = textwrap.fill(long_string, width=50)
print(wrapped_string)

# Printing a progress bar
import time
for i in range(0, 101, 5):
    print(f"\rProgress: [{'#' * i:<100}] {i}%", end="")
    time.sleep(0.02)
print()  # Move to new line

# Printing a simple table
data = [
    ("Name", "Age", "City"),
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago")
]
for row in data:
    print(f"{row[0]:<10} | {row[1]:<5} | {row[2]:<15}")

# ========== 6️⃣ FILE AND PRETTY PRINTING ==========

# Printing to a file
with open("output.txt", "w") as f:
    print("This line is written to a file.", file=f)

# Pretty printing (for structured data)
import pprint
info = {
    "name": "Alice",
    "skills": ["Python", "Django", "Flask"],
    "details": {"age": 30, "city": "New York"}
}
print("\nDefault dict print:")
print(info)
print("\nPretty printed dict:")
pprint.pprint(info, width=40)

# JSON-style formatted print
import json
print("\nJSON formatted output:")
print(json.dumps(info, indent=4))

# ========== 7️⃣ COLORED AND STYLED OUTPUT (BONUS) ==========

# ANSI escape codes for color (works in most terminals)
print("\033[31mThis is red text\033[0m")
print("\033[32mThis is green text\033[0m")
print("\033[33mThis is yellow text\033[0m")

# Using colorama for cross-platform colors
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    print(Fore.CYAN + "This is cyan text")
    print(Fore.MAGENTA + "This is magenta text")
    print(Style.BRIGHT + "This is bright text")
except ImportError:
    print("Install colorama for color support: pip install colorama")
