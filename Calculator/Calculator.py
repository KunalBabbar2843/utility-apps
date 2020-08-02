from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

MainStr="""

Calculator:
	BoxLayout:
		id : main
		orientation:'vertical'
		BoxLayout:
			orientation:'vertical'
			size_hint_y:1
			Label:
				id:num1
				text:' '
				text_size:self.size
				halign:'right'
				valign:'top'
			Label:
				id:num2
				text:' '
				text_size:self.size
				halign:'right'
				valign:'top'
		BoxLayout:
			size_hint_y:4
			BoxLayout:
				orientation:'vertical'
				size_hint_x:3
				BoxLayout:
					Button:
						text:'1'
						on_press:root.add_num('1')
					Button:
						text:'2'
						on_press:root.add_num('2')
					Button:
						text:'3'
						on_press:root.add_num('3')
				BoxLayout:
					Button:
						text:'4'
						on_press:root.add_num('4')
					Button:
						text:'5'
						on_press:root.add_num('5')
					Button:
						text:'6'
						on_press:root.add_num('6')
				BoxLayout:
					Button:
						text:'7'
						on_press:root.add_num('7')
					Button:
						text:'8'
						on_press:root.add_num('8')
					Button:
						text:'9'
						on_press:root.add_num('9')
				BoxLayout:
					Button:
						size_hint_x:2
						text:'0'
						on_press:root.add_num('0')
					Button:
						size_hint_x:1
						text:'.'
						on_press:root.add_num('.')
			BoxLayout:
				size_hint_x:1
				BoxLayout:
					orientation:'vertical'
					Button:
						size_hint_y:1
						text:'+'
						on_press:root.add_num('+')
					Button:
						size_hint_y:1
						text:'-'
						on_press:root.add_num('-')
					Button:
						size_hint_y:1
						text:'x'
						on_press:root.add_num('x')
					Button:
						size_hint_y:1
						text:'÷'
						on_press:root.add_num('÷')
					Button:
						size_hint_y:3
						text:'='
						on_press:root.add_num('=')
		BoxLayout:
			size_hint_y:0.5
			Button:
				text:'clear'
				on_press:root.clear_cal()


"""

class calculation:
	def __init__(self):
		self.num1=''
		self.cmp=False
		self.num2=''
		self.operator=''
		self.floatpoint1=False
		self.floatpoint2=False
		self.oper=''

class Calculator(BoxLayout):
	def __init__(self,**kwargs):
		super(Calculator,self).__init__(**kwargs)
		self.cal=calculation()
	def clear_cal(self):
		self.cal=calculation()
		self.ids.num1.text=''
		self.ids.num2.text=''
	def add_num(self,obj):
		operators=['+','-','x','÷']
		if obj=='=':
			if self.cal.oper=='+':
				self.ids.num1.text=str(float(self.ids.num1.text)+float(self.ids.num2.text.replace('+','0')))
			elif self.cal.oper=='-':
				self.ids.num1.text=str(float(self.ids.num1.text)-float(self.ids.num2.text.replace('-','0')))			
			elif self.cal.oper=='x':
				self.ids.num1.text=str(float(self.ids.num1.text)*float(self.ids.num2.text.replace('x','0')))
			elif self.cal.oper=='÷':
				self.ids.num1.text=str(float(self.ids.num1.text)/float(self.ids.num2.text.replace('÷','0')))
			self.ids.num2.text=''
			self.cal=calculation()
			self.cal.floatpoint1=True
			self.cal.cmp=True
			return
			
			
		for op in operators:
			if obj==op:
				if self.cal.oper==''  :
					self.cal.cmp=True
					self.cal.oper=obj
					self.ids.num2.text+=obj
				return
				
		if not self.cal.cmp:
			if obj=='.':
				if not self.cal.floatpoint1:
					self.cal.floatpoint1=True
					self.ids.num1.text+=obj
			else:
				self.ids.num1.text+=obj
		else:
			if self.ids.num2.text=='':
				if obj in operators:
					self.ids.num2.text+=obj
			elif obj=='.':
				if not self.cal.floatpoint2:
					self.cal.floatpoint2=True
					self.ids.num2.text+=obj
			else:
				self.ids.num2.text+=obj
				
	

class Test(App):
	def build(self):
		return Builder.load_string(MainStr)
		
Test().run()