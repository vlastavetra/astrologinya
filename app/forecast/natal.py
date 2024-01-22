from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.const import SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, ASC, MC

def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60) * 3600)
    return f"{degrees}:{minutes}:{seconds}"

def calculate_natal():
  date = '1986/07/11'
  time = '17:00'
  location = 'Moscow, Russia'

  latitude = decimal_to_dms(55.76) 
  longitude = decimal_to_dms(37.62)

  birthdate = Datetime(date, time)
  birthplace = GeoPos(latitude, longitude)

  chart = Chart(birthdate, birthplace)

  data = {}

  data["sun"] = chart.getObject(SUN)
  data["moon"] = chart.getObject(MOON)
  data["mercury"] = chart.getObject(MERCURY)
  data["venus"] = chart.getObject(VENUS)
  data["mars"] = chart.getObject(MARS)
  data["jupiter"] = chart.getObject(JUPITER)
  data["saturn"] = chart.getObject(SATURN)
  data["ascendant"] = chart.get(ASC)
  data["midheaven"] = chart.get(MC)

  return data
