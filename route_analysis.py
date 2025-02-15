import requests
import json
from requests.structures import CaseInsensitiveDict
import geopandas as gpd
from shapely.geometry import LineString
import warnings
warnings.simplefilter("ignore")
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


plt.savefig('sine_wave_chart.png')


#%matplotlib inline

from IPython.display import Image
Image(filename='images/sine_wave_chart.png')
