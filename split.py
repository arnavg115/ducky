import argparse
import os
import math
import cv2
import time

init = time.time()
parser = argparse.ArgumentParser()

parser.add_argument("-f","--folder",default=None)
parser.add_argument("-p", "--percentage", default=10)


args = parser.parse_args()
per = int(args.percentage)



if args.folder == None:
    raise Exception("No folder specified")

folder = str(args.folder)

if f"ml_{folder}" not in os.listdir():
    os.mkdir(f"ml_{folder}")

if "train" not in os.listdir(f"ml_{folder}") or "test" not in os.listdir(f"ml_{folder}"):
    os.mkdir(f"ml_{folder}/train")
    os.mkdir(f"ml_{folder}/test")

nums = math.floor((1 - per/100) * len(os.listdir(folder)))


for index,file in enumerate(os.listdir(folder)):
    img = cv2.imread(f"{folder}/{file}")
    if(index  < nums):
        cv2.imwrite(f"ml_{folder}/train/{file}",img)
    else:
        cv2.imwrite(f"ml_{folder}/test/{file}",img)



final = time.time()
total = round(final-init, 3)
print("-"*len(f"Operation took {total}s"))
print(f"Operation took {total}s")
print("-"*len(f"Operation took {total}s"))