import statistics
import matplotlib.pyplot as plt
f = open("Downloads/sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices=listItems
for i in range(0, len(listItems)): 
 appleprices[i] = float(listItems[i])
# Create the line plot
plt.plot(appleprices)

# Add labels and title
plt.xlabel("Day")
plt.ylabel("Trading price")
plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
plt.xlim(1, 252)
# Display the plot
plt.show()
current_max_val=0
max_profit_val=0
min_value = min(appleprices)
max_value = max(appleprices)
min_index = appleprices.index(min_value)
max_index = appleprices.index(max_value)
print ('min_value=',min_value)
print ('max_value=',max_value)
print ('min_index=',min_index)
print ('max_index=',max_index)
for price in reversed(appleprices): 
 current_max_val = max(current_max_val, price) 
 potential_profit = current_max_val - price 
 max_profit_val = max(potential_profit, max_profit_val)

print ('current_max_val=',current_max_val)
print ('max_profit_val=',max_profit_val)
