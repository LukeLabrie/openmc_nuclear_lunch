import CAD_to_OpenMC.assembly as ab
GI_full = ab.Assembly(['step_files/godivaI_sphere.step'])
GI_full.run(backend='stl2', h5m_filename='godivaI_sphere.h5m')

GI_top = ab.Assembly(['step_files/godivaI_top.step'])
GI_top.run(backend='stl2', h5m_filename='godivaI_top.h5m')

GI_bottom = ab.Assembly(['step_files/godivaI_bottom.step'])
GI_bottom.run(backend='stl2', h5m_filename='godivaI_bottom.h5m')


