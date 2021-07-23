# WW - Semi leptonic production - A guide to create your Ntuple generator 

## Setting the workspace 

Install the 10_6_20 release of CMSSW and set the environment

```
export SCRAM_ARCH=slc7_amd64_gcc700 
cmsrel CMSSW_10_6_20
cd CMSSW_10_6_20/src/
cmsenv 
```

Install all additional packages that are not included in the $CMSSW_RELEASE_BASE

**PS.: The consecutive *scram b -j8* commands are being made just to check each package installation**

```
git cms-init
git cms-merge-topic cms-egamma:EgammaPostRecoTools
git cms-addpkg RecoMET/METFilters
scram b -j8

git clone git@github.com:miguelgallo/SlimmedNtuple.git SlimmedNtuple
cd SlimmedNtuple
git checkout CMSSW_10_6_x-FatJetMiniAOD
scram b -j8
cd ..

git cms-addpkg RecoEgamma/EgammaTools
git clone https://github.com/cms-egamma/EgammaPostRecoTools.git
mv EgammaPostRecoTools/python/EgammaPostRecoTools.py RecoEgamma/EgammaTools/python/
scram b -j8

git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_102X_v3
scram b -j8

git clone https://github.com/jan-kaspar/proton_simulation_validation.git
cd proton_simulation_validation
git checkout 9b2cff77711484e90c2323008eedc8c717cfcc41
cd ..
scram b -j8
```

Make a test folder just to see if everything's working fine with the proton direct simulation package

```
mkdir test
cd test

cp ../proton_simulation_validation/settings/2017_postTS2/* .
cp ../proton_simulation_validation/templates/test_acceptance_cfg.py .
cmsRun test_acceptance_cfg.py
```

With everything set and done as explained in this tutorial, one should be able to run the script *Ntupler/python/ConfFile_cfg_2017.py* and run the Ntuple generator for the WW semi leptonic analysis

**PS.: Remember to change my addresses to the one using this tutorial at *Ntupler/python/ConfFile_cfg_2017.py* and *Ntupler/plugins/Ntupler.cc*, since the SlimmeNtuple folder are being installed from my fork at GitHub**
