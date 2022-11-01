.def("release", &TdApi::release)
.def("init", &TdApi::init)
.def("registerFront", &TdApi::registerFront)
.def("subscribePrivateTopic", &TdApi::subscribePrivateTopic)
.def("subscribePublicTopic", &TdApi::subscribePublicTopic)
.def("registerSpi", &TdApi::registerSpi)
.def("join", &TdApi::join)
.def("reqUserLogin", &TdApi::reqUserLogin)
.def("reqUserLogout", &TdApi::reqUserLogout)
.def("reqQryInstrument", &TdApi::reqQryInstrument)
.def("reqQryVarietyCode", &TdApi::reqQryVarietyCode)
.def("reqOrderInsert", &TdApi::reqOrderInsert)
.def("reqOrderAction", &TdApi::reqOrderAction)
.def("reqQryInvestorPosition", &TdApi::reqQryInvestorPosition)
.def("reqQryTradingAccount", &TdApi::reqQryTradingAccount)
.def("reqQryTrade", &TdApi::reqQryTrade)
.def("reqQryOrder", &TdApi::reqQryOrder)
.def("reqQryStorage", &TdApi::reqQryStorage)
.def("reqQryCostMarginFeeRate", &TdApi::reqQryCostMarginFeeRate)
.def("reqConditionOrderInsert", &TdApi::reqConditionOrderInsert)
.def("reqConditionOrderAction", &TdApi::reqConditionOrderAction)
.def("reqQryConditionOrder", &TdApi::reqQryConditionOrder)
.def("reqQryConditionOrderTrade", &TdApi::reqQryConditionOrderTrade)
.def("reqQryClientSessionInfo", &TdApi::reqQryClientSessionInfo)
.def("reqQryQuotation", &TdApi::reqQryQuotation)
.def("reqQryInvestorPositionDetail", &TdApi::reqQryInvestorPositionDetail)
.def("reqModifyPassword", &TdApi::reqModifyPassword)
.def("reqQryHisCapital", &TdApi::reqQryHisCapital)
.def("reqETFSubScription", &TdApi::reqETFSubScription)
.def("reqETFApplyForPurchase", &TdApi::reqETFApplyForPurchase)
.def("reqETFRedeem", &TdApi::reqETFRedeem)
.def("reqETFAccountBinding", &TdApi::reqETFAccountBinding)
.def("reqETFAccountUnbinding", &TdApi::reqETFAccountUnbinding)
.def("reqETFTradeDetail", &TdApi::reqETFTradeDetail)
.def("reqETFPcfDetail", &TdApi::reqETFPcfDetail)
.def("reqBOCMoneyIO", &TdApi::reqBOCMoneyIO)

.def("onFrontConnected", &TdApi::onFrontConnected)
.def("onFrontDisconnected", &TdApi::onFrontDisconnected)
.def("onRspUserLogin", &TdApi::onRspUserLogin)
.def("onRspUserLogout", &TdApi::onRspUserLogout)
.def("onNtyMktStatus", &TdApi::onNtyMktStatus)
.def("onRtnInstrumentStatus", &TdApi::onRtnInstrumentStatus)
.def("onRspQryInstrument", &TdApi::onRspQryInstrument)
.def("onRspReqQryVarietyCode", &TdApi::onRspReqQryVarietyCode)
.def("onRspOrderInsert", &TdApi::onRspOrderInsert)
.def("onRspETFSubscriptionOrderInsert", &TdApi::onRspETFSubscriptionOrderInsert)
.def("onRspETFPurchaseOrderInsert", &TdApi::onRspETFPurchaseOrderInsert)
.def("onRspETFRedeemInsert", &TdApi::onRspETFRedeemInsert)
.def("onRspETFAccountBinding", &TdApi::onRspETFAccountBinding)
.def("onRspETFAccountUnbinding", &TdApi::onRspETFAccountUnbinding)
.def("onRtnOrder", &TdApi::onRtnOrder)
.def("onForceLogout", &TdApi::onForceLogout)
.def("onRtnETFAccountBindingStatus", &TdApi::onRtnETFAccountBindingStatus)
.def("onRtnETFOrder", &TdApi::onRtnETFOrder)
.def("onRspOrderAction", &TdApi::onRspOrderAction)
.def("onRspError", &TdApi::onRspError)
.def("onRtnTrade", &TdApi::onRtnTrade)
.def("onRspQryTradingAccount", &TdApi::onRspQryTradingAccount)
.def("onRspQryHisCapital", &TdApi::onRspQryHisCapital)
.def("onRspQryOrder", &TdApi::onRspQryOrder)
.def("onRspQryTrade", &TdApi::onRspQryTrade)
.def("onRspQryInvestorPosition", &TdApi::onRspQryInvestorPosition)
.def("onRspQryClientStorage", &TdApi::onRspQryClientStorage)
.def("onRspQryCostMarginFeeRate", &TdApi::onRspQryCostMarginFeeRate)
.def("onRspConditionOrderInsert", &TdApi::onRspConditionOrderInsert)
.def("onRspConditionOrderAction", &TdApi::onRspConditionOrderAction)
.def("onRspQryConditionOrder", &TdApi::onRspQryConditionOrder)
.def("onRspQryConditionOrderTrade", &TdApi::onRspQryConditionOrderTrade)
.def("onRspQryClientSessionInfo", &TdApi::onRspQryClientSessionInfo)
.def("onRspQryQuotation", &TdApi::onRspQryQuotation)
.def("onRspQryInvestorPositionDetail", &TdApi::onRspQryInvestorPositionDetail)
.def("onRspQryETFradeDetail", &TdApi::onRspQryETFradeDetail)
.def("onRspQryETFPcfDetail", &TdApi::onRspQryETFPcfDetail)
.def("onRspModifyPassword", &TdApi::onRspModifyPassword)
.def("onRspB0CMoneyIO", &TdApi::onRspB0CMoneyIO)
;
