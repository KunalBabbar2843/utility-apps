import requests

def converter(curr_from,curr_to):
	curr_str=curr_from+'_'+curr_to
	url='https://free.currconv.com/api/v7/convert?q='+curr_str+'&compact=ultra&callback=sampleCallback&apiKey=8d474ea331f4d8aa5015'
	try:
		data=requests.get(url)
		conversion=(((data.text).split('{')[1]).split('}')[0]).split(':')[1]
		return float(conversion)
	except:
		return 0