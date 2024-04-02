from PIL import Image

def purple():
    picture = Image.open("beach.jpg")
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
    picture = Image.open("beach.jpg")
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
    picture = Image.open("beach.jpg")
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

oddelovac = "=" * 70
types = ("Purple filter - 1", "Warm filter - 2", "Black and white filter - 3")
print("\n")
print("Welcome in mine filter studio!".upper().center(70),"Which filter would you like to apply on photo?".lower().center(62),
          oddelovac,sep="\n")
print(f"| {' | '.join(types)} |".center(62), oddelovac, sep="\n")

volba = int(input("1,2,3 ?\n: "))

if (volba == 1):
    purple()

if (volba == 2):
    warm_colors()

if (volba == 3):
    blckwhite()    