import pyglet
from Tablet import Tablet
from MainWindow import MainWindow

window = MainWindow()
tablet = Tablet()

@window.event
def on_draw():
    window.resize()

@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x,y,button)

@tablet.control_presion.event
@tablet.control_x.event
@tablet.control_y.event
def on_change(presion):
    tablet.process()

pyglet.app.run()