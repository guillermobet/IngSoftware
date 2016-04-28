#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de abr. de 2016
@author:    Guillermo Betancourt    carnet 11-10103
            Gabriel Gimenez         carnet 12-11006
'''
from datetime import *
from decimal import *
from copy import deepcopy

class Tarifa(object):
    weekday = 0
    weekend = 0

    def __init__(self, wd, we):
        self.weekday = wd
        self.weekend = we
        
def calcularPrecio(tarifa, tiempoInicial, tiempoFinal):
    tmp = tiempoFinal - tiempoInicial
    if tmp.days < 0:
        print("\nError, la fecha de inicial es mayor que la fecha final")
        return -1
    
    if (tmp.seconds < 15 * 60  and tmp.days == 0) or (tmp.days >= 7 and tmp.seconds > 0):
        print ("\nError, el tiempo debe estar entre 15 minutos y 7 días")
        return -1

    precioTotal = Decimal(0)
    iterator = deepcopy(tiempoInicial)
    prevHour = deepcopy(iterator)
    
    while iterator < tiempoFinal:
        iterator += timedelta(seconds = 3600)
        if isWeekend(iterator) == isWeekend(prevHour):
            if isWeekend(iterator):
                precioTotal += tarifa.weekend
            else:
                precioTotal += tarifa.weekday
            prevHour += timedelta(seconds = 3600)
        else:
            if isWeekend(prevHour):
                precioTotal += tarifa.weekend
            else:
                precioTotal += tarifa.weekday
            prevHour += timedelta(seconds = 3600)
            iterator = iterator.replace(hour = 0, minute = 0)
            prevHour = prevHour.replace(hour = 0, minute = 0)
    
    return precioTotal

def isWeekend(datetime):
    return datetime.weekday() > 4
    
def inputInsert():
    try:
        inicioDeTrabajo = datetime.strptime(input("\nInserte la fecha inicial (dd/mm/aaaa hh:mm am|pm): "), "%d/%m/%Y %I:%M %p")
        finDeTrabajo = datetime.strptime(input("Inserte la fecha final (dd/mm/aaaa hh:mm am|pm): "), '%d/%m/%Y %I:%M %p')
    except ValueError:
        print("\nError al ingresar las fechas")
        exit(1)

    return [inicioDeTrabajo, finDeTrabajo]

def tarifas():
    try:
        wd = Decimal(input("\nInserte la tarifa de los días de semana: "))
        we = Decimal(input("Inserte la tarifa de los fines de semana: "))
        if (wd < 0 or we < 0):
            raise ValueError
    except:
        print("\nError al ingresar las tarifas")
        exit(1);
    return [wd,we]

if __name__ == '__main__':
    getcontext().prec = 5
    precios = tarifas()
    t = Tarifa(precios[0],precios[1])
    tiempoDeTrabajo = inputInsert()
    precioTotal = calcularPrecio(t, tiempoDeTrabajo[0], tiempoDeTrabajo[1])
    print("____________________________")
    print("\nTarifa en día de semana: " + str(t.weekday) + " BsF/hora")
    print("Tarifa en fin de semana: " + str(t.weekend) + " BsF/hora")
    print("\nFecha de inicio: " + str(tiempoDeTrabajo[0]))
    print("Fecha de fin: " + str(tiempoDeTrabajo[1]))
    print("\nPrecio a pagar: " + str(precioTotal) + " BsF\n")
    exit(0)