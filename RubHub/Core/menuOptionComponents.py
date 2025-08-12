import os, subprocess
from typing import Dict


def AddComponentToList(cls):
    allComponentTypes[cls.__name__] = cls
    return cls

class Component:
    def __init__(self) -> None:
        pass
    def Chosen(self):
        pass
    
allComponentTypes:Dict[str, type] = {}
    
@AddComponentToList
class LoadMenu(Component):
    def __init__(self, menu:str) -> None:
        super().__init__()
        self.menu = menu
    def Chosen(self):
        from RubHub.Core.menuManager import MenuManager
        from RubHub.Core.menu import Menu
        MenuManager.SetMenu(Menu(self.menu))
        return super().Chosen()
    
@AddComponentToList
class OpenFile(Component):
    def __init__(self, filePath:str) -> None:
        super().__init__()
        self.filePath = filePath
    def Chosen(self):
        os.startfile(self.filePath)
        return super().Chosen()
    
@AddComponentToList
class OpenFolder(Component):
    def __init__(self, filePath:str) -> None:
        super().__init__()
        self.filePath = filePath
    def Chosen(self):
        os.startfile(self.filePath)
        return super().Chosen()
    
@AddComponentToList
class RunPython(Component):
    def __init__(self, filePath:str) -> None:
        super().__init__()
        self.filePath = filePath
    def Chosen(self):
        subprocess.run(["python", self.filePath])
        return super().Chosen()