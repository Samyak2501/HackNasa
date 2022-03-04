from termcolor import colored
from tqdm import tqdm
import time

Name = input("Enter your name: ")


print(colored("\n\n****HACKING NASA****\n\n", "green"))
time.sleep(3)


print(colored("*****DDOS AATACK STARTED*****\n\n", "green"))


print(colored("*****TRACKING IP*****", "green"))

time.sleep(3)



for i in tqdm (range (100), 
               desc="Tracking…", 
               ascii=False, ncols=75):
    time.sleep(0.02)

print("\n\n")

print(colored("*****IP FOUND*****\n\n", "green"))


print(colored("*****BYPASSING ALL SECURITY*****\n", "green"))

time.sleep(1)

for i in tqdm (range (100), 
               desc="Tracking…", 
               ascii=False, ncols=75):
    time.sleep(0.02)

print("\n\nCongratulations "+Name+"! You have successfully hacked NASA")