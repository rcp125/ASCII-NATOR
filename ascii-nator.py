from PIL import Image

chars = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 
        'Z', 'O', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', 
        '|', '(', ')', '1', '[', ']', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',',' ', ' ']

path = 'sample.jpg'
image = Image.open(path).convert('L')

def resize(image):
    ascii_height = 50 # number of ascii characters in image height
    adjustment = 2 # to account for character:pixel distortion
    (width, height) = image.size
    aspect_ratio = width / height
    nwidth = int(aspect_ratio * ascii_height * adjustment)
    nheight = ascii_height
    nsize = (nwidth, nheight)
    new = image.resize(nsize)
    return new

def charSelect(x, y):
    val = image.getpixel((x,y))
    pos = int(val/4.25)
    return chars[pos]

### execute
image = resize(image)

output = ""
for j in range(0, image.height):
    for i in range(0, image.width):
        output += charSelect(i,j)
    output += "\n"

# print(output)  #! if you want to print out result in terminal

filename = open("output.txt", "w")
filename.write(output)
filename.close()