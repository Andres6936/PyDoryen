import cppyy
import importlib


def bootstrap():
    cppyy.add_include_path('.')
    cppyy.include('Doryen/Doryen.hpp')
    cppyy.load_library('Library/libDoryen.Framework.so')


from Sample.SceneManager import SceneManager

if __name__ == '__main__':
    bootstrap()

    scene = SceneManager()
    # while scene.isRunning():
    #     scene.processInput()
    #     scene.update()
    #     scene.draw()

    # Lazy import of Console
    imp = importlib.import_module("Source.Console.Console", "Console")

    console = imp.Console(40, 40)

    while console.isRunning():
        console.draw()
