## Data frame basics
Dataframe is a two dimensional structure with rows and columns

- columns can be of different type
- size is mutables
- Labeled axes for both rows and columns
- Can perform arithmetic operations on rows and columns

      pandas.DataFrame( data, index, columns, dtype, copy)


- Data : can be ndarray, series,map, dict, constants and also can be another data frame.

## Creating data frame:

### Empty data frameimport
      import pandas as pd
      df = pd.DataFrame()
      print df

### From lists

Single Columns

    import pandas as pd
    data = [1,2,3,4,5]
    df = pd.DataFrame(data)
    print df

Multiple Columns

    import pandas as pd
    data = [['Alex',10],['Bob',12],['Clarke',13]]
    df = pd.DataFrame(data,columns=['Name','Age'])
    print df

With datatype

    import pandas as pd
    data = [['Alex',10],['Bob',12],['Clarke',13]]
    df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
    print df


### From Dictionary

    import pandas as pd
    data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
    df = pd.DataFrame(data)
    print df

Indexed data frame:

    import pandas as pd
    data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
    df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
    print df

### From list of dict:

    import pandas as pd
    data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
    df = pd.DataFrame(data)
    print df

With index:

    import pandas as pd
    data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
    df = pd.DataFrame(data, index=['first', 'second'])
    print df

With row index and column indexing

    import pandas as pd
    data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
    df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

    df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
    print df1
    print df2

From dict of Series

    import pandas as pd
    d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
   df = pd.DataFrame(d)
   print df

### Working with columns

#### Column selection

    import pandas as pd
    d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

        df = pd.DataFrame(d)
        print df ['one']

#### Column addition

    import pandas as pd
    d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)

    print ("Adding a new column by passing as Series:")
    df['three']=pd.Series([10,20,30],index=['a','b','c'])
    print df
    print ("Adding a new column using the existing columns in DataFrame:")
    df['four']=df['one']+df['three']
    print df


#### Columns deletion

    import pandas as pd

    d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'three' : pd.Series([10,20,30], index=['a','b','c'])}
    df = pd.DataFrame(d)
    print ("Our dataframe is:")
    print df

    print ("Deleting the first column using DEL function:")
    del df['one']
    print df

    print ("Deleting another column using POP function:")
    df.pop('two')
    print df

### Row selection, Additon and deletion

Selection by label

    import pandas as pd
    d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a','b', 'c', 'd'])}

    df = pd.DataFrame(d)
    print df.loc['b']

Selection by location

    print df.loc[2]

Slice rows

      print df[2:4]
Addition of rows

    import pandas as pd
    df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
    df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
    df = df.append(df2)
    print df

Deletion of rows

    import pandas as pd
    df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
    df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

    df = df.append(df2)
    df = df.drop(0)

    print df
