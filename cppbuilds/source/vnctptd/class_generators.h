#pragma once


#include <pybind11/pybind11.h>

#include "dispatcher.h"
#include "property_helper.h"
#include "wrapper_helper.h"
#include "class_generators.h"

#include "ctp/ThostFtdcTraderApi.h"


void generate_class_CThostFtdcDisseminationField(pybind11::module &m);
void generate_class_CThostFtdcReqUserLoginField(pybind11::module &m);
void generate_class_CThostFtdcRspUserLoginField(pybind11::module &m);
void generate_class_CThostFtdcUserLogoutField(pybind11::module &m);
void generate_class_CThostFtdcForceUserLogoutField(pybind11::module &m);
void generate_class_CThostFtdcReqAuthenticateField(pybind11::module &m);
void generate_class_CThostFtdcRspAuthenticateField(pybind11::module &m);
void generate_class_CThostFtdcAuthenticationInfoField(pybind11::module &m);
void generate_class_CThostFtdcTransferHeaderField(pybind11::module &m);
void generate_class_CThostFtdcTransferBankToFutureReqField(pybind11::module &m);
void generate_class_CThostFtdcTransferBankToFutureRspField(pybind11::module &m);
void generate_class_CThostFtdcTransferFutureToBankReqField(pybind11::module &m);
void generate_class_CThostFtdcTransferFutureToBankRspField(pybind11::module &m);
void generate_class_CThostFtdcTransferQryBankReqField(pybind11::module &m);
void generate_class_CThostFtdcTransferQryBankRspField(pybind11::module &m);
void generate_class_CThostFtdcTransferQryDetailReqField(pybind11::module &m);
void generate_class_CThostFtdcTransferQryDetailRspField(pybind11::module &m);
void generate_class_CThostFtdcRspInfoField(pybind11::module &m);
void generate_class_CThostFtdcExchangeField(pybind11::module &m);
void generate_class_CThostFtdcProductField(pybind11::module &m);
void generate_class_CThostFtdcInstrumentField(pybind11::module &m);
void generate_class_CThostFtdcBrokerField(pybind11::module &m);
void generate_class_CThostFtdcTraderField(pybind11::module &m);
void generate_class_CThostFtdcInvestorField(pybind11::module &m);
void generate_class_CThostFtdcTradingCodeField(pybind11::module &m);
void generate_class_CThostFtdcPartBrokerField(pybind11::module &m);
void generate_class_CThostFtdcSuperUserField(pybind11::module &m);
void generate_class_CThostFtdcSuperUserFunctionField(pybind11::module &m);
void generate_class_CThostFtdcInvestorGroupField(pybind11::module &m);
void generate_class_CThostFtdcTradingAccountField(pybind11::module &m);
void generate_class_CThostFtdcInvestorPositionField(pybind11::module &m);
void generate_class_CThostFtdcInstrumentMarginRateField(pybind11::module &m);
void generate_class_CThostFtdcInstrumentCommissionRateField(pybind11::module &m);
void generate_class_CThostFtdcDepthMarketDataField(pybind11::module &m);
void generate_class_CThostFtdcInstrumentTradingRightField(pybind11::module &m);
void generate_class_CThostFtdcBrokerUserField(pybind11::module &m);
void generate_class_CThostFtdcBrokerUserPasswordField(pybind11::module &m);
void generate_class_CThostFtdcBrokerUserFunctionField(pybind11::module &m);
void generate_class_CThostFtdcTraderOfferField(pybind11::module &m);
void generate_class_CThostFtdcSettlementInfoField(pybind11::module &m);
void generate_class_CThostFtdcInstrumentMarginRateAdjustField(pybind11::module &m);
void generate_class_CThostFtdcExchangeMarginRateField(pybind11::module &m);
void generate_class_CThostFtdcExchangeMarginRateAdjustField(pybind11::module &m);
void generate_class_CThostFtdcExchangeRateField(pybind11::module &m);
void generate_class_CThostFtdcSettlementRefField(pybind11::module &m);
void generate_class_CThostFtdcCurrentTimeField(pybind11::module &m);
void generate_class_CThostFtdcCommPhaseField(pybind11::module &m);
void generate_class_CThostFtdcLoginInfoField(pybind11::module &m);
void generate_class_CThostFtdcLogoutAllField(pybind11::module &m);
void generate_class_CThostFtdcFrontStatusField(pybind11::module &m);
void generate_class_CThostFtdcUserPasswordUpdateField(pybind11::module &m);
void generate_class_CThostFtdcInputOrderField(pybind11::module &m);
void generate_class_CThostFtdcOrderField(pybind11::module &m);
void generate_class_CThostFtdcExchangeOrderField(pybind11::module &m);
void generate_class_CThostFtdcExchangeOrderInsertErrorField(pybind11::module &m);
void generate_class_CThostFtdcInputOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeOrderActionErrorField(pybind11::module &m);
void generate_class_CThostFtdcExchangeTradeField(pybind11::module &m);
void generate_class_CThostFtdcTradeField(pybind11::module &m);
void generate_class_CThostFtdcUserSessionField(pybind11::module &m);
void generate_class_CThostFtdcQueryMaxOrderVolumeField(pybind11::module &m);
void generate_class_CThostFtdcSettlementInfoConfirmField(pybind11::module &m);
void generate_class_CThostFtdcSyncDepositField(pybind11::module &m);
void generate_class_CThostFtdcSyncFundMortgageField(pybind11::module &m);
void generate_class_CThostFtdcBrokerSyncField(pybind11::module &m);
void generate_class_CThostFtdcSyncingInvestorField(pybind11::module &m);
void generate_class_CThostFtdcSyncingTradingCodeField(pybind11::module &m);
void generate_class_CThostFtdcSyncingInvestorGroupField(pybind11::module &m);
void generate_class_CThostFtdcSyncingTradingAccountField(pybind11::module &m);
void generate_class_CThostFtdcSyncingInvestorPositionField(pybind11::module &m);
void generate_class_CThostFtdcSyncingInstrumentMarginRateField(pybind11::module &m);
void generate_class_CThostFtdcSyncingInstrumentCommissionRateField(pybind11::module &m);
void generate_class_CThostFtdcSyncingInstrumentTradingRightField(pybind11::module &m);
void generate_class_CThostFtdcQryOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryTradeField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorPositionField(pybind11::module &m);
void generate_class_CThostFtdcQryTradingAccountField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorField(pybind11::module &m);
void generate_class_CThostFtdcQryTradingCodeField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorGroupField(pybind11::module &m);
void generate_class_CThostFtdcQryInstrumentMarginRateField(pybind11::module &m);
void generate_class_CThostFtdcQryInstrumentCommissionRateField(pybind11::module &m);
void generate_class_CThostFtdcQryInstrumentTradingRightField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerField(pybind11::module &m);
void generate_class_CThostFtdcQryTraderField(pybind11::module &m);
void generate_class_CThostFtdcQrySuperUserFunctionField(pybind11::module &m);
void generate_class_CThostFtdcQryUserSessionField(pybind11::module &m);
void generate_class_CThostFtdcQryPartBrokerField(pybind11::module &m);
void generate_class_CThostFtdcQryFrontStatusField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQrySuperUserField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeField(pybind11::module &m);
void generate_class_CThostFtdcQryProductField(pybind11::module &m);
void generate_class_CThostFtdcQryInstrumentField(pybind11::module &m);
void generate_class_CThostFtdcQryDepthMarketDataField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerUserField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerUserFunctionField(pybind11::module &m);
void generate_class_CThostFtdcQryTraderOfferField(pybind11::module &m);
void generate_class_CThostFtdcQrySyncDepositField(pybind11::module &m);
void generate_class_CThostFtdcQrySettlementInfoField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeMarginRateField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeMarginRateAdjustField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeRateField(pybind11::module &m);
void generate_class_CThostFtdcQrySyncFundMortgageField(pybind11::module &m);
void generate_class_CThostFtdcQryHisOrderField(pybind11::module &m);
void generate_class_CThostFtdcOptionInstrMiniMarginField(pybind11::module &m);
void generate_class_CThostFtdcOptionInstrMarginAdjustField(pybind11::module &m);
void generate_class_CThostFtdcOptionInstrCommRateField(pybind11::module &m);
void generate_class_CThostFtdcOptionInstrTradeCostField(pybind11::module &m);
void generate_class_CThostFtdcQryOptionInstrTradeCostField(pybind11::module &m);
void generate_class_CThostFtdcQryOptionInstrCommRateField(pybind11::module &m);
void generate_class_CThostFtdcIndexPriceField(pybind11::module &m);
void generate_class_CThostFtdcInputExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcInputExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcExchangeExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcErrExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryErrExecOrderField(pybind11::module &m);
void generate_class_CThostFtdcErrExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryErrExecOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcOptionInstrTradingRightField(pybind11::module &m);
void generate_class_CThostFtdcQryOptionInstrTradingRightField(pybind11::module &m);
void generate_class_CThostFtdcInputForQuoteField(pybind11::module &m);
void generate_class_CThostFtdcForQuoteField(pybind11::module &m);
void generate_class_CThostFtdcQryForQuoteField(pybind11::module &m);
void generate_class_CThostFtdcExchangeForQuoteField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeForQuoteField(pybind11::module &m);
void generate_class_CThostFtdcInputQuoteField(pybind11::module &m);
void generate_class_CThostFtdcInputQuoteActionField(pybind11::module &m);
void generate_class_CThostFtdcQuoteField(pybind11::module &m);
void generate_class_CThostFtdcQuoteActionField(pybind11::module &m);
void generate_class_CThostFtdcQryQuoteField(pybind11::module &m);
void generate_class_CThostFtdcExchangeQuoteField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeQuoteField(pybind11::module &m);
void generate_class_CThostFtdcQryQuoteActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeQuoteActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeQuoteActionField(pybind11::module &m);
void generate_class_CThostFtdcOptionInstrDeltaField(pybind11::module &m);
void generate_class_CThostFtdcForQuoteRspField(pybind11::module &m);
void generate_class_CThostFtdcStrikeOffsetField(pybind11::module &m);
void generate_class_CThostFtdcQryStrikeOffsetField(pybind11::module &m);
void generate_class_CThostFtdcInputLockField(pybind11::module &m);
void generate_class_CThostFtdcLockField(pybind11::module &m);
void generate_class_CThostFtdcQryLockField(pybind11::module &m);
void generate_class_CThostFtdcLockPositionField(pybind11::module &m);
void generate_class_CThostFtdcQryLockPositionField(pybind11::module &m);
void generate_class_CThostFtdcETFOptionInstrCommRateField(pybind11::module &m);
void generate_class_CThostFtdcQryETFOptionInstrCommRateField(pybind11::module &m);
void generate_class_CThostFtdcPosiFreezeField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeLockField(pybind11::module &m);
void generate_class_CThostFtdcExchangeLockField(pybind11::module &m);
void generate_class_CThostFtdcExchangeExecOrderActionErrorField(pybind11::module &m);
void generate_class_CThostFtdcInputBatchOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcBatchOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeBatchOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryBatchOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcLimitPosiField(pybind11::module &m);
void generate_class_CThostFtdcQryLimitPosiField(pybind11::module &m);
void generate_class_CThostFtdcBrokerLimitPosiField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerLimitPosiField(pybind11::module &m);
void generate_class_CThostFtdcLimitPosiSField(pybind11::module &m);
void generate_class_CThostFtdcQryLimitPosiSField(pybind11::module &m);
void generate_class_CThostFtdcLimitPosiParamField(pybind11::module &m);
void generate_class_CThostFtdcBrokerLimitPosiParamField(pybind11::module &m);
void generate_class_CThostFtdcLimitPosiParamSField(pybind11::module &m);
void generate_class_CThostFtdcInputStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcQryStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcQryErrStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeStockDisposalActionErrorField(pybind11::module &m);
void generate_class_CThostFtdcErrStockDisposalActionField(pybind11::module &m);
void generate_class_CThostFtdcInvestorLevelField(pybind11::module &m);
void generate_class_CThostFtdcCombInstrumentGuardField(pybind11::module &m);
void generate_class_CThostFtdcQryCombInstrumentGuardField(pybind11::module &m);
void generate_class_CThostFtdcInputCombActionField(pybind11::module &m);
void generate_class_CThostFtdcCombActionField(pybind11::module &m);
void generate_class_CThostFtdcQryCombActionField(pybind11::module &m);
void generate_class_CThostFtdcExchangeCombActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeCombActionField(pybind11::module &m);
void generate_class_CThostFtdcProductExchRateField(pybind11::module &m);
void generate_class_CThostFtdcQryProductExchRateField(pybind11::module &m);
void generate_class_CThostFtdcInputDesignateField(pybind11::module &m);
void generate_class_CThostFtdcDesignateField(pybind11::module &m);
void generate_class_CThostFtdcQryDesignateField(pybind11::module &m);
void generate_class_CThostFtdcExchangeDesignateField(pybind11::module &m);
void generate_class_CThostFtdcInputStockDisposalField(pybind11::module &m);
void generate_class_CThostFtdcStockDisposalField(pybind11::module &m);
void generate_class_CThostFtdcQryStockDisposalField(pybind11::module &m);
void generate_class_CThostFtdcExchangeStockDisposalField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorLevelField(pybind11::module &m);
void generate_class_CThostFtdcQryForQuoteParamField(pybind11::module &m);
void generate_class_CThostFtdcForQuoteParamField(pybind11::module &m);
void generate_class_CThostFtdcQryExecFreezeField(pybind11::module &m);
void generate_class_CThostFtdcExecFreezeField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataBaseField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataStaticField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataLastMatchField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataBestPriceField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataBid23Field(pybind11::module &m);
void generate_class_CThostFtdcMarketDataAsk23Field(pybind11::module &m);
void generate_class_CThostFtdcMarketDataBid45Field(pybind11::module &m);
void generate_class_CThostFtdcMarketDataAsk45Field(pybind11::module &m);
void generate_class_CThostFtdcMarketDataUpdateTimeField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataExchangeField(pybind11::module &m);
void generate_class_CThostFtdcSpecificInstrumentField(pybind11::module &m);
void generate_class_CThostFtdcInstrumentStatusField(pybind11::module &m);
void generate_class_CThostFtdcQryInstrumentStatusField(pybind11::module &m);
void generate_class_CThostFtdcInvestorAccountField(pybind11::module &m);
void generate_class_CThostFtdcPositionProfitAlgorithmField(pybind11::module &m);
void generate_class_CThostFtdcDiscountField(pybind11::module &m);
void generate_class_CThostFtdcQryTransferBankField(pybind11::module &m);
void generate_class_CThostFtdcTransferBankField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorPositionDetailField(pybind11::module &m);
void generate_class_CThostFtdcInvestorPositionDetailField(pybind11::module &m);
void generate_class_CThostFtdcTradingAccountPasswordField(pybind11::module &m);
void generate_class_CThostFtdcMDTraderOfferField(pybind11::module &m);
void generate_class_CThostFtdcQryMDTraderOfferField(pybind11::module &m);
void generate_class_CThostFtdcQryNoticeField(pybind11::module &m);
void generate_class_CThostFtdcNoticeField(pybind11::module &m);
void generate_class_CThostFtdcUserRightField(pybind11::module &m);
void generate_class_CThostFtdcQrySettlementInfoConfirmField(pybind11::module &m);
void generate_class_CThostFtdcLoadSettlementInfoField(pybind11::module &m);
void generate_class_CThostFtdcBrokerWithdrawAlgorithmField(pybind11::module &m);
void generate_class_CThostFtdcTradingAccountPasswordUpdateV1Field(pybind11::module &m);
void generate_class_CThostFtdcTradingAccountPasswordUpdateField(pybind11::module &m);
void generate_class_CThostFtdcQryCombinationLegField(pybind11::module &m);
void generate_class_CThostFtdcQrySyncStatusField(pybind11::module &m);
void generate_class_CThostFtdcCombinationLegField(pybind11::module &m);
void generate_class_CThostFtdcSyncStatusField(pybind11::module &m);
void generate_class_CThostFtdcQryLinkManField(pybind11::module &m);
void generate_class_CThostFtdcLinkManField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerUserEventField(pybind11::module &m);
void generate_class_CThostFtdcBrokerUserEventField(pybind11::module &m);
void generate_class_CThostFtdcQryContractBankField(pybind11::module &m);
void generate_class_CThostFtdcContractBankField(pybind11::module &m);
void generate_class_CThostFtdcInvestorPositionCombineDetailField(pybind11::module &m);
void generate_class_CThostFtdcParkedOrderField(pybind11::module &m);
void generate_class_CThostFtdcParkedOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryParkedOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryParkedOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcRemoveParkedOrderField(pybind11::module &m);
void generate_class_CThostFtdcRemoveParkedOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcInvestorWithdrawAlgorithmField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorPositionCombineDetailField(pybind11::module &m);
void generate_class_CThostFtdcMarketDataAveragePriceField(pybind11::module &m);
void generate_class_CThostFtdcVerifyInvestorPasswordField(pybind11::module &m);
void generate_class_CThostFtdcUserIPField(pybind11::module &m);
void generate_class_CThostFtdcTradingNoticeInfoField(pybind11::module &m);
void generate_class_CThostFtdcTradingNoticeField(pybind11::module &m);
void generate_class_CThostFtdcQryTradingNoticeField(pybind11::module &m);
void generate_class_CThostFtdcQryErrOrderField(pybind11::module &m);
void generate_class_CThostFtdcErrOrderField(pybind11::module &m);
void generate_class_CThostFtdcErrorConditionalOrderField(pybind11::module &m);
void generate_class_CThostFtdcQryErrOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcErrOrderActionField(pybind11::module &m);
void generate_class_CThostFtdcQryExchangeSequenceField(pybind11::module &m);
void generate_class_CThostFtdcExchangeSequenceField(pybind11::module &m);
void generate_class_CThostFtdcQueryMaxOrderVolumeWithPriceField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerTradingParamsField(pybind11::module &m);
void generate_class_CThostFtdcBrokerTradingParamsField(pybind11::module &m);
void generate_class_CThostFtdcQryBrokerTradingAlgosField(pybind11::module &m);
void generate_class_CThostFtdcBrokerTradingAlgosField(pybind11::module &m);
void generate_class_CThostFtdcQueryBrokerDepositField(pybind11::module &m);
void generate_class_CThostFtdcBrokerDepositField(pybind11::module &m);
void generate_class_CThostFtdcQryCFMMCBrokerKeyField(pybind11::module &m);
void generate_class_CThostFtdcCFMMCBrokerKeyField(pybind11::module &m);
void generate_class_CThostFtdcCFMMCTradingAccountKeyField(pybind11::module &m);
void generate_class_CThostFtdcQryCFMMCTradingAccountKeyField(pybind11::module &m);
void generate_class_CThostFtdcBrokerUserOTPParamField(pybind11::module &m);
void generate_class_CThostFtdcManualSyncBrokerUserOTPField(pybind11::module &m);
void generate_class_CThostFtdcCommRateModelField(pybind11::module &m);
void generate_class_CThostFtdcQryCommRateModelField(pybind11::module &m);
void generate_class_CThostFtdcMarginModelField(pybind11::module &m);
void generate_class_CThostFtdcQryMarginModelField(pybind11::module &m);
void generate_class_CThostFtdcEWarrantOffsetField(pybind11::module &m);
void generate_class_CThostFtdcQryEWarrantOffsetField(pybind11::module &m);
void generate_class_CThostFtdcQryInvestorProductGroupMarginField(pybind11::module &m);
void generate_class_CThostFtdcInvestorProductGroupMarginField(pybind11::module &m);
void generate_class_CThostFtdcQueryCFMMCTradingAccountTokenField(pybind11::module &m);
void generate_class_CThostFtdcCFMMCTradingAccountTokenField(pybind11::module &m);
void generate_class_CThostFtdcInstructionRightField(pybind11::module &m);
void generate_class_CThostFtdcQryProductGroupField(pybind11::module &m);
void generate_class_CThostFtdcProductGroupField(pybind11::module &m);
void generate_class_CThostFtdcReqOpenAccountField(pybind11::module &m);
void generate_class_CThostFtdcReqCancelAccountField(pybind11::module &m);
void generate_class_CThostFtdcReqChangeAccountField(pybind11::module &m);
void generate_class_CThostFtdcReqTransferField(pybind11::module &m);
void generate_class_CThostFtdcRspTransferField(pybind11::module &m);
void generate_class_CThostFtdcReqRepealField(pybind11::module &m);
void generate_class_CThostFtdcRspRepealField(pybind11::module &m);
void generate_class_CThostFtdcReqQueryAccountField(pybind11::module &m);
void generate_class_CThostFtdcRspQueryAccountField(pybind11::module &m);
void generate_class_CThostFtdcFutureSignIOField(pybind11::module &m);
void generate_class_CThostFtdcRspFutureSignInField(pybind11::module &m);
void generate_class_CThostFtdcReqFutureSignOutField(pybind11::module &m);
void generate_class_CThostFtdcRspFutureSignOutField(pybind11::module &m);
void generate_class_CThostFtdcReqQueryTradeResultBySerialField(pybind11::module &m);
void generate_class_CThostFtdcRspQueryTradeResultBySerialField(pybind11::module &m);
void generate_class_CThostFtdcReqDayEndFileReadyField(pybind11::module &m);
void generate_class_CThostFtdcReturnResultField(pybind11::module &m);
void generate_class_CThostFtdcVerifyFuturePasswordField(pybind11::module &m);
void generate_class_CThostFtdcVerifyCustInfoField(pybind11::module &m);
void generate_class_CThostFtdcVerifyFuturePasswordAndCustInfoField(pybind11::module &m);
void generate_class_CThostFtdcDepositResultInformField(pybind11::module &m);
void generate_class_CThostFtdcReqSyncKeyField(pybind11::module &m);
void generate_class_CThostFtdcRspSyncKeyField(pybind11::module &m);
void generate_class_CThostFtdcNotifyQueryAccountField(pybind11::module &m);
void generate_class_CThostFtdcTransferSerialField(pybind11::module &m);
void generate_class_CThostFtdcQryTransferSerialField(pybind11::module &m);
void generate_class_CThostFtdcNotifyFutureSignInField(pybind11::module &m);
void generate_class_CThostFtdcNotifyFutureSignOutField(pybind11::module &m);
void generate_class_CThostFtdcNotifySyncKeyField(pybind11::module &m);
void generate_class_CThostFtdcQryAccountregisterField(pybind11::module &m);
void generate_class_CThostFtdcAccountregisterField(pybind11::module &m);
void generate_class_CThostFtdcOpenAccountField(pybind11::module &m);
void generate_class_CThostFtdcCancelAccountField(pybind11::module &m);
void generate_class_CThostFtdcChangeAccountField(pybind11::module &m);
void generate_class_CThostFtdcSecAgentACIDMapField(pybind11::module &m);
void generate_class_CThostFtdcQrySecAgentACIDMapField(pybind11::module &m);
void generate_class_CThostFtdcUserRightsAssignField(pybind11::module &m);
void generate_class_CThostFtdcBrokerUserRightAssignField(pybind11::module &m);
void generate_class_CThostFtdcDRTransferField(pybind11::module &m);
void generate_class_CThostFtdcFensUserInfoField(pybind11::module &m);
void generate_class_CThostFtdcCurrTransferIdentityField(pybind11::module &m);
void generate_class_CThostFtdcLoginForbiddenUserField(pybind11::module &m);
void generate_class_CThostFtdcQryLoginForbiddenUserField(pybind11::module &m);
void generate_class_CThostFtdcMulticastGroupInfoField(pybind11::module &m);
void generate_class_CThostFtdcTradingAccountReserveField(pybind11::module &m);
void generate_class_CThostFtdcDBFRecordField(pybind11::module &m);
void generate_class_CThostFtdcTraderSpi(pybind11::module &m);
void generate_class_CThostFtdcTraderApi(pybind11::module &m);


