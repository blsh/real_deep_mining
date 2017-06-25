#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

import tushare as ts

# 沪深300指数
df=ts.get_h_data('000300', index=True, start='2005-01-01', end='2016-06-08')
df.to_csv('hushen300zhishu.csv')

# 上海股票综合指数
df=ts.get_h_data('000001', index=True, start='2005-01-01', end='2016-06-08')
df.to_csv('shanghaizongzhi.csv')

# 深圳综合股票指数
df=ts.get_h_data('399001', index=True, start='2005-01-01', end='2016-06-08')
df.to_csv('shenzhenzongzhi.csv')
