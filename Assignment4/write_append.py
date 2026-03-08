"""
In this file we are first writing the content to the file "output.txt"
Then we will append the more lines in same "output.txt"
"""

# To create a new file and write in it.
with open("output.txt", "wt") as fh:
    fh.write(input("Enter text to write to the file: "))
    print("Data successfully written to the file")

# To Append the addition line in above file
with open("output.txt", "at") as fh:
    fh.write("\n")
    fh.write(input("Enter additional text to append: "))
    print("Data successfully appended to the file")

# To read the above file
with open("output.txt", "r") as fh:
    print(f"Final content of output.txt:\n{fh.read()}")
