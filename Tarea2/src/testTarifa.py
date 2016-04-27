#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 24 de abr. de 2016

@author:    Guillermo Betancourt    carnet 11-10103 
            Gabriel Gimenez         carnet 12-11006
'''

import unittest
from Tarea2 import *
from datetime import *

class TestTarea(unittest.TestCase):
    
    def testIsWeekend(self):
        dias = [ 
                datetime(year = 2016, month = 4, day = 23),
                datetime(year = 2016, month = 4, day = 24),
                datetime(year = 2016, month = 4, day = 25),
                datetime(year = 2016, month = 4, day = 26),
                datetime(year = 2016, month = 4, day = 27),
                datetime(year = 2016, month = 4, day = 28),
                datetime(year = 2016, month = 4, day = 29),
                ]
        
        for day in dias[:2]:
            self.assertTrue(isWeekend(day), "Error de isWeekend True")
        for day in dias[3:]:
            self.assertFalse(isWeekend(day), "Error de isWeekend False")
            
    def testCalcularPrecio(self):
        tarifas = [Tarifa(5,10)]
        tiempos = [ # Caso normal
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("23/4/2016 11:59 pm", "%d/%m/%Y %I:%M %p"), 10 ],
                    # Pasando de dia
                   [ datetime.strptime("22/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"), 240 ],
                    # Pasando de weekend a weekday
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("25/4/2016 11:59 pm", "%d/%m/%Y %I:%M %p"), 365 ],
                    # Caso normal
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("24/4/2016 01:00 am", "%d/%m/%Y %I:%M %p"), 20 ],
                    # Caso negativo
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("23/4/2016 10:00 am", "%d/%m/%Y %I:%M %p"), -1 ],
                    # Caso < 15 minutos
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("23/4/2016 11:14 pm", "%d/%m/%Y %I:%M %p"), -1 ],
                    # Caso 15 minutos
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("23/4/2016 11:15 pm", "%d/%m/%Y %I:%M %p"), 10 ],
                    # Caso > 15 minutos
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("23/4/2016 11:16 pm", "%d/%m/%Y %I:%M %p"), 10 ],
                    # Caso < 7 dias
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("30/4/2016 10:59 pm", "%d/%m/%Y %I:%M %p"), 1080 ],
                    # Caso 7 dias
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("30/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"), 1080 ],   
                    # Caso > 7 dias
                   [ datetime.strptime("23/4/2016 11:00 pm", "%d/%m/%Y %I:%M %p"),datetime.strptime("30/4/2016 11:01 pm", "%d/%m/%Y %I:%M %p"), -1 ]   
                   ]
        for tarifa in tarifas:
            for tiempo in tiempos:
                self.assertEqual(calcularPrecio(tarifa,tiempo[0], tiempo[1]), tiempo[2], "Error calculando la tarifa")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()