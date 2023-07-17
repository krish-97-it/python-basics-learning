def createSeries(a,b):
    distance_between = b-a/2
    series  = a
    term = a
    for i in range (1,4):
        term = term + distance_between
        series = str(series)+", "+str(term)

    return series

n1 =  int(input("Enter First number of the series: "))
n4 =  int(input("Enter Last number of the series: "))
res_series = createSeries(n1,n4)
print(res_series)
