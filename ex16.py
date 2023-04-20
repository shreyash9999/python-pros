from sys import argv

script , filename = argv

print(f"We're going to erase {filename}.")
print("If you don't won't that, hit CLRT-C (^C).")
print("If you do wantt that, hit RETURN.")

input("?")

print("Opening file...")
target = open(filename, 'w')

print("Turncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
