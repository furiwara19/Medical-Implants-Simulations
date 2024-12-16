# plot secondary particles spectra

import matplotlib.pyplot as plt
import os

materials = ['PMMA', 'Titanium','Gold']
source    = ['proton', 'carbon_ion']

def spectra(file_path):
    energy  = []
    results = []
    with open(file_path, errors='ignore') as f:
        data = f.readlines()
        reading = False
        for index, line in enumerate(data):
            if line.startswith('#  e-lower      e-upper        all       r.err'):
                reading = True
            elif '#   sum over' in line:
                reading = False
                break
            if reading:
                try:
                    split_line = data[index + 1].split()
                    energy.append(float(split_line[0]))
                    results.append(float(split_line[2]))
                except (IndexError, ValueError) as e:
                    print(f"Error parsing line {index + 1} in {file_path}: {e}")
                    continue  # データが正しくない場合はスキップ
    return energy, results


# ベースディレクトリ
base_dir = r"C:\Python\data\microdosimetry"

# フォルダパスをループで生成
for particle in source:
    folder_path = os.path.join(base_dir, particle, "secondary_particles")
    for m in materials:
        file_path = os.path.join(folder_path, f"secondary_particles_{m}_{particle}.out")
        print(file_path)
        energy, results = spectra(file_path)
        plt.plot(energy, results, label= f'{m}')
    if particle == 'carbon_ion':
        plt.xlabel('Energy (MeV/u)', fontsize=14)
    else:
        plt.xlabel('Energy (MeV)', fontsize=14)
    plt.ylabel('Flux (1/cm²/source)', fontsize=14)
    plt.xscale('log')
    plt.legend()
    plt.show()
            
# 粒子ごとの寄与を計算
def spectra_particles(file_path):
    energy           = []
    results_all      = []
    results_alpha    = []
    results_photon   = []
    results_electron = []
    results_neutron  = []
    with open(file_path, errors='ignore') as f:
        data = f.readlines()
        reading = False
        for index, line in enumerate(data):
            if line.startswith('#  e-lower      e-upper        all       r.err'):
                reading = True
            elif '#   sum over' in line:
                reading = False
                break
            if reading:
                try:
                    split_line = data[index + 1].split()
                    energy.append(float(split_line[0]))
                    results_all.append(float(split_line[2]))
                    results_alpha.append(float(split_line[6]))
                    results_photon.append(float(split_line[10]))
                    results_electron.append(float(split_line[12]))
                    results_neutron.append(float(split_line[14]))
                except (IndexError, ValueError) as e:
                    print(f"Error parsing line {index + 1} in {file_path}: {e}")
                    continue  # データが正しくない場合はスキップ
        plt.plot(energy, results_all, label= 'all_particles')
        plt.plot(energy, results_alpha, label= 'alpha_ray')
        plt.plot(energy, results_photon, label= 'photon')
        plt.plot(energy, results_electron, label= 'electron')
        plt.plot(energy, results_neutron, label= 'neutron')
    plt.xlabel('Energy (MeV)', fontsize=14)
    plt.ylabel('Flux (1/cm²/source)', fontsize=14)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

file_path = os.path.join(base_dir, 'proton','secondary_particles', 'secondary_particles_PMMA_proton.out')
spectra_particles(file_path)

file_path = os.path.join(base_dir, 'proton','secondary_particles', 'secondary_particles_Titanium_proton.out')
spectra_particles(file_path)



