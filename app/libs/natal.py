from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.const import SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, ASC, MC

def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60) * 3600)
    return f"{degrees}:{minutes}:{seconds}"

if __name__ == "__main__":
  date = '1986/07/11'
  time = '17:00'
  location = 'Moscow, Russia'

  latitude = decimal_to_dms(55.76) 
  longitude = decimal_to_dms(37.62)

  birthdate = Datetime(date, time)
  birthplace = GeoPos(latitude, longitude)

  chart = Chart(birthdate, birthplace)

  sun = chart.getObject(SUN)
  moon = chart.getObject(MOON)
  mercury = chart.getObject(MERCURY)
  venus = chart.getObject(VENUS)
  mars = chart.getObject(MARS)
  jupiter = chart.getObject(JUPITER)
  saturn = chart.getObject(SATURN)
  ascendant = chart.get(ASC)
  midheaven = chart.get(MC)

  print(f"Sun: {sun}")
  print(f"Moon: {moon}")
  print(f"Mercury: {mercury}")
  print(f"Venus: {venus}")
  print(f"Mars: {mars}")
  print(f"Jupiter: {jupiter}")
  print(f"Saturn: {saturn}")
  print(f"Ascendant: {ascendant}")
  print(f"Midheaven: {midheaven}")
