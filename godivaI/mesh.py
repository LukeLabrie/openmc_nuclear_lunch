import CAD_to_OpenMC.assembly as ab
GI_full = ab.Assembly(['godivaI_full.step'])
GI_full.run(backend='stl2', h5m_filename='godivaI_full.h5m')

GI_top = ab.Assembly(['godivaI_top.step'])
GI_top.run(backend='stl2', h5m_filename='godivaI_top.h5m')

GI_bottom = ab.Assembly(['godivaI_bottom.step'])
GI_bottom.run(backend='stl2', h5m_filename='godivaI_bottom.h5m')


