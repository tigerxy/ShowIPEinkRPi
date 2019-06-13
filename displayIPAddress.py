#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import socket
import datetime

try:
	epd = epd2in13.EPD()

	host_name = socket.gethostname() 
	host_ip = socket.gethostbyname(host_name + ".local")
	date_time = str(datetime.datetime.now())[:19] 

	epd.init(epd.lut_full_update)

	try:
		image = Image.open('/home/pi/.config/autostart/train.bmp') 
	except:
		image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
	font24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 24)
	font18 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 18)
	fontbold24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
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

