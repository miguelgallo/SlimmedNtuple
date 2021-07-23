import sys
import FWCore.ParameterSet.Config as cms
#process = cms.Process("Demo")
#process = cms.Process("CTPPSTestProtonReconstruction", eras.ctpps_2016)
#from Configuration.StandardSequences.Eras import eras
#process = cms.Process("Demo", eras.Run2_2017)

Run2_2017=True
MC=True
DATA=False
preTS2=True
postTS2=False
if Run2_2017 and MC and preTS2:
  sys.path.insert(0, '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_20/src/proton_simulation_validation/settings/2017_preTS2/')
  import direct_simu_reco_cff as profile
  process = cms.Process('CTPPSTest', profile.era)
  profile.LoadConfig(process)
  profile.config.SetDefaults(process)
  process.load("CalibPPS.ESProducers.ctppsBeamParametersESSource_cfi")
  process.load("Validation.CTPPS.simu_config.year_2017_preTS2_cff")
  process.load("direct_simu_reco_cff")
elif Run2_2017 and MC and postTS2:
  sys.path.insert(0, '/afs/cern.ch/user/m/malvesga/work/ProtonRecon/TEST/CMSSW_10_6_20/src/proton_simulation_validation/settings/2017_postTS2/')
  import direct_simu_reco_cff as profile
  process = cms.Process('CTPPSTest', profile.era)
  profile.LoadConfig(process)
  profile.config.SetDefaults(process)
  process.load("CalibPPS.ESProducers.ctppsBeamParametersESSource_cfi")
  process.load("Validation.CTPPS.simu_config.year_2017_postTS2_cff")
  process.load("direct_simu_reco_cff")
else:
  process = cms.Process("CTPPSTestProtonReconstruction", eras.ctpps_2017)

#process.Timing = cms.Service("Timing",
#  summaryOnly = cms.untracked.bool(False),
#  useJobReport = cms.untracked.bool(True)
#)

#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#    ignoreTotal = cms.untracked.int32(1)
#)

#Details for this here https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
#from FWCore.ParameterSet.VarParsing import VarParsing
#options = VarParsing ('analysis')
#options.register('pileupName',
#                 'WJetsToLNu_2J_TuneCP5_13TeV_amcatnloFXFX_pythia8',
#                 VarParsing.multiplicity.singleton,
#                 VarParsing.varType.string,
#                 "Name for pileup sample")
#options.register('era',
#                 'C',
#                 VarParsing.multiplicity.singleton,
#                 VarParsing.varType.string,
#                 "Era")
#options.register('interactive',
#                 1,
#                 VarParsing.multiplicity.singleton,
#                 VarParsing.varType.int,
#                 "Determines whether it is an interactive or crab run")
#options.parseArguments()

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(2000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

if MC:
  process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      #This file below is from /GGToWW_bSM-A0W1e-6_13TeV-fpmc-herwig6/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM
      #"file:/home/users/rebassoo/work/2019_07_02_JanRecent-2ndTry/CMSSW_10_6_0/src/test-Finn/062366B6-DF2B-E911-BB28-C45444922958.root"
      #"root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4C6E31C1-1742-E811-9CE3-002590491B22.root"
      #"root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/FE7ABAEB-4A42-E811-87A3-0CC47AD98D26.root"
      #'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/0299C20A-7736-E811-ABC8-008CFAE453D8.root'
      #"root://cms-xrd-global.cern.ch//store/mc/RunIISummer19UL17MiniAODv2/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/00BCF6C2-D719-184F-9CEF-EE252E6F37BD.root"
      "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/00BDA6DC-2D12-6D45-B837-9D7C71AB9CDB.root"
    )
  )


