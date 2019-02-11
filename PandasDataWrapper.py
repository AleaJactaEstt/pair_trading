import backtrader as bt
import pandas as pd 

'''
TODO: Оформить в пакет
'''

class btPandasStrategy(bt.Strategy):
    '''
    class wrapper that help to process with pandas DataFrames
    '''
    
    def get_df_slice(self, data, ago=0, size=0, datasname='close'):
        
        assert (len(self) >= size), "There are no data at that moment, try to get less size."

        data = data or self.datas[0]

        time_index = self.convert_btdate_to_dateIndex(ago=ago, lookback_window=size)

        return pd.DataFrame(list(data.get(ago = ago, size = size)), index=time_index)
    
    def convert_btdate_to_dateIndex(self, ago = 0, lookback_window=0):
        '''
        As bt doesn't support datetime slicing(it's support Line slicing, but datetime in bt is special type 
        that should be converted from numerical representation to date representation(see docs "datetime" method
        and "tz" - parameter)).
        This method return pandas DateIndex from lookback_window to current time. 
        Special is that in bt another indexation 0 - is current time, -n - is n-th past time bar.
        '''
		
        assert (len(self) >= lookback_window), "There are no data at that moment, try to get less size."
		
        bt_date = [self.datetime.datetime(ago = i) for i in range(-lookback_window+1, ago+1, 1)]

        str_date = [str(date) for date in bt_date]
 
        pd_dateIndex = pd.to_datetime(str_date, format="%Y-%m-%d %H:%M:%S")
 
        return pd_dateIndex
	
	#def get_all(self, data, ago=0, datasname='close')