import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class Solution:
    def calc(self, inputList):
        return 5














if (__name__ == "__main__"):
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))


    df2 = pd.DataFrame({'A': 1.,'B': pd.Timestamp('20130102'),'C': np.array(7,dtype='float32'),'D': np.array([3] * 4, dtype='int32'),'E': pd.Categorical(["test", "train", "test", "train"]),'F': 'foo'})
    wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],major_axis = pd.date_range('1/1/2000', periods=5), minor_axis = ['A', 'B', 'C', 'D'])
    print(wp['Item1'])
    print(wp['Item2'])

    # df.add(df2, fill_value=0)

    