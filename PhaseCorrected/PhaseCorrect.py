#!/usr/bin/env python

from os import path

def GetPhases(fname):
 f = open(fname)
 pd5,ps1,pd3,nd5,ns1,nd3 = -1,-1,-1,-1,-1,-1
 for line in f:
  if '!' in line: continue
  if '1   1   1   3    2   1' in line:
    if( float(line.split()[-1]) ) > 0:
      pd5 *= -1
      pd3 *= -1
  if '1   1   1   2    2   1' in line:
    if( float(line.split()[-1]) ) > 0:
      pd5 *= -1
      ps1 *= -1
  if '2   3   3   3    2   1' in line:
    if( float(line.split()[-1]) ) > 0:
      pd3 *= -1
      ps1 *= -1
  if '4   4   4   6    2   1' in line:
    if( float(line.split()[-1]) ) > 0:
      nd5 *= -1
      nd3 *= -1
  if '4   4   4   5    2   1' in line:
    if( float(line.split()[-1]) ) > 0:
      nd5 *= -1
      ns1 *= -1
  if '5   6   6   6    2   1' in line:
    if( float(line.split()[-1]) ) > 0:
      nd3 *= -1
      ns1 *= -1

 if pd5<0 and ps1<0 and pd3<0: pd5,ps1,pd3 = 1,1,1
 if nd5<0 and ns1<0 and nd3<0: nd5,ns1,nd3 = 1,1,1
 print fname,(pd5,ps1,pd3,nd5,ns1,nd3)
 return (pd5,ps1,pd3,nd5,ns1,nd3)


def PhaseCorrect(fname, phases, output):
 f = open(fname)
 fout = open(output,'w')
 for line in f:
  if '!' in line:
#    print line.strip('\n')
    fout.write(line)
    continue
  ldat = line.split()
  if len(ldat) > 7:
#    print line.strip('\n')
    fout.write(line)
    continue
  a,b,c,d,J,T = [int(x) for x in ldat[:6]]
  v = float(ldat[6])
  phasefactor = phases[a-1]*phases[b-1]*phases[c-1]*phases[d-1]
#  print '%3d %3d %3d %3d  %3d  %3d  %10.6f'%(a,b,c,d,J,T,v*phasefactor)
  fout.write('%3d %3d %3d %3d  %3d %3d  %10.6f\n'%(a,b,c,d,J,T,v*phasefactor))


for hw in [20,24]:
 for A in range(17,35):
  fname = '../SD_e14_hw%d_A%d.int'%(hw,A)
  output = 'SD_e14_hw%d_A%d_phase_corrected.int'%(hw,A)
  if not path.exists(fname): continue
  phases = GetPhases(fname)
  PhaseCorrect(fname,phases, output)


