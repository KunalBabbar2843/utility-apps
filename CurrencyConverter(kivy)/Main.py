from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from kivy.lang.builder import Builder
import requests
from converter import converter
from countrysearch import info

currency=list(info)
MainStr="""

<DisplayData>:
	orientation:'vertical'
	Label:
		text:'ONLINE CURRENCY CONVERTER'
		size_hint_y:2
	Label:
		id:amount
		text:'enter amount:'
	BoxLayout:
		Label:
			id : rate
			text:'Conversion Rate:'
			text_size:self.size
			halign:'left'
			valign:'bottom'
		Label:
			id :ans
			text:'Amount:'
			text_size:self.size
			halign:'left'
			valign:'bottom'

<SearchBar>:
	orientation:'vertical'
	BoxLayout:
		TextInput:
			id : bar
			text:'Search Currency'
	BoxLayout:
		Button:
			id : pFrom
			text:'Put In From:'
			disabled:True
			on_press:root.parent.update('From')
		Button:
			id : pTo
			text:'Put In To:'
			disabled:True
			on_press:root.parent.update('To')
		Button:
			id :Search
			text:'Search'
			on_press:root.search()

<CountrySelectorFrom>:
	Button:
		size_hint_x:1
		text:'previous'
		on_press:root.ChangeCurrency('prev')
	BoxLayout:
		orientation:'vertical'
		size_hint_x:3
		Label:
			text_size:self.size
			text:'From:'
			halign:'left'
			valign:'top'
		Label:
			id:code1
			text:'INR'
		Label:
			id:C_name1
			text:'Indian Ruppe'
		Label:
			id:Cntry1
			text:'INDIA'
	Button:
		size_hint_x:1
		text:'next'
		on_press:root.ChangeCurrency('next')
<CountrySelectorTo>:
	Button:
		size_hint_x:1
		text:'previous'
		on_press:root.ChangeCurrency('prev')
	BoxLayout:
		orientation:'vertical'
		size_hint_x:3
		Label:
			text_size:self.size
			text:'To:'
			halign:'left'
			valign:'top'
		Label:
			id:code2
			text:'USD'
		Label:
			id:C_name2
			text:'US Dollar'
		Label:
			id:Cntry2
			text:'USA'
	Button:
		size_hint_x:1
		text:'next'
		on_press:root.ChangeCurrency('next')
		
<NumPad>:
	BoxLayout:
		orientation:'vertical'
		BoxLayout:
			Button:
				text:'1'
				on_press:root.parent.take_input('1')
			Button:
				text:'2'
				on_press:root.parent.take_input('2')
			Button:
				text:'3'
				on_press:root.parent.take_input('3')
		BoxLayout:
			Button:
				text:'4'
				on_press:root.parent.take_input('4')
			Button:
				text:'5'
				on_press:root.parent.take_input('5')
			Button:
				text:'6'
				on_press:root.parent.take_input('6')
		BoxLayout:
			Button:
				text:'7'
				on_press:root.parent.take_input('7')
			Button:
				text:'8'
				on_press:root.parent.take_input('8')
			Button:
				text:'9'
				on_press:root.parent.take_input('9')
		BoxLayout:
			Button:
				id:decimal
				size_hint_x:1
				text:'.'
				on_press:root.parent.take_input('.')
			Button:
				size_hint_x:1
				text:'0'
				on_press:root.parent.take_input('0')
			Button:
				size_hint_x:1
				text:'clear'
				on_press:root.parent.clear()
		BoxLayout:
			Button:
				text:'convert'
				on_press:root.parent.convert()
		

<MainLayout>:
	orientation:'vertical'
	DisplayData:
		id:display
		size_hint_y:3.5
	CountrySelectorFrom:
		id:From
		size_hint_y:1.5
	Button:
		id:switch
		size_hint_y:0.5
		text:'Switch'
		on_press:root.switch()
	CountrySelectorTo:
		id :To
		size_hint_y:1.5
	SearchBar:
		id: Sbar
		size_hint_y:2
	NumPad:
		id : n_pad
		size_hint_y:6
		

"""


Builder.load_string(MainStr)





