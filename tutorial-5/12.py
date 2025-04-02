import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


months = range(1, 13)
product1_sales = [4500, 4700, 4300, 4800, 4600, 5000, 5200, 5100, 4800, 5300, 5500, 5700]
product2_sales = [3800, 3600, 3900, 4100, 4300, 4500, 4700, 4600, 4400, 4800, 5000, 5200]
product3_sales = [2800, 3100, 3300, 3200, 3500, 3800, 4100, 4300, 4500, 4700, 4600, 4800]

# Create a figure and axis
plt.figure(figsize=(12, 6))

# Plot multiple lines
plt.plot(months, product1_sales, color='blue', linestyle='-', marker='o', linewidth=2, label='Product 1')
plt.plot(months, product2_sales, color='green', linestyle='--', marker='s', linewidth=2, label='Product 2')
plt.plot(months, product3_sales, color='red', linestyle='-.', marker='^', linewidth=2, label='Product 3')

# Add labels and title
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Monthly Sales Comparison of Multiple Products', fontsize=14)
plt.legend(loc='best', fontsize=10)


plt.xticks(months)


plt.grid(True, linestyle='--', alpha=0.7)
max_product1_month = months[product1_sales.index(max(product1_sales))]
max_product1_sales = max(product1_sales)
plt.annotate(f'Peak: {max_product1_sales}', 
             xy=(max_product1_month, max_product1_sales),
             xytext=(max_product1_month-0.5, max_product1_sales+200),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
plt.ylim(min(min(product1_sales), min(product2_sales), min(product3_sales))-200, 
         max(max(product1_sales), max(product2_sales), max(product3_sales))+300)


plt.tight_layout()
plt.savefig('multi_line_plot.png')
plt.show()