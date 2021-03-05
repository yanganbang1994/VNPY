.def("reqAuthenticate", &FuturesTdApi::reqAuthenticate)
.def("reqUserLogin", &FuturesTdApi::reqUserLogin)
.def("reqUserLogout", &FuturesTdApi::reqUserLogout)
.def("reqUserPasswordUpdate", &FuturesTdApi::reqUserPasswordUpdate)
.def("reqTradingAccountPasswordUpdate", &FuturesTdApi::reqTradingAccountPasswordUpdate)
.def("reqUserLogin2", &FuturesTdApi::reqUserLogin2)
.def("reqUserPasswordUpdate2", &FuturesTdApi::reqUserPasswordUpdate2)
.def("reqOrderInsert", &FuturesTdApi::reqOrderInsert)
.def("reqParkedOrderInsert", &FuturesTdApi::reqParkedOrderInsert)
.def("reqParkedOrderAction", &FuturesTdApi::reqParkedOrderAction)
.def("reqOrderAction", &FuturesTdApi::reqOrderAction)
.def("reqQueryMaxOrderVolume", &FuturesTdApi::reqQueryMaxOrderVolume)
.def("reqSettlementInfoConfirm", &FuturesTdApi::reqSettlementInfoConfirm)
.def("reqRemoveParkedOrder", &FuturesTdApi::reqRemoveParkedOrder)
.def("reqRemoveParkedOrderAction", &FuturesTdApi::reqRemoveParkedOrderAction)
.def("reqExecOrderInsert", &FuturesTdApi::reqExecOrderInsert)
.def("reqExecOrderAction", &FuturesTdApi::reqExecOrderAction)
.def("reqForQuoteInsert", &FuturesTdApi::reqForQuoteInsert)
.def("reqQuoteInsert", &FuturesTdApi::reqQuoteInsert)
.def("reqQuoteAction", &FuturesTdApi::reqQuoteAction)
.def("reqBatchOrderAction", &FuturesTdApi::reqBatchOrderAction)
.def("reqOptionSelfCloseInsert", &FuturesTdApi::reqOptionSelfCloseInsert)
.def("reqOptionSelfCloseAction", &FuturesTdApi::reqOptionSelfCloseAction)
.def("reqCombActionInsert", &FuturesTdApi::reqCombActionInsert)
.def("reqQryOrder", &FuturesTdApi::reqQryOrder)
.def("reqQryTrade", &FuturesTdApi::reqQryTrade)
.def("reqQryInvestorPosition", &FuturesTdApi::reqQryInvestorPosition)
.def("reqQryTradingAccount", &FuturesTdApi::reqQryTradingAccount)
.def("reqQryInvestor", &FuturesTdApi::reqQryInvestor)
.def("reqQryTradingCode", &FuturesTdApi::reqQryTradingCode)
.def("reqQryInstrumentMarginRate", &FuturesTdApi::reqQryInstrumentMarginRate)
.def("reqQryInstrumentCommissionRate", &FuturesTdApi::reqQryInstrumentCommissionRate)
.def("reqQryExchange", &FuturesTdApi::reqQryExchange)
.def("reqQryProduct", &FuturesTdApi::reqQryProduct)
.def("reqQryInstrument", &FuturesTdApi::reqQryInstrument)
.def("reqQryDepthMarketData", &FuturesTdApi::reqQryDepthMarketData)
.def("reqQrySettlementInfo", &FuturesTdApi::reqQrySettlementInfo)
.def("reqQryTransferBank", &FuturesTdApi::reqQryTransferBank)
.def("reqQryInvestorPositionDetail", &FuturesTdApi::reqQryInvestorPositionDetail)
.def("reqQryNotice", &FuturesTdApi::reqQryNotice)
.def("reqQrySettlementInfoConfirm", &FuturesTdApi::reqQrySettlementInfoConfirm)
.def("reqQryInvestorPositionCombineDetail", &FuturesTdApi::reqQryInvestorPositionCombineDetail)
.def("reqQryCFMMCTradingAccountKey", &FuturesTdApi::reqQryCFMMCTradingAccountKey)
.def("reqQryEWarrantOffset", &FuturesTdApi::reqQryEWarrantOffset)
.def("reqQryInvestorProductGroupMargin", &FuturesTdApi::reqQryInvestorProductGroupMargin)
.def("reqQryExchangeMarginRate", &FuturesTdApi::reqQryExchangeMarginRate)
.def("reqQryExchangeMarginRateAdjust", &FuturesTdApi::reqQryExchangeMarginRateAdjust)
.def("reqQryExchangeRate", &FuturesTdApi::reqQryExchangeRate)
.def("reqQrySecAgentACIDMap", &FuturesTdApi::reqQrySecAgentACIDMap)
.def("reqQryProductExchRate", &FuturesTdApi::reqQryProductExchRate)
.def("reqQryProductGroup", &FuturesTdApi::reqQryProductGroup)
.def("reqQryMMInstrumentCommissionRate", &FuturesTdApi::reqQryMMInstrumentCommissionRate)
.def("reqQryMMOptionInstrCommRate", &FuturesTdApi::reqQryMMOptionInstrCommRate)
.def("reqQryInstrumentOrderCommRate", &FuturesTdApi::reqQryInstrumentOrderCommRate)
.def("reqQrySecAgentTradingAccount", &FuturesTdApi::reqQrySecAgentTradingAccount)
.def("reqQrySecAgentCheckMode", &FuturesTdApi::reqQrySecAgentCheckMode)
.def("reqQryOptionInstrTradeCost", &FuturesTdApi::reqQryOptionInstrTradeCost)
.def("reqQryOptionInstrCommRate", &FuturesTdApi::reqQryOptionInstrCommRate)
.def("reqQryExecOrder", &FuturesTdApi::reqQryExecOrder)
.def("reqQryForQuote", &FuturesTdApi::reqQryForQuote)
.def("reqQryQuote", &FuturesTdApi::reqQryQuote)
.def("reqQryOptionSelfClose", &FuturesTdApi::reqQryOptionSelfClose)
.def("reqQryInvestUnit", &FuturesTdApi::reqQryInvestUnit)
.def("reqQryCombInstrumentGuard", &FuturesTdApi::reqQryCombInstrumentGuard)
.def("reqQryCombAction", &FuturesTdApi::reqQryCombAction)
.def("reqQryTransferSerial", &FuturesTdApi::reqQryTransferSerial)
.def("reqQryAccountregister", &FuturesTdApi::reqQryAccountregister)
.def("reqQryContractBank", &FuturesTdApi::reqQryContractBank)
.def("reqQryParkedOrder", &FuturesTdApi::reqQryParkedOrder)
.def("reqQryParkedOrderAction", &FuturesTdApi::reqQryParkedOrderAction)
.def("reqQryTradingNotice", &FuturesTdApi::reqQryTradingNotice)
.def("reqQryBrokerTradingParams", &FuturesTdApi::reqQryBrokerTradingParams)
.def("reqQryBrokerTradingAlgos", &FuturesTdApi::reqQryBrokerTradingAlgos)
.def("reqQueryCFMMCTradingAccountToken", &FuturesTdApi::reqQueryCFMMCTradingAccountToken)
.def("reqFromBankToFutureByFuture", &FuturesTdApi::reqFromBankToFutureByFuture)
.def("reqFromFutureToBankByFuture", &FuturesTdApi::reqFromFutureToBankByFuture)
.def("reqQueryBankAccountMoneyByFuture", &FuturesTdApi::reqQueryBankAccountMoneyByFuture)

