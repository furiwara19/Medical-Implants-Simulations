import matplotlib.pyplot as plt
import pandas as pd

def read_microdosimetric_spectra(file_path):
    target_data = []
    reading = False
    with open(file_path) as f:
        for line in f:
            if line.startswith('#  sed-lwr'):
                reading = True
                continue
            elif line.startswith('   9.2612E+03   1.0000E+04   0.0000E+00  0.0000'):
                reading = False
                break
            if reading:
                elements = line.split()
                target_data.append(elements)
    return target_data

def plot_microdosimetric_spectra(file_paths, names):
    for i, file_path in enumerate(file_paths):
        target_data = read_microdosimetric_spectra(file_path)
        print(target_data)
        energy = [float(item[0]) for item in target_data]
        energy_deposit = [float(item[2]) for item in target_data]
        total_deposit = sum(energy_deposit)
        normalized_deposit = [j / total_deposit for j in energy_deposit]
        plt.plot(energy, normalized_deposit, label=names[i])
    
def read_dose_mean(file_paths):
    mean_dose = []

    for file_path in file_paths:
        with open(file_path) as f:
            data = f.readlines()
            for index, line in enumerate(data):
                if '#               Dose mean    ' in line:
                    mean_dose.append(float(data[index].split()[3]))

    return mean_dose


# Define base path
base_path = r'C:\Python\data\microdosimetry\carbon_ion\step2\case5'


names = ["PMMA", "Ti", "gold"]
# Define file paths and names
file_paths_case_1 = [f'{base_path}\ydy_{i}.out' for i in names]
'''
file_paths_case_2 = [f'{base_path}\case2\ydy_{i}.out' for i in range(4)]
"file_paths_case_3 = [f'{base_path}\case3\ydy_{i}.out' for i in range(4)]
file_paths_case_4 = [f'{base_path}\case4\ydy_{i}.out' for i in range(4)]
#file_paths_case_5 = [f'{base_path}\case_5\ydy_{i}.out' for i in range(4)]
#file_paths_case_6 = [f'{base_path}\case_6\ydy_{i}.out' for i in range(4)]
# file_paths_case_7 = [f'{base_path}\case_7\ydy_{i}.out' for i in range(4)]

# Plot for case 2
plot_microdosimetric_spectra(axes[1], file_paths_case_2, names)
mean_dose_2 = read_dose_mean(file_paths_case_2)

plot_microdosimetric_spectra(axes[2], file_paths_case_3, names)
mean_dose_3 = read_dose_mean(file_paths_case_3)

plot_microdosimetric_spectra(axes[3], file_paths_case_4, names)
mean_dose_4 = read_dose_mean(file_paths_case_4)
'''

# Plot for case 1
plot_microdosimetric_spectra(file_paths_case_1, names)
mean_dose_1 = read_dose_mean(file_paths_case_1)



#plot_microdosimetric_spectra(axes[4], file_paths_case_5, names)
#mean_dose_5 = read_dose_mean(file_paths_case_5)

#plot_microdosimetric_spectra(axes[5], file_paths_case_6, names)
#mean_dose_6 = read_dose_mean(file_paths_case_6)

#plot_microdosimetric_spectra(axes[6], file_paths_case_7, names)
# mean_dose_7 = read_dose_mean(file_paths_case_7)

# plot_microdosimetric_spectra(axes[4], file_paths_case_5, names)


data = {'Name': names, 'Case 1': mean_dose_1}
df = pd.DataFrame(data = data)
excel_file_path = f'{base_path}\\mean_dose.xlsx'
df.to_excel(excel_file_path, index=False)


plt.xscale('log')
plt.legend()
plt.xlabel('y(keV/μm)',fontsize=12)
plt.ylabel('yd(y)',fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
