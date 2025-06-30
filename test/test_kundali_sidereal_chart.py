import pytest
from datetime import datetime
from chart.kundali_sidereal_chart import KundaliSiderealChart, ChartInputData

@pytest.fixture
def vivekananda_chart_data():
    """Provides Swami Vivekananda's birth data as a dictionary."""
    return {
        "number": "70141",
        "prsName": "Vivekananda, Swami",
        "dob": "01/12/1863 06:33:00",
        "dob_tz": "+05:53",
        "place": "Kolkata, India",
        "latitude": 22.53,
        "longitude": 88.36
    }

@pytest.fixture
def kundali(vivekananda_chart_data):
    """Creates a Kundali object for Swami Vivekananda."""
    return KundaliSiderealChart(ChartInputData(**vivekananda_chart_data))

def test_create_chart_from_dict(kundali, vivekananda_chart_data):
    """Test that a Kundali object is created successfully from a dictionary."""
    assert isinstance(kundali, KundaliSiderealChart)
    assert kundali.lat == vivekananda_chart_data["latitude"]
    assert kundali.lon == vivekananda_chart_data["longitude"]

def test_lagna_calculation(kundali):
    """Test the Lagna (Ascendant) calculation."""
    # Expected Lagna for Swami Vivekananda is Sagittarius (240-270 degrees).
    assert 240 <= kundali.lagnaDec < 270

def test_vimshottari_dasha(kundali):
    """Test the Vimshottari Dasha calculation."""
    # For a Virgo Moon, the starting Dasha lord should be the Moon.
    first_dasha = kundali.mahadashas[0]
    assert first_dasha['planet'] == 'CH'

def test_to_dict_serialization(kundali, vivekananda_chart_data):
    """Test that the Kundali object can be serialized to a dictionary."""
    kundali_dict = kundali.to_dict()
    assert isinstance(kundali_dict, dict)
    assert "Grahas" in kundali_dict
    assert "Rashis" in kundali_dict
    assert "mahadashas" in kundali_dict
    assert kundali_dict['lat'] == vivekananda_chart_data['latitude']
    assert kundali_dict['lon'] == vivekananda_chart_data['longitude']


# Expected values for all Grahas
expected_graha_values = {
    'SY': {'name_of_graha': 'Surya', 'degree_in_decimal': 269.42335, 'desposited_in_bhava': '1', 'desposited_in_rashi': 'Sag', 'lord_of_bhavas': ['9'], 'desposited_in_nakshatra': 'Uttara Ashadha'},
    'CH': {'name_of_graha': 'Chandra', 'degree_in_decimal': 167.44958, 'desposited_in_bhava': '10', 'desposited_in_rashi': 'Vir', 'lord_of_bhavas': ['8'], 'desposited_in_nakshatra': 'Hasta'},
    'BU': {'name_of_graha': 'Budha', 'degree_in_decimal': 281.77302, 'desposited_in_bhava': '2', 'desposited_in_rashi': 'Cap', 'lord_of_bhavas': ['7', '10'], 'desposited_in_nakshatra': 'Shravana'},
    'SK': {'name_of_graha': 'Shukra', 'degree_in_decimal': 277.10305, 'desposited_in_bhava': '1', 'desposited_in_rashi': 'Cap', 'lord_of_bhavas': ['11', '6'], 'desposited_in_nakshatra': 'Uttara Ashadha'},
    'MA': {'name_of_graha': 'Mangal', 'degree_in_decimal': 6.32356, 'desposited_in_bhava': '4', 'desposited_in_rashi': 'Ari', 'lord_of_bhavas': ['5', '12'], 'desposited_in_nakshatra': 'Ashwini'},
    'GU': {'name_of_graha': 'Guru', 'degree_in_decimal': 184.01386, 'desposited_in_bhava': '10', 'desposited_in_rashi': 'Lib', 'lord_of_bhavas': ['1', '4'], 'desposited_in_nakshatra': 'Chitra'},
    'SA': {'name_of_graha': 'Shani', 'degree_in_decimal': 163.57357, 'desposited_in_bhava': '10', 'desposited_in_rashi': 'Vir', 'lord_of_bhavas': ['2', '3'], 'desposited_in_nakshatra': 'Hasta'},
    'RA': {'name_of_graha': 'Rahu', 'degree_in_decimal': 232.24713, 'desposited_in_bhava': '12', 'desposited_in_rashi': 'Sco', 'lord_of_bhavas': ['3'], 'desposited_in_nakshatra': 'Jyeshta'},
    'KE': {'name_of_graha': 'Ketu', 'degree_in_decimal': 52.24713, 'desposited_in_bhava': '6', 'desposited_in_rashi': 'Tau', 'lord_of_bhavas': ['12'], 'desposited_in_nakshatra': 'Rohini'},
    'LG': {'name_of_graha': 'Lagna', 'degree_in_decimal': 266.15779, 'desposited_in_bhava': '1', 'desposited_in_rashi': 'Sag', 'lord_of_bhavas': [], 'desposited_in_nakshatra': 'Purva Ashadha'},
}

