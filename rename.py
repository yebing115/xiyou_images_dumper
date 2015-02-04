#!/usr/bin/python

import glob
import os

if __name__ == '__main__':
    names = glob.glob('*-*-*-*-*')
    for name in names:
        f = open(name, 'r')
        content = f.read(0x10)
        f.close()
        if content.find('plist') >= 0:
            os.rename(name, name + '.plist')
        elif content.find('WEBP') >= 0:
            os.rename(name, name + '.webp')
        elif content.find('PNG') >= 0:
            os.rename(name, name + '.png')
        elif content.find('xml') >= 0:
            os.rename(name, name + '.plist')
        elif content.find('ibcc') >= 0:
            os.rename(name, name + '.ccbi')
        elif content.find('SQL') >= 0:
            os.rename(name, name + '.sql')
        elif content.find('PKM') >= 0:
            os.rename(name, name + '.pkm')
        elif content.find('CCZ') >= 0:
            os.rename(name, name + '.pvr.ccz')
