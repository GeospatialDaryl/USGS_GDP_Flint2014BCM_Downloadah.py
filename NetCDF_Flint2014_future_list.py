import os


fileNC = urllib.URLopener()

for items in listFiles:
    print "Starting", items
            fileNC.retrieve(items,items.split('/')[-1])