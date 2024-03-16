import pyjoycon
from .peripheral import Peripheral
from constants import *

class JoyCon(
    pyjoycon.GyroTrackingJoyCon,
    pyjoycon.ButtonEventJoyCon): 
    pass

class ExternalPeripheral(Peripheral):
    def __init__(self):
        joycon_id = pyjoycon.get_R_id()
        self.joycon = JoyCon(*joycon_id)
    
    def get_pointer_position(self):
        return self.joycon.pointer
    
    def get_button_events(self):
        button_events = self.joycon.events()
        shoot_events = [(event_type, status) for event_type, status in button_events if event_type == SHOOT_ACTION and status == SHOOT_MADE]
        return shoot_events
