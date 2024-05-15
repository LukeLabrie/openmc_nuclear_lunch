# openmc_nuclear_lunch
1.) Install some dependencies. Note, package names may depend on os. The below are for ubuntu:
```bash
sudo apt-get install libgl1-mesa-glx python3.10-venv libglu1-mesa libxcursor1 libxinerama1
```
2.) Set up a python environment 
```bash
python3 -m venv <environment_name> 
```
3.) Activate the environment
```bash
source <environment_name>/bin/activate 
```
4.) Install some dependencies with pip
```bash
pip install numpy CAD_to_OpenMC
```
5.) Clone [openmc_install_scripts](https://github.com/openmsr/openmc_install_scripts)
```bash
git clone https://github.com/openmsr/openmc_install_scripts.git
```
6.) Go into the directory associated with your OS
```
cd openmc_install_scripts/<your-os>
```
7.) Install to your environment
```
./install-all.sh --prefix=$VIRTUAL_ENV
```
8.) Install the CAD_to_OpenMC converter tool to your virtual environment
```
pip install CAD_to_OpenMC
```
