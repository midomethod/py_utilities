import math, string, sys, os, subprocess


print("Hello Python...")

# Compile C code
os.system("cd ../c_portion; make >/dev/null 2>&1;")

# Run an executable through python and pipe the output
proc = subprocess.Popen( [ '../c_portion/out' ], stdout=subprocess.PIPE )
stdout, _ = proc.communicate()
print(stdout.decode("utf-8"))