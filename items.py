# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:01:43 2024

@author: pjpet
"""
class Games:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    def getDescription(self): 
        return self.name + " - Amount In Stock: " + str(self.stock)
class XboxGame(Games):
    def __int__(self,name,price,system):
        self.system = "Xbox"
        Games.__init__(name,price)
        
    def getDescription(self):
        return str(Games.getDescription(self)) + " System: Xbox"
        
class SonyGame(Games):
    def __int__(self,name,price,system,stock):
        Games.__init__(name,price,stock)
        self.system = "Sony"

    def getDescription(self):
        return str(Games.getDescription(self)) + " System: Sony"
        
class SteamGame(Games):
    def __int__(self,name,price,system,stock):
        Games.__init__(name,price,stock)
        self.system = "Steam"
        
    def getDescription(self):
        return str(Games.getDescription(self)) + " System: Steam"
    
class NintendoGame(Games):
    def __int__(self,name,price,system,stock):
        Games.__init__(name,price,stock)
        self.system = "Nintendo"
        
    def getDescription(self):
        return str(Games.getDescription(self)) + " System: Nintendo"

        
    
