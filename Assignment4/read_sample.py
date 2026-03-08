"""
This file opens and read the sample.txt file.
This file also handles exception/error
"""

try:
    with open("sample.txt", "r") as fh:
        print("This is a sample file conent:")
        print("----------------------------------------")
        print(f"Line1: {fh.readline()}Line2: {fh.readline()}Line3: {fh.readline()}Line4: {fh.readline()}")
except FileNotFoundError:
    print("Error: The file you are trying to open is not found")