if not MC:
  process.source = cms.Source("PoolSource",
      fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/MINIAOD/31Mar2018-v1/30000/EA6122AF-1137-E811-B552-FA163E28D344.root'
        #'file:EA6122AF-1137-E811-B552-FA163E28D344.root'
        #'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/MINIAOD/31Mar2018-v1/30000/34D2D750-5037-E811-B6AA-FA163E516F5B.root'
        #'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAOD/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/0299C20A-7736-E811-ABC8-008CFAE453D8.root'
        #'root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/B4005649-E955-E811-BE7B-0CC47A7C353E.root'
        #'root://cmsxrootd.fnal.gov//store/mc/RunIIFall17MiniAODv2/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/00469E05-E055-E811-807F-008CFAF7174A.root'
      ),
      secondaryFileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/1C82A25C-C8D8-E711-8FA6-02163E019B54.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/40564C61-C2D8-E711-91A7-02163E019CDB.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40005/18E6A929-10DA-E711-B4DE-02163E019BF5.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40005/4CBF455E-0FDA-E711-8573-02163E01352C.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40005/545B0594-11DA-E711-88BE-02163E019CD8.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40005/687423EA-15DA-E711-A0A6-02163E019C95.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40005/C0D24DD8-05DA-E711-ACC4-02163E011B0D.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/60002/8852ED33-F6D8-E711-8FA2-02163E01A6C4.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/60002/944EA579-FAD8-E711-BD8B-02163E014737.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/60002/EA4A4045-F6D8-E711-A4D5-02163E01A35D.root',
        'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/60002/F03EBC89-FAD8-E711-BCB3-02163E011A7C.root'
      )#,
      #skipEvents=cms.untracked.uint32(2000)
  )

process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CaloEventSetup.CaloTowerConstituents_cfi")
process.load('Configuration.StandardSequences.GeometryDB_cff')

process.load("SlimmedNtuple.Ntupler.CfiFile_cfi")
process.load("SlimmedNtuple.Ntupler.HLTFilter_cfi")
process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.load("SlimmedNtuple.Ntupler.METFilter_cfi")

#from HLTrigger.HLTfilters.hltHighLevel_cfi import *
#process.hltFilter = copy.deepcopy(hltHighLevel)
#process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
#process.hltFilter.HLTPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele32_WPTight_Gsf_v*', 'HLT_IsoMu27_v*','HLT_IsoMu24_v*']
#process.hltFilter.throw = cms.bool(False)
#process.hltFilter.andOr = cms.bool(True) # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true

#process.METFilter = copy.deepcopy(hltHighLevel) #HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
#if MC:
#   process.METFilter.TriggerResultsTag =  cms.InputTag("TriggerResults","","PAT") # cms.InputTag("TriggerResults","","RECO")
#   process.METFilter.HLTPaths = ['Flag_goodVertices','Flag_HBHENoiseFilter','Flag_HBHENoiseIsoFilter','Flag_EcalDeadCellTriggerPrimitiveFilter','Flag_BadPFMuonFilter','Flag_BadChargedCandidateFilter']
#
#else:
#   process.METFilter.TriggerResultsTag =  cms.InputTag("TriggerResults","","RECO")
#   process.METFilter.HLTPaths = ['Flag_goodVertices','Flag_globalSuperTightHalo2016Filter','Flag_HBHENoiseFilter','Flag_HBHENoiseIsoFilter','Flag_EcalDeadCellTriggerPrimitiveFilter','Flag_BadPFMuonFilter','Flag_BadChargedCandidateFilter','Flag_eeBadScFilter'] #MC
#
#   process.METFilter.throw = cms.bool(False) # throw exception on unknown path names
#   process.METFilter.andOr = cms.bool(False) # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
#   # Filters from here: https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2
#   # MET filter recommendations will be updated for UltraLegacy datasets. The filters are currently under review and it is likely that the recommendations for ECAL related filters will change. Updates recommendations to be released as soon as they are available.


#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag


# If using full proton re-reco (legacy) - local RP reconstruction chain with standard settings         
process.load("RecoCTPPS.Configuration.recoCTPPS_cff")
#process.ctppsLocalTrackLiteProducer.includePixels = cms.bool(True)
#process.ctppsLocalTrackLiteProducer.includeStrips = cms.bool(True)
##process.ctppsLocalTrackLiteProducer.includeDiamonds = cms.bool(True)
#process.ctppsProtons.doSingleRPReconstruction = cms.bool(True)
#process.ctppsProtons.tagLocalTrackLite = cms.InputTag("ctppsLocalTrackLiteProducer","","Demo")


