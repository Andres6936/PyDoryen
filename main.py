import cppyy
from Sample.SceneManager import SceneManager

def bootstrap():
    cppyy.add_include_path('.')
    cppyy.include('Doryen/Doryen.hpp')
    cppyy.load_library('Library/libDoryen.Framework.so')

if __name__ == '__main__':
    bootstrap()

    scene = SceneManager()
    while scene.isRunning():
        scene.processInput()
        scene.update()
        scene.draw()
