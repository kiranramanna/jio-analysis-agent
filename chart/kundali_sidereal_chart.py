import time
from datetime import datetime, timedelta
import swisseph as swe
import collections

import os
import sys



# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from .Swiss_eph_constants import *
from .utils import decdeg2dms, hrtodec, getRashiNum, getDegreeStr, prnt, getHouse, GetHourStrToDecimal

# swe.set_ephe_path('/usr/share/ephe') # set path to ephemeris files

# Jul 14 run : 2023-07-14 23:56:51.515288 - Time taken:  56 seconds
# 2023-09-21 00:33:02.723189 - Time taken:  68.63500595092773

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class Graha(BaseModel):
    name_of_graha: str
    degree: str
    degree_in_decimal: float
    desposited_in_bhava: str
    desposited_in_rashi: str
    lord_of_bhavas: List[str]
    desposited_in_nakshatra: str

class Rashi(BaseModel):
    rashi: str
    grahas: List[Graha]

class ChartInputData(BaseModel):
    number: str
    prsName: str
    dob: str
    dob_tz: str
    place: str
    latitude: float
    longitude: float

class KundaliSiderealChart(object):
    
    def __init__(self, kundali_obj: ChartInputData):
        self.HousePosList = []
        self.Bday_accurate = 0
        self.lat = kundali_obj.latitude
        self.lon = kundali_obj.longitude
        self.HouseDict = collections.OrderedDict()
        self.RashiToHouseMap = {}
        self.Grahas = {}
        self.Rashis = {}
        self.lagnaDec = 0
        swe.set_ephe_path(os.path.dirname(os.path.abspath(__file__))+"/jhcore/ephe") # set path to ephemeris files
        # swe.set_sid_mode(AYANAMSHA_RAMAN)
        swe.set_sid_mode(AYANAMSHA_LAHIRI)
        # swe.set_sid_mode(AYANAMSHA_TRUE_PUSHYA)
        
        # Add Vimshottari Dasha periods for each planet
        self.vimshottari_periods = {
            "KE": 7,   # Ketu
            "SK": 20,  # Venus
            "SY": 6,   # Sun
            "CH": 10,  # Moon
            "MA": 7,   # Mars
            "RA": 18,  # Rahu
            "GU": 16,  # Jupiter
            "SA": 19,  # Saturn
            "BU": 17   # Mercury
        }
        
        # Define the order of Mahadashas
        self.dasha_order = ["KE", "SK", "SY", "CH", "MA", "RA", "GU", "SA", "BU"]

        # Perform chart calculations
        self.Setup_eph(self.lat, self.lon)
        dob = kundali_obj.dob.split(" ")
        dob_date = dob[0].split("/") # mm/dd/yyyy
        dob_time = dob[1]
        dob_tz = kundali_obj.dob_tz
        self.getJulByTimeDec(int(dob_date[2]), int(dob_date[0]), int(dob_date[1]), dob_time, dob_tz)

        self.GetAyanamsa()
        self.CaclHouses()
        self.CalcPlanets()
        self.getASC()
        self.caclRashi()
        
        # Calculate Vimshottari Dashas
        birth_date = datetime.strptime(kundali_obj.dob, '%m/%d/%Y %H:%M:%S')
        moon_nakshatra = self.Grahas["CH"].desposited_in_nakshatra
        moon_degree = self.Grahas["CH"].degree_in_decimal
        
        self.mahadashas = self.calculate_vimshottari_dashas(birth_date, moon_nakshatra, moon_degree)
        
    def to_dict(self):
        # Convert all attributes to dictionary format
        return {
            "HousePosList": self.HousePosList,
            "Bday_accurate": self.Bday_accurate,
            "lat": self.lat,
            "lon": self.lon,
            "HouseDict": dict(self.HouseDict),  # Convert OrderedDict to a regular dictionary
            "RashiToHouseMap": self.RashiToHouseMap,
            "Grahas": {k: v.model_dump() for k, v in self.Grahas.items()},
            "Rashis": {k: v.model_dump() for k, v in self.Rashis.items()},
            "lagnaDec": self.lagnaDec,
            "mahadashas": self.mahadashas
        }

    

    def Setup_eph(self, lat, long):
        self.lat = lat
        self.lon = long
        swe.set_topo(lat,long)

    
   
    

    
    
    
        
    

    

    def CaclHouses(self):
        # Vehlow = V - scroll down from :  https://www.astro.com/swisseph/swephprg.htm#_Toc112949026
        # house_loc = swe.houses_ex2(self.Bday_accurate, self.lat, self.lon, str.encode('V'), FLG_SIDEREAL)
        house_loc = swe.houses_ex2(self.Bday_accurate, self.lat, self.lon, str.encode('V'), FLG_SIDEREAL)
        Cusps = house_loc[0]
        Asc = house_loc[1]
        # print("Asc ", Asc)
        self.lagnaDec = Asc[0]
        for j in House_list:
            self.HouseDict[Cusps[j - 1]] = str(j)
            self.RashiToHouseMap[Zodiac_sign[getRashiNum(Cusps[j - 1])]] = str(j)
        self.HousePosList = sorted(self.HouseDict.keys())
        # firstkey= self.HousePosList[0]
        # self.HousePosList.insert(0,firstkey)
        self.HousePosList.insert(13, 360)
        self.HouseDict = self.HouseDict
        # print("self.HouseDict", self.HouseDict)
        # print("self.HousePosList", self.HousePosList)
        # print("self.RashiToHouseMap", self.RashiToHouseMap)
    

    def getASC(self):
        self.Grahas["LG"] = self.createGrahaJson("LG", "")

    def createGrahaJson(self, planet, planetPosition):
        graha_degree = 0
        lordOf = []
        if planet in ["KE", "LG"]:
            if planet == "LG":
                graha_degree = self.lagnaDec
            elif planet == "KE":
                # print(self.Grahas)
                graha_degree =  round((self.Grahas["RA"].degree_in_decimal + 180) % 360, 5)
            name = planet
        else:            
            graha_degree = planetPosition[0][0]
            name = Planet_List[planet]
        house = self.HouseDict[getHouse(self.HousePosList, graha_degree)]
        rashi = Zodiac_sign[getRashiNum(graha_degree)]
        # print(f"{planetPosition}")
        # print(f"{name} {graha_degree} {house} {rashi}")
        if(planet == "KE"):
            ke_house_calc = (int(self.Grahas["RA"].desposited_in_bhava) + 6) %12
            if( ke_house_calc != int(house) and ke_house_calc+12 != int(house)):
                print(f"{self.details[0]} -- {(int(self.Grahas['RA'].desposited_in_bhava) + 6) %12} -- Error: RA -{self.Grahas['RA'].desposited_in_bhava}-{self.Grahas['RA'].degree_in_decimal} and KE-{house}-{graha_degree} are not in opposite houses")
                
        # lamda function to get the lord of bhava per rashi for given planet using Lord_of_rashi and RashiToHouseMap
        if planet != "LG":
            [lordOf.append(self.RashiToHouseMap[x]) for x in Lord_of_rashi[name]]
            # [print(x) for x in Lord_of_rashi[name]]
        
        # calculate nakshatra
        nakshatra = ""
        nakshatra_degree = graha_degree % 13.33
        nakshatra_index = int(graha_degree / 13.33333333)
        nakshatra = nakshatras_first_3_letters[nakshatra_index]
        return Graha(
                name_of_graha=Planet_shortcut_to_name[name],
                degree=getDegreeStr(graha_degree),
                degree_in_decimal=graha_degree,
                desposited_in_bhava=house,
                desposited_in_rashi=rashi,
                lord_of_bhavas=lordOf,
                desposited_in_nakshatra=nakshatra_abbr_to_full[nakshatra]
            )

    def CalcPlanets(self):
        for i in Planet_List_loop:
            # response xx = array of 6 doubles for longitude, latitude, distance, speed in long., speed in lat., and speed in dist.
            # print("self.Bday_accurate:", self.Bday_accurate)
            # print("i:", i)
            # print("FLG_SIDEREAL:", FLG_SIDEREAL)
            # print("FLG_SWIEPH:", FLG_SWIEPH)
            planet_pos = swe.calc(self.Bday_accurate, i, FLG_SIDEREAL + FLG_SWIEPH)
            self.Grahas[Planet_List[i]] = self.createGrahaJson(i, planet_pos)

        # keDec =  round((Grahas["RA"]["degree_in_decimal"] + 180) % 360, 5)
        self.Grahas["KE"] = self.createGrahaJson("KE", "")
        
    
    
    def caclRashi(self):
        Rashis = {rashi_name: [] for rashi_name in Rashi_shortcut_to_name.values()}
        Grahas = self.Grahas
        for key in Grahas:
            thisRashi = Rashi_shortcut_to_name[Grahas[key].desposited_in_rashi]
            Rashis[thisRashi].append(Grahas[key])
        
        self.Rashis = {rashi_name: Rashi(rashi=rashi_name, grahas=grahas_list) for rashi_name, grahas_list in Rashis.items()}

    def GetAyanamsa(self):
        ayan = swe.get_ayanamsa_ut(self.Bday_accurate)
        print("Ayanamsa = ", prnt(decdeg2dms(ayan)))


    
        
    

    def DateTime(self,year,month,date,hr,min,sec,tz):
        time = hrtodec(hr,min,sec)
        if tz is not None:
            tzDec = GetHourStrToDecimal(tz)
            time = time - tzDec
        self.Bday_accurate = swe.julday(year,month,date,time,GREG_CAL)
        
    def getJulByTimeDec(self,year,month,date,time,tz):
        timeDec = GetHourStrToDecimal(time)
        if tz is not None:
            tzDec = GetHourStrToDecimal(tz)
            timeDec = timeDec - tzDec
        self.Bday_accurate = swe.julday(year,month,date,timeDec,GREG_CAL)

    def calculate_vimshottari_dashas(self, birth_date, moon_nakshatra, moon_degree):
        """Calculate Vimshottari Dashas for 120 years from birth."""
        # Convert birth_date string to datetime object if it's not already
        if isinstance(birth_date, str):
            birth_date = datetime.strptime(birth_date, '%m/%d/%Y %H:%M:%S')
            
        # Get the lord of birth nakshatra
        birth_lord = nakshatra_lords[moon_nakshatra]
        
        # Calculate consumed degree in nakshatra (each nakshatra is 13°20' or 13.3333... degrees)
        nakshatra_span = 13 + 1/3  # 13°20' in decimal
        consumed_degree = moon_degree % nakshatra_span
        consumed_ratio = consumed_degree / nakshatra_span
        
        # Find starting lord index
        start_index = self.dasha_order.index(birth_lord)
        
        # Calculate remaining period of first dasha
        first_period_total = self.vimshottari_periods[birth_lord]
        first_period_remaining = first_period_total * (1 - consumed_ratio)
        
        mahadashas = []
        current_date = birth_date
        
        # Add first partial dasha
        end_date = current_date + timedelta(days=first_period_remaining * 365.2564)
        mahadashas.append({
            "planet": birth_lord,
            "start_date": current_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d'),
            "duration": first_period_remaining
        })
        current_date = end_date
        
        # Calculate remaining dashas
        years_calculated = first_period_remaining
        current_index = (start_index + 1) % 9
        
        while years_calculated < 120:
            planet = self.dasha_order[current_index]
            period = self.vimshottari_periods[planet]
            
            # Adjust period if it would exceed 120 years
            if years_calculated + period > 120:
                period = 120 - years_calculated
            
            end_date = current_date + timedelta(days=period * 365.25)
            mahadashas.append({
                "planet": planet,
                "start_date": current_date.strftime('%Y-%m-%d'),
                "end_date": end_date.strftime('%Y-%m-%d'),
                "duration": period
            })
            
            current_date = end_date
            years_calculated += period
            current_index = (current_index + 1) % 9
        
        return mahadashas

    

    
            
    