# remove locally-defined conditions -> consume conditions from GT
#del process.ctppsOpticalFunctionsESSource
#del process.esPreferLocalOptics

#del process.ctppsRPAlignmentCorrectionsDataESSourceXML
#del process.esPreferLocalAlignment

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
        beamDivergenceVtxGenerator = cms.PSet(initialSeed =cms.untracked.uint32(849))
        )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag

# define global tag (for LHC data reconstruction)
if not MC:
  process.GlobalTag = GlobalTag(process.GlobalTag, "106X_dataRun2_v11")
  #process.GlobalTag = GlobalTag(process.GlobalTag, "106X_dataRun2_v32")

# conditions for simu are not DB, load them from local sources
if MC:
  # load base settings

  #process.GlobalTag = GlobalTag(process.GlobalTag, "94X_mc2017_realistic_v17")
  process.GlobalTag = GlobalTag(process.GlobalTag, "106X_mc2017_realistic_v8")

  # update settings of beam-smearing module
  process.beamDivergenceVtxGenerator.src = cms.InputTag("")
  process.beamDivergenceVtxGenerator.srcGenParticle = cms.VInputTag(
    #cms.InputTag("genPUProtons", "genPUProtons"), (?)
    cms.InputTag("prunedGenParticles")
  )

  # do not apply vertex smearing again
  process.ctppsBeamParametersESSource.vtxStddevX = 0
  process.ctppsBeamParametersESSource.vtxStddevY = 0
  process.ctppsBeamParametersESSource.vtxStddevZ = 0

  # undo CMS vertex shift
  process.ctppsBeamParametersESSource.vtxOffsetX45 = +0.024755 
  process.ctppsBeamParametersESSource.vtxOffsetY45 = -0.069233
  process.ctppsBeamParametersESSource.vtxOffsetZ45 = -0.82054

  # define alignment
  #process.ctppsRPAlignmentCorrectionsDataESSourceXML.MisalignedFiles = ["test-Finn/alignment.xml"]
  #process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles = ["test-Finn/alignment.xml"]

  # update reco settings
  #process.totemRPUVPatternFinder.tagRecHit = cms.InputTag('ctppsDirectProtonSimulation')
  #process.ctppsPixelLocalTracks.label = "ctppsDirectProtonSimulation"
  #process.ctppsLocalTrackLiteProducer.includeDiamonds = False

  #def UseCrossingAngle(xangle):
  #  process.ctppsLHCInfoESSource.xangle = xangle
  #  process.ctppsBeamParametersESSource.halfXangleX45 = xangle * 1E-6
  #  process.ctppsBeamParametersESSource.halfXangleX56 = xangle * 1E-6

  #UseCrossingAngle(150)

##Global tags from here:https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
##To print out global tag: conddb list 94X_mc2017_realistic_v16
##For v16 global tag uses v23 of Jet energy corrections. Newest is 32.
#if MC:
#    process.GlobalTag.globaltag ='94X_mc2017_realistic_v17'
#else:
#    #process.GlobalTag.globaltag ='94X_dataRun2_v11'
#    #process.GlobalTag.globaltag ='106X_dataRun2_testPPS_v1'
#    process.GlobalTag.globaltag ='106X_dataRun2_v11'


### ADD SOME NEW JET COLLECTIONS                                                                                                              
# New (March 8, 2019) - to recover ak8 CHS jets with 2017 MiniAOD
#################################
  ###  JET TOOLBOX FOR CHS ###
