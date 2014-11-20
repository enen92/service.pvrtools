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
from common_variables import *

def m3u_merge(notification=False):
	print "Starting m3u8 list processing..."
	if selfAddon.getSetting('l1') == 'true':
		if selfAddon.getSetting('l1-type') == '1':
			t1 = threading.Thread(name='list1', target=download_and_extract , args=(selfAddon.getSetting('l1-url'),))
		else:
			t1 = threading.Thread(name='list1', target=copy_file , args=(selfAddon.getSetting('l1-loc'),))	
		t1.start()
	if selfAddon.getSetting('l2') == 'true':
		if selfAddon.getSetting('l2-type') == '1':
			t2 = threading.Thread(name='list2', target=download_and_extract , args=(selfAddon.getSetting('l2-url'),))
		else:
			t2 = threading.Thread(name='list2', target=copy_file , args=(selfAddon.getSetting('l2-loc'),))	
		t2.start()
	if selfAddon.getSetting('l3') == 'true':
		if selfAddon.getSetting('l3-type') == '1':
			t3 = threading.Thread(name='list3', target=download_and_extract , args=(selfAddon.getSetting('l3-url'),))
		else:
			t3 = threading.Thread(name='list3', target=copy_file , args=(selfAddon.getSetting('l3-loc'),))	
		t3.start()
	if selfAddon.getSetting('l4') == 'true':
		if selfAddon.getSetting('l4-type') == '1':
			t4 = threading.Thread(name='list4', target=download_and_extract , args=(selfAddon.getSetting('l4-url'),))
		else:
			t4 = threading.Thread(name='list4', target=copy_file , args=(selfAddon.getSetting('l4-loc'),))	
		t4.start()
	if selfAddon.getSetting('l5') == 'true':
		if selfAddon.getSetting('l5-type') == '1':
			t5 = threading.Thread(name='list5', target=download_and_extract , args=(selfAddon.getSetting('l5-url'),))
		else:
			t5 = threading.Thread(name='list5', target=copy_file , args=(selfAddon.getSetting('l5-loc'),))	
		t5.start()

	try:t1.join()
	except:pass
	try: t2.join()
	except:pass
	try: t3.join()
	except:pass
	try: t4.join()
	except:pass
	try: t5.join()
	except:pass
	xbmc.sleep(1000)
	print "Starting m3u8 list merging..."
	dirs, m3u_list = xbmcvfs.listdir(os.path.join(datapath,'download_folder'))
	out = os.path.join(selfAddon.getSetting('output_folder'),selfAddon.getSetting('file_name_lists').replace('.m3u8','').replace('.m3u','')+'.m3u')
	if xbmcvfs.exists(out): os.remove(out)
	i=1
	total = len(m3u_list)	
	for m3u in m3u_list:
		if i==1:
			f = open(os.path.join(datapath,'download_folder',m3u), "r")
			text = f.read()
			f.close()
			with open(out, "a") as myfile:
				myfile.write(text)
		else:
			f = open(os.path.join(datapath,'download_folder',m3u), "r")
			text = f.read()
			f.close()
			with open(out, "a") as myfile:
				myfile.write(text.replace('#EXTM3U#','').replace('#EXTM3U',''))
		os.remove(os.path.join(datapath,'download_folder',m3u))
		i+=1
	print "M3u8 lists have been merged..."
	if notification:
		xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('PVR Tools', 'Lists have been merged!', 1,os.path.join(addonfolder,"icon.png")))
	return
