import openmc

#This class attempts to mimic the fast, bare uranium, benchmark Godiva.
class spherical_GodivaI:
  def __init__(self):
    self.materials = openmc.Materials.from_xml('xml/materials.xml')
    self.settings = openmc.Settings.from_xml('xml/settings.xml')
    self.build_geometry()
    self.build_plots()
    self.build_model()

  def build_geometry(self):
    dagmc_universe = openmc.DAGMCUniverse('godivaI_sphere.h5m', auto_geom_ids=True)
    #boundary = openmc.Sphere(r=25)
    boundary=dagmc_universe.bounding_region(bounded_type='sphere')
    cell=openmc.Cell()
    cell.region=boundary
    cell.fill=dagmc_universe

    root=openmc.Universe()
    root.add_cell(cell)

    self.geometry=openmc.Geometry(root)

  def build_plots(self):
    pyz=openmc.Plot().from_geometry(self.geometry)
    pyz.basis='yz'
    pyz.origin = (0.0, 0.0, 0.0)
    pyz.width = (20, 20)
    pyz.color_by = "material"
    pyz.pixels = (512, 512)
    pyz.filename = f"godivaI_full_yz.png"

    self.plots = openmc.Plots([pyz])

  def build_model(self):
    model = openmc.Model(geometry = self.geometry, materials=self.materials, plots=self.plots, settings=self.settings)
    model.export_to_model_xml()


if __name__=='__main__':
  reactor=spherical_GodivaI()
