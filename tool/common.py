#!/usr/bin/python
#########################################################################################
# Copyright 2020 by Heqing Huang (heqinghuangusc@gmail.com)
#
# Project: Simple CSR Generator
# Author: Heqing Huang
# Date: 10/22/2020
#
# Description:
#   Common file
#
#########################################################################################

############################
# Date
############################
from datetime import datetime
YEAR = datetime.now().year
MONTH = datetime.now().month
DAY = datetime.now().day
HOUR = datetime.now().hour
MINUTE = datetime.now().minute

############################
# Global Define
############################

# Define the field for fieldInfo Array
# [field1, MSb, LSb, SW_TYPE, HW_TYPE, Reset_value, Description(note)]
REGNAME = 0
ADDR    = 1
FNAME   = 0
MSB     = 1
LSB     = 2
SWTYPE  = 3
HWTYPE  = 4
RESET   = 5
NOTE    = 6

# Other global define
RSVR        = 'RSVR'
RSVR_NOTE   = 'Reserved Field'
REG_WIDTH   = 32

############################
# Global Function
############################
INDENT = lambda x: '  ' * x



