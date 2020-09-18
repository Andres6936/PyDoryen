import cppyy
from Source.Event.Key import Key

# Set a new abbreviation
Doryen = cppyy.gbl.Doryen

class Console:
    def __init__(self, width : int, height : int) -> None:
        self.__instance : Doryen.Console = Doryen.Console(width, height)

    def clear(self) -> None:
        self.__instance.clear()

    def isRunning(self) -> bool:
        return self.__instance.isRunning()

    # Getters

    def getKeyPressed(self) -> Key:
        pass