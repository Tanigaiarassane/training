#Pandas - series

pandas.Series( data, index, dtype, copy)

Data can ebe Array, dictionary , scalar or constant

Empty Series:

>> Series([], dtype: float64)


## From Dictonary:

import pandas as pd
data = {'India' : 130, 'China' : 134, 'US' : 32}
s = pd.Series(data)
print s

==> dictionary keys are used as index.

import pandas as pd
data = {'India' : 130, 'China' : 134, 'US' : 32}
s = pd.Series(data,index=['India','China','US','Russia'])
print s

==> Index order is persisted and the missing element is filled with NaN (Not a Number).


##From scalar
import pandas as pd
s = pd.Series(130, index=[0, 1, 2, 3])
print s


Retrieval by location:
print s[1]
print s[:3]
print s[:-3]
print s[14]

Retrieval by label:
print s['India']
print s['UK']
