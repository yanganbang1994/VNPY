# encoding: UTF-8

defineDict = {}
typedefDict = {}

#//////////////////////////////////////////////////////////////////////
#@system QuantDo Platform
#@company QuantDo
#@file QdpFtdcUserApiDataType.h
#@brief 定义了客户端接口使用的业务数据类型
#@history
#
#//////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////////////////
#定义交易通道类型类别
#//////////////////////////////////////////////////////////////////////
defineDict["QDP_EI_CFFEX"] = "CFFEX"
defineDict["QDP_EI_SHFE"] = "SHFE"
defineDict["QDP_EI_DCE"] = "DCE"
defineDict["QDP_EI_ZCE"] = "CZCE"
defineDict["QDP_EI_SSE"] = "SSE"
defineDict["QDP_EI_SZSE"] = "SZSE"
defineDict["QDP_EI_SGE"] = "SGE"
defineDict["QDP_EI_CME"] = "CME"
defineDict["QDP_EI_LME"] = "LME"
defineDict["QDP_EI_GTJA"] = "GTJA"
defineDict["QDP_EI_INE"] = "INE"


#//////////////////////////////////////////////////////////////////////
#TFtdcPriceTickType是一个最小变动价位类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcPriceTickType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcPriceType是一个价格类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcPriceType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcRatioType是一个比率类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcRatioType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcMoneyType是一个资金类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcMoneyType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcLargeVolumeType是一个大额数量类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcLargeVolumeType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcFeeType是一个费用类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcFeeType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcInventoryType是一个库存类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcInventoryType"] = "float"

#//////////////////////////////////////////////////////////////////////
#TFtdcSequenceNoType是一个序列号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSequenceNoType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcMillisecType是一个最后修改毫秒类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcMillisecType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcVolumeType是一个数量类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcVolumeType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcUnderlyingMultipleType是一个合约乘数类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcUnderlyingMultipleType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcVolumeMultipleType是一个数量乘数类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcVolumeMultipleType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcSequenceSeriesType是一个序列系列号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSequenceSeriesType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcSessionIDType是一个会话编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSessionIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcErrorIDType是一个错误代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcErrorIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcDataCenterIDType是一个数据中心代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcDataCenterIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcFrontIDType是一个前置编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcFrontIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcRequestIDType是一个报单编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcRequestIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcTopicIDType是一个主题代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTopicIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcSettlementIDType是一个结算编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSettlementIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcTotalNumsType是一个累加次数类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTotalNumsType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcDiffSndType是一个偏差时间类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcDiffSndType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcTIDType是一个交易ID类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTIDType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcMonthType是一个月份类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcMonthType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcBoolType是一个布尔型类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBoolType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcYearType是一个年类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcYearType"] = "int"

