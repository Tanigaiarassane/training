# Pandas - series

pandas.Series( data, index, dtype, copy)

Data can ebe Array, dictionary , scalar or constant

Empty Series:

    pd.Series([], dtype: float64)


## From Dictionary:

    import pandas as pd
    data = {'India' : 130, 'China' : 134, 'US' : 32}
    s = pd.Series(data)
    print s

- Dictionary keys are used as index.

      import pandas as pd
      data = {'India' : 130, 'China' : 134, 'US' : 32}
      s = pd.Series(data,index=['India','China','US','Russia'])
      print s

- Index order is persisted and the missing element is filled with NaN (Not a Number).


## From scalar

    import pandas as pd
    s = pd.Series(130, index=[0, 1, 2, 3])
    print s


## Retrieval by location:
    print s[1]
    print s[:3]
    print s[:-3]
    print s[14]

## Retrieval by label:

    print s['India']
    print s['UK']


## Basic functionalities - Series
import pandas as pd
import numpy as np

#Create a series with 100 random numbers

    s = pd.Series(np.random.randn(4))
    print s

    - Axes - returns the list of labels of the Series

    >>> s.axes
    >>> [RangeIndex(start=0, stop=4, step=1)]

  - is empty?


    >>> s.empty
    False

  - dimension


    >>>print s.ndim
  1

  - Size


    >>> s.size
    4

  - Values
    >>> s.values

  - Head  & tail


      print s.head(2)
      print s.tail(2)
