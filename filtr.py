from PIL import Image



oddelovac = "=" * 62
sluzby = ("zluty filtr", "cerveny filtr", "cerrnobily filtr")
print("Vitejte v nasem filtrovem studiu!".upper().center(62),"Jaký filtr by jsi chtěl na fotku dát?".lower().center(62),
          oddelovac,sep="\n")
print(f"| {' | '.join(sluzby)} |".center(62), oddelovac, sep="\n")



