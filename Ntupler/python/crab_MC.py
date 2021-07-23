#from CRABClient.UserUtiilities import config, getUsernameFromSiteDB

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

# We want to put all the CRAB project directories from the tasks we submit here into one common directory.
# That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

from WMCore.Configuration import Configuration

config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ConfFile_cfg_2017.py'
#config.JobType.maxMemoryMB = 760
config.JobType.outputFiles = ['SlimmedNtuple.root']
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased' #'FileBased'
#config.Data.splitting = 'Automatic' #'FileBased'
#config.Data.totalUnits = 100
config.Data.publication = False

config.section_('Site')
config.Site.storageSite = 'T2_BR_UERJ'
config.Site.whitelist = ['T2_CH_*','T2_BE_*', 'T2_DE_*', 'T2_RU_*','T2_US_*', 'T2_IT_*', 'T2_ES_*', 'T2_UA_*', 'T1_US_*', 'T3_UK_*', 'T1_RU_*', 'T1_UK_*']
#config.Site.storageSite = 'T2_IT_Bari'

def submit(config):
   try:
      crabCommand('submit', config = config)
   except HTTPException as hte:
      print "Failed submitting task: %s" % (hte.headers)
   except ClientException as cle:
      print "Failed submitting task: %s" % (cle)

if __name__ == '__main__':

   config.General.requestName = 'TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8-RunIISummer20UL17MiniAOD-preTS2'
   #config.JobType.inputFiles = ['/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/proton_simulation_validation/settings/2017_preTS2/direct_simu_reco_cff.py','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_data.root','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_mc.root']
   config.JobType.inputFiles = ['/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/proton_simulation_validation/settings/2017_preTS2/direct_simu_reco_cff.py','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_data.root','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_mc.root', '/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_20/src/Validation/CTPPS/alignment/2017_preTS2.xml','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_17Nov2017_V32_MC_L1FastJet_AK8PFchs.txt', '/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_17Nov2017_V32_MC_L2Relative_AK8PFchs.txt', '/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_17Nov2017_V32_MC_L3Absolute_AK8PFchs.txt', '/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_V3_MC_PtResolution_AK4PFchs.txt', '/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_V3_MC_PtResolution_AK8PFchs.txt', '/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_V3_MC_SF_AK4PFchs.txt', '/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Fall17_V3_MC_SF_AK8PFchs.txt']
   config.Data.unitsPerJob = 30000
   config.Data.inputDataset = '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM'
   config.Data.outLFNDirBase = '/store/user/malvesga/miniaod/WW_2017/MC/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8-RunIISummer20UL17MiniAOD-preTS2'
   submit(config)

   #config.General.requestName = 'TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8-RunIISummer20UL17MiniAOD-postTS2'
   #config.JobType.inputFiles = ['/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/proton_simulation_validation/settings/2017_preTS2/direct_simu_reco_cff.py','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_data.root','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_mc.root']
   #config.JobType.inputFiles = ['direct_simu_reco_cff_2017_postTS2.py','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_data.root','/home/malvesga/Ntuple_build/CMSSW_10_6_20/src/SlimmedNtuple/Ntupler/python/PUHistos_mc.root']
   #config.Data.unitsPerJob = 5000
   #config.Data.inputDataset = '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM'
   #config.Data.outLFNDirBase = '/store/user/malvesga/miniaod/WW_2017/MC/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8-RunIISummer20UL17MiniAOD-postTS2'
   #submit(config)
