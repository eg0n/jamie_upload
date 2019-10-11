#!/usr/bin/env python3

import csv, subprocess

with open('upload.csv', 'r') as iafile:
    iacsv = csv.reader(iafile)
    for row in iacsv:
        item = row[6]
        if (item == 'identifier'): continue
        subprocess.run("./ia download -d -f \"VBR MP3\" %s" % item, shell='True')
