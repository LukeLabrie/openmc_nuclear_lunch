import matplotlib.pyplot as plt
import openmc
from materials import create_materials
import os

###############################################################################
#create .png file of neutron flux (all safety rods inserted)
###############################################################################

#Geometry
h5m_filepath = 'are.h5m'
graveyard=openmc.Sphere(r=10000,boundary_type='vacuum')
cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True,universe_id=996 )
cad_cell = openmc.Cell(cell_id=997 , region= -graveyard, fill= cad_univ)
root = openmc.Universe(universe_id=998)
root.add_cells([cad_cell])
geometry = openmc.Geometry(root)
geometry.export_to_xml()

#materials
mats = openmc.Materials(create_materials(operating_temp=977))
nuclear_data_filepath = os.environ['HOME'] + '/openmc/nuclear_data/mcnp_endfb71/cross_sections.xml'
mats.cross_sections = nuclear_data_filepath
mats.export_to_xml()

#settings
settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 50
settings.inactive = 20
settings.particles = 40000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#tallies
tallies = openmc.Tallies()

# resolution
res = 500

mesh = openmc.RegularMesh()
mesh.dimension = [res,res,res]
mesh.lower_left = [-72,-70,-15]
mesh.upper_right = [72,70,115]

mesh_filter = openmc.MeshFilter(mesh)

tally = openmc.Tally(name='flux')
tally.filters = [mesh_filter]
tally.scores = ['flux'] # ,'fission']
tallies.append(tally)

tallies.export_to_xml()

model = openmc.model.Model(geometry, mats, settings, tallies)
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)

s_tally = sp.get_tally(scores=['flux']) #,'fission'])
flux = s_tally.get_slice(scores=['flux'])

flux.std_dev.shape = (res,res,res)
flux.mean.shape = (res,res,res)


split_index = int(res/2)

# flux
# xy plot
xy_mean = flux.mean[split_index,:,:]
fig,ax = plt.subplots()
pos = ax.imshow(xy_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Y / cm')
ax.set_title('mean neutron flux: xy plane')
plt.colorbar(pos,ax=ax,label=r'Flux [neutrons/cm$^2$-s]')
plt.savefig('neutron_flux_xy')

# xz plot
xz_mean = flux.mean[:,split_index, :]
fig,ax = plt.subplots(figsize=(2*4.41, 2*5.12))
pos = ax.imshow(xz_mean)
ax.set_xlabel('X / cm',fontsize=14)
ax.set_ylabel('Z / cm',fontsize=14)
ax.set_title('mean neutron flux: xz plane',fontsize=20)
plt.colorbar(pos,ax=ax,label=r'Flux [neutrons/cm$^2$-s]')
plt.savefig('neutron_flux_xz')

# yz plot
yz_mean = flux.mean[:,:,split_index]
fig,ax = plt.subplots()
pos = ax.imshow(yz_mean)
ax.set_xlabel('Y / cm')
ax.set_ylabel('Z / cm')
ax.set_title('mean neutron flux: yz plane')
plt.colorbar(pos, ax=ax,label=r'Flux [neutrons/cm$^2$-s]')
plt.savefig('neutron_flux_yz')
