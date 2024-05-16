import CAD_to_OpenMC.assembly as ab
a=ab.Assembly(['are.step'])
a.run(backend='stl2',h5m_filename='are.h5m')
