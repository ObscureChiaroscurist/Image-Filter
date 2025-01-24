######################################
# Image Filter Project Starter Code  #
#                                    #
#           Project STEM             #
#                                    #
#              9/20/19               #
#                                    #
######################################

# Before running any code, please run the following in the shell :
# pip install -r requirement.txt

# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os

# Deletes old created images if they exist
images = ["combinedFilters.jpg","shade.jpg","tempdiffusion.jpg","enhance.jpg","grey.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#    Example Filter    #
########################
def grey():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components

    newr = (r + g + b) // 3 
    newg = (r + g + b) // 3 
    newb = (r + g + b) // 3

    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage


#####################
#    Your Filter    #
#####################
#Establishing variables for color manipulation
Rvalue = 0
Gvalue = 0
Bvalue = 0

def shade(color):
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # Creates variables for color RGB manipulation

  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  
  if color == "pink":
    Rvalue = 50
    Bvalue = 50
    Gvalue = 1
  elif color == "green":
    Rvalue = 1
    Bvalue = 1
    Gvalue = 60
  elif color == "orange":
    Rvalue = 60
    Bvalue = 1
    Gvalue = 20
 
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components

    newr = r + Rvalue
    newg = g + Gvalue
    newb = b + Bvalue

    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage
 



#####################################
#    Your Filters with User Input   #
#####################################
#establishing variables for color manipulation
coolr = 0
coolg = 0
coolb = 0

def tempdiffusion(tone):
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  if tone == "warm":
    while location < len(new_pixels):
      # Gets the current color of the pixel at location
      p = new_pixels[location]
      # Splits color into red, green and blue components
      r = p[0]
      g = p[1]
      b = p[2]
      # Perform pixel manipulation and stores results
      # to a new red, green and blue components
      
      #Setting variables to change RGB values
    

      newr = r + (r // 2)
      newg = g + (g // 2)
      newb = b 

      
      # Assign new red, green and blue components to pixel
      # at that specific location
      new_pixels[location] = (newr, newg, newb)
      # Changes the location to the next pixel in array
      location = location + 1
  if tone == "cool":
    while location < len(new_pixels):
      # Gets the current color of the pixel at location
      p = new_pixels[location]
      # Splits color into red, green and blue components
      r = p[0]
      g = p[1]
      b = p[2]
      # Perform pixel manipulation and stores results
      # to a new red, green and blue components


      newr = r 
      newg = g + (g // 2)
      newb = b + (b // 2)

      # Assign new red, green and blue components to pixel
      # at that specific location
      new_pixels[location] = (newr, newg, newb)
      # Changes the location to the next pixel in array
      location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage

def enhance(scale):
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    enhanceScale = ((scale * 8) + 50) // 10

    newr = r // 5 * enhanceScale
    newg = g // 5 * enhanceScale
    newb = b // 5 * enhanceScale

    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage

# Creates the four filter images and saves them to our files
a = grey()
a.save("grey.jpg")
b = shade("pink")
b.save("Pink.jpg")
c = shade("green")
c. save("Green.jpg")
d = shade("orange")
d.save("Orange.jpg")
e = tempdiffusion("warm")
e.save("tempdiffusion_warm.jpg")
f = tempdiffusion("cool")
f.save("tempdiffusion_cool.jpg") 
g = enhance(5)
g.save("enhance.jpg")


# Image filter names for use below
f1 = "shade"
f2 = "tempdiffusion"
f3 = "enhance"



# Apply multiple filters through prompts with the user
answer = input("\nWhich filter do you want me to apply?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
  answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == "grey" or answer == f1 or answer == f2 or answer == f3:
  if answer == "grey":
    img = grey()
  elif answer == f1:
    answer = input(print("What color shade would you like to add to the image?\n pink\n green\n orange\n\n"))
    while answer != "pink" and answer != "green" and answer != "orange":
      answer = input("Incorrect color, please enter:\n pink\n green\n orange\n\n")
    img = shade(answer)
  elif answer == f2:
    answer = input("Would you like to apply a warm or cool tone to the image?\n warm\n cool\n\n")
    while answer != "warm" and answer != "cool":
      answer = input("Incorrect tone, please enter:\n warm\n cool\n\n")
      img = tempdiffusion(answer)
  elif answer == f3:
    answer = input("On a scale of 1 to 10, how much would you like to enhance the image?\n\n")
    while int(answer) < 1 or int(answer) > 10:
      answer = input("Number out of range, please enter a number between 1 and 10:\n\n")
    img = enhance(int(answer))
  else:
    break
  print("Filter \"" + answer + "\" applied...")
  answer = input("\nWhich filter do you want me to apply next?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
    answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
print("Image being created...Done")

# Create the combined filter image and saves it to our files
img.save("combinedFilters.jpg")