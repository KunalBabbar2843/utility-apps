import xml.etree.ElementTree as ET
country_name=[ ]
currency_name=[ ]
currency_code=[ ]
data=ET.parse('list_one.xml')
root=(data.getroot())[0]
for cntry in root.findall('CcyNtry'):
	country_name.append(cntry.find('CtryNm').text)
	currency_name.append(cntry.find('CcyNm').text)
	code=cntry.find('Ccy')
	if code is not None:
		currency_code.append(code.text)
	else:
		currency_code.append('None')
		
info=zip(country_name,currency_name,currency_code)
