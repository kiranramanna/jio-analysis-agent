FLG_TOPOCTR = 32768
FLG_SPEED = 256
FLG_SWIEPH =2
FLG_SIDEREAL = 65536
GREG_CAL= 1
JULIAN_CAL=0
AYANAMSHA_LAHIRI = 1 # # SE_SIDM_LAHIRI = 1 # https://www.astro.com/swisseph/swephprg.htm#_Toc112949017
AYANAMSHA_RAMAN = 3 # # SE_SIDM_RAMAN = 1 # https://www.astro.com/swisseph/swephprg.htm#_Toc112949017
AYANAMSHA_TRUE_PUSHYA = 3 # # SE_SIDM_TRUE_PUSHYA = 29 # https://www.astro.com/swisseph/swephprg.htm#_Toc112949017

ARIES = "Ari"
TAURUS = "Tau"
GEMINI = "Gem"
CANCER = "Can"
LEO = "Leo"
VIRGO = "Vir"
LIBRA = "Lib"
SCORPIO = "Sco"
SAGITTARIUS = "Sag"
CAPRICORN = "Cap"
AQUARIUS = "Aqu"
PISCES = "Pis"

SURYA_SYM = "☉"
CHANDRA_SYM = "☽"
MANGAL_SYM = "♂"
BUDHA_SYM = "☿"
GURU_SYM = "♃"
SHUKRA_SYM = "♀"
SHANI_SYM = "♄"
RAHU_SYM = "☊"
KETU_SYM = "☋"
URANUS_SYM = "♅"
NEPTUNE_SYM = "♆"
PLUTO_SYM = "♇"

SURYA_NAME = "SY"
CHANDRA_NAME = "CH"
MANGAL_NAME = "MA"
BUDHA_NAME = "BU"
GURU_NAME = "GU"
SHUKRA_NAME = "SK"
SHANI_NAME = "SA"
RAHU_NAME = "RA"
KETU_NAME = "KE"
LAGNA_NAME = "LG"
URANUS_NAME = "URAN"
NEPTUNE_NAME = "NEPT"
PLUTO_NAME = "PLUT"



# graha_cols_new = ['SY', 'CH', 'BU', 'SK', 'MA', 'GU', 'SA', "SW", "SM", "TE", 'RA', 'KE', 'LG']



Zodiac_sign= {0:ARIES, 1:TAURUS, 2:GEMINI, 3:CANCER, 4:LEO, 5:VIRGO, 6:LIBRA, 7:SCORPIO, 8:SAGITTARIUS, 9:CAPRICORN, 10:AQUARIUS, 11:PISCES}
Num_To_Zodiac_sign= {ARIES:1, TAURUS:2, GEMINI:3, CANCER:4, LEO:5, VIRGO:6, LIBRA:7, SCORPIO:8, SAGITTARIUS:9, CAPRICORN:10, AQUARIUS:11, PISCES:12}

# Planet_List = {0:"SU", 1:"MO", 2:"ME", 3:"VE", 4:"MA", 5:"JU", 6:"SA",7:"URAN", 8:"NEPT", 9:"PLUT", 10:"RA"}
Planet_List = {0:SURYA_NAME, 1:CHANDRA_NAME, 2:BUDHA_NAME, 3:SHUKRA_NAME, 4:MANGAL_NAME, 5:GURU_NAME, 6:SHANI_NAME,7:URANUS_NAME, 8:NEPTUNE_NAME, 9:PLUTO_NAME, 10:RAHU_NAME}

House_list= [1,2,3,4,5,6,7,8,9,10,11,12]
#Planet_List_loop = [0,1,2,3,4,5,6,7,8,9,11]
Planet_List_loop = [0,1,2,3,4,5,6,10]
# Planet_Loop = ["SU","MO","ME","VE","MA","JU","SA","RA"]
Planet_Loop = [SURYA_NAME,CHANDRA_NAME,BUDHA_NAME,SHUKRA_NAME,MANGAL_NAME,GURU_NAME,SHANI_NAME,RAHU_NAME]

# Planet_Loop_ws = {"SU":"2","MO":"3","ME":"4","VE":"5","MA":"6","JU":"7","SA":"8","RA":"9"}
Planet_Loop_ws = {SURYA_NAME:"2",CHANDRA_NAME:"3",BUDHA_NAME:"4",SHUKRA_NAME:"5",MANGAL_NAME:"6",GURU_NAME:"7",SHANI_NAME:"8",RAHU_NAME:"9"}

