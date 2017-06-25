#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


histdir_cyb='./chuangyeban_20160608/'
histdir_sha='./shanghaiAgu_20160608/'
histdir_sza='./shenzhenAgu_20160608/'


histcol_set= ['代码', '简称', '日期',
 '前收盘价(元)', '开盘价(元)', '最高价(元)', '最低价(元)', '收盘价(元)',
 '成交量(股)', '成交金额(元)', '涨跌(元)', '涨跌幅(%)', '均价(元)', '换手率(%)',
 'A股流通市值(元)', 'B股流通市值(元)', '总市值(元)',
 'A股流通股本(股)', 'B股流通股本(股)', '总股本(股)',
 '市盈率', '市净率', '市销率', '市现率', 'Unnamed: 24']  #df.columns
'NOTE: 注意，上面的均价是多日的日间均价，不是一日的日内均价!'


def get_stock_path(scode):
    if type(scode) == int:
        scode = str(scode).zfill(6)
    if scode[0] == '0':
        return histdir_sza+scode+'.SZ.CSV'
    elif scode[0] == '3':
        return histdir_sza+scode+'.SZ.CSV'
    elif scode[0] == '6':
        return histdir_sza+scode+'.SH.CSV'
    return ''


def read_stock_hist(scode, columns, fromdate='2005-01-01', todate='2015-12-31'):
    df = pd.read_csv(get_stock_path(scode), encoding='GB18030')
    df.index=df['日期']  # 使用日期作为行index，便于按日期检索
    return df.loc[fromdate:todate, columns]


def read_stock_hist_arrays(scode, columns, fromdate='2005-01-01', todate='2015-12-31'):
    df = read_stock_hist(scode, columns, fromdate, todate)
    return [array(df.loc[:,c]) for c in columns]


# example of using read_stock_hist()
df=read_stock_hist('300005',['开盘价(元)', '收盘价(元)', '成交量(股)', 'A股流通股本(股)', '市盈率', '市净率', '市销率', '市现率'])
#df.plot(x=df.index, y=['开盘价(元)', '最高价(元)', '最低价(元)', '收盘价(元)'], legend=False, logy=True, fontsize=5)
df.plot(x=df.index, y=['开盘价(元)'], legend=False, fontsize=5)

x=read_stock_hist_arrays('300005',['收盘价(元)'])
plot(x[0], '.');  # plot on the previous frame, so that we have  x=date
show()