#//////////////////////////////////////////////////////////////////////
#TFtdcMemTableNameType是一个内存表名类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcMemTableNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcOrderSysIDType是一个报单编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcOrderSysIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcTradeIDType是一个成交编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTradeIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUserIDType是一个用户代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcUserIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcParticipantIDType是一个会员编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcParticipantIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcIPAddressType是一个IP地址类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcIPAddressType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcMacAddressType是一个Mac地址类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcMacAddressType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcInstrumentNameType是一个合约名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcInstrumentNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBranchIDType是一个营业部代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBranchIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcInstrumentIDType是一个合约编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcInstrumentIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcIdentifiedCardNoType是一个证件号码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcIdentifiedCardNoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcIdentifiedCardTypeType是一个证件类型类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcIdentifiedCardTypeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcExchangeIDType是一个交易(所)通道类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcExchangeIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcExchangeNameType是一个交易(所)所名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcExchangeNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcDateType是一个日期类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcDateType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcTimeType是一个时间类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTimeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcClientTypeType是一个客户类型类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcClientTypeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcClientNameType是一个客户名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcClientNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcClientIDType是一个客户编码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcClientIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcAccountIDType是一个资金帐号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcAccountIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcSeatIDType是一个席位号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSeatIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcProductNameType是一个品种名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcProductNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUserOrderLocalIDType是一个用户本地报单号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcUserOrderLocalIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcOrderLocalIDType是一个本地报单编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcOrderLocalIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcInvestorIDType是一个投资者编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcInvestorIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcUserNameType是一个用户编码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcUserNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcPasswordType是一个密码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcPasswordType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcAbstractType是一个消息摘要类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcAbstractType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcProductInfoType是一个产品信息类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcProductInfoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcProtocolInfoType是一个协议信息类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcProtocolInfoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBusinessUnitType是一个业务单元类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBusinessUnitType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcTradingSystemNameType是一个交易系统名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTradingSystemNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBrokerIDType是一个经纪公司代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBrokerIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcCustomType是一个用户自定义域类型类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcCustomType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcTradingDayType是一个交易日类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTradingDayType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcDepartmentType是一个营业部类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcDepartmentType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcGrantFuncSetType是一个授权功能号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcGrantFuncSetType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcProductIDType是一个品种编号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcProductIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcAccountSeqNoType是一个资金流水号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcAccountSeqNoType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcSettlementGroupIDType是一个结算组代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSettlementGroupIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBankIDType是一个银行代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBankIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBankBrchIDType是一个银行分中心代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBankBrchIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBankAccountType是一个银行账号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBankAccountType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcNameType是一个名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcTradeCodeType是一个业务功能码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcTradeCodeType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcSerialType是一个流水号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcSerialType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcDeviceIDType是一个渠道标志类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcDeviceIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBankCodingForFutureType是一个期货公司银行编码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcBankCodingForFutureType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcErrorMsgType是一个错误信息类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcErrorMsgType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcVolumeConditionType是一个成交量类型类型
#//////////////////////////////////////////////////////////////////////
#任何数量
defineDict["QDP_FTDC_VC_AV"] = '1'
#最小数量
defineDict["QDP_FTDC_VC_MV"] = '2'
#全部数量
defineDict["QDP_FTDC_VC_CV"] = '3'

