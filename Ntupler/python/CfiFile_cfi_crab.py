import sys
import FWCore.ParameterSet.Config as cms
import os

TFileService = cms.Service("TFileService", fileName = cms.string("SlimmedNtuple.root") )
#TFileService = cms.Service("TFileService", fileName = outputName )

print os.getcwd()

demo = cms.EDAnalyzer('Ntupler')
