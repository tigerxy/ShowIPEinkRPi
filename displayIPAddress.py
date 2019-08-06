#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import socket
import datetime

def tryGetIPAddress():
	try:
		return socket.gethostbyname(socket.gethostname() + ".local")
	except:
		return 0

try:
	epd = epd2in13.EPD()
	epd.init(epd.lut_full_update)
	
	# Define fonts
	font18 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 18)
	font24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 24)
	fontbold24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
		
	# Waiting for IP-Address
	while not tryGetIPAddress():
		# Drawing warning
		date_time = str(datetime.datetime.now())[:19] 
		image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
		draw = ImageDraw.Draw(image)
		draw.text((10, 10), "No IP Address :(", font = font24, fill = 0)
		draw.text((10, 35), "Plug in Ethernet", font = fontbold24, fill = 0)
		draw.text((10, 65), "Cable!", font = fontbold24, fill = 0)
		draw.text((10, 95), date_time, font = font18, fill = 0)
		epd.display(epd.getbuffer(image.rotate(180)))
		epd.sleep()
		time.sleep(10)

	# Collect informations
	host_name = socket.gethostname() 
	host_ip = tryGetIPAddress()
	date_time = str(datetime.datetime.now())[:19] 

	# Drawing informations on diplay
	try:
		image = Image.open('/home/pi/.config/autostart/train.bmp') 
	except:
		image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
	draw = ImageDraw.Draw(image)
	draw.text((10, 10), "Hostname/IP:", font = font24, fill = 0)
	draw.text((10, 35), host_name, font = fontbold24, fill = 0)
	draw.text((10, 65), host_ip, font = fontbold24, fill = 0)
	draw.text((10, 95), date_time, font = font18, fill = 0)
	epd.display(epd.getbuffer(image.rotate(180)))
	epd.sleep()
        
except:
	print( 'traceback.format_exc():\n%s',traceback.format_exc())
	exit()