# --- Granular Graha Tests ---
@pytest.mark.parametrize("planet_shortcut, expected_values", expected_graha_values.items())
def test_graha_attributes(kundali, planet_shortcut, expected_values):
    graha = kundali.Grahas[planet_shortcut]
    assert graha.name_of_graha == expected_values['name_of_graha']
    assert abs(graha.degree_in_decimal - expected_values['degree_in_decimal']) < 0.0001
    assert graha.desposited_in_bhava == expected_values['desposited_in_bhava']
    assert graha.desposited_in_rashi == expected_values['desposited_in_rashi']
    assert graha.lord_of_bhavas == expected_values['lord_of_bhavas']
    assert graha.desposited_in_nakshatra == expected_values['desposited_in_nakshatra']

expected_rashi_grahas = {
    'Mesha': ['MA'],
    'Vrishabha': ['KE'],
    'Mithuna': [],
    'Karka': [],
    'Simha': [],
    'Kanya': ['CH', 'SA'],
    'Tula': ['GU'],
    'Vrishchika': ['RA'],
    'Dhanu': ['SY', 'LG'],
    'Makara': ['BU', 'SK'],
    'Kumbha': [],
    'Meena': [],
}

# --- Granular Rashi Tests ---
@pytest.mark.parametrize("rashi_name, expected_graha_shortcuts", expected_rashi_grahas.items())
def test_rashi_attributes(kundali, rashi_name, expected_graha_shortcuts):
    rashi = kundali.Rashis[rashi_name]
    assert rashi.rashi == rashi_name
    assert len(rashi.grahas) == len(expected_graha_shortcuts)
    graha_names = [g.name_of_graha for g in rashi.grahas]
    for shortcut in expected_graha_shortcuts:
        assert expected_graha_values[shortcut]['name_of_graha'] in graha_names

expected_mahadasha_values = [
    {'planet': 'CH', 'start_date': '1863-01-12', 'end_date': '1867-06-12', 'duration': 4.412818278171917},
    {'planet': 'MA', 'start_date': '1867-06-12', 'end_date': '1874-06-11', 'duration': 7.0},
    {'planet': 'RA', 'start_date': '1874-06-11', 'end_date': '1892-06-11', 'duration': 18.0},
    {'planet': 'GU', 'start_date': '1892-06-11', 'end_date': '1908-06-12', 'duration': 16.0},
    {'planet': 'SA', 'start_date': '1908-06-12', 'end_date': '1927-06-13', 'duration': 19.0},
    {'planet': 'BU', 'start_date': '1927-06-13', 'end_date': '1944-06-12', 'duration': 17.0},
    {'planet': 'KE', 'start_date': '1944-06-12', 'end_date': '1951-06-13', 'duration': 7.0},
    {'planet': 'SK', 'start_date': '1951-06-13', 'end_date': '1971-06-13', 'duration': 20.0},
    {'planet': 'SY', 'start_date': '1971-06-13', 'end_date': '1977-06-12', 'duration': 6.0},
]

# --- Granular Mahadasha Tests ---
@pytest.mark.parametrize("mahadasha_index, expected_values", enumerate(expected_mahadasha_values))
def test_mahadasha_attributes(kundali, mahadasha_index, expected_values):
    mahadasha = kundali.mahadashas[mahadasha_index]
    assert mahadasha['planet'] == expected_values['planet']
    assert mahadasha['start_date'] == expected_values['start_date']
    assert mahadasha['end_date'] == expected_values['end_date']
    assert abs(mahadasha['duration'] - expected_values['duration']) < 0.0001
