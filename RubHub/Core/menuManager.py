from RubHub.Core.menu import Menu
import os, sys, time
from typing import List

class MenuManager:
    currentMenu:Menu
    path:List[str] = []
    
    titleStr:str = """\r\n\r\n ________  ___  ___  ________          ___  ___  ___  ___  ________     \r\n|\\   __  \\|\\  \\|\\  \\|\\   __  \\        |\\  \\|\\  \\|\\  \\|\\  \\|\\   __  \\    \r\n\\ \\  \\|\\  \\ \\  \\\\\\  \\ \\  \\|\\ /_       \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\|\\ /_   \r\n \\ \\   _  _\\ \\  \\\\\\  \\ \\   __  \\       \\ \\   __  \\ \\  \\\\\\  \\ \\   __  \\  \r\n  \\ \\  \\\\  \\\\ \\  \\\\\\  \\ \\  \\|\\  \\       \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\|\\  \\ \r\n   \\ \\__\\\\ _\\\\ \\_______\\ \\_______\\       \\ \\__\\ \\__\\ \\_______\\ \\_______\\\r\n    \\|__|\\|__|\\|_______|\\|_______|        \\|__|\\|__|\\|_______|\\|_______|"""
    
    @staticmethod
    def SetMenu(menu:Menu, addToPath:bool=True):
        setOldMenu = True
        try:
            oldMenu:Menu = MenuManager.currentMenu
        except:
            setOldMenu = False
        MenuManager.currentMenu = menu
        if addToPath:
            MenuManager.path.append(menu.menuName)
            if setOldMenu:
                menu.topMenu = oldMenu
        else:
            MenuManager.path.pop(-1)
    
    @staticmethod
    def DisplayMenu():
        # os.system("cls")
        print(MenuManager.titleStr)
        print(f"\nPath:\n{MenuManager.CreatePathString()}")
        if len(MenuManager.path) > 1:
            print(f"{MenuManager.currentMenu.menuString}0: Back")
        else:
            print(f"{MenuManager.currentMenu.menuString}0: Quit")
    @staticmethod
    def PickOption():
        try:
            ans:int = int(input("> "))
        except ValueError:
            print("invalid option")
            return
        if ans == 0:
            try:
                if not MenuManager.currentMenu.topMenu is None:
                    MenuManager.SetMenu(MenuManager.currentMenu.topMenu, False)
                else:
                    MenuManager.Exit()
            except AttributeError:
                MenuManager.Exit()
        else:
            MenuManager.currentMenu.ChoseOption(ans)
                
    @staticmethod
    def CreatePathString() -> str:
        returnString = ""
        first:bool = True
        for name in MenuManager.path:
            if not first:
                returnString = f"{returnString} > {name}"
            else:
                returnString = f"{name}"
                first = False
        return returnString
           
    @staticmethod     
    def Exit():
        print("Goodbye")
        sys.exit()
        