#################################
# AK R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging                                                            
from JMEAnalysis.JetToolbox.jetToolbox_cff import *
jetToolbox( process, 'ak8', 'ak8JetSubs', 'noOutput',
#jetToolbox( process, 'ak8', 'jetSequence', 'noOutput',
                PUMethod='CHS',runOnMC=MC,
                addPruning=True, addSoftDrop=False ,           # add basic grooming                                                            
                addTrimming=False, addFiltering=False,
                addSoftDropSubjets=False,
                addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4                                      
                Cut='pt > 100.0',
                bTagDiscriminators=['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
                #bTagDiscriminators=['pfCombinedSecondaryVertexV2BJetTags'],
                # added L1FastJet on top of the example config file
                JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']
                )

jetToolbox( process, 'ak4', 'ak4JetSubs', 'noOutput',
#jetToolbox( process, 'ak4', 'jetSequence', 'noOutput',
                PUMethod='CHS',runOnMC=MC,
                addPruning=True, addSoftDrop=False ,           # add basic grooming                                                            
                addTrimming=False, addFiltering=False,
                addSoftDropSubjets=False,
                addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4                                      
                Cut='pt > 10.0',
                bTagDiscriminators=['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
                #bTagDiscriminators=['pfCombinedSecondaryVertexV2BJetTags'],
                # added L1FastJet on top of the example config file
                JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']
                )


if MC:
    #################################
    ###  JER SMEARING AK8###
    #################################
    COLLECTIONTOSMEARAK8="selectedPatJetsAK8PFCHS"
    from RecoMET.METProducers.METSigParams_cfi import *
    process.slimmedAK8JetsSmeared = cms.EDProducer('SmearedPATJetProducer',
        src = cms.InputTag(COLLECTIONTOSMEARAK8),
        enabled = cms.bool(True),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        algo = cms.string('AK8PFchs'),
        algopt = cms.string('AK8PFchs_pt'),

        genJets = cms.InputTag('slimmedGenJets'),
        dRMax = cms.double(0.2),
        dPtMaxFactor = cms.double(3),
        seed = cms.uint32(37428479),
        debug = cms.untracked.bool(False),
    # Systematic variation
    # 0: Nominal
    # -1: -1 sigma (down variation)
    # 1: +1 sigma (up variation)
     variation = cms.int32(0)  # If not specified, default to 0
       )
    #################################
    ###  JER SMEARING AK4###
    #################################
    COLLECTIONTOSMEARAK4="selectedPatJetsAK4PFCHS"
    from RecoMET.METProducers.METSigParams_cfi import *
    process.slimmedAK4JetsSmeared = cms.EDProducer('SmearedPATJetProducer',
        src = cms.InputTag(COLLECTIONTOSMEARAK4),
        enabled = cms.bool(True),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        algo = cms.string('AK4PFchs'),
        algopt = cms.string('AK4PFchs_pt'),

        genJets = cms.InputTag('slimmedGenJets'),
        dRMax = cms.double(0.2),
        dPtMaxFactor = cms.double(3),
        seed = cms.uint32(37424479),
        debug = cms.untracked.bool(False),
    # Systematic variation
    # 0: Nominal
    # -1: -1 sigma (down variation)
    # 1: +1 sigma (up variation)
    variation = cms.int32(0)  # If not specified, default to 0
        )


COLLECTIONFORIDAK8="slimmedAK8JetsSmeared"
COLLECTIONFORIDAK4="slimmedAK4JetsSmeared"
if not MC:
    COLLECTIONFORIDAK8="selectedPatJetsAK8PFCHS"
    COLLECTIONFORIDAK4="selectedPatJetsAK4PFCHS"

    

from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.slimmedJetsAK8JetId = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                           filterParams = pfJetIDSelector.clone(),
                                           #src = cms.InputTag("slimmedJetsAK8"),
                                           #src = cms.InputTag("updatedPatJetsUpdatedJECAK8"),
                                           src = cms.InputTag(COLLECTIONFORIDAK8),
                                           #src = cms.InputTag("selectedPatJetsAK8PFCHS"),
                                           filter = cms.bool(True)
                                           )
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.slimmedJetsJetId = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                           filterParams = pfJetIDSelector.clone(),
                                           #src = cms.InputTag("slimmedJets"),
                                           #src = cms.InputTag("updatedPatJetsUpdatedJEC"), 
                                           src = cms.InputTag(COLLECTIONFORIDAK4),  
                                           #src = cms.InputTag("selectedPatJetsAK4PFCHS"),  
                                           filter = cms.bool(True)
                                           )

