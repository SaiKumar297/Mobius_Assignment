from datetime import datetime

total = 0.00
sales_month = {} 
pop_items_monthly = {}  
revenue_monthly = {}  
stats_monthly = {} 

def get_month(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m")


with open('ice_cream_sales.csv', 'r') as file:
    next(file)
    for i in file:
        date, item,uprice, quantity, price = i.strip().split(',')
        quantity = int(quantity)
        price = float(price)
        amount = quantity * price

        total += amount

        month = get_month(date)
        if month not in sales_month:
            sales_month[month] = 0.0
        sales_month[month] += amount


        if month not in pop_items_monthly:
            pop_items_monthly[month] = {}
        if item not in pop_items_monthly[month]:
            pop_items_monthly[month][item] = 0
        pop_items_monthly[month][item] += quantity

        if month not in revenue_monthly:
            revenue_monthly[month] = {}
        if item not in revenue_monthly[month]:
            revenue_monthly[month][item] = 0.0
        revenue_monthly[month][item] += amount

        if month not in stats_monthly:
            stats_monthly[month] = {'min': float('inf'), 'max': float('-inf'), 'total_orders': 0, 'order_count': 0}

        stats_monthly[month]['total_orders'] += quantity
        stats_monthly[month]['order_count'] += 1
        if quantity < stats_monthly[month]['min']:
            stats_monthly[month]['min'] = quantity
        if quantity > stats_monthly[month]['max']:
            stats_monthly[month]['max'] = quantity

print("Total Sales of the Store:", total)

print("\nMonth-wise Sales Totals:")
for month, sales in sales_month.items():
    print(f"{month}: {sales}")

print("\nMost Popular Item (most quantity sold) in each Month:")
for month, items in pop_items_monthly.items():
    popular_item = max(items, key=items.get)
    print(f"{month}: {popular_item} ({items[popular_item]} units)")

print("\nItems Generating Most Revenue in each Month:")
for month, items in revenue_monthly.items():
    top_revenue_item = max(items, key=items.get)
    print(f"{month}: {top_revenue_item} (${items[top_revenue_item]})")

print("\nStatistics for Most Popular Item Each Month (Min, Max, Average Orders):")
for month, stats in stats_monthly.items():
    avg_orders = stats['total_orders'] / stats['order_count'] 
    if stats['order_count'] > 0:
        avg_orders = stats['total_orders'] / stats['order_count'] 
    else:
        avg_orders = 0
    print(f"{month}: Min = {stats['min']}, Max = {stats['max']}, Average = {avg_orders:.2f}")
