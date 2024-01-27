from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib.const import SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, ASC, MC, HOUSE1, HOUSE2, HOUSE3, HOUSE4, HOUSE5, HOUSE6, HOUSE7, HOUSE8, HOUSE9, HOUSE10, HOUSE11, HOUSE12

import geocoder
from openai import OpenAI


class ForcastCreator:
  def __init__(self, date="15/02/1988", time="06:00", loc="Moscow, Russia", language="english") -> None:
    self.latitude, self.longitude = self.get_coordinates(loc) 
    self.birthdate = Datetime(date, time)
    self.birthplace = GeoPos(self.latitude, self.longitude)
    self.chart = Chart(self.birthdate, self.birthplace)
    self.language = language

  def get_coordinates(self, loc):
    location_data = geocoder.arcgis(loc)

    if location_data.ok:
        return location_data.latlng[0], location_data.latlng[1]

  def calculate_natal(self, language):
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

    return f"discribe on {self.language} natal card by planets: sun in {data['sun'].sign}, moon in {data['moon'].sign}, mercury in {data['mercury'].sign}, venus in {data['venus'].sign}, mars in {data['mars'].sign}, jupiter in {data['jupiter'].sign}, saturn in {data['saturn'].sign}, ascendant in {data['ascendant'].sign}, midheaven in {data['midheaven'].sign}"

  
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
  

    return f"discribe on {self.language} natal card by houses: house 1 in {data['house1'].sign}, house 2 in {data['house2'].sign}, house 3 in {data['house3'].sign}, house 4 in {data['house4'].sign}, house 5 in {data['house5'].sign}, house 6 in {data['house6'].sign}, house 7 in {data['house7'].sign}, house 8 in {data['house8'].sign}, house 9 in {data['house9'].sign}, house 10 in {data['house10'].sign}, house 11 in {data['house11'].sign}, house 12 in {data['house12'].sign}"
  
  def generate_chat_response(self, key, input_text):
    client = OpenAI(api_key=key)

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a astrology assistant."},
        {"role": "user", "content": input_text},
      ]
    )

    return response.choices[0].message.content