# ASCII-NATOR

ASCII-NATOR converts JPEG images into ASCII art and exports it into a text file.

## Requirements

ASCII-NATOR uses the Python Imaging Library (PIL) to convert images to ASCII. To install:

```bash
pip install pillow
```

## Usage

After cloning and opening the file, change the path location to the location of the image. Then, run the script.

```python

path = ' [ENTER PATH] '

```

## How It Works
The general algorithm is as follows:
  1) Create a chars array that will represent various degrees of brightness
  2) Convert image to greyscale
  3) Resize the image to match the ASCII height & width
  4) Traversing through each pixel in the image, do the following:
  * Calculate the luminance value in the greyscale image
  * Normalize the value so that 255 (white) corresponds to the last index in
       the chars array and 0 (black) corresponds to the first index in array (and for
       any other value in between)
  * Output the corresponding ASCII character

## License
[MIT](https://choosealicense.com/licenses/mit/)
