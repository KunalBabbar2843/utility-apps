import requests
import json
from weatherapi import WeatherInfo
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
#from file import MainStr

class SearchCity(BoxLayout):
	def pullcityname(self):
		return self.ids.result.text

class Weather(BoxLayout):
	def update(self,Wobj):
		if Wobj.Found=='NC':
			self.ids.location.text='No Internet Connection'
			self.ids.description.text='None'
			self.ids.temp.text='None'
			self.ids.humidity.text='None'
			self.ids.pressure.text='None'
			self.ids.wspeed.text='None'			
		elif Wobj.Found=='NF':
			self.ids.location.text='No Location Found'
			self.ids.description.text='None'
			self.ids.temp.text='None'
			self.ids.humidity.text='None'
			self.ids.pressure.text='None'
			self.ids.wspeed.text='None'
		elif Wobj.Found=='F':
			self.ids.location.text=Wobj.cityname
			self.ids.description.text=Wobj.Wtype
			self.ids.temp.text=str(Wobj.Temp)+' degee centigrate'
			self.ids.humidity.text=str(Wobj.humidity)+'%'
			self.ids.pressure.text=str(Wobj.pressure)+'hPa'
			self.ids.wspeed.text=str(Wobj.windspeed)+' meter per second'

class MainLayout(BoxLayout):
	def findW(self):
		self.city=self.ids.Sbar.pullcityname()
		self.weatherdata=WeatherInfo(self.city)
		self.ids.Winfo.update(self.weatherdata)
	
class WeatherApp(App):
	def build(self):
		Builder.load_file('LayoutFile.kv')
		return MainLayout()
		
WeatherApp().run()