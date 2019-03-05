## Descriptive statitics
Descriptive statistics are done based on the dataframe axis
- sum :

      pd.sum(axis=0|1)
   sum across rows | Columns
- mean, mode, median, mode, std, min, max, abs, prod

### Cumulative sum

    df = pd.DataFrame({"A":[5, 3, 6, 4],
                   "B":[11, 2, 4, 3],
                   "C":[4, 3, 8, 5],
                   "D":[5, 4, 2, 8]})
    df
  - Cumulative sum across rows
        df.cumsum(axis = 0)
  - Cumulative sum across column
        df.cumsum(axis = 0)

### Cumulative product

    df.cumprod(axis=0)
    df.cumprod(axis=1)
