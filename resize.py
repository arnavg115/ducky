import argparse
import time
import cv2
import os

init = time.time()
parser = argparse.ArgumentParser()

parser.add_argument("-hg","--height", default=600)
parser.add_argument("-w", "--width", default=600)
parser.add_argument("-f", "--folder", default=None)

args = parser.parse_args()

height = int(args.height)
width = int(args.width)
if args.folder == None:
    raise Exception("No folder provided")
folder = str(args.folder)

if f"resized_{folder}" not in os.listdir():
    os.mkdir(f"resized_{folder}")

for file in os.listdir(folder):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".tiff") or file.endswith(".JPG"):
        img = cv2.imread(f"{folder}/"+file)
        resized = cv2.resize(img, (width, height))
        cv2.imwrite(f"resized_{folder}/{file}",resized)

final = time.time()
total = round(final-init, 3)
print("-"*len(f"Operation took {total}s"))
print(f"Operation took {total}s")
print("-"*len(f"Operation took {total}s"))