import requests
import json
class WeatherInfo:
	def __init__(self,city):
		self.url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=f9395d4e84b1339dc85e1ad20d521a6b&units=metric'.format(city)
		self.Found='NF'
		self.cityname=None
		self.Wtype=None
		self.Wicon=None
		self.Temp=None
		self.humidity=None
		self.pressure=None
		self.windspeed=None
		self.Wdata=None
		try:
		    self.data=requests.get(self.url)
		    self.Wdata=json.loads(self.data.text)
		except:
			self.Found='NC'
		if self.Wdata is not None and self.Wdata['cod']==200:
			self.Found='F'
			self.cityname=self.Wdata['name']
			self.Wtype=self.Wdata['weather'][0]['description']
			self.Wicon='http://openweathermap.org/img/wn/{}@2x.png'.format(self.Wdata['weather'][0]['icon'])
			self.Temp=self.Wdata['main']['temp']
			self.humidity=self.Wdata['main']['humidity']
			self.pressure=self.Wdata['main']['pressure']
			self.windspeed=self.Wdata['wind']['speed']
			