Rashi_shortcut_to_name = {ARIES:"Mesha", TAURUS:"Vrishabha", GEMINI:"Mithuna", CANCER:"Karka", LEO:"Simha", VIRGO:"Kanya", LIBRA:"Tula", SCORPIO:"Vrishchika", SAGITTARIUS:"Dhanu", CAPRICORN:"Makara", AQUARIUS:"Kumbha", PISCES:"Meena"}
Planet_shortcut_to_name = {SURYA_NAME:"Surya", CHANDRA_NAME:"Chandra", BUDHA_NAME:"Budha", SHUKRA_NAME:"Shukra", MANGAL_NAME:"Mangal", GURU_NAME:"Guru", SHANI_NAME:"Shani", RAHU_NAME:"Rahu", KETU_NAME:"Ketu", LAGNA_NAME:"Lagna"}
# Lord_of_rashi = {
#    "SU": ["Leo"],
#    "MO": ["Can"],
#    "ME": ["Gem", "Vir"],
#    "VE": ["Lib", "Tau"],
#    "MA": ["Ari", "Sco"],
#    "JU": ["Sag", "Pis"],
#    "SA": ["Cap", "Aqu"],
#    "RA": ["Aqu"],
#    "KE": ["Sco"],
# }

Lord_of_rashi = { SURYA_NAME: [LEO], CHANDRA_NAME: [CANCER], BUDHA_NAME: [GEMINI, VIRGO], SHUKRA_NAME: [LIBRA, TAURUS], MANGAL_NAME: [ARIES, SCORPIO], GURU_NAME: [SAGITTARIUS, PISCES], SHANI_NAME: [CAPRICORN, AQUARIUS], RAHU_NAME: [AQUARIUS], KETU_NAME: [SCORPIO]}

Rashi_pandas_list = {ARIES:"rashi01", TAURUS:"rashi02", GEMINI:"rashi03", CANCER:"rashi04", LEO:"rashi05", VIRGO:"rashi06", LIBRA:"rashi07", SCORPIO:"rashi08", SAGITTARIUS:"rashi09", CAPRICORN:"rashi10", AQUARIUS:"rashi11", PISCES:"rashi12"}

nakshatras_first_3_letters = ["Ash", "Bar", "Kri", "Roh", "Mrig", "Ard", "Pun", "Push", "Ashl", "Mag", "PuP", "UtP", "Has", "Chit", "Swat", "Vis", "Anu", "Jye", "Mul", "PuA", "UtA", "Shra", "Dha", "Sha", "PuB", "UtB", "Rev"]

# Nakshatra abbreviations to full names mapping
nakshatra_abbr_to_full = {
    "Ash": "Ashwini",
    "Bar": "Bharani",
    "Kri": "Krittika",
    "Roh": "Rohini",
    "Mrig": "Mrigashira",
    "Ard": "Ardra",
    "Pun": "Punarvasu",
    "Push": "Pushya",
    "Ashl": "Ashlesha",
    "Mag": "Magha",
    "PuP": "Purva Phalguni",
    "UtP": "Uttara Phalguni",
    "Has": "Hasta",
    "Chit": "Chitra",
    "Swat": "Swati",
    "Vis": "Vishakha",
    "Anu": "Anuradha",
    "Jye": "Jyeshta",
    "Mul": "Mula",
    "PuA": "Purva Ashadha",
    "UtA": "Uttara Ashadha",
    "Shra": "Shravana",
    "Dha": "Dhanishta",
    "Sha": "Shatabhisha",
    "PuB": "Purva Bhadrapada",
    "UtB": "Uttara Bhadrapada",
    "Rev": "Revati"
}

# Nakshatra lords mapping
nakshatra_lords = {
    "Ashwini": "KE", "Bharani": "SK", "Krittika": "SY",
    "Rohini": "CH", "Mrigashira": "MA", "Ardra": "RA",
    "Punarvasu": "GU", "Pushya": "SA", "Ashlesha": "BU",
    "Magha": "KE", "Purva Phalguni": "SK", "Uttara Phalguni": "SY",
    "Hasta": "CH", "Chitra": "MA", "Swati": "RA",
    "Vishakha": "GU", "Anuradha": "SA", "Jyeshta": "BU",
    "Mula": "KE", "Purva Ashadha": "SK", "Uttara Ashadha": "SY",
    "Shravana": "CH", "Dhanishta": "MA", "Shatabhisha": "RA",
    "Purva Bhadrapada": "GU", "Uttara Bhadrapada": "SA", "Revati": "BU"
}