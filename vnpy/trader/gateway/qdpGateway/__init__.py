# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .qdpGateway import QdpGateway

gatewayClass = QdpGateway
gatewayName = "QDP"
gatewayDisplayName = gatewayName
gatewayType = vtConstant.GATEWAYTYPE_FUTURES
gatewayQryEnabled = True
