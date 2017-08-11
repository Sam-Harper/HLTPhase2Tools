import FWCore.ParameterSet.Config as cms

def printWarning(process):
    modulesToOverride=["hltPixelLayerPairs","hltPixelLayerTriplets","hltEgammaHoverE","hltEgammaSuperClustersToPixelMatch","hltEleSeedsTrackingRegions","hltElePixelHitDoublets","hltElePixelHitDoubletsForTriplets","hltElePixelHitTriplets","hltElePixelSeedsDoublets","hltElePixelSeedsTriplets","hltElePixelSeedsCombined","hltEgammaElectronPixelSeeds","hltEgammaPixelMatchVars"]
    seqsToOverride=["HLTElePixelMatchSequence"]
    print "[customiseEGPixelMatching] Customising E/gamma pixel matching"
    print "[customiseEGPixelMatching] only seeded sequence is setup right now"
    
    for module in modulesToOverride:
        if hasattr(process,module):
            print "[customiseEGPixelMatching] overriding module:",module
    for seq in seqsToOverride:
        if hasattr(process,seq):
            print "[customiseEGPixelMatching] overriding sequence:",seq

def customisePixelMatching(process):

    printWarning(process)

    process.hltPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
                                                  layerList = cms.vstring( 'BPix1+BPix2',
                                                                           'BPix1+BPix3',
                                                                           'BPix1+BPix4',
                                                                           'BPix2+BPix3',
                                                                           'BPix2+BPix4',
                                                                           'BPix3+BPix4',
                                                                           'FPix1_pos+FPix2_pos',
                                                                           'FPix1_pos+FPix3_pos',
                                                                           'FPix2_pos+FPix3_pos',
                                                                           'BPix1+FPix1_pos',
                                                                           'BPix1+FPix2_pos',
                                                                           'BPix1+FPix3_pos',
                                                                           'BPix2+FPix1_pos',
                                                                           'BPix2+FPix2_pos',
                                                                           'BPix2+FPix3_pos',
                                                                           'BPix3+FPix1_pos',
                                                                           'BPix3+FPix2_pos',
                                                                           'BPix3+FPix3_pos',
                                                                           'BPix4+FPix1_pos',
                                                                           'BPix4+FPix2_pos',
                                                                           'BPix4+FPix3_pos',
                                                                           'FPix1_neg+FPix2_neg',
                                                                           'FPix1_neg+FPix3_neg',
                                                                           'FPix2_neg+FPix3_neg',
                                                                           'BPix1+FPix1_neg',
                                                                           'BPix1+FPix2_neg',
                                                                           'BPix1+FPix3_neg',
                                                                           'BPix2+FPix1_neg',
                                                                           'BPix2+FPix2_neg',
                                                                           'BPix2+FPix3_neg',
                                                                           'BPix3+FPix1_neg',
                                                                           'BPix3+FPix2_neg',
                                                                           'BPix3+FPix3_neg',
                                                                           'BPix4+FPix1_neg',
                                                                           'BPix4+FPix2_neg',
                                                                           'BPix4+FPix3_neg' ),
                                                  MTOB = cms.PSet(  ),
                                                  TEC = cms.PSet(  ),
                                                  MTID = cms.PSet(  ),
                                                  FPix = cms.PSet( 
            hitErrorRPhi = cms.double( 0.0051 ),
            TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
            useErrorsFromParam = cms.bool( True ),
            hitErrorRZ = cms.double( 0.0036 ),
            HitProducer = cms.string( "hltSiPixelRecHits" )
            ),
                                                  MTEC = cms.PSet(  ),
                                                  MTIB = cms.PSet(  ),
                                                  TID = cms.PSet(  ),
                                                  TOB = cms.PSet(  ),
                                                  BPix = cms.PSet( 
            hitErrorRPhi = cms.double( 0.0027 ),
            TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
            useErrorsFromParam = cms.bool( True ),
            hitErrorRZ = cms.double( 0.006 ),
            HitProducer = cms.string( "hltSiPixelRecHits" )
            ),
                                                  TIB = cms.PSet(  )
                                                  )
    process.hltPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
                                                 layerList = cms.vstring( 'BPix1+BPix2+BPix3',
                                                                          'BPix2+BPix3+BPix4',
                                                                          'BPix1+BPix3+BPix4',
                                                                          'BPix1+BPix2+BPix4',
                                                                          'BPix2+BPix3+FPix1_pos',
                                                                          'BPix2+BPix3+FPix1_neg',
                                                                          'BPix1+BPix2+FPix1_pos',
                                                                          'BPix1+BPix2+FPix1_neg',
                                                                          'BPix2+FPix1_pos+FPix2_pos',
                                                                          'BPix2+FPix1_neg+FPix2_neg',
                                                                          'BPix1+FPix1_pos+FPix2_pos',
                                                                          'BPix1+FPix1_neg+FPix2_neg',
                                                                          'FPix1_pos+FPix2_pos+FPix3_pos',
                                                                          'FPix1_neg+FPix2_neg+FPix3_neg',
                                                                          'BPix1+BPix3+FPix1_pos',
                                                                          'BPix1+BPix2+FPix2_pos',
                                                                          'BPix1+BPix3+FPix1_neg',
                                                                          'BPix1+BPix2+FPix2_neg',
                                                                          'BPix1+FPix2_neg+FPix3_neg',
                                                                          'BPix1+FPix1_neg+FPix3_neg',
                                                                          'BPix1+FPix2_pos+FPix3_pos',
                                                                          'BPix1+FPix1_pos+FPix3_pos' ),
                                                     MTOB = cms.PSet(  ),
                                                     TEC = cms.PSet(  ),
                                                     MTID = cms.PSet(  ),
                                                     FPix = cms.PSet( 
            hitErrorRPhi = cms.double( 0.0051 ),
            TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
            useErrorsFromParam = cms.bool( True ),
            hitErrorRZ = cms.double( 0.0036 ),
            HitProducer = cms.string( "hltSiPixelRecHits" )
            ),
                                                     MTEC = cms.PSet(  ),
                                                     MTIB = cms.PSet(  ),
                                                     TID = cms.PSet(  ),
                                                     TOB = cms.PSet(  ),
                                                     BPix = cms.PSet( 
            hitErrorRPhi = cms.double( 0.0027 ),
            TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
            useErrorsFromParam = cms.bool( True ),
            hitErrorRZ = cms.double( 0.006 ),
            HitProducer = cms.string( "hltSiPixelRecHits" )
            ),
                                                     TIB = cms.PSet(  )
                                                     )
    process.hltEgammaHoverE = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
                                               effectiveAreas = cms.vdouble( 0.105, 0.17 ),
                                               doRhoCorrection = cms.bool( False ),
                                               outerCone = cms.double( 0.14 ),
                                               caloTowerProducer = cms.InputTag( "hltTowerMakerMethod2L1EGSeeded" ),
                                               innerCone = cms.double( 0.0 ),
                                               useSingleTower = cms.bool( False ),
                                               rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
                                               depth = cms.int32( -1 ),
                                               absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
                                               recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
                                               rhoMax = cms.double( 9.9999999E7 ),
                                               etMin = cms.double( 0.0 ),
                                               rhoScale = cms.double( 1.0 ),
                                               doEtSum = cms.bool( False )
                                               )
    process.hltEgammaSuperClustersToPixelMatch = cms.EDProducer( "EgammaHLTFilteredSuperClusterProducer",
                                                                  cands = cms.InputTag( "hltEgammaCandidates" ),
                                                                  cuts = cms.VPSet( 
            cms.PSet(  endcapCut = cms.PSet( 
                    useEt = cms.bool( False ),
                    cutOverE = cms.double( 0.2 )
                    ),
                       var = cms.InputTag( "hltEgammaHoverE" ),
                       barrelCut = cms.PSet( 
                    useEt = cms.bool( False ),
                    cutOverE = cms.double( 0.2 )
                    )
                       )
            )
                                                                  )
    process.hltEleSeedsTrackingRegions = cms.EDProducer( "TrackingRegionsFromSuperClustersEDProducer",
                                                          RegionPSet = cms.PSet( 
            useZInBeamspot = cms.bool( False ),
            useZInVertex = cms.bool( False ),
            defaultZ = cms.double( 0.0 ),
            originHalfLength = cms.double( 12.5 ),
            originRadius = cms.double( 0.2 ),
            minBSDeltaZ = cms.double( 0.0 ),
            nrSigmaForBSDeltaZ = cms.double( 4.0 ),
            vertices = cms.InputTag( "" ),
            beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
            ptMin = cms.double( 1.5 ),
            deltaEtaRegion = cms.double( 0.1 ),
            deltaPhiRegion = cms.double( 0.4 ),
            precise = cms.bool( True ),
            measurementTrackerEvent = cms.InputTag( "" ),
            whereToUseMeasTracker = cms.string( "kNever" ),
            superClusters = cms.VInputTag( 'hltEgammaSuperClustersToPixelMatch' )
            )
                                                          )
    process.hltElePixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
                                                      trackingRegions = cms.InputTag( "hltEleSeedsTrackingRegions" ),
                                                      layerPairs = cms.vuint32( 0 ),
                                                      clusterCheck = cms.InputTag( "" ),
                                                      produceSeedingHitSets = cms.bool( True ),
                                                      produceIntermediateHitDoublets = cms.bool( True ),
                                                      maxElement = cms.uint32( 0 ),
                                                      seedingLayers = cms.InputTag( "hltPixelLayerPairs" )
                                                      )
    process.hltElePixelHitDoubletsForTriplets = cms.EDProducer( "HitPairEDProducer",
                                                                 trackingRegions = cms.InputTag( "hltEleSeedsTrackingRegions" ),
                                                                 layerPairs = cms.vuint32( 0, 1 ),
                                                                 clusterCheck = cms.InputTag( "" ),
                                                                 produceSeedingHitSets = cms.bool( True ),
                                                                 produceIntermediateHitDoublets = cms.bool( True ),
                                                                 maxElement = cms.uint32( 0 ),
                                                                 seedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
                                                                 )
    process.hltElePixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
                                                      CAHardPtCut = cms.double( 0.3 ),
                                                      SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
                                                      extraHitRPhitolerance = cms.double( 0.032 ),
                                                      doublets = cms.InputTag( "hltElePixelHitDoubletsForTriplets" ),
                                                      CAThetaCut = cms.double( 0.004 ),
                                                      maxChi2 = cms.PSet( 
            value2 = cms.double( 6.0 ),
            value1 = cms.double( 100.0 ),
            pt1 = cms.double( 0.8 ),
            enabled = cms.bool( True ),
            pt2 = cms.double( 8.0 )
            ),
                                                      CAPhiCut = cms.double( 0.1 ),
                                                      useBendingCorrection = cms.bool( True )
                                                      )
    process.hltElePixelSeedsDoublets = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
                                                        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
                                                        forceKinematicWithRegionDirection = cms.bool( False ),
                                                        magneticField = cms.string( "ParabolicMf" ),
                                                        SeedMomentumForBOFF = cms.double( 5.0 ),
                                                        OriginTransverseErrorMultiplier = cms.double( 1.0 ),
                                                        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
                                                        MinOneOverPtError = cms.double( 1.0 ),
                                                        seedingHitSets = cms.InputTag( "hltElePixelHitDoublets" ),
                                                        propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
                                                        )
    process.hltElePixelSeedsTriplets = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
                                                        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
                                                        forceKinematicWithRegionDirection = cms.bool( False ),
                                                        magneticField = cms.string( "ParabolicMf" ),
                                                        SeedMomentumForBOFF = cms.double( 5.0 ),
                                                        OriginTransverseErrorMultiplier = cms.double( 1.0 ),
                                                        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
                                                        MinOneOverPtError = cms.double( 1.0 ),
                                                        seedingHitSets = cms.InputTag( "hltElePixelHitTriplets" ),
                                                        propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
                                                        )
    process.hltElePixelSeedsCombined = cms.EDProducer( "SeedCombiner",
                                                        seedCollections = cms.VInputTag( 'hltElePixelSeedsDoublets','hltElePixelSeedsTriplets' )
                                                        )
    process.hltEgammaElectronPixelSeeds = cms.EDProducer( "ElectronNHitSeedProducer",
                                                           matcherConfig = cms.PSet( 
            detLayerGeom = cms.string( "hltESPGlobalDetLayerGeometry" ),
            navSchool = cms.string( "SimpleNavigationSchool" ),
            useRecoVertex = cms.bool( False ),
            minNrHits = cms.vuint32( 2, 3 ),
            matchingCuts = cms.VPSet( 
                cms.PSet(  version = cms.int32( 2 ),
                           dPhiMaxHighEt = cms.vdouble( 0.05 ),
                           dPhiMaxHighEtThres = cms.vdouble( 20.0 ),
                           dPhiMaxLowEtGrad = cms.vdouble( -0.002 ),
                           dRZMaxHighEt = cms.vdouble( 9999.0 ),
                           dRZMaxHighEtThres = cms.vdouble( 0.0 ),
                           dRZMaxLowEtGrad = cms.vdouble( 0.0 )
                           ),
                cms.PSet(  version = cms.int32( 2 ),
                           dPhiMaxHighEt = cms.vdouble( 0.003 ),
                           dPhiMaxHighEtThres = cms.vdouble( 0.0 ),
                           dPhiMaxLowEtGrad = cms.vdouble( 0.0 ),
                           dRZMaxHighEt = cms.vdouble( 0.05 ),
                           dRZMaxHighEtThres = cms.vdouble( 30.0 ),
                           dRZMaxLowEtGrad = cms.vdouble( -0.002 ),
                           etaBins = cms.vdouble(  )
                           ),
                cms.PSet(  version = cms.int32( 2 ),
                           dPhiMaxHighEt = cms.vdouble( 0.003 ),
                           dPhiMaxHighEtThres = cms.vdouble( 0.0 ),
                           dPhiMaxLowEtGrad = cms.vdouble( 0.0 ),
                           dRZMaxHighEt = cms.vdouble( 0.05 ),
                           dRZMaxHighEtThres = cms.vdouble( 30.0 ),
                           dRZMaxLowEtGrad = cms.vdouble( -0.002 ),
                           etaBins = cms.vdouble(  )
                           )
                ),
            minNrHitsValidLayerBins = cms.vint32( 4 )
            ),
                                                           beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
                                                           measTkEvt = cms.InputTag( "hltSiStripClusters" ),
                                                           vertices = cms.InputTag( "" ),
                                                           superClusters = cms.VInputTag( 'hltEgammaSuperClustersToPixelMatch' ),
                                                           initialSeeds = cms.InputTag( "hltElePixelSeedsCombined" )
                                                           )
    process.hltEgammaPixelMatchVars = cms.EDProducer( "EgammaHLTPixelMatchVarProducer",
                                                       productsToWrite = cms.int32( 0 ),
                                                       dRZ2SParams = cms.PSet(  bins = cms.VPSet( 
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.00299, 2.99E-4, -4.13E-6, 0.00191 ),
                           xMin = cms.double( 0.0 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 1.5 ),
                           funcType = cms.string( "TF1:=pol3" )
                           ),
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.248, -0.329, 0.148, -0.0222 ),
                           xMin = cms.double( 1.5 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 3.0 ),
                           funcType = cms.string( "TF1:=pol3" )
                           )
                ) ),
                                                       pixelSeedsProducer = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
                                                       dPhi2SParams = cms.PSet(  bins = cms.VPSet( 
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 1.3E-4 ),
                           xMin = cms.double( 0.0 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 1.6 ),
                           funcType = cms.string( "TF1:=pol0" )
                           ),
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 4.5E-4, -1.99E-4 ),
                           xMin = cms.double( 1.5 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 1.9 ),
                           funcType = cms.string( "TF1:=pol1" )
                           ),
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 7.94E-5 ),
                           xMin = cms.double( 1.9 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 3.0 ),
                           funcType = cms.string( "TF1:=pol0" )
                           )
                ) ),
                                                       recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
                                                       dPhi1SParams = cms.PSet(  bins = cms.VPSet( 
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.00112, 7.52E-4, -0.00122, 0.00109 ),
                           xMin = cms.double( 0.0 ),
                           yMax = cms.int32( 1 ),
                           xMax = cms.double( 1.5 ),
                           funcType = cms.string( "TF1:=pol3" )
                           ),
                cms.PSet(  yMin = cms.int32( 2 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.00222, 1.96E-4, -2.03E-4, 4.47E-4 ),
                           xMin = cms.double( 0.0 ),
                           yMax = cms.int32( 2 ),
                           xMax = cms.double( 1.5 ),
                           funcType = cms.string( "TF1:=pol3" )
                           ),
                cms.PSet(  yMin = cms.int32( 3 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.00236, 6.91E-4, 1.99E-4, 4.16E-4 ),
                           xMin = cms.double( 0.0 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 1.5 ),
                           funcType = cms.string( "TF1:=pol3" )
                           ),
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.00823, -0.0029 ),
                           xMin = cms.double( 1.5 ),
                           yMax = cms.int32( 1 ),
                           xMax = cms.double( 2.0 ),
                           funcType = cms.string( "TF1:=pol1" )
                           ),
                cms.PSet(  yMin = cms.int32( 1 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.00282 ),
                           xMin = cms.double( 2.0 ),
                           yMax = cms.int32( 1 ),
                           xMax = cms.double( 3.0 ),
                           funcType = cms.string( "TF1:=pol0" )
                           ),
                cms.PSet(  yMin = cms.int32( 2 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.010838, -0.00345 ),
                           xMin = cms.double( 1.5 ),
                           yMax = cms.int32( 2 ),
                           xMax = cms.double( 2.0 ),
                           funcType = cms.string( "TF1:=pol1" )
                           ),
                cms.PSet(  yMin = cms.int32( 2 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.0043 ),
                           xMin = cms.double( 2.0 ),
                           yMax = cms.int32( 2 ),
                           xMax = cms.double( 3.0 ),
                           funcType = cms.string( "TF1:=pol0" )
                           ),
                cms.PSet(  yMin = cms.int32( 3 ),
                           binType = cms.string( "AbsEtaClus" ),
                           funcParams = cms.vdouble( 0.0208, -0.0125, 0.00231 ),
                           xMin = cms.double( 1.5 ),
                           yMax = cms.int32( 99999 ),
                           xMax = cms.double( 3.0 ),
                           funcType = cms.string( "TF1:=pol2" )
                           )
                ) )
                                                       )
    process.HLTElePixelMatchSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltPixelLayerPairs + process.hltPixelLayerTriplets + process.hltEgammaHoverE + process.hltEgammaSuperClustersToPixelMatch + process.hltEleSeedsTrackingRegions + process.hltElePixelHitDoublets + process.hltElePixelHitDoubletsForTriplets + process.hltElePixelHitTriplets + process.hltElePixelSeedsDoublets + process.hltElePixelSeedsTriplets + process.hltElePixelSeedsCombined + process.hltEgammaElectronPixelSeeds + process.hltEgammaPixelMatchVars )
    
    return process