#################### P R E F I R I N G ####################
from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
      TheJets = cms.InputTag(COLLECTIONFORIDAK8) #this should be the slimmedJets collection with up to date JECs !
      , DataEra = cms.string("2017BtoF") 
      , UseJetEMPt = cms.bool(False)
      , PrefiringRateSystematicUncty = cms.double(0.2)
      , SkipWarnings = False)


from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
                       runVID=True, #saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
                       era='2017-Nov17ReReco')  

###################   M E T   C O R R     #################

# MET
if MC:
   process.genMet = cms.EDProducer("GenMETExtractor",
         metSource = cms.InputTag("slimmedMETs", "", "@skipCurrentProcess")
         )

# Raw MET
process.uncorrectedMet = cms.EDProducer("RecoMETExtractor",
      correctionLevel = cms.string('raw'),
      metSource = cms.InputTag("slimmedMETs", "", "@skipCurrentProcess")
      )

# Raw PAT MET
from PhysicsTools.PatAlgos.tools.metTools import addMETCollection
addMETCollection(process, labelName="uncorrectedPatMet", metSource="uncorrectedMet")
if MC:
   process.uncorrectedPatMet.genMETSource = cms.InputTag('genMet')
else:
   process.uncorrectedPatMet.addGenMET = False

#Type-1 correction
process.Type1CorrForNewJEC = cms.EDProducer("PATPFJetMETcorrInputProducer",
      src = cms.InputTag("selectedPatJetsAK4PFCHS"),
      jetCorrLabel = cms.InputTag("L3Absolute"),
      jetCorrLabelRes = cms.InputTag("L2L3Residual"),
      offsetCorrLabel = cms.InputTag("L1FastJet"),
      skipEM = cms.bool(True),
      skipEMfractionThreshold = cms.double(0.9),
      skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
      skipMuons = cms.bool(True),
      type1JetPtThreshold = cms.double(15.0)
      )
if MC:
   process.slimmedMETsNewJEC = cms.EDProducer('CorrectedPATMETProducer',
         src = cms.InputTag('uncorrectedPatMet'),
         srcCorrections = cms.VInputTag(cms.InputTag('Type1CorrForNewJEC', 'type1'))
         )
else:
   process.slimmedMETsNewJEC = cms.EDProducer('CorrectedPATMETProducer',
         src = cms.InputTag('uncorrectedPatMet'),
         srcCorrections = cms.VInputTag(cms.InputTag('Type1CorrForNewJEC', 'type1')),
         applyType2Corrections = cms.bool(False)
         )

if MC:
   process.shiftedMETCorrModuleForSmearedJets = cms.EDProducer('ShiftedParticleMETcorrInputProducer',
         srcOriginal = cms.InputTag("selectedPatJetsAK4PFCHS"),
         srcShifted = cms.InputTag(COLLECTIONFORIDAK4)
         )
   process.slimmedMETsSmeared = cms.EDProducer('CorrectedPATMETProducer',
         src = cms.InputTag('slimmedMETsNewJEC'),
         srcCorrections = cms.VInputTag(cms.InputTag('shiftedMETCorrModuleForSmearedJets'))
         )

if MC:
   METCollection="slimmedMETsSmeared"
else:
   METCollection="slimmedMETsNewJEC"


process.demo = cms.EDAnalyzer('Ntupler')
# Select data or MC - this controls which jet corrections are used and whether PU reweighting info is filled                           
process.demo.isMC = cms.bool(MC)
process.demo.isSignalMC = cms.bool(True)
process.demo.year = cms.int32(2017)
process.demo.era = cms.string('C')
process.demo.isInteractive = cms.bool(True)
#process.demo.ppsRecoProtonSingleRPTag = cms.InputTag("ctppsProtons", "singleRP")
#process.demo.ppsRecoProtonMultiRPTag  = cms.InputTag("ctppsProtons", "multiRP")
#pileupName="WJetsToLNu_2J_TuneCP5_13TeV_amcatnloFXFX_pythia8"
process.demo.mcName=cms.string("input_Event/N_TrueInteractions")

