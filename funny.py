import os, time
np = 0
for i in range(1000):
    time.sleep(0.5)
    os.system("start cmd")
    while np<1000:
        print(f"run cmd{np}")
        np=np+1