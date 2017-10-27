import gettemplate
import matplotlib.pyplot  as plt
import random

for val in range(10):
  teff=random.randint(2601,30000.)
  logg=4.5
  feh=-random.randint(0,2)
  x,y=gettemplate.interpolate((teff,logg,feh))
  plt.plot(x,y)

plt.show()

