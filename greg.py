import calc
import pandas as pd
from datetime import date, timedelta
import numpy as np

BUY_LIMIT = 10000
BUY_PERCENTAGE = 1

instrument_strategies = {
    0: {"strategy": "RSI", "mean": 642.2065750000056},
    1: {"strategy": "SELL", "mean": 1661.685400000004},
    2: {"strategy": "SELL", "mean": 716.1606999999913},
    3: {"strategy": "MOVAVG", "mean": 418.24525000000904},
    4: {"strategy": "MOVAVG", "mean": 204.8790500000032},
    5: {"strategy": "MOVAVG", "mean": 660.6695500000023},
    6: {"strategy": "SELL", "mean": 272.80122499999743},
    7: {"strategy": "SMA", "mean": 1374.7589999999946, "short": 20, "long": 40},
    8: {"strategy": "SELL", "mean": 480.9752500000013},
    9: None,
    10: {"strategy": "SELL", "mean": 1838.0653000000093},
    11: {"strategy": "SELL", "mean": 175.83562499999607},
    12: {"strategy": "SELL", "mean": 1221.718100000011},
    13: {"strategy": "SELL", "mean": 919.9443999999985},
    14: {"strategy": "SELL", "mean": 1392.3925499999914},
    15: {"strategy": "SELL", "mean": 510.5314249999956},
    16: {"strategy": "MOVAVG", "mean": 378.10645000000113},
    17: {"strategy": "SELL", "mean": 297.8787500000053},
    18: {"strategy": "SELL", "mean": 2474.148525000008},
    19: {"strategy": "RSI", "mean": 573.9114500000032},
    20: {"strategy": "RSI", "mean": 219.97379999999066},
    21: {"strategy": "SELL", "mean": 1070.5849499999913},
    22: {"strategy": "SELL", "mean": 958.8406000000014},
    23: {"strategy": "SMA", "mean": 575.1337750000057, "short": 40, "long": 90},
    24: {"strategy": "RSI", "mean": 941.0062749999943},
    25: {"strategy": "SELL", "mean": 1020.4821499999998},
    26: {"strategy": "SMA", "mean": 1103.1041000000005, "short": 20, "long": 50},
    27: {"strategy": "RSI", "mean": 657.2213249999986},
    28: {"strategy": "MOVAVG", "mean": 866.9937500000015},
    29: {"strategy": "SELL", "mean": 2526.662324999983},
    30: {"strategy": "RSI", "mean": 404.9219000000048},
    31: {"strategy": "SELL", "mean": 429.02712499999143},
    32: {"strategy": "SELL", "mean": 1679.0680249999987},
    33: {"strategy": "SELL", "mean": 2848.4683750000004},
    34: {"strategy": "SELL", "mean": 3232.2757999999976},
    35: {"strategy": "MOVAVG", "mean": 377.5446250000041},
    36: {"strategy": "SELL", "mean": 2515.595249999991},
    37: {"strategy": "SMA", "mean": 69.15235000000757, "short": 10, "long": 40},
    38: None,
    39: {"strategy": "SELL", "mean": 269.89667499999814},
    40: {"strategy": "SELL", "mean": 2389.929499999993},
    41: {"strategy": "MOVAVG", "mean": 718.9660249999906},
    42: {"strategy": "SMA", "mean": 1222.6584500000063, "short": 10, "long": 30},
    43: {"strategy": "SELL", "mean": 129.77294999999867},
    44: {"strategy": "SELL", "mean": 2539.2798999999904},
    45: {"strategy": "RSI", "mean": 1219.6205499999978},
    46: {"strategy": "RSI", "mean": 2763.142574999998},
    47: {"strategy": "SELL", "mean": 1993.5557750000098},
    48: {"strategy": "SELL", "mean": 517.0267750000003},
    49: {"strategy": "SELL", "mean": 952.6667750000051},
    50: {"strategy": "MOVAVG", "mean": 1218.7889499999856},
    51: {"strategy": "SELL", "mean": 1999.071249999999},
    52: {"strategy": "SELL", "mean": 3155.7141749999973},
    53: {"strategy": "RSI", "mean": 13.294450000003053},
    54: {"strategy": "SELL", "mean": 1185.54770000001},
    55: None,
    56: {"strategy": "RSI", "mean": 332.80817500000194},
    57: {"strategy": "SELL", "mean": 896.8366250000054},
    58: {"strategy": "SELL", "mean": 575.9714250000015},
    59: {"strategy": "RSI", "mean": 178.043700000002},
    60: {"strategy": "SELL", "mean": 2512.3964249999954},
    61: {"strategy": "MOVAVG", "mean": 393.6413750000065},
    62: {"strategy": "SELL", "mean": 2020.0109249999896},
    63: {"strategy": "SMA", "mean": 1110.8986750000022, "short": 10, "long": 150},
    64: {"strategy": "MOVAVG", "mean": 295.40777499998876},
    65: {"strategy": "MOVAVG", "mean": 1150.0067249999938},
    66: {"strategy": "SELL", "mean": 171.68047499999375},
    67: {"strategy": "SMA", "mean": 122.2712500000016, "short": 10, "long": 140},
    68: {"strategy": "SELL", "mean": 805.6002499999922},
    69: {"strategy": "SELL", "mean": 875.090325000001},
    70: {"strategy": "SELL", "mean": 819.4765999999945},
    71: {"strategy": "SMA", "mean": 1490.45615, "short": 20, "long": 60},
    72: {"strategy": "SELL", "mean": 1113.8353999999945},
    73: {"strategy": "SELL", "mean": 2075.257999999987},
    74: {"strategy": "SELL", "mean": 1675.849900000003},
    75: {"strategy": "MOVAVG", "mean": 170.8750999999902},
    76: {"strategy": "SELL", "mean": 391.4915749999982},
    77: {"strategy": "SMA", "mean": 446.1295000000009, "short": 10, "long": 200},
    78: None,
    79: {"strategy": "MOVAVG", "mean": 717.3465999999971},
    80: {"strategy": "SELL", "mean": 1004.6924749999816},
    81: {"strategy": "MOVAVG", "mean": 364.6591000000026},
    82: {"strategy": "SELL", "mean": 511.9321499999951},
    83: {"strategy": "SELL", "mean": 128.15102500000648},
    84: {"strategy": "SELL", "mean": 531.8912500000024},
    85: {"strategy": "SMA", "mean": 853.6199499999966, "short": 40, "long": 80},
    86: {"strategy": "SMA", "mean": 1409.4003000000012, "short": 30, "long": 140},
    87: {"strategy": "SMA", "mean": 1613.6965499999933, "short": 20, "long": 40},
    88: {"strategy": "RSI", "mean": 449.29347500000404},
    89: {"strategy": "SELL", "mean": 2502.8341250000067},
    90: {"strategy": "SMA", "mean": 402.6643249999943, "short": 10, "long": 160},
    91: {"strategy": "SELL", "mean": 284.77850000000217},
    92: {"strategy": "SELL", "mean": 278.5541250000024},
    93: {"strategy": "SELL", "mean": 804.5842500000163},
    94: {"strategy": "SMA", "mean": 646.2218500000017, "short": 10, "long": 40},
    95: {"strategy": "SELL", "mean": 202.36127499999384},
    96: {"strategy": "SELL", "mean": 226.86134999999558},
    97: {"strategy": "SELL", "mean": 1230.001350000004},
    98: {"strategy": "RSI", "mean": 481.6512500000008},
    99: {"strategy": "MOVAVG", "mean": 996.5819499999943},
}


