from pyopenms import *

mzXML = MzXMLFile()
exp = MSExperiment()
exp_picked = MSExperiment()
print(exp.getMinRT())
print(exp.getMaxRT())
params = Param()
a = MSSpectrum()
mzXML.load("../data/B2_IDA.mzXML",exp)
print("Finished Loading!")
gf = GaussFilter()
gf.filterExperiment(exp)
print("created a GuassFilter!")
mzXML.store("../data/B2_IDA.mzXML",exp)
