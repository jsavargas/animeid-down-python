#!/usr/bin/env python
# -*- coding: utf-8 -*-


####### jsavargas
####### MODO DE USO
####### python jkanimedown -s dragon-ball-super -i 10
####### python animeid.tv-down-arguments.py -s dragon-ball-super -i 10


from bs4 import BeautifulSoup
import requests
import urllib
import httplib
import json
import sys

import urllib2
import re

import json
from pprint import pprint

import datetime

import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-s','--serie', nargs='?', default=None,help='sum the integers (default: find the max)')
parser.add_argument('-c','--capitulo', nargs='?', default=None)
parser.add_argument('-i','--inicio', nargs='?', default=None)
parser.add_argument('-f','--final', nargs='?', default=None)
args = parser.parse_args()
#print(args)
#print args.example

var_serie  = args.serie
var_cap    = args.capitulo
var_inicio = args.inicio
var_final  = args.final


if(var_serie):
	print "SERIE: ",var_serie
else:
	exit()

if(var_cap or var_inicio):
	var_cap = (var_cap if var_cap else var_inicio)
	print "INICIO: ",var_cap	
else:
	exit()

if(var_final):
	print "FINAL: ",var_final
else:
	print "FINAL: ",var_inicio
	var_final = var_inicio
	
def getsource(url):
	try:
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
		headers = { 'User-Agent' : user_agent }
	
		req = urllib2.Request(url, None, headers)
		response = urllib2.urlopen(req)
		page = response.read()
		response.close() # its always safe to close an open connection
		
		return page
	except:
		return None


def getvideolink(page):
	soup = BeautifulSoup(page, 'html.parser')
		
	for param in soup.find_all('script',{'type' : 'text/javascript'}):
			
		try:
			myVar
			
			#print str(param.contents)
			matchObj = re.match('.*file":"(.*)","type.*', str(param.contents))
	
			if matchObj:
				#print "matchObj.group() : ", matchObj.group()
				#print "matchObj.group: [", matchObj.group(1),"]aaaaa"
				return matchObj.group(1).strip()			
		except NameError:
			myVar = None




def downloadVideo(link,serie,capitulo):
	try:
		capitulo = str(capitulo).zfill(3)		
		varmkdir = "mkdir -p {}".format(serie)
		code = os.system(varmkdir)
		down = "wget --tries=5 " + str(link) + " -O " + str(serie) + "/" + str(serie) + "-" + str(capitulo) + ".mp4"
		print "WGET: ", down
		code = os.system(down)
		print "CODE:", code

		return code	
	except Exception,e:
		print "ERROR def downloadVideo >>>>>>>>", str(e)
		return None
	
					
					
for num in range(int(var_inicio),(int(var_final) + 1)):  
	print "=============================================================================================="
	print "CAPITULO EN CURSO >>>>>>> ",num


	serie    = var_serie # 'dragon-ball-z'
	capitulo = num
	
	pagina = 'http://jkanime.net/' + serie + "/" + str(capitulo)
	pagina = 'https://www.animeid.tv/v/' + serie + "-" + str(capitulo)
	
	print "PAGINA: ",pagina
	
	user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
	
	
	headers = { 'User-Agent' : user_agent }
	#req = urllib2.Request('http://www.instagram.com/jsavargas', None, headers)
	req = urllib2.Request(pagina, None, headers)
	response = urllib2.urlopen(req)
	page = response.read()
	
	response.close() # its always safe to close an open connection
	
	print "DESCARGANDO INICIANDO EL PROCESO"
	print datetime.datetime.now()
				
	
	
	if page:
		#print page
		#print "=============================================================================================="
		
		soup = BeautifulSoup(page, 'html.parser')
		#print(soup.prettify())
	
	
		links1   = ''
		links2   = ''
		alllinks = []
		mirrors = []
		
		for div in soup.find_all('li', {'class': 'tab'}):
			print div.contents[0].strip()
			mirrors.append(div.contents[0].strip())
			#print(div.get('data-old-title'))

		#for div in soup.find_all('div', class_=re.compile('the_video lgv_')):
		for div in soup.find_all('div', {'class': 'parte'}):
			#print ">>DATA>>",div['data']
			m = re.match(".*src=(?:\\\\u0022)?(?:\\\\/\\\\/)?(.+?)(?:\\\\u0022)?\s", div['data'])
			if m:
				
				try:
					#print ">>DATA.re>>",m.group()
					alllinks.append(m.group(1))
					links1 = ("http://"+ str(m.group(1)).replace("\\", ""))#.replace("http://https://", "https://")
					print ">>links1.re>>",links1 
					#page   = getsource("http://s102.animeid.tv/?vid=eJwBQwC8_3Iiwpcuw6rDrMOgwqLCh0LCujMPwpNywrTCrB7CoxxEw4kbwoTDhMO0KMOjFnDDj8ODwo7Cs8KWb8Oqb07CvcOKCU7_BCWG")
					page   = getsource(links1)
					if (page==None): break
					videos = getvideolink(page)
					if (videos==None): break
					
					print ">>VIDEO LINK.re>>",videos
					if videos is not None:
						print ">>IS VIDEO LINK.re>>",videos
						code = downloadVideo(videos,serie,capitulo)
						if (code==None): break
						print "CODE VIDEO DOWNLOAD 1 :",code
						break
						
				except Exception,e:
					print "ERROR VIDEO DOWNLOAD 1 >>>>>>>>", str(e)
		
				

					

				
				


		
		
		#exit()
	
