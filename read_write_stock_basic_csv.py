import tushare as ts

# get all living stock information
df = ts.get_stock_basics('2017-06-02')
df.to_csv('stock_basics_2017-06-04.csv') # today

# read csv
de = pd.read_csv('stock_basics_2017-06-04.csv')

# now, save the data
savetxt('stock_codes_2017-06-04.txt', array(de['code'], dtype=np.int), fmt='%06d')

# how to load
tt = loadtxt('stock_codes_2017-06-04.txt', dtype=np.int)
codes = array([str(x).zfill(6) for x in tt])
