## Pandas function application

We can apply library or user defined functions to Pandas.
The function can be applied on an entiredataframe, column-wise or row-wise.

pipe() - Table wise function application.
apply() - Row or Column wise funcation appliction.
applymap - Element-wise function application.

### Table-wise function application:

    def addition(e1, e2):
      return e1+e2

    df = pd.DataFrame(np.random.randn(5,3), columns([Col1, Col2, Col3]))
    df.pipe(addition, 2)

### Column-Wise or Row-Wise function application:

Any function can be applied along the axis of Dataframe or Panel

- Column Wise

      >>> df.apply(np.mean)
      Col1   -0.457612
      Col2    0.443900
      Col3   -0.289733
      dtype: float64

- Row Wise

      >>> df.apply(np.mean, axis=1)
      0   -1.037471
      1    0.666415
      2    0.349844
      3    0.102358
      4   -0.586889
      dtype: float64

### Element-wise function application


    >>> df.applymap(lambda x:x+12)
        Col1       Col2       Col3
        0  10.555316  10.573832  11.758440
        1  11.544891  13.371140  13.083213
        2  12.949671  13.556540  10.543320
        3  11.439487  12.524023  12.343565
        4  11.222573  12.193966  10.822795
