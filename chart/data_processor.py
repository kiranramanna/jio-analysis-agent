import csv
import os
from datetime import datetime
import swisseph as swe
import collections
import sys

from .kundali_sidereal_chart import KundaliSiderealChart
from .Swiss_eph_constants import *
from .utils import GetHourStrToDecimal, getRashiNum, prnt, decdeg2dms, hrtodec, getHouse, getDegreeStr

def process_line(row):
    eachChart = KundaliSiderealChart()
    eachChart.ReadingSetup([row['number'], row['prsName'], row['dobStr']+" "+row['dobTz']])
    eachChart.Setup_eph(float(row['latitude']), float(row['longitude']))
    dob = row['dobStr'].split(" ")
    dob_date = dob[0].split("-")
    dob_time = dob[1]
    dob_tz = row['dobTz']
    eachChart.getJulByTimeDec(int(dob_date[0]), int(dob_date[1]), int(dob_date[2]), dob_time, dob_tz)
    eachChart.CaclHouses()
    eachChart.CalcPlanets()
    eachChart.getASC()
    eachChart.caclRashi()
    
    pandasRow = {}
    pandasRow["number"] = row['number']
    pandasRow["prsName"] = row['prsName']
    pandasRow["dob"] = row['dobStr'] + " " + row['dobTz']
    pandasRow["place"] = row['place']
    pandasRow["latitude"] = row['latitude']
    pandasRow["longitude"] = row['longitude']
    pandasRow["lordsToBhavaMap"] = {}
    for x in eachChart.Grahas:
        eachGraha = eachChart.Grahas[x]
        if eachGraha["lordOf"] != "":
            pandasRow["lordsToBhavaMap"][eachGraha["name"]] = eachGraha["lordOf"]
    
    for eachKey in Rashi_pandas_list.keys():
        eachRashiNumColumn = Rashi_pandas_list[eachKey]
        pandasRow[eachRashiNumColumn] = ''
        if eachKey in eachChart.Rashis.keys():
            pandasRow[eachRashiNumColumn] = {}
            pandasRow[eachRashiNumColumn]["rashi"] = Num_To_Zodiac_sign.get(eachKey)
            pandasRow[eachRashiNumColumn]["grahas"] = eachChart.Rashis[eachKey]
    return pandasRow

def readFromCsv(filepath, pandasOutFile, pandasRowHeader):
    # Assuming GetAyanamsa is part of KundaliSiderealChart or moved to utils
    # For now, we'll skip calling it here if it's not a standalone function
    writeToCsv(pandasOutFile, pandasRowHeader, 'w') # set header
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pandasRow = process_line(row)
            writeToCsv(pandasOutFile, list(pandasRow.values()), 'a')

def writeToCsv(filepath, dataArr, type):
    with open(filepath, type, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(dataArr)
