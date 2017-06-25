import tushare as ts


# load stock codes:
tt = loadtxt('stock_codes_2017-06-04.txt', dtype=np.int)
codes = array([str(x).zfill(6) for x in tt])


# get and save qian-fu-quan
for i,c in enum(codes):
    print('\n\n',i,':',c)
    '''
    # tons of data (till 2016-06-08) have been downloaded::
    df = ts.get_h_data(c,start='2010-01-01',end='2010-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2010.csv')
    df = ts.get_h_data(c,start='2011-01-01',end='2011-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2011.csv')
    df = ts.get_h_data(c,start='2012-01-01',end='2012-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2012.csv')
    df = ts.get_h_data(c,start='2013-01-01',end='2013-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2013.csv')
    df = ts.get_h_data(c,start='2014-01-01',end='2014-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2014.csv')
    df = ts.get_h_data(c,start='2015-01-01',end='2015-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2015.csv')
    df = ts.get_h_data(c,start='2016-01-01',end='2016-12-31')
    if shape(df) != (): df.to_csv('qfq_'+c+'_2016.csv')
    '''
    df = ts.get_h_data(c,start='2016-06-09',end='2016-06-08')
    if shape(df) != (): df.to_csv('qfq_'+c+'_16to17.csv')
