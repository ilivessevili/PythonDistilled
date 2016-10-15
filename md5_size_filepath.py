#!/usr/local/env python
"""
Description:

Walk thru file recursively and write md5sum filesize filepath in md5_size_file.txt in current working dir.
eg:
==============================================================
92811660f0171a96716901eb9e4f8b6a 157 /root/test/novarc.188
35b3600e707b76da3fe6b3f7fbea2c2a 554 /root/test/md5_size_file.py
863b68a273d2decc5db2574bb10a3e0e 165 /root/test/novarc
d41d8cd98f00b204e9800998ecf8427e 0 /root/test/md5_size_file.txt
09ca8721b40a4649e0245ed4c90f3eb4 165 /root/test/novarc.191
09ca8721b40a4649e0245ed4c90f3eb4 165 /root/test/novarc-liberty
ae164c945acb2e50a4ec043d913df401 190 /root/test/md5.sh
==============================================================
"""

import os
import subprocess

top='/root/test'
with open('md5_size_file.txt','a') as f:
    for root,dirs,files in os.walk(top):
        for file_name in files:
            file_path=os.path.join(root,file_name)
            if os.path.isfile(file_path):
              #get md5
              output=subprocess.check_output(['md5sum', file_path])
              md5,filename=output.split()
              size=os.path.getsize(file_path)
              line=md5 + ' ' + str(size) + ' ' + file_path
              f.write(line +"\n")
