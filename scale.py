import RPi.GPIO as GPIO
from hx711 import HX711

class Scale:
    
    def __init__(self):
        self.hx = HX711(5, 6)
        self.hx.set_reading_format("LSB", "MSB")
        self.hx.set_reference_unit(92)
        self.hx.reset()
        self.hx.tare()
        
        self.bounds = 0.5
    
    def get_weight(self):
        return self.hx.get_weight(5)
        
    def weight_changed(self, oldWeight):
        return oldWeight != self.get_weight()
    
    def weight_within_bounds(self, w1, w2):
        return (weight_below(w1, w2)) && (weight_above(w1, w2))
    
    def weight_below(self, newWeight, oldWeight):
        return newWeight < oldWeight + self.bounds
    
    def weight_above(self, newWeight, oldWeight):
        return newWeight > oldWeight - self.bounds