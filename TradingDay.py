from Time import *
import random as rd
import time
import pandas

class TradingDay:

    NbTradingDays = 0

    def __init__(self,Forex_Name = "EURSUD" , Forex = 1.2851 , Day_BEG = Time(9,0,0) , Day_END= Time(16,0,0), step = 1, speed = 0):

        # Attributs immuable
        self.beg = Day_BEG
        self.end = Day_END
        self.fxinit = Forex
        self.fxname = Forex_Name
        self.step = step
        self.nb = int(self.NbTradingDays) + 1
        TradingDay.NbTradingDays += 1
        self.speed = speed

        # Attrubuts muable
        self.current = Time(self.beg.hour, self.beg.minute, self.beg.seconde)
        self.fx = Forex
        self.fin = False
        self.historic = {str(self.beg):self.fxinit}

    def reset(self):
        self.current = self.beg
        self.fin = False
        self.fx = self.fxinit
        self.historic = {str(self.beg):self.fxinit}

    def __str__(self):
        if self.fin:
            var = round((self.fx/self.fxinit -1) *100,3)
            return """FIN DE SEANCE
il est {} et le cours {} est de {}
Performance de la journée: {} % """.format(self.current ,self.fxname ,self.fx, var)
        else:
            return "il est {} et le cours {} est de {}".format(self.current , self.fxname, self.fx)

    def next(self):

        #Parametres for initiation
        Tip =0.0001
        if (self.current+self.step) >= self.end:
            self.current = Time(self.end.hour, self.end.minute, self.end.seconde)
            self.fin = True
        else:
            self.current += self.step
            self.fx = min(1.2*self.fxinit,max( round(self.fx + Tip*rd.randrange(-2,3),4), 0.8*self.fxinit) )

        self.historic[str(Time(self.current.hour, self.current.minute, self.current.seconde))] = self.fx


    def run(self):
        while (not self.fin):
            time.sleep(self.speed)
            self.next()
        return self


