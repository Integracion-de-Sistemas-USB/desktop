from abc import ABC, abstractmethod

class Peripheral(ABC):
    @abstractmethod
    def get_pointer_position(self):
        pass
    
    @abstractmethod
    def get_button_events(self):
        pass
