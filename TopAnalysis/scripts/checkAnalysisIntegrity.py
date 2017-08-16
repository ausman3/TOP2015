#!/usr/bin/env python

import sys
import os

FARMDIR,OUTDIR=sys.argv[1:]

#check if there is one ROOT file per job script
scriptFiles = [f for f in os.listdir(FARMDIR) if os.path.isfile(os.path.join(FARMDIR, f)) and os.path.splitext(f)[1]=='.sh']
toRun=[]
for script in scriptFiles:
    if os.path.isfile(os.path.join(OUTDIR, script.replace('.sh','.root'))): continue
    toRun.append( os.path.splitext(script)[0] )
print 'There are %d/%d outputs missing, will resubmit them on condor'%(len(toRun),len(scriptFiles))

#create a new condor script
condor=open(os.path.join(FARMDIR,'condor.sub'),'r')
newCondorName=os.path.join(FARMDIR,'condor_resub.sub')
newCondor=open(newCondorName,'w')
for line in condor:
    if 'jobName=' in line: break
    newCondor.write(line)
for jobName in toRun:
    newCondor.write('jobName=%s\n'%jobName)
    newCondor.write('queue 1\n')
condor.close()
newCondor.close()

#submit jobs
print 'Resubmitting to condor from',newCondorName
os.system('condor_submit %s'%newCondorName)
