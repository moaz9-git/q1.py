import statistics
f = open("Downloads/sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices=listItems
for i in range(0, len(listItems)): 
 appleprices[i] = float(listItems[i])
mean_val= (statistics.mean(appleprices))
stdev = statistics.stdev(appleprices)
print (mean_val)
print (stdev)
