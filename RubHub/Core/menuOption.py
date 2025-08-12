from RubHub.Core.actionTypes import ActionTypes
from RubHub.Core.menuOptionComponents import allComponentTypes, Component
from typing import List

class MenuOption:
    def __init__(self, info:dict):
        self.name = self.SetAttribute(info, "name", "untitled option")
        self.action = self.SetAttribute(info, "action", [])
        self.actionType:ActionTypes
        self.components:List[Component] = []
        for action in self.action:
            actionName = list(action.keys())[0]
            if actionName in allComponentTypes:
                self.components.append(allComponentTypes[actionName](action[actionName]))
        
    def SetAttribute(self, dictionary, key, defaultValue):
        if key in dictionary:
            return dictionary[key]
        else: 
            return defaultValue
        
    def Chosen(self):
        for component in self.components:
            component.Chosen()
        
        