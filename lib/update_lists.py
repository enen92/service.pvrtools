import os
from common_variables import *
from listmerger import *
xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('PVR Tools', "Merging Lists. Wait...", 1,os.path.join(addonfolder,"icon.png")))
m3u_merge(notification=True)
