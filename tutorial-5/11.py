import pandas as pd
import matplotlib.pyplot as plt

def visualize_sales_data():
    
    data = {
        'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
        'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
        'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 4580, 5200, 5300],
        'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 7580, 8200, 7300],
        'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2580, 2200, 1300],
        'moisturizer': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    }
    
    
    data['total_units'] = [sum(data[product][i] for product in 
                               ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']) 
                           for i in range(12)]

    data['total_profit'] = [data['total_units'][i] * 0.1 for i in range(12)]

    df = pd.DataFrame(data)

    df.to_csv('sales_data.csv', index=False)
    
   
    sales_df = pd.read_csv('sales_data.csv')
    

    plt.figure(figsize=(10, 6))
    plt.scatter(sales_df['month_number'], sales_df['toothpaste'], 
                color='blue', marker='o', s=100)
    

    plt.xlabel('Month Number')
    plt.ylabel('Units Sold')
    plt.title('Toothpaste Sales Data')

    plt.grid(True, linestyle='--', alpha=0.7)
    

    plt.xticks(sales_df['month_number'])
    
  
    for i, txt in enumerate(sales_df['toothpaste']):
        plt.annotate(txt, (sales_df['month_number'][i], sales_df['toothpaste'][i]), 
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('toothpaste_sales_scatter.png')
    plt.show()
    
    \
    plt.figure(figsize=(12, 6))
    bar_width = 0.4
 
    r1 = sales_df['month_number']
    r2 = [x + bar_width for x in r1]
    

    plt.bar(r1, sales_df['facecream'], width=bar_width, color='skyblue', edgecolor='grey', label='Face Cream')
    plt.bar(r2, sales_df['facewash'], width=bar_width, color='lightgreen', edgecolor='grey', label='Face Wash')
    
 
    plt.xlabel('Month Number')
    plt.ylabel('Units Sold')
    plt.title('Face Cream vs Face Wash Sales Data')
    
    plt.legend()
 
    plt.xticks([r + bar_width/2 for r in range(1, 13)], sales_df['month_number'])
    
    plt.tight_layout()
    plt.savefig('facecream_facewash_bar.png')
    plt.show()
  
    total_sales = {
        'Face Cream': sales_df['facecream'].sum(),
        'Face Wash': sales_df['facewash'].sum(),
        'Toothpaste': sales_df['toothpaste'].sum(),
        'Bathing Soap': sales_df['bathingsoap'].sum(),
        'Shampoo': sales_df['shampoo'].sum(),
        'Moisturizer': sales_df['moisturizer'].sum()
    }
  
    labels = total_sales.keys()
    values = total_sales.values()

    plt.figure(figsize=(10, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.title('Total Sales Distribution by Product')
    
    plt.tight_layout()
    plt.savefig('total_sales_pie.png')
    plt.show()
    
    print("All visualizations have been created and saved as:")
    print("1. toothpaste_sales_scatter.png")
    print("2. facecream_facewash_bar.png")
    print("3. total_sales_pie.png")


if __name__ == "__main__":
    visualize_sales_data()