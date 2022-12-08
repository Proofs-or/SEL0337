#-------Inclusão das Bibliotecas-------#
from requests import get
import json
from pprint import pprint
from haversine import haversine

#------------Iclusão da API------------#

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

#----Obtenção dos Dados Climáticos----#

all_stations = get(stations).json()['items']
closest_stn = 966583
weather = weather + str(closest_stn)
my_weather = get(weather).json()['items']
pprint(my_weather)