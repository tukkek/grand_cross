#!/usr/bin/python2.7
import itertools,sys,os,glob
from multiprocessing.pool import ThreadPool

if len(sys.argv[1:])<2:
  print('Usage: '+sys.argv[0]+' "command" "rom"')
  sys.exit()

FLAGS='abcdilmopqsty'
RESUME=False
DELETE=False

COMMAND=sys.argv[1]
ROM=sys.argv[2]
KEEP=glob.glob('*')
POOL=ThreadPool(1 if DELETE else None)
RUNS=[]

abort=False

def test(flags):
  if abort:
    return
  command=COMMAND+' "'+ROM+'" '+flags
  if os.system(command)!=0:
    print('Error running: '+command)
    global abort
    abort=True
  if DELETE:
    for f in glob.glob('*'):
      if not f in KEEP:
        os.system('rm "'+f+'"')

for n in range(1,len(FLAGS)+1):
  for f in itertools.combinations(FLAGS,n):
    f=''.join(f)
    if RESUME and f!=RESUME:
      continue
    RESUME=False
    RUNS.append(f)
POOL.map(test,RUNS)