def spikeySignal(strategy, instPrc):
    return +1
    if len(instPrc) < 10:
        return 0
    
    THESHOLD = 0.4
    """if instPrc[-1] - instPrc[-2] > THESHOLD:
        return 1
    elif instPrc[-1] - instPrc[-2] < -THESHOLD:
        return -1"""
    if instPrc[-1] == instPrc[-5:].max():
        return 1
    elif instPrc[-1] == instPrc[-5:].min():
        return -1

def RSISignal(strategy, instPrc):
    prices = pd.Series(instPrc)
    inst1_rsi = calc.RSI(prices)

    signal = inst1_rsi.copy()
    signal[inst1_rsi.isnull()] = 0

    signal[inst1_rsi < 30] = 1
    signal[inst1_rsi > 70] = -1
    signal[(inst1_rsi <= 70) & (inst1_rsi >= 30)] = 0
    
    return signal.iloc[-1]

def SMASignal(strategy, instPrc):
    short_period = strategy["short"]
    long_period = strategy["long"]
    prices = pd.Series(instPrc)
    SMA_short = calc.SMA(prices, timeperiod=short_period)
    SMA_long = calc.SMA(prices, timeperiod=long_period)

    signal = SMA_long.copy()
    signal[SMA_long.isnull()] = 0
    signal[SMA_short > SMA_long] = 1
    signal[SMA_short < SMA_long] = -1

    return signal.iloc[-1]

def sellSignal(strategy, instPrc):
    return -1

def movAvgSignal(strategy, instPrc):
    k = 4 
    l = 40
    day = len(instPrc)
    if day < l:
        return 0
    elif day == l: 
        return +1
    else:
        wmaK = sum([instPrc[k - i] * (k - i + 1) for i in range(1,k + 1)]) / sum(range(1,k + 1))
        movAvgL = sum(instPrc[-l - 1:-1])/l
        if wmaK == movAvgL:
            return 0
        elif wmaK > movAvgL:
            return +1
        elif wmaK < movAvgL:
            return -1

currentPos = np.zeros(100)

def getMyPosition(prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape
    
    for inst in range(100):
        strategy = instrument_strategies[inst]
        if strategy == None:
            # No optimal strategy found, don"t change current position
            continue

        instPrc = prcSoFar[inst]
        if strategy["strategy"] == "RSI":
            signal = RSISignal(strategy, instPrc)
            if currentPos[inst] == 0 and signal == 1:
                # Buy
                currentPos[inst] = int(BUY_LIMIT * BUY_PERCENTAGE / instPrc[-1])
            elif currentPos[inst] == 0 and signal == -1:
                # Sell all
                currentPos[inst] = 0
                
        elif strategy["strategy"] == "SMA":
            signal = SMASignal(strategy, instPrc)
            if currentPos[inst] == 0 and signal == 1:
                currentPos[inst] = int(BUY_LIMIT * BUY_PERCENTAGE / instPrc[-1])
            elif currentPos[inst] == 0 and signal == -1:
                currentPos[inst] = -int(BUY_LIMIT * BUY_PERCENTAGE / instPrc[-1])
                
        elif strategy["strategy"] == "MOVAVG":
            signal = movAvgSignal(strategy, instPrc)
            currentPos[inst] += signal * 100
            
        elif strategy["strategy"] == "SELL":
            signal = sellSignal(strategy, instPrc)
            if signal == +1:
                currentPos[inst] = +1000000000
            elif signal == -1:
                currentPos[inst] = -1000000000
        elif strategy["strategy"] == "SPIKEY":
            signal = spikeySignal(strategy, instPrc)
            if signal == +1:
                currentPos[inst] = +1000000000
            elif signal == -1:
                currentPos[inst] = -1000000000
                
    return currentPos
    
