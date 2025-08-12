import enum

class ActionTypes(enum.Enum):
    LOAD_MENU=0
    OPEN_FILE=1
    OPEN_FOLDER=2
    RUN_PYTHON=3
    
    UNKNOWN=-1