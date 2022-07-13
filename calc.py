import pandas as pd

def RSI(prices, optInTimePeriod=14):
    startIdx = 14
    endIdx = len(prices) - 1
    assert 2 <= optInTimePeriod <= 100000
    if (startIdx > endIdx):
        return pd.Series([float("nan") for rep in range(len(prices))])

    out = [float("nan") for rep in range(optInTimePeriod)]
    
    lookbackTotal = 14
    if startIdx < lookbackTotal:
        startIdx = lookbackTotal
    today = startIdx - lookbackTotal
    prevValue = prices[today]
    if False:
        savePrevValue = prevValue
        prevGain = 0
        prevLoss = 0
        for i in range(optInTimePeriod, 0, -1):
            tempValue1 = prices[today]
            today += 1
            tempValue2 = tempValue1 - prevValue
            prevValue = tempValue1
            if tempValue2 < 0:
                prevLoss -= tempValue2
            else:
                prevGain += tempValue2
                
        tempValue1 = prevLoss/optInTimePeriod
        tempValue2 = prevGain/optInTimePeriod

        tempValue1 = tempValue2 + tempValue1
        if ((tempValue1 != 0)):
            out.append(100*tempValue2/tempValue1)
        else:
            out.append(0.0)

        if today > endIdx:
            return pd.Series(out)
        today -= optInTimePeriod
        prevValue = savePrevValue

    prevGain = 0
    prevLoss = 0
    today += 1
    for i in range(optInTimePeriod, 0, -1):
        tempValue1 = prices[today]
        today += 1
        tempValue2 = tempValue1 - prevValue
        prevValue = tempValue1
        if tempValue2 < 0:
            prevLoss -= tempValue2
        else:
            prevGain += tempValue2
    prevLoss /= optInTimePeriod
    prevGain /= optInTimePeriod
    if today > startIdx:
        tempValue1 = prevGain + prevLoss
        if ((tempValue1 != 0)):
            out.append(100*prevGain/tempValue1)
        else:
            out.append(0.0)
    else:
        while today < startIdx:
            tempValue1 = prices[today]
            tempValue2 = tempValue1 - prevValue
            prevValue = tempValue1

            prevLoss *= (optInTimePeriod-1)
            prevGain *= (optInTimePeriod-1)
            if tempValue2 < 0:
                prevLoss -= tempValue2
            else:
                prevGain += tempValue2
                
            prevLoss /= optInTimePeriod
            prevGain /= optInTimePeriod
            
            today += 1
    while today <= endIdx:
        tempValue1 = prices[today]
        today += 1
        tempValue2 = tempValue1 - prevValue
        prevValue = tempValue1

        prevLoss *= (optInTimePeriod-1)
        prevGain *= (optInTimePeriod-1)
        if tempValue2 < 0:
            prevLoss -= tempValue2
        else:
            prevGain += tempValue2
            
        prevLoss /= optInTimePeriod
        prevGain /= optInTimePeriod
        tempValue1 = prevGain + prevLoss
        if (tempValue1 != 0):
            out.append(100*prevGain/tempValue1)
        else:
            out.append(0.0)
    return pd.Series(out)
        
"""def SMA(inReal, timeperiod=14):
    startIdx = timeperiod
    endIdx = len(inReal) - 1
    optInTimePeriod = timeperiod
    lookbackTotal = (optInTimePeriod-1);
    outReal = [None for rep in range(len(inReal))]
    if( startIdx < lookbackTotal ):
      startIdx = lookbackTotal;

    if( startIdx > endIdx ):
        return pd.Series(outReal)
    

    periodTotal = 0;
    trailingIdx = startIdx-lookbackTotal;

    i=trailingIdx;
    if( optInTimePeriod > 1 ):
      while( i < startIdx ):
         periodTotal += inReal[i]; i += 1
    
    outIdx = 0;
    while True:
    
      periodTotal += inReal[i]; i += 1
      tempReal = periodTotal;
      periodTotal -= inReal[trailingIdx]; trailingIdx += 1
      outReal[outIdx] = tempReal / optInTimePeriod; outIdx += 1;
      if i > endIdx:
          break

    return pd.Series(outReal)
"""