class MainLayout(BoxLayout):
	def __init__(self,**kwargs):
		super(MainLayout,self).__init__(**kwargs)
	def getCodes(self):
		code1=self.ids.From.getCode()
		code2=self.ids.To.getCode()
		return code1,code2
	def take_input(self,num):
		if num=='.':
			self.ids.n_pad.switch_decimal(True)
		self.ids.display.registor(num)
	def clear(self):
		self.ids.display.registor('clr')
		self.ids.n_pad.switch_decimal(False)
	def convert(self):
		code1,code2=self.getCodes()
		rate=converter(code1,code2)
		self.ids.display.Amount(rate)
	def switch(self):
		first=self.ids.From.From
		second=self.ids.To.To
		self.ids.From.update(second)
		self.ids.To.update(first)
	def update(self,str_c):
		num=self.ids.Sbar.hold
		if str_c=='From':
			self.ids.From.update(num)
		else:
			self.ids.To.update(num)

class DisplayData(BoxLayout):
	def registor(self,num):
		if num=='clr':
			self.ids.amount.text='enter amaount:'
			self.ids.ans.text='Amount:'
			self.ids.rate.text='Conversion Rate:'
		else:
		    self.ids.amount.text+=num
	def Amount(self,rate):
		self.ids.rate.text='Coversion Rate:'+str(rate)
		amount=self.ids.amount.text.split(':')
		if amount[1]!='':
		    self.ids.ans.text='Amount:'+str(float(amount[1])*rate)
		   
		
		
		
		

class CountrySelectorFrom(BoxLayout):
	def __init__(self,**kwargs):
		super(CountrySelectorFrom,self).__init__(**kwargs)
		self.From=111
		self.CurrencyInfo=currency 
	def ChangeCurrency(self,N_or_P):
		if N_or_P=='prev':
			if self.From>0:
				self.From-=1
			else:
				self.From=len(self.CurrencyInfo)-11
		else:
			if self.From<len(self.CurrencyInfo)-11:
			    self.From+=1
			else:
				self.From=0
		self.ids.Cntry1.text=self.CurrencyInfo[self.From][0]
		self.ids.C_name1.text=self.CurrencyInfo[self.From][1]
		self.ids.code1.text=self.CurrencyInfo[self.From][2]
	def getCode(self):
		return self.ids.code1.text
	def update(self,change):
		self.From=change
		self.ids.Cntry1.text=self.CurrencyInfo[self.From][0]
		self.ids.C_name1.text=self.CurrencyInfo[self.From][1]
		self.ids.code1.text=self.CurrencyInfo[self.From][2]





class CountrySelectorTo(BoxLayout):
	def __init__(self,**kwargs):
		super(CountrySelectorTo,self).__init__(**kwargs)
		self.To=253
		self.CurrencyInfo=currency
	def ChangeCurrency(self,N_or_P):
		if N_or_P=='prev':
			if self.To>0:
				self.To-=1
			else:
				self.To=len(self.CurrencyInfo)-11
		else:
			if self.To<len(self.CurrencyInfo)-11:
			    self.To+=1
			else:
				self.To=0
		self.ids.Cntry2.text=self.CurrencyInfo[self.To][0]
		self.ids.C_name2.text=self.CurrencyInfo[self.To][1]
		self.ids.code2.text=self.CurrencyInfo[self.To][2]
	def getCode(self):
		return self.ids.code2.text
	def update(self,change):
		self.To=change
		self.ids.Cntry2.text=self.CurrencyInfo[self.To][0]
		self.ids.C_name2.text=self.CurrencyInfo[self.To][1]
		self.ids.code2.text=self.CurrencyInfo[self.To][2]		
		
		

class SearchBar(BoxLayout):
	def __init__(self,**kwargs):
		super(SearchBar,self).__init__(**kwargs)
		self.CurrencyInfo=currency
		self.hold=-1
	def search(self):
		str_c=self.ids.bar.text.upper()
		for i in range(len(self.CurrencyInfo)):
			if self.CurrencyInfo[i][0]==str_c:
				self.hold=i
				break
			elif self.CurrencyInfo[i][1]==str_c:
				self.hold=i
				break
			elif self.CurrencyInfo[i][2]==str_c:
				self.hold=i
				break
		if self.hold!=-1:
			Cntry=self.CurrencyInfo[i]
			self.ids.bar.text=str(Cntry[2])+','+str(Cntry[1])+","+str(Cntry[0])
			self.ids.pFrom.disabled=False
			self.ids.pTo.disabled=False
		else :
			self.hold=-1
			self.ids.bar.text='No Currency Found'
			self.ids.pFrom.disabled=True
			self.ids.pTo.disabled=True
	def Pullrequest(self):
		return self.hold
		
class NumPad(BoxLayout):
	def switch_decimal(self,bool):
		self.ids.decimal.disabled=bool
		

class CurrencyConverter(App):
	def build(self):
		return MainLayout()
		
CurrencyConverter().run()