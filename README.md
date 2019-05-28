# ASCII-NATOR
Convert any image into ASCII art!

General Algorithm:
  1) Load image
  2) Apply grayscale to image
  3) Loop through pixels in image (pixel:area size ratio will affect final image)
  4) Calculate brightness in each block
  5) Correspond and append ASCII character relative to calculated brightness
