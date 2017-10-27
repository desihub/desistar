#!/usr/bin/python
'''
Wrapper that calls FERRE (github.com/callendeprieto/ferre) to interpolate in a stellar spectral library

A collection of FERRE stellar libraries, specified in the "a" dictionary, and 
spanning overlapping Teff ranges, is used to interpolate and return a pair of 
arrays with wavelengths and model fluxes for a set of input atmospheric parameters 
params =(Teff, logg, [Fe/H])

Use (command line):
gettemplate teff logg feh

(python)
from  gettemplate import interpolate
x,y = interpolate([3500.,4.0,-1.0])

Author C. Allende Prieto

'''

import os
import sys
import numpy as np

#extract the header of a synthfile
def head_synth(synthfile):
    file=open(synthfile,'r')
    line=file.readline()
    header={}
    while (1):
        line=file.readline()
        part=line.split('=')
	if (len(part) < 2): break
        k=part[0].strip()
        v=part[1].strip()
	header[k]=v
    return header


#extract the wavelength array for a FERRE synth file
def lambda_synth(synthfile):
    header=head_synth(synthfile)
    tmp=header['WAVE'].split()
    npix=int(header['NPIX'])
    step=float(tmp[1])
    x0=float(tmp[0])
    x=np.arange(npix)*step+x0
    if header['LOGW']:
      if int(header['LOGW']) == 1: x=10.**x
      if int(header['LOGW']) == 2: x=exp(x)  
    return x
  
#interpolate
def interpolate(params):

    teff=float(params[0])
    logg=float(params[1])
    feh=float(params[2])


    #input parameters
    #teff=5800.
    #logg=2.3
    #feh=-1.2

    #filename  (minteff, maxteff, minlogg, maxlogg, minfeh, maxfeh, ndim, inter )
    a={ 'n_10kbt1.dat':(2600,3500.,2.5, 5.5, -2.5, 0.5, 3,3),
    'n_nsc1.dat':(3500,6000.,0.0, 5.0, -5.0, 0.5, 3,3),
    'n_nsc2.dat':(6000.,8000,1.0, 5.0, -5.0, 0.5, 3, 3),
    'n_nsc3.dat':(8000.,12000.,2.0, 5.0, -5.0, 0.5, 3, 3),
    'n_nsc4.dat':(12000.,20000.,3.0, 5.0, -5.0, 0.5, 3, 2),
    'n_nsc5.dat':(20000.,30000.,4.0, 5.0, -5.0, 0.5, 3, 1)
    }


    #identify appropriate filename depending on teff
    found=0
    for synthfile in a:
	if (teff > a[synthfile][0] and teff <=  a[synthfile][1] and logg > a[synthfile][2] and logg <= a[synthfile][3] and feh > a[synthfile][4] and feh <= a[synthfile][5]): 
		print  "for teff=",teff,"we'll use",synthfile
                found=1
		break

    if (found == 0): 
      print("error -- input values out of range")
      sys.exit(1)
    

    #write FERRE parameter file
    ffile=open('test.opf','w')
    if synthfile == 'n_10kbt1.dat':
      ffile.write('test   '+str(teff)+" "+str(logg)+" "+str(feh)+"\n")
    else:
      ffile.write('test   '+str(feh)+" "+str(teff)+" "+str(logg)+"\n")
    ffile.close()

    #write FERRE input file
    ffile=open('input.nml','w')
    ffile.write("&LISTA\n")
    ffile.write("NDIM="+str(a[synthfile][6])+"\n")
    ffile.write("NOV=0\n") #nov=0 <=> interpolation
    ffile.write("SYNTHFILE(1)='"+synthfile+"'\n")
    ffile.write("PFILE='test.opf'\n")
    ffile.write("OFFILE='test.frd'\n")
    ffile.write("F_FORMAT=1\n") #binary format (f_nsc?.unf)
    ffile.write("F_ACCESS=1\n") #access file as a direct access file (1) or loading it in ram (0)
    ffile.write("INTER="+str(a[synthfile][7])+"\n") # 1-linear 2-quadratic 3-cubic
    ffile.write(" /\n")
    ffile.close()


    #run ferre
    path="/home/callende/ferre/bin/"
    ferre="ferre.x"
    os.system(path+ferre)

    x=lambda_synth(synthfile)
    y=np.loadtxt('test.frd')
    return x,y
    
if __name__ == "__main__":

    if (len(sys.argv) == 1):
      print("syntax -- gettemplate teff logg feh ...")
      sys.exit(1)
    else:      
        params=sys.argv[1:]
        x,y = interpolate(params)
        f=open('test.dat','w')
        for i in range(x.size):
	  f.write(str(x[i])+' '+str(y[i])+"\n")
