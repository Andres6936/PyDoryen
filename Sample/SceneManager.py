class SceneManager:
    def __init__(self) -> None:
        self.running : bool = True

    def draw(self) -> None:
        pass

    def update(self) -> None:
        pass

    def processInput(self) -> None :
        pass

    def isRunning(self) -> bool:
        return self.running