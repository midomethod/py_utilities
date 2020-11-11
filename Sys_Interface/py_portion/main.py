import math, string, sys, os, subprocess


print("Hello Python...")

#os.system("cd ../c_portion; make >/dev/null 2>&1;")

proc = subprocess.Popen( [ '../c_portion/out' ], stdout=subprocess.PIPE )
stdout, _ = proc.communicate()

print(stdout.decode("utf-8"))