import time
import subprocess
i=0
while True:
    f = open("main_file.txt", "w")
    f2 = open("script.txt", "r")
    f2 = f2.read()
    f.write(f2.read()[i])
    i+=1
    