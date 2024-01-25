from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.const import SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, ASC, MC, HOUSE1, HOUSE2, HOUSE3, HOUSE4, HOUSE5, HOUSE6, HOUSE7, HOUSE8, HOUSE9, HOUSE10, HOUSE11, HOUSE12
import geocoder


class ForcastCreator:
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
  
  def calculate_house(self):
    data = {}

    data["house1"] = self.chart.getHouse(HOUSE1)
    data["house2"] = self.chart.getHouse(HOUSE2)
    data["house3"] = self.chart.getHouse(HOUSE3)
    data["house4"] = self.chart.getHouse(HOUSE4)
    data["house5"] = self.chart.getHouse(HOUSE5)
    data["house6"] = self.chart.getHouse(HOUSE6)
    data["house7"] = self.chart.getHouse(HOUSE7)
    data["house8"] = self.chart.getHouse(HOUSE8)
    data["house9"] = self.chart.getHouse(HOUSE9)
    data["house10"] = self.chart.getHouse(HOUSE10)
    data["house11"] = self.chart.getHouse(HOUSE11)
    data["house12"] = self.chart.getHouse(HOUSE12)
  

    return data