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
#config.JobType.maxMemoryMB = 760
config.JobType.outputFiles = ['SlimmedNtuple.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000

config.section_('Data')
#config.Data.ignoreLocality = True
#config.Data.lumiMask = '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/json_file_cms_2017.txt'
#config.Data.lumiMask = '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/combined_RPIN_CMS.json' #2017
config.Data.lumiMask = '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/CMSgolden_2RPGood_anyarms.json' #2018 
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased' #'FileBased'
#config.Data.splitting = 'LumiBased' #'FileBased'
#config.Data.splitting = 'Automatic' #'FileBased'
#config.Data.totalUnits = 100
#config.Data.unitsPerJob = 30000
config.Data.publication = False
config.Data.outputDatasetTag = 'data'

config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'
#config.Site.whitelist = ['T2_BE_IIHE','T2_BE_UCL','T2_CH_CSCS','T2_CN_Beijing','T2_DE_DESY','T2_EE_Estonia','T2_ES_CIEMAT','T2_ES_IFCA','T2_FI_HIP','T2_FR_IPHC','T2_HU_Budapest','T2_IN_TIFR','T2_IT_Bari','T2_IT_Legnaro','T2_IT_Pisa','T2_IT_Rome','T2_KR_KISTI','T2_RU_IHEP','T2_RU_JINR','T2_TR_METU','T2_TW_NCHC','T2_UK_SGrid_RALPP','T2_US_Caltech','T2_US_Florida','T2_US_MIT','T2_US_Nebraska','T2_US_Purdue','T2_US_UCSD','T2_US_Vanderbilt','T2_US_Wisconsin']
#config.Site.whitelist = ['T2_BE_IIHE','T2_CH_CSCS','T2_DE_DESY','T2_FI_HIP','T2_FR_IPHC','T2_IT_Bari','T2_IT_Pisa','T2_UK_SGrid_RALPP','T2_US_MIT','T2_US_Nebraska','T2_US_Purdue','T2_US_Vanderbilt','T2_US_Wisconsin']
#config.Site.whitelist = ['T2_BR_UERJ', 'T2_CN_Beijing', 'T2_ES_CIEMAT', 'T2_HU_Budapest',  'T2_IT_Legnaro', 'T2_IT_Rome', 'T2_UK_SGrid_RALPP', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_Wisconsin']
#config.Site.whitelist = ['T1_ES_PIC_Disk', 'T1_RU_JINR_Disk', 'T1_US_FNAL_Disk', 'T1_US_FNAL_Tape', 'T2_BR_UERJ', 'T2_CN_Beijing', 'T2_ES_CIEMAT', 'T2_HU_Budapest',  'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Rome', 'T2_UK_SGrid_RALPP', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_Wisconsin']

#config.Site.whitelist = ['T2_CH_*', 'T2_CN_*', 'T2_HU_*', 'T2_BE_*', 'T2_DE_*', 'T2_RU_*','T2_US_*','T2_IT_*', 'T2_ES_*', 'T2_UA_*', 'T1_US_*', 'T3_UK_*', 'T1_RU_*', 'T1_UK_*', 'T2_BR_UERJ']
config.Site.whitelist = ['T2_CH_CERN', 'T2_IN_TIFR', 'T3_US_FNALLPC']
#config.Site.blacklist = ['T2_US_Nebraska']
#config.Site.storageSite = 'T2_IT_Bari'

def submit(config):
   try:
      crabCommand('submit', config = config)
   except HTTPException as hte:
      print "Failed submitting task: %s" % (hte.headers)
   except ClientException as cle:
      print "Failed submitting task: %s" % (cle)

if __name__ == '__main__':

   ### Put MC = False, Run2_2017 = True and process.demo.isInteractive = cms.bool(False) at line 389 in ConfFile_cfg_crab.py
   ### Change to the specific ERA in ConfFile_cfg_MIGUEL.py

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleElectron_UL2017B_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunB_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunB_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunB_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleElectron/Run2017B-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleElectron_UL2017B_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleElectron_UL2017C_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunC_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunC_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunC_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleElectron/Run2017C-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleElectron_UL2017C_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleElectron_UL2017D_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunD_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunD_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunD_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleElectron/Run2017D-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleElectron_UL2017D_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleElectron_UL2017E_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunE_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunE_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunE_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleElectron/Run2017E-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleElectron_UL2017E_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleElectron_UL2017F_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunF_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunF_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunF_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleElectron/Run2017F-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleElectron_UL2017F_MiniAODv2-v1-newjson'
   #submit(config)

   config.JobType.psetName = 'ConfFile_cfg_crab.py'
   config.General.requestName = 'EGamma_UL2018A_MiniAODv2-v1-2'
   config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunA_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunA_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunA_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   config.Data.unitsPerJob = 29720
   config.Data.inputDataset = '/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD'
   config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/EGamma_UL2018A_MiniAODv2-v1'
   submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'EGamma_UL2018B_MiniAODv2-v1'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunB_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunB_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunB_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 17000
   #config.Data.inputDataset = '/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/EGamma_UL2018B_MiniAODv2-v1'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'EGamma_UL2018C_MiniAODv2-v1'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunC_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunC_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunC_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 17000
   #config.Data.inputDataset = '/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/EGamma_UL2018C_MiniAODv2-v1'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'EGamma_UL2018D_MiniAODv2-v2-2'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunD_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunD_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunD_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 71990
   #config.Data.inputDataset = '/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/EGamma_UL2018D_MiniAODv2-v2'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2017B_MiniAODv2-v1-newjson-2nd'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunB_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunB_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunB_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleMuon_UL2017B_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2017C_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunC_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunC_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunC_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleMuon_UL2017C_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2017D_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunD_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunD_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunD_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleMuon_UL2017D_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2017E_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunE_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunE_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunE_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleMuon_UL2017E_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2017F_MiniAODv2-v1-newjson'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2017.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2017_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunF_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunF_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2017-JEC-JER/Summer19UL17_RunF_V5_DATA_L2L3Residual_AK8PFchs.txt']
   #config.Data.inputDataset = '/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2017/SingleMuon_UL2017F_MiniAODv2-v1-newjson'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2018A_MiniAODv2-v3'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunA_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunA_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunA_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 25000
   #config.Data.inputDataset = '/SingleMuon/Run2018A-UL2018_MiniAODv2-v3/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/SingleMuon_UL2018A_MiniAODv2-v3'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2018B_MiniAODv2-v2'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunB_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunB_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunB_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 13000
   #config.Data.inputDataset = '/SingleMuon/Run2018B-UL2018_MiniAODv2-v2/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/SingleMuon_UL2018B_MiniAODv2-v2'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2018C_MiniAODv2-v2'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunC_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunC_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunC_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 13000
   #config.Data.inputDataset = '/SingleMuon/Run2018C-UL2018_MiniAODv2-v2/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/SingleMuon_UL2018C_MiniAODv2-v2'
   #submit(config)

   #config.JobType.psetName = 'ConfFile_cfg_crab.py'
   #config.General.requestName = 'SingleMuon_UL2018D_MiniAODv2-v3-2'
   #config.JobType.inputFiles = ['/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_data_2018.root','/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/PUHistos_mc_2018_UL.root', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunD_V5_DATA_L2Relative_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunD_V5_DATA_L3Absolute_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/SlimmedNtuple/Ntupler/python/2018-JEC-JER/Summer19UL18_RunD_V5_DATA_L2L3Residual_AK8PFchs.txt', '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_30/src/Roccor/RoccoR2018UL.txt']
   #config.Data.unitsPerJob = 49490
   #config.Data.inputDataset = '/SingleMuon/Run2018D-UL2018_MiniAODv2-v3/MINIAOD'
   #config.Data.outLFNDirBase = '/store/user/malvesga/WW/Data_2018/SingleMuon_UL2018D_MiniAODv2-v3'
   #submit(config)
