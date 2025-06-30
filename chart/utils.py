from .Swiss_eph_constants import *

def decdeg2dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   return (int(degrees),int(minutes),round(seconds, 3))

def hrtodec(hr, min, sec):
    return(hr + (min/60) + (sec/3600))

def getRashiNum(degree):
    return(int(degree/30))

def prnt(var):
    return(str(var[0])+'.'+str(var[1])+"."+str(var[2]))

def getDegreeStr(degree):
    return str(getRashiNum(degree)+1)+'.'+prnt(decdeg2dms((degree % 30)))

def getHouse(HousePosList, PlanetDegree):
    if PlanetDegree<HousePosList[0]:
        # return last index
        return HousePosList[len(HousePosList)-2]

    for a in range(1,14):
         if PlanetDegree<=HousePosList[a]:
             return HousePosList[a-1]
             break

def GetHourStrToDecimal(hour):
    hr = hour.split(":")
    hr_dec = float(hr[0])
    if len(hr) > 1:
        hr_dec += (float(hr[1]) / 60.0)
    if len(hr) > 2:
        hr_dec += (float(hr[2]) / 3600.0)
    return hr_dec