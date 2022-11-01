.def("reqUserLogin", &TdApi::reqUserLogin)
.def("reqUserLogout", &TdApi::reqUserLogout)
.def("reqOrderAction", &TdApi::reqOrderAction)
.def("reqTradingAccount", &TdApi::reqTradingAccount)
.def("reqQryOrder", &TdApi::reqQryOrder)
.def("reqQryTrade", &TdApi::reqQryTrade)
.def("reqQryInvestorPosition", &TdApi::reqQryInvestorPosition)
.def("reqChangePwd", &TdApi::reqChangePwd)
.def("reqQryTest", &TdApi::reqQryTest)

.def("onFrontConnected", &TdApi::onFrontConnected)
.def("onRspUserLogin", &TdApi::onRspUserLogin)
.def("onAnsOrderInsert", &TdApi::onAnsOrderInsert)
.def("onRspOrderInsert", &TdApi::onRspOrderInsert)
.def("onAnsOrderAction", &TdApi::onAnsOrderAction)
.def("onRspOrderAction", &TdApi::onRspOrderAction)
.def("onOrderRtn", &TdApi::onOrderRtn)
.def("onTradeRtn", &TdApi::onTradeRtn)
.def("onRspTradingAccount", &TdApi::onRspTradingAccount)
.def("onRspError", &TdApi::onRspError)
.def("onRspQryOrder", &TdApi::onRspQryOrder)
.def("onRspQryTrade", &TdApi::onRspQryTrade)
.def("onRspQryInvestorPosition", &TdApi::onRspQryInvestorPosition)
.def("onRspQryChangePwd", &TdApi::onRspQryChangePwd)
.def("onRspLogout", &TdApi::onRspLogout)
.def("onRtnInstrumentStatus", &TdApi::onRtnInstrumentStatus)
.def("onRspTest", &TdApi::onRspTest)
.def("onErrRtnOrderInsert", &TdApi::onErrRtnOrderInsert)
.def("onErrRtnOrderAction", &TdApi::onErrRtnOrderAction)
;
