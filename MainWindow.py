import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self) -> None:
        super().__init__(resizable=True)

        self.win_size = (self.width, self.height)

    def resize(self) -> None:
        if self.win_size == (self.width, self.height):
            return
        
        self.clear()
        label = pyglet.text.Label('Hello, world',
                        font_name='Times New Roman',
                        font_size=36,
                        x=self.width//2, y=self.height//2,
                        anchor_x='center', anchor_y='center')
        
        self.win_size = (self.width, self.height)
        label.draw()