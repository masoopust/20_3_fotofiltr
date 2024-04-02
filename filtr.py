from PIL import Image

oddelovac = "=" * 120
types = ("Purple filter - 1", "Warm filter - 2", "Black and white filter - 3")
photos = ("Friends on the beach - 1", "Football goalkeeper - 2", "Forest - 3","Friends on Volcano - 4","Erasmus group photo - 5",)
print("\n")
print("Welcome in mine filter studio!".upper().center(62),"Which photo would you like to edit?". lower().center(62),
          oddelovac,sep="\n")
print(f"| {' | '.join(photos)} |".center(62), oddelovac, sep="\n")

volba0 = int(input("1,2,3,4,5 ?\n: "))

if (volba0 == 1):
    picture = Image.open("beach.jpg")

if (volba0 == 2):
    picture = Image.open("gadzo.jpg")

if (volba0 == 3):
    picture = Image.open("forest.jpg")

if (volba0 == 4):
    picture = Image.open("erasmus_volcano.jpg")

if (volba0 == 5):
    picture = Image.open("erasmus_group_photo.jpg")   

print("Which filter would you like to apply on photo?".lower().center(62),)
print(f"| {' | '.join(types)} |".center(62), oddelovac, sep="\n")


def purple():
   # picture = Image.open("beach.jpg")
    width, high = picture.size
    x = 0
    while x < width:
        y = 0
        while y < high:
            r, g, b = picture.getpixel((x,y))
            diameter = int((r+g+b)/3)
            picture.putpixel((x,y), (r , b, r))
            y += 1
        x += 1
    picture.show()


def warm_colors():
    #picture = Image.open("beach.jpg")
    width, high = picture.size
    x = 0
    while x < width:
        y = 0
        while y < high:
            r, g, b = picture.getpixel((x,y))
             # Color adjustment for warmer tone
            r_new = min(255, r + 50)  # Increase of the red component by 50
            g_new = min(255, g + 30)  # Increase of the green component by 30
            b_new = max(0, b - 30)    # Reduce of the blue component by 50
            picture.putpixel((x,y), (r_new, g_new, b_new))
            y += 1
        x += 1
    picture.show()


def blckwhite():
    #picture = Image.open("beach.jpg")
    width, high = picture.size
    x = 0
    while x < width:
        y = 0
        while y < high:
            r, g, b = picture.getpixel((x,y))
            # Calculate the average of R, G, B values ​​and use it for all components
            diameter = int((r + g + b) / 3)
            # Set the new value for gray shadows 
            picture.putpixel((x,y), (diameter, diameter, diameter))
            y += 1
        x += 1
    picture.show()

volba1 = int(input("1,2,3 ?\n: "))

if (volba1 == 1):
    purple()

if (volba1 == 2):
    warm_colors()

if (volba1 == 3):
    blckwhite()    