from PIL import Image

def fialovyf():
    obrazek = Image.open("plaz.jpg")
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            y += 1
        x += 1
    obrazek.show()

def teple_barevny_filtr():
    obrazek = Image.open("plaz.jpg")
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            # Úprava barev pro teplý tón
            r_new = min(255, r + 50)  # Zvýšíme červenou složku o 50
            g_new = min(255, g + 30)  # Zvýšíme zelenou složku o 30
            b_new = max(0, b - 30)    # Snížíme modrou složku o 30
            obrazek.putpixel((x,y), (r_new, g_new, b_new))
            y += 1
        x += 1
    obrazek.show()   


def cernobily():
    obrazek = Image.open("plaz.jpg")
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            # Vypočítáme průměr hodnot R, G, B a použijeme ho pro všechny složky
            prumer = int((r + g + b) / 3)
            # Nastavíme novou hodnotu barvy na odstíny šedé
            obrazek.putpixel((x,y), (prumer, prumer, prumer))
            y += 1
        x += 1
    obrazek.show()

oddelovac = "=" * 62
sluzby = ("fialovy filtr - 1", "teply filtr - 2", "cerrnobily filtr - 3")
print("Vitejte v nasem filtrovem studiu!".upper().center(62),"Jaký filtr by jsi chtěl na fotku dát?".lower().center(62),
          oddelovac,sep="\n")
print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")

volba = int(input("1,2,3 ?"))

if (volba == 1):
    fialovyf()

if (volba == 2):
    teple_barevny_filtr()

if (volba == 3):
    cernobily()    