from bs4 import BeautifulSoup
import json

with open('centrecom-po.xml', 'r') as file:
	data = file.read()


soup = BeautifulSoup(data, features = "lxml")

#print(soup)


print(soup.find("ltpage")["y1"])
pdf_height = float(soup.find("ltpage")["y1"])

print(len(soup.findAll("lttextboxhorizontal")))

print(len(soup.findAll("lttextlinehorizontal")))


data = {}

data["TextLines"] = []
for textline in soup.findAll("lttextlinehorizontal"):
	#print(textline["bbox"])
	#print(textline["width"])
	#print(textline["height"])
	#print()

	textline_dict = {
	"bbox" : textline["bbox"],
	"x0" : float(textline["x0"]),
	"y1" : pdf_height - float(textline["y1"]),
	"width" : float(textline["width"]),
	"height" : float(textline["height"])
	} 

	data["TextLines"].append(textline_dict)


data["TextBoxes"] = []
for textbox in soup.findAll("lttextboxhorizontal"):
	textbox_dict = {
	"bbox" : textbox["bbox"],
	"x0" : float(textbox["x0"]),
	"y1" : pdf_height - float(textbox["y1"]),
	"width" : float(textbox["width"]),
	"height" : float(textbox["height"])
	} 

	data["TextBoxes"].append(textbox_dict)



with open('data.json', 'w') as outfile:
	json.dump(data, outfile)








