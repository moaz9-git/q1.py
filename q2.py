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
