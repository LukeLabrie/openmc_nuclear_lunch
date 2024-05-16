import matplotlib.pyplot as plt
from materials import create_materials
import openmc
import os

###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted)
###############################################################################

h5m_filepath = os.getcwd() + '/are.h5m'
operating_temperature = 977

#geometry
graveyard=openmc.Sphere(r=10000,boundary_type='vacuum')

cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True,universe_id=996 )
cad_cell = openmc.Cell(cell_id=997 , region= -graveyard, fill= cad_univ)
root = openmc.Universe(universe_id=998)
root.add_cells([cad_cell])
geometry = openmc.Geometry(root)
geometry.export_to_xml()

nuclear_data_filepath = os.environ['HOME'] + '/openmc/nuclear_data/mcnp_endfb71/cross_sections.xml'
mats = openmc.Materials(create_materials(operating_temperature))
mats.cross_sections = nuclear_data_filepath
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 1
settings.particles = 1000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

# tallies
tallies = openmc.Tallies()

model = openmc.model.Model(geometry, mats, settings, tallies)
sp_filename = model.run()

