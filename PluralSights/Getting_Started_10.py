#https://github.com/danielabar/python-pluralsight/blob/master/code/classes/airtravel.py

""" Model for aircraft flights."""
import sys
import os
from pprint import pprint as pp

class Flight:
    #f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    def __init__(self, number, aircraft):    #__init__ is the inital phase of a class
        #check if values are inserted properly for a flight
        if not number[:2].isalpha(): #is it a letter
            raise ValueError(f"No airline code in '{number}'")
            
        if not number[:2].isupper(): 
            raise ValueError(f"Invalid airline code '{number}'")
            
        if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
            raise ValueError(f"Invalid route number '{number}'")            
       
        #Characteristics for a flight
        self._number = number    #_number to seperate from number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
    
    def aircraft__model(self):
        return self._aircraft.model()
    
    def number(self): 
        return self._number
        
    def airline(self):
        return self._number[:2] 
        
        
class Aircraft:
    #a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)    
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows   
        self._num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration
        
    def model(self):
        return self._model
        
    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK" [:self._num_seats_per_row])