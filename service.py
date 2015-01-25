#!/usr/bin/python
import threading
import requests
import shutil
import os
import time
import gzip
import datetime
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import sys
from lib.common_variables import *
from lib import xmltvmerger,listmerger

if not xbmcvfs.exists(os.path.join(datapath,'download_folder')): xbmcvfs.mkdir(os.path.join(datapath,'download_folder'))

class service:
	def __init__(self):
		intro = False
		while (not xbmc.abortRequested):
			if not intro:
				print " _____ _____ _____    _____ _____ _____ __    _____"
				print "|  _  |  |  | __  |  |_   _|     |     |  |  |   __|"
				print "|   __|  |  |    -|    | | |  |  |  |  |  |__|__   |"
				print "|__|   \___/|__|__|    |_| |_____|_____|_____|_____|"
				print "Service started..."
				intro = True
			try:
				t1 = datetime.datetime.strptime(xbmcaddon.Addon().getSetting("last_merge"), "%Y-%m-%d %H:%M:%S.%f")
				t2 = datetime.datetime.now()
				interval = int(xbmcaddon.Addon().getSetting("check_interval"))
				update = abs(t2 - t1) > datetime.timedelta(days=interval)
				if update is False: raise Exception()
				if not (xbmc.Player().isPlaying() or xbmc.getCondVisibility('Library.IsScanningVideo')):
					xmltvmerger.xml_merge()
					xbmcaddon.Addon().setSetting("last_merge", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
			except:
				pass
			try:
				t1 = datetime.datetime.strptime(xbmcaddon.Addon().getSetting("last_merge_m3u"), "%Y-%m-%d %H:%M:%S.%f")
				t2 = datetime.datetime.now()
				interval = int(xbmcaddon.Addon().getSetting("check_interval_m3u"))
				update = abs(t2 - t1) > datetime.timedelta(hours=interval)
				if update is False: raise Exception()
				if not (xbmc.Player().isPlaying() or xbmc.getCondVisibility('Library.IsScanningVideo')):
					listmerger.m3u_merge()
					xbmcaddon.Addon().setSetting("last_merge_m3u", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
			except:
				pass

			xbmc.sleep(200)

service()


