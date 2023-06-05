import pyglet

class Tablet(pyglet.input.Device):
    def __init__(self) -> None:
        global control_presion

        for device in pyglet.input.get_devices():
            if "XP-Pen" in device.name:
                tablet = device
                break

        super(Tablet, self).__init__(tablet.display, tablet.name)

        controls = tablet.get_controls()
        self.tablet = tablet
        self.control_presion = controls[7]
        self.button = controls[3]
        self.control_x =  controls[0]
        self.control_y = controls[2] 
    
    def process(self):
        pass
        #print(self.control_x.value, self.control_y.value, self.control_presion.value)
    