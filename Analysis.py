import pickle
import pandas as pd
import matplotlib.pyplot as plt

# ANALYSE RUNNER
# When trading days have been simulated (CreateSample.py), display datas for analysis.
with open('donnees.txt', 'rb') as file:
    mon_depickler = pickle.Unpickler(file)
    TradingBase = mon_depickler.load()

print(TradingBase["J-30"]["16:00:00"]/TradingBase["J-1"]["09:00:00"])

test = pd.DataFrame.from_dict(TradingBase,orient='columns')


#test.plot()
#plt.show()
