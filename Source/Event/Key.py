import cppyy
from Source.Event.KeyCode import KeyCode

# Set a new abbreviation
Doryen = cppyy.gbl.Doryen

class Key:

    def __init__(self, key : Doryen.Key = None) -> None:
        """
        Construct the object Key
        :param key: Object of type Doryen::Key, if is None the
            default value for keyCode is None
        """
        if key is None:
            self.__keyCode : KeyCode = KeyCode.NONE
        else:
            self.__keyCode : KeyCode = Key.__convertEvent(key)

    @staticmethod
    def __convertEvent(keyCode : Doryen.KeyCode ) -> KeyCode:
        if keyCode is Doryen.KeyCode.NONE:
            return KeyCode.NONE
        elif keyCode is Doryen.KeyCode.ESCAPE:
            return KeyCode.ESCAPE
        elif keyCode is Doryen.KeyCode.BACKSPACE:
            return KeyCode.BACKSPACE
        elif keyCode is Doryen.KeyCode.TAB:
            return KeyCode.TAB
        elif keyCode is Doryen.KeyCode.ENTER:
            return KeyCode.ENTER
        elif keyCode is Doryen.KeyCode.SHIFT:
            return KeyCode.SHIFT
        elif keyCode is Doryen.KeyCode.CONTROL:
            return KeyCode.CONTROL
        elif keyCode is Doryen.KeyCode.ALT:
            return KeyCode.ALT
        elif keyCode is Doryen.KeyCode.PAUSE:
            return KeyCode.PAUSE
        elif keyCode is Doryen.KeyCode.PAGE_UP:
            return KeyCode.PAGE_UP
        elif keyCode is Doryen.KeyCode.PAGE_DOWN:
            return KeyCode.PAGE_DOWN
        elif keyCode is Doryen.KeyCode.END:
            return KeyCode.END
        elif keyCode is Doryen.KeyCode.HOME:
            return KeyCode.HOME
        elif keyCode is Doryen.KeyCode.UP:
            return KeyCode.UP
        elif keyCode is Doryen.KeyCode.LEFT:
            return KeyCode.LEFT
        elif keyCode is Doryen.KeyCode.RIGHT:
            return KeyCode.RIGHT
        elif keyCode is Doryen.KeyCode.DOWN:
            return KeyCode.DOWN
        elif keyCode is Doryen.KeyCode.PRINT_SCREEN:
            return KeyCode.PRINT_SCREEN
        elif keyCode is Doryen.KeyCode.DELETE:
            return KeyCode.DELETE
        elif keyCode is Doryen.KeyCode.SPACE:
            return KeyCode.SPACE

        elif keyCode is Doryen.KeyCode.A:
            pass
        elif keyCode is Doryen.KeyCode.B:
            pass
        elif keyCode is Doryen.KeyCode.C:
            pass
        elif keyCode is Doryen.KeyCode.D:
            pass
        elif keyCode is Doryen.KeyCode.E:
            pass
        elif keyCode is Doryen.KeyCode.F:
            pass
        elif keyCode is Doryen.KeyCode.G:
            pass
        elif keyCode is Doryen.KeyCode.H:
            pass
        elif keyCode is Doryen.KeyCode.I:
            pass
        elif keyCode is Doryen.KeyCode.J:
            pass
        elif keyCode is Doryen.KeyCode.K:
            pass
        elif keyCode is Doryen.KeyCode.L:
            pass
        elif keyCode is Doryen.KeyCode.M:
            pass
        elif keyCode is Doryen.KeyCode.N:
            pass
        elif keyCode is Doryen.KeyCode.O:
            pass
        elif keyCode is Doryen.KeyCode.P:
            pass
        elif keyCode is Doryen.KeyCode.Q:
            pass
        elif keyCode is Doryen.KeyCode.R:
            pass
        elif keyCode is Doryen.KeyCode.S:
            pass
        elif keyCode is Doryen.KeyCode.T:
            pass
        elif keyCode is Doryen.KeyCode.W:
            pass
        elif keyCode is Doryen.KeyCode.X:
            pass
        elif keyCode is Doryen.KeyCode.Y:
            pass
        elif keyCode is Doryen.KeyCode.Z:
            pass
