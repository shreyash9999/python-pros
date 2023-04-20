from sys import argv
from os.path import exists

script , from_file , to_file = argv

print(f"Copying from {from_file} to {to_file}.")

#We could ddo this to on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long.")

print(f"Dose the output file exist? {exists(to_file)}.")
print("Ready, hit RETURN to continue, CLTR-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