.def("onFrontConnected", &FuturesTdApi::onFrontConnected)
.def("onFrontDisconnected", &FuturesTdApi::onFrontDisconnected)
.def("onHeartBeatWarning", &FuturesTdApi::onHeartBeatWarning)
.def("onRspAuthenticate", &FuturesTdApi::onRspAuthenticate)
.def("onRspUserLogin", &FuturesTdApi::onRspUserLogin)
.def("onRspUserLogout", &FuturesTdApi::onRspUserLogout)
.def("onRspUserPasswordUpdate", &FuturesTdApi::onRspUserPasswordUpdate)
.def("onRspTradingAccountPasswordUpdate", &FuturesTdApi::onRspTradingAccountPasswordUpdate)
.def("onRspOrderInsert", &FuturesTdApi::onRspOrderInsert)
.def("onRspParkedOrderInsert", &FuturesTdApi::onRspParkedOrderInsert)
.def("onRspParkedOrderAction", &FuturesTdApi::onRspParkedOrderAction)
.def("onRspOrderAction", &FuturesTdApi::onRspOrderAction)
.def("onRspQueryMaxOrderVolume", &FuturesTdApi::onRspQueryMaxOrderVolume)
.def("onRspSettlementInfoConfirm", &FuturesTdApi::onRspSettlementInfoConfirm)
.def("onRspRemoveParkedOrder", &FuturesTdApi::onRspRemoveParkedOrder)
.def("onRspRemoveParkedOrderAction", &FuturesTdApi::onRspRemoveParkedOrderAction)
.def("onRspExecOrderInsert", &FuturesTdApi::onRspExecOrderInsert)
.def("onRspExecOrderAction", &FuturesTdApi::onRspExecOrderAction)
.def("onRspForQuoteInsert", &FuturesTdApi::onRspForQuoteInsert)
.def("onRspQuoteInsert", &FuturesTdApi::onRspQuoteInsert)
.def("onRspQuoteAction", &FuturesTdApi::onRspQuoteAction)
.def("onRspBatchOrderAction", &FuturesTdApi::onRspBatchOrderAction)
.def("onRspOptionSelfCloseInsert", &FuturesTdApi::onRspOptionSelfCloseInsert)
.def("onRspOptionSelfCloseAction", &FuturesTdApi::onRspOptionSelfCloseAction)
.def("onRspCombActionInsert", &FuturesTdApi::onRspCombActionInsert)
.def("onRspQryOrder", &FuturesTdApi::onRspQryOrder)
.def("onRspQryTrade", &FuturesTdApi::onRspQryTrade)
.def("onRspQryInvestorPosition", &FuturesTdApi::onRspQryInvestorPosition)
.def("onRspQryTradingAccount", &FuturesTdApi::onRspQryTradingAccount)
.def("onRspQryInvestor", &FuturesTdApi::onRspQryInvestor)
.def("onRspQryTradingCode", &FuturesTdApi::onRspQryTradingCode)
.def("onRspQryInstrumentMarginRate", &FuturesTdApi::onRspQryInstrumentMarginRate)
.def("onRspQryInstrumentCommissionRate", &FuturesTdApi::onRspQryInstrumentCommissionRate)
.def("onRspQryExchange", &FuturesTdApi::onRspQryExchange)
.def("onRspQryProduct", &FuturesTdApi::onRspQryProduct)
.def("onRspQryInstrument", &FuturesTdApi::onRspQryInstrument)
.def("onRspQryDepthMarketData", &FuturesTdApi::onRspQryDepthMarketData)
.def("onRspQrySettlementInfo", &FuturesTdApi::onRspQrySettlementInfo)
.def("onRspQryTransferBank", &FuturesTdApi::onRspQryTransferBank)
.def("onRspQryInvestorPositionDetail", &FuturesTdApi::onRspQryInvestorPositionDetail)
.def("onRspQryNotice", &FuturesTdApi::onRspQryNotice)
.def("onRspQrySettlementInfoConfirm", &FuturesTdApi::onRspQrySettlementInfoConfirm)
.def("onRspQryInvestorPositionCombineDetail", &FuturesTdApi::onRspQryInvestorPositionCombineDetail)
.def("onRspQryCFMMCTradingAccountKey", &FuturesTdApi::onRspQryCFMMCTradingAccountKey)
.def("onRspQryEWarrantOffset", &FuturesTdApi::onRspQryEWarrantOffset)
.def("onRspQryInvestorProductGroupMargin", &FuturesTdApi::onRspQryInvestorProductGroupMargin)
.def("onRspQryExchangeMarginRate", &FuturesTdApi::onRspQryExchangeMarginRate)
.def("onRspQryExchangeMarginRateAdjust", &FuturesTdApi::onRspQryExchangeMarginRateAdjust)
.def("onRspQryExchangeRate", &FuturesTdApi::onRspQryExchangeRate)
.def("onRspQrySecAgentACIDMap", &FuturesTdApi::onRspQrySecAgentACIDMap)
.def("onRspQryProductExchRate", &FuturesTdApi::onRspQryProductExchRate)
.def("onRspQryProductGroup", &FuturesTdApi::onRspQryProductGroup)
.def("onRspQryMMInstrumentCommissionRate", &FuturesTdApi::onRspQryMMInstrumentCommissionRate)
.def("onRspQryMMOptionInstrCommRate", &FuturesTdApi::onRspQryMMOptionInstrCommRate)
.def("onRspQryInstrumentOrderCommRate", &FuturesTdApi::onRspQryInstrumentOrderCommRate)
.def("onRspQrySecAgentTradingAccount", &FuturesTdApi::onRspQrySecAgentTradingAccount)
.def("onRspQrySecAgentCheckMode", &FuturesTdApi::onRspQrySecAgentCheckMode)
.def("onRspQryOptionInstrTradeCost", &FuturesTdApi::onRspQryOptionInstrTradeCost)
.def("onRspQryOptionInstrCommRate", &FuturesTdApi::onRspQryOptionInstrCommRate)
.def("onRspQryExecOrder", &FuturesTdApi::onRspQryExecOrder)
.def("onRspQryForQuote", &FuturesTdApi::onRspQryForQuote)
.def("onRspQryQuote", &FuturesTdApi::onRspQryQuote)
.def("onRspQryOptionSelfClose", &FuturesTdApi::onRspQryOptionSelfClose)
.def("onRspQryInvestUnit", &FuturesTdApi::onRspQryInvestUnit)
.def("onRspQryCombInstrumentGuard", &FuturesTdApi::onRspQryCombInstrumentGuard)
.def("onRspQryCombAction", &FuturesTdApi::onRspQryCombAction)
.def("onRspQryTransferSerial", &FuturesTdApi::onRspQryTransferSerial)
.def("onRspQryAccountregister", &FuturesTdApi::onRspQryAccountregister)
.def("onRspForQuote", &FuturesTdApi::onRspForQuote)
.def("onRspError", &FuturesTdApi::onRspError)
.def("onRtnOrder", &FuturesTdApi::onRtnOrder)
.def("onRtnTrade", &FuturesTdApi::onRtnTrade)
.def("onErrRtnOrderInsert", &FuturesTdApi::onErrRtnOrderInsert)
.def("onErrRtnOrderAction", &FuturesTdApi::onErrRtnOrderAction)
.def("onRtnInstrumentStatus", &FuturesTdApi::onRtnInstrumentStatus)
.def("onRtnBulletin", &FuturesTdApi::onRtnBulletin)
.def("onRtnTradingNotice", &FuturesTdApi::onRtnTradingNotice)
.def("onRtnErrorConditionalOrder", &FuturesTdApi::onRtnErrorConditionalOrder)
.def("onRtnExecOrder", &FuturesTdApi::onRtnExecOrder)
.def("onErrRtnExecOrderInsert", &FuturesTdApi::onErrRtnExecOrderInsert)
.def("onErrRtnExecOrderAction", &FuturesTdApi::onErrRtnExecOrderAction)
.def("onErrRtnForQuoteInsert", &FuturesTdApi::onErrRtnForQuoteInsert)
.def("onRtnQuote", &FuturesTdApi::onRtnQuote)
.def("onErrRtnQuoteInsert", &FuturesTdApi::onErrRtnQuoteInsert)
.def("onErrRtnQuoteAction", &FuturesTdApi::onErrRtnQuoteAction)
.def("onRtnForQuote", &FuturesTdApi::onRtnForQuote)
.def("onRtnCFMMCTradingAccountToken", &FuturesTdApi::onRtnCFMMCTradingAccountToken)
.def("onErrRtnBatchOrderAction", &FuturesTdApi::onErrRtnBatchOrderAction)
.def("onRtnOptionSelfClose", &FuturesTdApi::onRtnOptionSelfClose)
.def("onErrRtnOptionSelfCloseInsert", &FuturesTdApi::onErrRtnOptionSelfCloseInsert)
.def("onErrRtnOptionSelfCloseAction", &FuturesTdApi::onErrRtnOptionSelfCloseAction)
.def("onRtnCombAction", &FuturesTdApi::onRtnCombAction)
.def("onErrRtnCombActionInsert", &FuturesTdApi::onErrRtnCombActionInsert)
.def("onRspQryContractBank", &FuturesTdApi::onRspQryContractBank)
.def("onRspQryParkedOrder", &FuturesTdApi::onRspQryParkedOrder)
.def("onRspQryParkedOrderAction", &FuturesTdApi::onRspQryParkedOrderAction)
.def("onRspQryTradingNotice", &FuturesTdApi::onRspQryTradingNotice)
.def("onRspQryBrokerTradingParams", &FuturesTdApi::onRspQryBrokerTradingParams)
.def("onRspQryBrokerTradingAlgos", &FuturesTdApi::onRspQryBrokerTradingAlgos)
.def("onRspQueryCFMMCTradingAccountToken", &FuturesTdApi::onRspQueryCFMMCTradingAccountToken)
.def("onRtnFromBankToFutureByBank", &FuturesTdApi::onRtnFromBankToFutureByBank)
.def("onRtnFromFutureToBankByBank", &FuturesTdApi::onRtnFromFutureToBankByBank)
.def("onRtnRepealFromBankToFutureByBank", &FuturesTdApi::onRtnRepealFromBankToFutureByBank)
.def("onRtnRepealFromFutureToBankByBank", &FuturesTdApi::onRtnRepealFromFutureToBankByBank)
.def("onRtnFromBankToFutureByFuture", &FuturesTdApi::onRtnFromBankToFutureByFuture)
.def("onRtnFromFutureToBankByFuture", &FuturesTdApi::onRtnFromFutureToBankByFuture)
.def("onRtnRepealFromBankToFutureByFutureManual", &FuturesTdApi::onRtnRepealFromBankToFutureByFutureManual)
.def("onRtnRepealFromFutureToBankByFutureManual", &FuturesTdApi::onRtnRepealFromFutureToBankByFutureManual)
.def("onRtnQueryBankBalanceByFuture", &FuturesTdApi::onRtnQueryBankBalanceByFuture)
.def("onErrRtnBankToFutureByFuture", &FuturesTdApi::onErrRtnBankToFutureByFuture)
.def("onErrRtnFutureToBankByFuture", &FuturesTdApi::onErrRtnFutureToBankByFuture)
.def("onErrRtnRepealBankToFutureByFutureManual", &FuturesTdApi::onErrRtnRepealBankToFutureByFutureManual)
.def("onErrRtnRepealFutureToBankByFutureManual", &FuturesTdApi::onErrRtnRepealFutureToBankByFutureManual)
.def("onErrRtnQueryBankBalanceByFuture", &FuturesTdApi::onErrRtnQueryBankBalanceByFuture)
.def("onRtnRepealFromBankToFutureByFuture", &FuturesTdApi::onRtnRepealFromBankToFutureByFuture)
.def("onRtnRepealFromFutureToBankByFuture", &FuturesTdApi::onRtnRepealFromFutureToBankByFuture)
.def("onRspFromBankToFutureByFuture", &FuturesTdApi::onRspFromBankToFutureByFuture)
.def("onRspFromFutureToBankByFuture", &FuturesTdApi::onRspFromFutureToBankByFuture)
.def("onRspQueryBankAccountMoneyByFuture", &FuturesTdApi::onRspQueryBankAccountMoneyByFuture)
.def("onRtnOpenAccountByBank", &FuturesTdApi::onRtnOpenAccountByBank)
.def("onRtnCancelAccountByBank", &FuturesTdApi::onRtnCancelAccountByBank)
.def("onRtnChangeAccountByBank", &FuturesTdApi::onRtnChangeAccountByBank)
;
