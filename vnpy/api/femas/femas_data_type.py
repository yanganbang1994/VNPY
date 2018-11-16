# encoding: UTF-8

defineDict = {}
typedefDict = {}

#//////////////////////////////////////////////////////////////////////
#@system 风控前置系统
#@company CFFEX
#@file USTPFtdcUserApiDataType.h
#@brief 定义了客户端接口使用的业务数据类型
#@history
#
#//////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////////////////
#TFtdcUstpPriceTickType是一个最小变动价位类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcPriceTickType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpPriceType是一个价格类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcPriceType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpRatioType是一个比率类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcRatioType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpMoneyType是一个资金类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcMoneyType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpLargeVolumeType是一个大额数量类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcLargeVolumeType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpSequenceNoType是一个序列号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcSequenceNoType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpMillisecType是一个最后修改毫秒类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcMillisecType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpVolumeType是一个数量类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcVolumeType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpUnderlyingMultipleType是一个合约乘数类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcUnderlyingMultipleType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpVolumeMultipleType是一个数量乘数类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcVolumeMultipleType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpSequenceSeriesType是一个序列系列号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcSequenceSeriesType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpErrorIDType是一个错误代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcErrorIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpDataCenterIDType是一个数据中心代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcDataCenterIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpSettlementIDType是一个结算编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcSettlementIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpMonthType是一个月份类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcMonthType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpBoolType是一个布尔型类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcBoolType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpYearType是一个年类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcYearType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpMemTableNameType是一个内存表名类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcMemTableNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOrderSysIDType是一个报单编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcOrderSysIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpTradeIDType是一个成交编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcTradeIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpUserIDType是一个用户代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcUserIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpParticipantIDType是一个会员编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcParticipantIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpIPAddressType是一个IP地址类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcIPAddressType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpMacAddressType是一个Mac地址类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcMacAddressType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpInstrumentNameType是一个合约名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcInstrumentNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpInstrumentIDType是一个合约编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcInstrumentIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpExchangeNameType是一个交易所名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcExchangeNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpExchangeIDType是一个交易所代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcExchangeIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpDateType是一个日期类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcDateType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpTimeType是一个时间类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcTimeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpClientIDType是一个客户编码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcClientIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpAccountIDType是一个资金帐号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcAccountIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpSeatIDType是一个席位号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcSeatIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpProductNameType是一个品种名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcProductNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpUserOrderLocalIDType是一个用户本地报单号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcUserOrderLocalIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOrderLocalIDType是一个本地报单编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcOrderLocalIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpInvestorIDType是一个投资者编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcInvestorIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpUserNameType是一个用户编码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcUserNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpPasswordType是一个密码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcPasswordType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpProductInfoType是一个产品信息类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcProductInfoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpProtocolInfoType是一个协议信息类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcProtocolInfoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpBusinessUnitType是一个业务单元类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcBusinessUnitType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpTradingSystemNameType是一个交易系统名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcTradingSystemNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpBrokerIDType是一个经纪公司代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcBrokerIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpCustomType是一个用户自定义域类型类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcCustomType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpTradingDayType是一个交易日类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcTradingDayType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpDepartmentType是一个营业部类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcDepartmentType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpGrantFuncSetType是一个授权功能号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcGrantFuncSetType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpProductIDType是一个品种编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcProductIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpAccountSeqNoType是一个资金流水号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcAccountSeqNoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpSettlementGroupIDType是一个结算组代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcSettlementGroupIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpErrorMsgType是一个错误信息类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcErrorMsgType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpVolumeConditionType是一个成交量类型类型
#//////////////////////////////////////////////////////////////////////
#任何数量
defineDict["USTP_FTDC_VC_AV"] = '1'
#最小数量
defineDict["USTP_FTDC_VC_MV"] = '2'
#全部数量
defineDict["USTP_FTDC_VC_CV"] = '3'

