# HR and Blood Pressure Code
 
# Graph raw data (just for visualization)
import pandas as pd
import matplotlib.pyplot as plt
sample = pd.read_csv('muestra.csv')
y = sample['y'].values
plt.plot(y)
plt.show()

# Entry Variables for HR 
sample1 = sample['y'].values
sps = 25 

# Main function for getting Heart Rates
def HR(data,freq):
    peaks = [0] # Store Peaks
    rates = []  # Store HRs
    for i in range(1, len(data)):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    for i in range(1, len(peaks)): 
        dpp = peaks[i]-peaks[i-1]
        hr = (freq*60)/dpp 
        rates.append(round(hr))
    return peaks, rates  # used for visualization

# Graph for peaks visualization
peaks1, Hrates1 = HR(sample1, sps)
print("Peaks position:",peaks1)
print("Historical heart rates:",Hrates1)
x1 = []
for i in range(0,len(sample1)):
    x1.append(i)
plt.plot(x1, y)
etiquetas_x1 = [str(x) if x in peaks1 else '' for x in x1]
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.xticks(x1, etiquetas_x1 , rotation='vertical')
plt.show()