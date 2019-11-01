from TradingDay import *
import pickle

# RUNNER FILE !
TradingBase= {}
fofo = 1.2851

# === Simulate 30 days of trading on the Forex and store it in 'donnees'

for i in range( 1,31):
    Tday = TradingDay(Forex = fofo).run()
    fofo = Tday.fx
    TradingBase["J-"+str(i)] = Tday.historic
with open('donnees.txt', "wb") as fiche:
    mon_pickler = pickle.Pickler(fiche)
    mon_pickler.dump(TradingBase)

with open('donnees.txt', 'rb') as file:
    mon_depickler = pickle.Unpickler(file)
    TradingBase = mon_depickler.load()

