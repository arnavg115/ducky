from utils.api import search
import wget
import argparse
import shutil
import os
import time

init = time.time()
parser = argparse.ArgumentParser()

parser.add_argument("-n","--number", default=10)
parser.add_argument("-q","--query", default="dogs")



args = parser.parse_args()
num = int(args.number)
query = str(args.query)


try:
    os.mkdir(query)

except Exception as e:
    print("skipping")

for i in search(query,num):
    try:
        file = wget.download(i["image"])
    except Exception as e:
        k = i["image"]
        print(f"skipping {k}")

for file in os.listdir():
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".tiff") or file.endswith(".JPG"):
        shutil.move(f"{os.getcwd()}/{file}",f"{os.getcwd()}/{query}/{file}")

final = time.time()
total = round(final-init, 3)
print("-"*len(f"Operation took {total}s"))
print(f"Operation took {total}s")
print("-"*len(f"Operation took {total}s"))