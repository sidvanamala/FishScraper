import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#import HTMLParser
# from beautifulsoup import BeautifulSoup
# import pandas as pd
import re


# FINDING THE BASIC BIO DATA OF FISH

textfile = open("/Users/sid/Documents/Programming/Symptomatic-main/fishes.txt", "r")
file = textfile.read().split("\n")
for stuff in file:
	stuff.replace("*", " ")

# giving basic bio data on each fish in our fishes.txt file
for fish in file:
	search = fish
	search2 = f"are {fish} endangered?"
	url = 'https://google.com/search?q=' + search
	url2 = 'https://google.com/search?q=' + search2
	request_result = requests.get( url )
	request_result2 = requests.get( url2 )
	soup = BeautifulSoup(request_result.content, "lxml")
	soup2 = BeautifulSoup(request_result2.content, "lxml")
	#print(soup2.prettify())
	box = soup.find('div', {'class': "BNeawe s3v9rd AP7Wnd"})
	box2 = soup2.find('div', {'class': "BNeawe iBp4i AP7Wnd"})


	if box != None and box2 != None:
		the_text = box.get_text()
		the_text2 = box2.get_text()
		print(str(fish) + " : " + the_text2 + " : " + the_text)
	elif box != None and box2 == None:
		the_text = box.get_text()
		print(str(fish) + " : " + the_text2 + " : " + "No bio data")
	elif box == None and box2 != None:
		the_text2 = box2.get_text()
		print(str(fish) + " : " + "Status not found" + " : " + the_text)
	elif box == None and box2 == None:
		print(str(fish) + " : no status found : No bio informations")

# CONSERVATION STATUS OF EACH FISH
def conservation_stat():	
	global file

	for bodwa in file:
		if "- " in bodwa:
			continue
		elif bodwa == "      No fish":
			continue
		else:
			search = f"are {bodwa} endangered?"
			url = 'https://google.com/search?q=' + search

			request_result = requests.get( url )



			soup = BeautifulSoup(request_result.content, "lxml")


			box = soup.find('div', {'class': "BNeawe iBp4i AP7Wnd"})
			if box != None:
				the_text = box.get_text()
				print(bodwa + ": " + the_text)
				print("______________________________________")
			else:
				print(bodwa + ": " + "Status not found")
				print("______________________________________")


#######################################################################################################################
# FISHS IN THAT LOCATION AND PUTTING INTO A LIST --> which is going to be organized in the fishes.txt file
def locate_fish():
	list = []
	search = f"the most common fishes in {bodwa}"
	url = 'https://google.com/search?q=' + search


	request_result = requests.get( url )



	soup = BeautifulSoup(request_result.content, "lxml")


	box = soup.find('span', {'class': "FCUp0c rQMQod"})
	#the_text = box.find('b').get_text()
	the_text = box.get_text()
	list.append(the_text)
	print(the_text)

