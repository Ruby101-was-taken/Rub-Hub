import os, sys, subprocess
from PIL import Image
from tkinter import filedialog
from RubHub.Core.menuManager import MenuManager
from RubHub.Core.menu import Menu
os.system("cls")

print("Welcome to RubHub")

# ans:int = int(input("What would you like to do.\n1.Resize all images\n0.Quit\n>"))

# match ans:
#     case 0:
#         sys.exit()
#     case 1:
#         directory = filedialog.askdirectory()
        
#         w = int(input("Width\n>"))
#         h = int(input("Height\n>"))
                    
#         for file in os.listdir(directory):
#             filename = os.fsdecode(file)
#             fullFileName = f"{directory}/{filename}"
#             try:
#                 image = Image.open(fullFileName)
#                 newImage = image.resize((w, h))
#                 newImage.save(fullFileName)
#             except OSError:
#                 print(f"Issue with {fullFileName}")

run:bool = True
MenuManager.SetMenu(Menu("MainMenu.json"))

while run:
    try:
        MenuManager.DisplayMenu()
        MenuManager.PickOption()
    except KeyboardInterrupt:
        print()
        MenuManager.Exit()

    # subprocess.run(["python", "test.py"])
    