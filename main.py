import time
import subprocess
i=0
while True:
    f = open("main_file.txt", "w")
    f2 = open("script.txt", "r")
    f2 = list(f2.read())
    f.write(f2[i])
    i+=1
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit","-m" ,f"{i} commit"])
    subprocess.run(["git", "push"])
    quit()
    