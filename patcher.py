#!/usr/bin/python3
import ips #`pip3 install python-ips`
import os,sys

ROM=len(sys.argv)>=2 and sys.argv[1]
PATCHES=sys.argv[2:]

if len(PATCHES)<1:
  print('Usage: rom.smc [patch1.ips patch2.ips ...]')
  sys.exit(1)

romname=ROM.rsplit('.',1)
filename=f"{romname[0]}.{'.'.join([os.path.basename(p).replace('.ips','') for p in PATCHES])}.{romname[1]}"
os.system(f'cp "{ROM}" "{filename}"')
for p in PATCHES:
  print(f'Applying {p}...')
  ips.apply(p,filename)
print(f'{filename} is ready!')
