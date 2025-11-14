def calculate_average_sales(sales_list):
    if not sales_list:
        return 0
    return sum(sales_list) / len(sales_list)

def get_employees_in_region(sales_data, region_name):
    lst = []
    for emp_id, region, sales in sales_data:
        if region == region_name:
            lst.append(emp_id)
    lst.sort()
    return lst

def find_top_salesperson(sales_data):
    best_id = None
    best_avg = -1
    for emp_id, region, sales in sales_data:
        avg = calculate_average_sales(sales)
        if best_id is None or avg > best_avg or (avg == best_avg and emp_id < best_id):
            best_avg = avg
            best_id = emp_id
    return best_id


def get_regional_sales_total(sales_data):
    d = {}
    for emp_id, region, sales in sales_data:
        t = sum(sales)
        if region not in d:
            d[region] = t
        else:
            d[region] += t

    out = []
    for k, v in d.items():
        out.append((k, v))
    return sorted(out)

def analyze_sales_data(sales_data):
    top = find_top_salesperson(sales_data)
    north = get_employees_in_region(sales_data, "North")
    reg = get_regional_sales_total(sales_data)
    return (top, north, reg)

sales_data = [
    ('E101', 'North', [50000, 60000, 55000]),
    ('E201', 'South', [70000, 75000, 80000]),
    ('E102', 'North', [85000, 90000, 95000]),
    ('E301', 'West', [65000, 60000, 58000])
]

print(analyze_sales_data(sales_data))