def SMA(prices, timeperiod=14):
    out = []
    for i in range(len(prices)):
        if i - timeperiod + 1 < 0:
            out.append(float("nan"))
        else:
            out.append(sum(prices[i-timeperiod+1:i+1])/timeperiod)
    return pd.Series(out)

if __name__ == "__main__":
    a=[40.44, 40.58, 40.52, 40.47, 40.23, 40.22, 40.28, 40.18, 40.3 ,
           40.28, 40.47, 40.54, 40.52, 40.7 , 40.82, 40.73, 40.67, 40.6 ,
           40.77, 41.  , 41.03, 41.03, 41.17, 41.16, 41.27, 41.37, 41.4 ,
           41.35, 41.54, 41.58, 41.39, 41.52, 41.35, 41.6 , 41.45, 41.5 ,
           41.48, 41.41, 41.66, 41.69, 41.54, 41.29, 41.46, 41.39, 41.44,
           41.5 , 41.67, 41.63, 41.92, 41.85, 42.07, 42.08, 42.22, 42.41,
           42.16, 42.24, 42.26, 41.98, 41.93, 41.73, 41.84, 41.97, 41.58,
           41.63, 41.66, 41.74, 41.48, 41.46, 41.34, 41.02, 41.06, 41.12,
           41.1 , 40.8 , 40.7 , 40.71, 40.4 , 40.48, 40.75, 40.92, 40.85,
           40.69, 40.79, 40.75, 40.92, 40.91, 41.02, 41.18, 41.21, 41.32,
           41.27, 41.21, 41.33, 41.3 , 41.37, 41.29, 41.3 , 41.32, 41.17,
           41.24, 41.4 , 41.29, 41.24, 41.13, 41.16, 41.3 , 41.2 , 41.05,
           40.93, 40.91, 41.06, 41.03, 40.98, 41.22, 41.31, 41.37, 41.68,
           41.65, 41.64, 41.68, 41.59, 41.34, 41.43, 41.61, 41.52, 41.47,
           41.59, 41.71, 41.81, 41.89, 41.76, 41.41, 41.47, 41.31, 41.33,
           41.35, 41.39, 41.71, 41.79, 41.65, 41.78, 41.86, 41.57, 41.47,
           41.48, 41.64, 41.54, 41.23, 41.32, 41.33, 41.35, 41.63, 41.34,
           41.68, 41.96, 41.89, 41.83, 41.78, 41.54, 41.57, 41.75, 41.8 ,
           41.97, 42.19, 41.97, 41.79, 41.75, 41.98, 42.02, 42.32, 42.27,
           42.47, 42.41, 42.35, 42.63, 42.88, 42.84, 42.84, 42.89, 42.83,
           42.74, 42.73, 42.67, 42.66, 42.63, 42.34, 42.42, 42.19, 42.3 ,
           42.  , 42.12, 42.25, 42.12, 42.27, 42.3 , 42.27, 42.4 , 42.57,
           42.04, 42.11, 42.18, 42.19, 42.41, 42.32, 42.73, 42.82, 43.19,
           43.16, 43.02, 43.18, 43.03, 43.13, 42.99, 43.16, 43.13, 43.2 ,
           43.04, 42.99, 43.16, 43.16, 43.01, 42.9 , 42.73, 42.83, 43.06,
           43.27, 43.09, 43.22, 43.22, 43.31, 43.32, 43.34, 43.26, 43.34,
           43.47, 43.65, 43.6 , 43.63, 43.87, 43.71, 43.64, 43.75, 43.7 ,
           43.8 , 43.69, 43.8 , 43.87, 43.66, 43.61, 43.52]
    a = pd.Series(a)
    print(RSI(a).to_list())
