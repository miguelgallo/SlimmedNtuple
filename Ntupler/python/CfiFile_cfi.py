import sys
import FWCore.ParameterSet.Config as cms
import os

for arg in sys.argv[2:]:
  opt = arg[0:arg.find("=")]
  if opt=="outputName":
    outputName = cms.string(arg[arg.find("=")+1:])

#TFileService = cms.Service("TFileService", fileName = cms.string("SlimmedNtuple.root") )
TFileService = cms.Service("TFileService", fileName = outputName )

print os.getcwd()

demo = cms.EDAnalyzer('Ntupler')
