# Trading Day Simulator  

__*Small project : June 2017*__  

## Introduction  
Short piece of code to simulate a trading day. I did this code to illustrate something learned durign a lecture about Black & Scholes and Brownian movements : The random step.  

This little project can also turn into a future tranding bot simulator or simulate a market to make an invest challenge for the ICN finance's club.

**TradingDay** : The market simulator. It is used to simulate forex market but parameters allow us to simulate other kind of markets. Also, Trading Days are independents, link between each others is done when using this class into an higher-level application.  
<br>  

**Time** : Own implementation of the Time class. Reduced to the minimum needed for TradingDay. Trading Day use it as a service.  
<br>  

**CreateSample** : Runner of this application. Create 30 trading days, and store datas into donnees.txt to let us analyse those datas.  
<br>  

**Analysis** : Only display the 30 trading days for the moment. It uses donnees.txt to provide analysis of trading days simulated.  
