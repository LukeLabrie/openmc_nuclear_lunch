import CAD_to_OpenMC.assembly as ab
a=ab.Assembly(['step_files/are_all.step'])
a.run(backend='stl2',h5m_filename='h5m_files/ARE.h5m')
