# openmc_nuclear_lunch

1.) Set up a python environment 
```bash
python3 -m venv <environment_name> 
```
2.) Activate the environment
```bash
source <environment_name>/bin/activate 
```
3.) Clone [openmc_install_scripts](https://github.com/openmsr/openmc_install_scripts)
```bash
git clone https://github.com/openmsr/openmc_install_scripts.git
```
4.) Go into the directory associated with your OS
```
cd openmc_install_scripts/<your-os>
```
5.) Install to your environment
```
./install-all.sh --prefix=$VIRTUAL_ENV
```
