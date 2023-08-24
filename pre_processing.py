import os

with open("text.txt", "r") as f:
    f2 = open("script.txt", "w")
    f2.write(str(f.read().replace("\n", " ").split(" ")))
    f2.close()

