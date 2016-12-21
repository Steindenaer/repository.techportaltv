import xbmc
import sys
import urllib

title = xbmc.getInfoLabel('ListItem.Label')
path = xbmc.getInfoLabel('ListItem.FileNameAndPath')
icon = xbmc.getInfoLabel('ListItem.Icon ')

url = "plugin://plugin.program.simple.folders/add_url/none/%s/%s/%s" % (urllib.quote_plus(title),urllib.quote_plus(path),urllib.quote_plus(icon))
xbmc.executebuiltin("PlayMedia(%s)" % url)