typedefDict["TQdpFtdcVolumeConditionType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcForceCloseReasonType是一个强平原因类型
#//////////////////////////////////////////////////////////////////////
#非强平
defineDict["QDP_FTDC_FCR_NotForceClose"] = '0'
#资金不足
defineDict["QDP_FTDC_FCR_LackDeposit"] = '1'
#客户超仓
defineDict["QDP_FTDC_FCR_ClientOverPositionLimit"] = '2'
#会员超仓
defineDict["QDP_FTDC_FCR_MemberOverPositionLimit"] = '3'
#持仓非整数倍
defineDict["QDP_FTDC_FCR_NotMultiple"] = '4'

typedefDict["TQdpFtdcForceCloseReasonType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcInstrumentStatusType是一个合约交易状态类型
#//////////////////////////////////////////////////////////////////////
#开盘前
defineDict["QDP_FTDC_IS_BeforeTrading"] = '0'
#非交易
defineDict["QDP_FTDC_IS_NoTrading"] = '1'
#连续交易
defineDict["QDP_FTDC_IS_Continous"] = '2'
#集合竞价报单
defineDict["QDP_FTDC_IS_AuctionOrdering"] = '3'
#集合竞价价格平衡
defineDict["QDP_FTDC_IS_AuctionBalance"] = '4'
#集合竞价撮合
defineDict["QDP_FTDC_IS_AuctionMatch"] = '5'
#收盘
defineDict["QDP_FTDC_IS_Closed"] = '6'
#金交所交割申报
defineDict["QDP_FTDC_IS_SGE_Dery_App"] = '7'
#金交所交割申报结束
defineDict["QDP_FTDC_IS_SGE_Dery_Match"] = '8'
#金交所中立仓申报
defineDict["QDP_FTDC_IS_SGE_Mid_App"] = '9'
#金交所交割申报撮合
defineDict["QDP_FTDC_IS_SGE_Mid_Match"] = 'a'
#大商所自动转换报警
defineDict["QDP_FTDC_IS_DCE_MarketStatusAlarm"] = 'b'

typedefDict["TQdpFtdcInstrumentStatusType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcOffsetFlagType是一个开平标志类型
#//////////////////////////////////////////////////////////////////////
#开仓
defineDict["QDP_FTDC_OF_Open"] = '0'
#平仓
defineDict["QDP_FTDC_OF_Close"] = '1'
#强平
defineDict["QDP_FTDC_OF_ForceClose"] = '2'
#平今
defineDict["QDP_FTDC_OF_CloseToday"] = '3'
#平昨
defineDict["QDP_FTDC_OF_CloseYesterday"] = '4'

typedefDict["TQdpFtdcOffsetFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcOrderPriceTypeType是一个报单价格条件类型
#//////////////////////////////////////////////////////////////////////
#任意价
defineDict["QDP_FTDC_OPT_AnyPrice"] = '1'
#限价
defineDict["QDP_FTDC_OPT_LimitPrice"] = '2'
#最优价
defineDict["QDP_FTDC_OPT_BestPrice"] = '3'
#五档价
defineDict["QDP_FTDC_OPT_FiveLevelPrice"] = '4'

typedefDict["TQdpFtdcOrderPriceTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcOrderStatusType是一个报单状态类型
#//////////////////////////////////////////////////////////////////////
#全部成交
defineDict["QDP_FTDC_OS_AllTraded"] = '0'
#部分成交还在队列中
defineDict["QDP_FTDC_OS_PartTradedQueueing"] = '1'
#部分成交不在队列中
defineDict["QDP_FTDC_OS_PartTradedNotQueueing"] = '2'
#未成交还在队列中
defineDict["QDP_FTDC_OS_NoTradeQueueing"] = '3'
#未成交不在队列中
defineDict["QDP_FTDC_OS_NoTradeNotQueueing"] = '4'
#撤单
defineDict["QDP_FTDC_OS_Canceled"] = '5'
#订单已报入交易所未应答
defineDict["QDP_FTDC_OS_AcceptedNoReply"] = '6'

typedefDict["TQdpFtdcOrderStatusType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcUserTypeType是一个用户类型类型
#//////////////////////////////////////////////////////////////////////
#自然人
defineDict["QDP_FTDC_UT_Person"] = '1'
#理财产品
defineDict["QDP_FTDC_UT_Product"] = '2'
#期货公司管理员
defineDict["QDP_FTDC_UT_Manager"] = '3'
#席位
defineDict["QDP_FTDC_UT_Seat"] = '4'

typedefDict["TQdpFtdcUserTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcTradingRightType是一个交易权限类型
#//////////////////////////////////////////////////////////////////////
#可以交易
defineDict["QDP_FTDC_TR_Allow"] = '0'
#只能平仓
defineDict["QDP_FTDC_TR_CloseOnly"] = '1'
#不能交易
defineDict["QDP_FTDC_TR_Forbidden"] = '2'

typedefDict["TQdpFtdcTradingRightType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcTimeConditionType是一个有效期类型类型
#//////////////////////////////////////////////////////////////////////
#立即完成，否则撤销
defineDict["QDP_FTDC_TC_IOC"] = '1'
#本节有效
defineDict["QDP_FTDC_TC_GFS"] = '2'
#当日有效
defineDict["QDP_FTDC_TC_GFD"] = '3'
#指定日期前有效
defineDict["QDP_FTDC_TC_GTD"] = '4'
#撤销前有效
defineDict["QDP_FTDC_TC_GTC"] = '5'
#集合竞价有效
defineDict["QDP_FTDC_TC_GFA"] = '6'

typedefDict["TQdpFtdcTimeConditionType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcOrderSourceType是一个报单来源类型
#//////////////////////////////////////////////////////////////////////
#来自参与者
defineDict["QDP_FTDC_OS_Participant"] = '0'
#来自管理员
defineDict["QDP_FTDC_OS_Administrator"] = '1'

typedefDict["TQdpFtdcOrderSourceType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcDirectionType是一个买卖方向类型
#//////////////////////////////////////////////////////////////////////
#买
defineDict["QDP_FTDC_D_Buy"] = '0'
#卖
defineDict["QDP_FTDC_D_Sell"] = '1'

typedefDict["TQdpFtdcDirectionType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcCurrencyType是一个币种类型
#//////////////////////////////////////////////////////////////////////
#人民币
defineDict["QDP_FTDC_C_RMB"] = '1'
#美元
defineDict["QDP_FTDC_C_UDOLLAR"] = '2'

typedefDict["TQdpFtdcCurrencyType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcAccountDirectionType是一个出入金方向类型
#//////////////////////////////////////////////////////////////////////
#入金
defineDict["QDP_FTDC_AD_In"] = '1'
#出金
defineDict["QDP_FTDC_AD_Out"] = '2'

typedefDict["TQdpFtdcAccountDirectionType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcClientHedgeFlagType是一个客户投机套保标志类型
#//////////////////////////////////////////////////////////////////////
#投机
defineDict["QDP_FTDC_CHF_Speculation"] = '1'
#套利
defineDict["QDP_FTDC_CHF_Arbitrage"] = '2'
#套保
defineDict["QDP_FTDC_CHF_Hedge"] = '3'
#做市商
defineDict["QDP_FTDC_CHF_MarketMaker"] = '4'

typedefDict["TQdpFtdcClientHedgeFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcHedgeFlagType是一个投机套保标志类型
#//////////////////////////////////////////////////////////////////////
#投机
defineDict["QDP_FTDC_CHF_Speculation"] = '1'
#套利
defineDict["QDP_FTDC_CHF_Arbitrage"] = '2'
#套保
defineDict["QDP_FTDC_CHF_Hedge"] = '3'
#做市商
defineDict["QDP_FTDC_CHF_MarketMaker"] = '4'

typedefDict["TQdpFtdcHedgeFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcActionFlagType是一个操作标志类型
#//////////////////////////////////////////////////////////////////////
#删除
defineDict["QDP_FTDC_AF_Delete"] = '0'
#挂起
defineDict["QDP_FTDC_AF_Suspend"] = '1'
#激活
defineDict["QDP_FTDC_AF_Active"] = '2'
#修改
defineDict["QDP_FTDC_AF_Modify"] = '3'

typedefDict["TQdpFtdcActionFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcPositionTypeType是一个持仓类型类型
#//////////////////////////////////////////////////////////////////////
#净持仓
defineDict["QDP_FTDC_PT_Net"] = '1'
#综合持仓
defineDict["QDP_FTDC_PT_Gross"] = '2'

typedefDict["TQdpFtdcPositionTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcOptionsTypeType是一个期权类型类型
#//////////////////////////////////////////////////////////////////////
#非期权
defineDict["QDP_FTDC_OT_NotOptions"] = '0'
#看涨
defineDict["QDP_FTDC_OT_CallOptions"] = '1'
#看跌
defineDict["QDP_FTDC_OT_PutOptions"] = '2'

typedefDict["TQdpFtdcOptionsTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcIsActiveType是一个是否活跃类型
#//////////////////////////////////////////////////////////////////////
#不活跃
defineDict["QDP_FTDC_UIA_NoActive"] = '0'
#活跃
defineDict["QDP_FTDC_UIA_Active"] = '1'

typedefDict["TQdpFtdcIsActiveType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcProductClassType是一个产品类型类型
#//////////////////////////////////////////////////////////////////////
#期货
defineDict["QDP_FTDC_PC_Futures"] = '1'
#期权
defineDict["QDP_FTDC_PC_Options"] = '2'
#组合
defineDict["QDP_FTDC_PC_Combination"] = '3'
#即期
defineDict["QDP_FTDC_PC_Spot"] = '4'
#期转现
defineDict["QDP_FTDC_PC_EFP"] = '5'
#未知类型
defineDict["QDP_FTDC_PC_Unknown"] = '6'
#证券
defineDict["QDP_FTDC_PC_Stocks"] = '7'
#股票期权
defineDict["QDP_FTDC_PC_StockOptions"] = '8'
#金交所现货
defineDict["QDP_FTDC_PC_SGE_SPOT"] = '9'
#金交所递延
defineDict["QDP_FTDC_PC_SGE_DEFER"] = 'a'
#金交所远期
defineDict["QDP_FTDC_PC_SGE_FOWARD"] = 'b'

typedefDict["TQdpFtdcProductClassType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcCurrencyIDType是一个币种代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["TQdpFtdcCurrencyIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#TFtdcBusinessTypeType是一个业务类别类型
#//////////////////////////////////////////////////////////////////////
#普通
defineDict["QDP_FTDC_BT_Normal"] = '1'
#撤单
defineDict["QDP_FTDC_BT_Cancel"] = '2'
#ETF申赎
defineDict["QDP_FTDC_BT_AppliedForRedeemed"] = '3'
#最优五档即时成交剩余撤销
defineDict["QDP_FTDC_BT_FiveLevelIOC"] = '4'
#最优五档即时成交剩余转限价
defineDict["QDP_FTDC_BT_FiveLevelGFD"] = '5'
#即时成交剩余撤销
defineDict["QDP_FTDC_BT_BestPriceIOC"] = '6'
#全额成交或撤销
defineDict["QDP_FTDC_BT_FOK"] = '7'
#本方最优价格
defineDict["QDP_FTDC_BT_SelfGFD"] = '8'
#对方最优价格
defineDict["QDP_FTDC_BT_CpGFD"] = '9'
#金交所中立仓申报
defineDict["QDP_FTDC_BT_SGEMidApp"] = 'a'
#套利组合单
defineDict["QDP_FTDC_BT_Combination"] = 'b'
#套利非组合单
defineDict["QDP_FTDC_BT_Grab"] = 'c'
#金交所递延交割申报
defineDict["QDP_FTDC_BT_SGEDeferDeliApp"] = 'd'

typedefDict["TQdpFtdcBusinessTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcTransferStatusType是一个转账交易状态类型
#//////////////////////////////////////////////////////////////////////
#正常
defineDict["QDP_FTDC_TS_TRFS_Normal"] = '0'
#被冲正
defineDict["QDP_FTDC_TS_TRFS_Repealed"] = '1'

typedefDict["TQdpFtdcTransferStatusType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcFeePayFlagType是一个费用支付标志类型
#//////////////////////////////////////////////////////////////////////
#由受益方支付费用
defineDict["QDP_FTDC_FPF_FPF_BEN"] = '0'
#由发送方支付费用
defineDict["QDP_FTDC_FPF_FPF_OUR"] = '1'
#由发送方支付发起的费用，受益方支付接受的费用
defineDict["QDP_FTDC_FPF_FPF_SHA"] = '2'

typedefDict["TQdpFtdcFeePayFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcPwdFlagType是一个密码标志类型
#//////////////////////////////////////////////////////////////////////
#不核对
defineDict["QDP_FTDC_PF_BPWDF_NoCheck"] = '0'
#明文核对
defineDict["QDP_FTDC_PF_BPWDF_BlankCheck"] = '1'
#密文核对
defineDict["QDP_FTDC_PF_BPWDF_EncryptCheck"] = '2'

typedefDict["TQdpFtdcPwdFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcBankAccTypeType是一个银行账号类型类型
#//////////////////////////////////////////////////////////////////////
#存折
defineDict["QDP_FTDC_BAT_VBAT_BankBook"] = '1'
#储蓄卡
defineDict["QDP_FTDC_BAT_VBAT_BankCard"] = '2'
#信用卡
defineDict["QDP_FTDC_BAT_VBAT_CreditCard"] = '3'

typedefDict["TQdpFtdcBankAccTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcYesNoIndicatorType是一个是否标志类型
#//////////////////////////////////////////////////////////////////////
#是
defineDict["QDP_FTDC_YNI_YNI_Yes"] = '0'
#否
defineDict["QDP_FTDC_YNI_YNI_No"] = '1'

typedefDict["TQdpFtdcYesNoIndicatorType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcAvailabilityFlagType是一个有效标志类型
#//////////////////////////////////////////////////////////////////////
#未确认
defineDict["QDP_FTDC_ALF_AVAF_Invalid"] = '0'
#有效
defineDict["QDP_FTDC_ALF_AVAF_Valid"] = '1'
#冲正
defineDict["QDP_FTDC_ALF_AVAF_Repeal"] = '2'
#失败
defineDict["QDP_FTDC_ALF_AVAF_FAIL"] = '3'

typedefDict["TQdpFtdcAvailabilityFlagType"] = "char"

#//////////////////////////////////////////////////////////////////////
#TFtdcPayDirectionType是一个金交所递延支付方向类型
#//////////////////////////////////////////////////////////////////////
#多付空
defineDict["QDP_FTDC_PD_Buy"] = '0'
#空付多
defineDict["QDP_FTDC_PD_Sell"] = '1'
#支付方向未定
defineDict["QDP_FTDC_PD_Unknown"] = '2'

typedefDict["TQdpFtdcPayDirectionType"] = "char"
