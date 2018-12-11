# Try out plotting pandas 

# Some imports needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Plot something
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

plt.plot(ts)
plt.show()

#ts.plot()

print(type(ts))
print("Goodbye")
# Expected output: <matplotlib.axes._subplots.AxesSubplot at 0x7f213444c048>