#from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
#switchOnVIDElectronIdProducer(process,DataFormat.MiniAOD)
#my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff']
#for idmod in my_id_modules:
#    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)



#from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
#runMetCorAndUncFromMiniAOD(process,
#                           isData= not MC
#                           )


process.load("SlimmedNtuple.TotalEvents.CfiFile_cfi")

process.load("RecoMET.METFilters.ecalBadCalibFilter_cfi")

baddetEcallist = cms.vuint32(
    [872439604,872422825,872420274,872423218,
     872423215,872416066,872435036,872439336,
     872420273,872436907,872420147,872439731,
     872436657,872420397,872439732,872439339,
     872439603,872422436,872439861,872437051,
     872437052,872420649,872422436,872421950,
     872437185,872422564,872421566,872421695,
     872421955,872421567,872437184,872421951,
     872421694,872437056,872437057,872437313])


process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter(
    "EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal    = baddetEcallist, 
    taggingMode = cms.bool(True),
    debug = cms.bool(False)
    )


process.dump=cms.EDAnalyzer('EventContentAnalyzer')

# Output
#process.TFileService = cms.Service("TFileService",
#                                             fileName = cms.string("out.root")
#                                             )

#Update for MET filter here: https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2#How_to_run_ecal_BadCalibReducedM
if MC:
    process.p = cms.Path(
        process.totalEvents*
        process.hltFilter*
        process.metFilterMC*
        #process.METFilter*
        process.ecalBadCalibReducedMINIAODFilter*
        #process.fullPatMetSequence*
        process.egammaPostRecoSeq*
        #process.egmGsfElectronIDSequence*
        process.slimmedAK8JetsSmeared*
        process.slimmedJetsAK8JetId*
        process.slimmedAK4JetsSmeared*
        process.slimmedJetsJetId*
        process.beamDivergenceVtxGenerator
        *process.genMet
        *process.uncorrectedMet
        *process.uncorrectedPatMet
        *process.Type1CorrForNewJEC
        *process.slimmedMETsNewJEC
        *process.shiftedMETCorrModuleForSmearedJets
        *process.slimmedMETsSmeared
        * process.ctppsDirectProtonSimulation
        * process.totemRPUVPatternFinder
        * process.totemRPLocalTrackFitter
        * process.ctppsPixelLocalTracks
        * process.ctppsLocalTrackLiteProducer
        #* process.dump
        * process.ctppsProtons
        *process.prefiringweight
        *process.demo
        )
    
else:
    process.p = cms.Path(
        process.hltFilter*
        process.metFilter*
        #process.METFilter*
        #process.totalEvents*
        process.ecalBadCalibReducedMINIAODFilter*
        #process.fullPatMetSequence*
        #process.egmGsfElectronIDSequence*
        process.egammaPostRecoSeq*
        #process.dump*
        process.slimmedJetsAK8JetId*
        process.slimmedJetsJetId*
        process.totemRPUVPatternFinder
        *process.genMet
        *process.uncorrectedMet
        *process.uncorrectedPatMet
        *process.Type1CorrForNewJEC
        *process.slimmedMETsNewJEC
        *process.shiftedMETCorrModuleForSmearedJets
        *process.slimmedMETsSmeared
        * process.totemRPLocalTrackFitter
        * process.ctppsDiamondRecHits
        * process.ctppsDiamondLocalTracks
        * process.ctppsPixelLocalTracks
        * process.ctppsLocalTrackLiteProducer
        * process.ctppsProtons
#        process.totemRPUVPatternFinder *
#        process.totemRPLocalTrackFitter *
#        process.ctppsDiamondRecHits *
#        process.ctppsDiamondLocalTracks *
#        #process.ctppsPixelLocalReconstruction *
#        process.ctppsPixelLocalTracks*
#        process.ctppsLocalTrackLiteProducer *
#        process.ctppsProtons *
#        #process.dump#*
        *process.prefiringweight
        *process.demo
        )


#print process.dumpPython()









