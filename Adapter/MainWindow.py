import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self) -> None:
        super().__init__(resizable=True)

        self.label = pyglet.text.Label('Hello, world',
                        font_name='Times New Roman',
                        font_size=36,
                        anchor_x='center', anchor_y='center')

    def resize(self) -> None:
        self.clear()
        self.label.x = self.width//2
        self.label.y = self.height//2
        self.label.draw()