typedefDict["TUstpFtdcVolumeConditionType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpForceCloseReasonType是一个强平原因类型
#//////////////////////////////////////////////////////////////////////
#非强平
defineDict["USTP_FTDC_FCR_NotForceClose"] = '0'
#资金不足
defineDict["USTP_FTDC_FCR_LackDeposit"] = '1'
#客户超仓
defineDict["USTP_FTDC_FCR_ClientOverPositionLimit"] = '2'
#会员超仓
defineDict["USTP_FTDC_FCR_MemberOverPositionLimit"] = '3'
#持仓非整数倍
defineDict["USTP_FTDC_FCR_NotMultiple"] = '4'

typedefDict["TUstpFtdcForceCloseReasonType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpInstrumentStatusType是一个合约交易状态类型
#//////////////////////////////////////////////////////////////////////
#开盘前
defineDict["USTP_FTDC_IS_BeforeTrading"] = '0'
#非交易
defineDict["USTP_FTDC_IS_NoTrading"] = '1'
#连续交易
defineDict["USTP_FTDC_IS_Continous"] = '2'
#集合竞价报单
defineDict["USTP_FTDC_IS_AuctionOrdering"] = '3'
#集合竞价价格平衡
defineDict["USTP_FTDC_IS_AuctionBalance"] = '4'
#集合竞价撮合
defineDict["USTP_FTDC_IS_AuctionMatch"] = '5'
#收盘
defineDict["USTP_FTDC_IS_Closed"] = '6'

typedefDict["TUstpFtdcInstrumentStatusType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOffsetFlagType是一个开平标志类型
#//////////////////////////////////////////////////////////////////////
#开仓
defineDict["USTP_FTDC_OF_Open"] = '0'
#平仓
defineDict["USTP_FTDC_OF_Close"] = '1'
#强平
defineDict["USTP_FTDC_OF_ForceClose"] = '2'
#平今
defineDict["USTP_FTDC_OF_CloseToday"] = '3'
#平昨
defineDict["USTP_FTDC_OF_CloseYesterday"] = '4'

typedefDict["TUstpFtdcOffsetFlagType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOrderPriceTypeType是一个报单价格条件类型
#//////////////////////////////////////////////////////////////////////
#任意价
defineDict["USTP_FTDC_OPT_AnyPrice"] = '1'
#限价
defineDict["USTP_FTDC_OPT_LimitPrice"] = '2'
#最优价
defineDict["USTP_FTDC_OPT_BestPrice"] = '3'
#五档价
defineDict["USTP_FTDC_OPT_FiveLevelPrice"] = '4'

typedefDict["TUstpFtdcOrderPriceTypeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOrderStatusType是一个报单状态类型
#//////////////////////////////////////////////////////////////////////
#全部成交
defineDict["USTP_FTDC_OS_AllTraded"] = '0'
#部分成交还在队列中
defineDict["USTP_FTDC_OS_PartTradedQueueing"] = '1'
#部分成交不在队列中
defineDict["USTP_FTDC_OS_PartTradedNotQueueing"] = '2'
#未成交还在队列中
defineDict["USTP_FTDC_OS_NoTradeQueueing"] = '3'
#未成交不在队列中
defineDict["USTP_FTDC_OS_NoTradeNotQueueing"] = '4'
#撤单
defineDict["USTP_FTDC_OS_Canceled"] = '5'
#订单已报入交易所未应答
defineDict["USTP_FTDC_OS_AcceptedNoReply"] = '6'

typedefDict["TUstpFtdcOrderStatusType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpUserTypeType是一个用户类型类型
#//////////////////////////////////////////////////////////////////////
#自然人
defineDict["USTP_FTDC_UT_Person"] = '1'
#理财产品
defineDict["USTP_FTDC_UT_Product"] = '2'
#期货公司管理员
defineDict["USTP_FTDC_UT_Manager"] = '3'
#席位
defineDict["USTP_FTDC_UT_Seat"] = '4'

typedefDict["TUstpFtdcUserTypeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpTradingRightType是一个交易权限类型
#//////////////////////////////////////////////////////////////////////
#可以交易
defineDict["USTP_FTDC_TR_Allow"] = '0'
#只能平仓
defineDict["USTP_FTDC_TR_CloseOnly"] = '1'
#不能交易
defineDict["USTP_FTDC_TR_Forbidden"] = '2'

typedefDict["TUstpFtdcTradingRightType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpTimeConditionType是一个有效期类型类型
#//////////////////////////////////////////////////////////////////////
#立即完成，否则撤销
defineDict["USTP_FTDC_TC_IOC"] = '1'
#本节有效
defineDict["USTP_FTDC_TC_GFS"] = '2'
#当日有效
defineDict["USTP_FTDC_TC_GFD"] = '3'
#指定日期前有效
defineDict["USTP_FTDC_TC_GTD"] = '4'
#撤销前有效
defineDict["USTP_FTDC_TC_GTC"] = '5'
#集合竞价有效
defineDict["USTP_FTDC_TC_GFA"] = '6'

typedefDict["TUstpFtdcTimeConditionType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOrderSourceType是一个报单来源类型
#//////////////////////////////////////////////////////////////////////
#来自参与者
defineDict["USTP_FTDC_OS_Participant"] = '0'
#来自管理员
defineDict["USTP_FTDC_OS_Administrator"] = '1'

typedefDict["TUstpFtdcOrderSourceType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpDirectionType是一个买卖方向类型
#//////////////////////////////////////////////////////////////////////
#买
defineDict["USTP_FTDC_D_Buy"] = '0'
#卖
defineDict["USTP_FTDC_D_Sell"] = '1'

typedefDict["TUstpFtdcDirectionType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpCurrencyType是一个币种类型
#//////////////////////////////////////////////////////////////////////
#人民币
defineDict["USTP_FTDC_C_RMB"] = '1'
#美元
defineDict["USTP_FTDC_C_UDOLLAR"] = '2'

typedefDict["TUstpFtdcCurrencyType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpAccountDirectionType是一个出入金方向类型
#//////////////////////////////////////////////////////////////////////
#入金
defineDict["USTP_FTDC_AD_In"] = '1'
#出金
defineDict["USTP_FTDC_AD_Out"] = '2'

typedefDict["TUstpFtdcAccountDirectionType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpHedgeFlagType是一个投机套保标志类型
#//////////////////////////////////////////////////////////////////////
#投机
defineDict["USTP_FTDC_CHF_Speculation"] = '1'
#套利
defineDict["USTP_FTDC_CHF_Arbitrage"] = '2'
#套保
defineDict["USTP_FTDC_CHF_Hedge"] = '3'
#做市商
defineDict["USTP_FTDC_CHF_MarketMaker"] = '4'

typedefDict["TUstpFtdcHedgeFlagType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpActionFlagType是一个操作标志类型
#//////////////////////////////////////////////////////////////////////
#删除
defineDict["USTP_FTDC_AF_Delete"] = '0'
#挂起
defineDict["USTP_FTDC_AF_Suspend"] = '1'
#激活
defineDict["USTP_FTDC_AF_Active"] = '2'
#修改
defineDict["USTP_FTDC_AF_Modify"] = '3'

typedefDict["TUstpFtdcActionFlagType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpPositionTypeType是一个持仓类型类型
#//////////////////////////////////////////////////////////////////////
#净持仓
defineDict["USTP_FTDC_PT_Net"] = '1'
#综合持仓
defineDict["USTP_FTDC_PT_Gross"] = '2'

typedefDict["TUstpFtdcPositionTypeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpOptionsTypeType是一个期权类型类型
#//////////////////////////////////////////////////////////////////////
#非期权
defineDict["USTP_FTDC_OT_NotOptions"] = '0'
#看涨
defineDict["USTP_FTDC_OT_CallOptions"] = '1'
#看跌
defineDict["USTP_FTDC_OT_PutOptions"] = '2'

typedefDict["TUstpFtdcOptionsTypeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpIsActiveType是一个是否活跃类型
#//////////////////////////////////////////////////////////////////////
#不活跃
defineDict["USTP_FTDC_UIA_NoActive"] = '0'
#活跃
defineDict["USTP_FTDC_UIA_Active"] = '1'

typedefDict["TUstpFtdcIsActiveType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUstpCurrencyIDType是一个币种代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TUstpFtdcCurrencyIDType"] = "string"
