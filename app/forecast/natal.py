from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.const import SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, ASC, MC
import geocoder


class NatalForcastCreator:
  def __init__(self, date, time, loc) -> None:
    self.latitude, self.longitude = self.get_coordinates(loc) 
    self.birthdate = Datetime(date, time)
    self.birthplace = GeoPos(self.latitude, self.longitude)
    self.chart = Chart(self.birthdate, self.birthplace)

  def get_coordinates(self, loc):
    location_data = geocoder.arcgis(loc)

    if location_data.ok:
        return location_data.latlng[0], location_data.latlng[1]

  def calculate_natal(self):
    data = {}

    data["sun"] = self.chart.getObject(SUN)
    data["moon"] = self.chart.getObject(MOON)
    data["mercury"] = self.chart.getObject(MERCURY)
    data["venus"] = self.chart.getObject(VENUS)
    data["mars"] = self.chart.getObject(MARS)
    data["jupiter"] = self.chart.getObject(JUPITER)
    data["saturn"] = self.chart.getObject(SATURN)
    data["ascendant"] = self.chart.get(ASC)
    data["midheaven"] = self.chart.get(MC)

    return data