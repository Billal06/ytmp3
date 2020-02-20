import requests, json, re
print ("""
   __ __ _____    _____ _____ ___ 
  |  |  |_   _|  |     |  _  |_  |
  |_   _| | |    | | | |   __|_  |
    |_|   |_|    |_|_|_|__|  |___|
   BILLAL | CYBER GHOST INDONESIAN
""")
url = raw_input("URL: ")
data = {"url":url,"ajax":"1"}
r = requests.post("https://mate02.y2mate.com/id12/mp3/ajax",data=data)
j = json.loads(r.text)["result"]
try:
	c = re.compile("var vlinks = (.*)")
	s = c.search(j)
	rp = (s.group()).replace("var vlinks = ","").replace(";","")
	file = raw_input("Nama File: ")
	print ("Downloading ...")
	rg = requests.get(json.loads(rp)["mp3"]["251"]["href"]).content
	print ("Saving ...")
	open(file, "wb").write(rg)
	print ("Selesai")
except:
	print ("Masukan URL dengan benar")
