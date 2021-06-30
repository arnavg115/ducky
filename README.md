# Ducky image downloader and other utils

This cli can be used to download many images. This also includes other utilities such as resizing and train-test splitting for machine learning purposes

<img src="https://upload.wikimedia.org/wikipedia/commons/4/45/Female_mallard.png" width="200px"/>

## Code

The code used to gain the uri's for the images is from this <a href="https://github.com/deepanprabhu/duckduckgo-images-api">repository.</a>

## Usage

```shell
pip install -r requirements.txt
```

### download

```shell
python3 download.py -n 100  -q Lion
```

The `-n` arg is the number and the `-q` is the query string.

### resize

```shell
python3 resize.py -f Lion -hg 600 -w 800
```

The `-f` is the folder of all of the images. `-hg` is the new height of all images and `-w` is the new width of all the image. It puts the outputs into a folder called resized\_[folder Name].

### split

```shell
python3 split.py -f resized_Lion -p 10
```

`-f` is the folder and `-p` is the percentage of images to be put for test.
