# braggpeak

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import numpy as np
import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill

# file = r"C:\Users\fjwry\Python_code\D1\research\microdosimetry\data\Braggpeak.out"
# file = r'C:\Users\fjwry\Python_code\D1\research\microdosimetry\data\Braggpeak.out'
folder = r'C:\Python\data\microdosimetry\Braggpeak\12Ctherapy'

names = ["PMMA","Titanium","gold"]
depth = np.linspace(0, 5, 999).tolist()
dose_data = {}
for i in names:
    file = os.path.join(folder, i, 'dose.out')
    print("Reading file:", file)
    # file = r"C:\Users\fujiwara21\OneDrive - OUMail (Osaka University)\microdosimetry_spectra\12C_source\Braggpeak\Braggpeak_"+ str(i)+".out"
    with open(file) as f:
        data = f.readlines()
        reading = False
        dose  = []
        for index, line in enumerate(data):
            if '#  z-lower      z-upper        all       r.err ' in line:
                reading = True
                continue
            elif '   2.4950E+00   2.5000E+00' in line:
                reading = False
                break
            if reading:
                dose.append(float(data[index].split()[2]))
        # print(dose)
        plt.plot(depth,dose,label=i)
        dose_data[i] = dose

df = pd.DataFrame({'Depth': depth, **dose_data})
#print(df)

# Excel ファイルに DataFrame を書き出す
# output_file = os.path.join(folder, 'dose_data.xlsx')  # Excel ファイルのパス
# df.to_excel(output_file, index=True)  # インデックスを含まないように設定

plt.xlabel('depth(cm)',fontsize = 15)
plt.ylabel('dose(Gy)',fontsize = 15)
x_major_locator = MultipleLocator(0.3)  # 0.5ごとに目盛りを表示
plt.gca().xaxis.set_major_locator(x_major_locator)
plt.xlim(0,5)
plt.legend()
plt.show()