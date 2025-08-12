from RubHub.Core.menuOption import MenuOption
from typing import List
from Util.jsonParse import parseJsonFile

class Menu:
    def __init__(self, path:str):
        self.info = parseJsonFile(f"Menus/{path}")
        self.menuName:str = self.SetAttribute(self.info, "name", "untitled_option")
        self.menuString:str = ""
        self.options:List[MenuOption] = []
        self.topMenu:Menu
        
        options = self.SetAttribute(self.info, "options", [])
        for opt in options:
            self.AddMenuOption(MenuOption(opt))
        
    def AddMenuOption(self, option:MenuOption):
        self.options.append(option)
        self.menuString = f"{self.menuString}{len(self.options)}: {option.name}\n"
        
    def SetAttribute(self, dictionary, key, defaultValue):
        if key in dictionary:
            return dictionary[key]
        else: 
            return defaultValue
        
        
    def ChoseOption(self, option:int):
        if -1 < option-1 < len(self.options):
            self.options[option-1].Chosen()