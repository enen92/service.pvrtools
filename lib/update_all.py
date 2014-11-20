import os
from common_variables import *
from xmltvmerger import *
from listmerger import *
xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('PVR Tools', "Merging epgs & lists. Wait...", 1,os.path.join(addonfolder,"icon.png")))
m3u_merge(notification=True)
xml_merge(notification=True)
xbmc.executebuiltin('XBMC.StartPVRManager')
