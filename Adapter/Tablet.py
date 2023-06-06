import pyglet
from Model.TabletData import TabletData

class Tablet(pyglet.input.Device):
    def __init__(self, window : pyglet.window.Window) -> None:
        for device in pyglet.input.get_devices():
            if "XP-Pen" in device.name:
                tablet = device
                break
            
        print(tablet)
        super(Tablet, self).__init__(tablet.display, tablet.name)

        controls = tablet.get_controls()
        self.tablet = tablet
        self.control_presion = controls[7]
        self.button = controls[3]
        self.control_x =  controls[0]
        self.control_y = controls[2]

        try:
            self.canvas = self.tablet.open(window)
        except pyglet.input.DeviceException:
            print('Failed to open tablet %d on window')
    
    def get_data(self) -> TabletData:
        return TabletData(
            x_pos=self.control_x,
            y_pos=self.control_y,
            presion=self.control_presion
        )
    