
from geopy import geocoders
import csv

g = geocoders.GoogleV3()

def main():
	print("hello!")

	bars = []

	f = open("tabc latlng 2.csv","r+")


	with open('tabc houston addy.csv', 'rb') as csvfile:
		tabcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in tabcreader:
			b = bar(row[0],row[1],row[2],row[3],row[4])
			try:
				b.makeLatLng()
			except Exception, e:
				print("couldn't get lat lng for " + b.id)
			
			bars.append(b)
			print "added bar " + b.id

	for bb in bars:
		if (bb.lat != ""):
			f.write(str(bb.dump()) + '\n')



class bar():
	lat = ""
	lng = ""

	def __init__(self,id,address,city,state,zip):
		self.id = id
		self.address = address
		self.city = city
		self.state = state
		self.zip = zip

	def makeLatLng(self):
		place, (lat, lng) = g.geocode(self.getaddy()) 
		self.lat = lat
		self.lng = lng 

	def getaddy(self):
		return self.address + " " + self.city  + " " + self.state  + " " + self.zip

	def dump(self):
		return self.id + "," + str(self.lat) + "," + str(self.lng)



if __name__ == "__main__": main()    

