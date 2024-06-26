import openmc

#This class attempts to mimic the fast, bare uranium, benchmark Godiva.
class split_GodivaI:
  def __init__(self, gap=1.0):
    self.materials = openmc.Materials.from_xml('xml/materials.xml')
    self.settings = openmc.Settings.from_xml('xml/settings.xml')
    self.gap=gap
    self.build_geometry()
    self.build_plots()
    self.build_model()

  def build_geometry(self):
    top_universe = openmc.DAGMCUniverse('godivaI_top.h5m', auto_geom_ids=True)
    bottom_universe = openmc.DAGMCUniverse('godivaI_bottom.h5m', auto_geom_ids=True)

    split_plane = openmc.ZPlane(z0=0.0)

    top_boundary = openmc.ZPlane(z0 = 100, boundary_type='vacuum')
    bottom_boundary = openmc.ZPlane(z0 = -100, boundary_type='vacuum')

    boundary_cylinder = openmc.ZCylinder(r=20, boundary_type='vacuum')

    top_cell=openmc.Cell()
    top_cell.region=-top_boundary & +split_plane & -boundary_cylinder
    top_cell.fill=top_universe
    top_cell.translation = [0.0, 0.0, self.gap/2.0]

    bottom_cell=openmc.Cell()
    bottom_cell.region=+bottom_boundary & -split_plane & -boundary_cylinder
    bottom_cell.fill=bottom_universe
    bottom_cell.translation = [0.0, 0.0, -self.gap/2.0]

    root=openmc.Universe()
    root.add_cells([top_cell,bottom_cell])

    self.geometry=openmc.Geometry(root)

  def build_plots(self):
    pyz=openmc.Plot().from_geometry(self.geometry)
    pyz.basis='yz'
    pyz.origin = (0.0, 0.0, 0.0)
    pyz.width = (20, 80)
    pyz.color_by = "material"
    pyz.pixels = (512, 1024)
    pyz.filename = f"godivaI_split_yz.png"

    self.plots = openmc.Plots([pyz])

  def build_model(self):
    model = openmc.Model(geometry = self.geometry, materials=self.materials, plots=self.plots, settings=self.settings)
    model.export_to_model_xml()


if __name__=='__main__':
  reactor=split_GodivaI(1.0)
