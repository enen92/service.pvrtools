#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xbmc,xbmcgui,xbmcaddon,os,shutil,requests,time

addon_id = 'service.pvrtools'

selfAddon = xbmcaddon.Addon(id=addon_id)
datapath = xbmc.translatePath(selfAddon.getAddonInfo('profile')).decode('utf-8')
addonfolder = xbmc.translatePath(selfAddon.getAddonInfo('path')).decode('utf-8')
artfolder = os.path.join(addonfolder,'resources','img')
msgok = xbmcgui.Dialog().ok
mensagemprogresso = xbmcgui.DialogProgress()

def copy_file(path):
	print "Copy file to addon_data... " + str(path)
	shutil.copy(path, os.path.join(datapath,'download_folder'))
	print "File has been copied..."

def download_and_extract(name):
	print "starting download... " + str(name)
	start_time = time.time()
	r = requests.get(name, stream=True)
	if r.status_code == 200:
		with open(os.path.join(datapath,'download_folder',name.split('/')[-1]), 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f) 
		print "download finished..." + name
		print "elapsed time:" + str(time.time() - start_time)
	else:
		print "download failed (error status != 200)..." + name
