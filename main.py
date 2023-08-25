import time
import os
import random
i=1
f2 = open("script.txt", "r")
f2 = f2.read().replace("'", "").split(",")
while True:
    f = open("main_file.txt", "a")      
    word = f2[i]
    print(word)
    f.write(word)
    f.close()
    i+=1
    print(f"Current num: {i}")
    os.system("git add .")
    os.system(f"git commit -m \"{i} commit\"")
    os.system("git push")
    x=random.randint(2.700, 8.6400)
    print(f"Waiting {x/60/60} hours before next commit")
    time.sleep(x) #Between 45mins and 1day
    