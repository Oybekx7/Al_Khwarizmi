def calculate_average_sales(sales_list):
    if not sales_list:
        return 0.0
    return sum(sales_list) / len(sales_list)

def find_top_salesperson(sales_data):
    max_avg_sales = 0
    top_salesperson_id = ""

    for employee_id, _, quarterly_sales_list in sales_data:
        current_avg = calculate_average_sales(quarterly_sales_list)

        if current_avg > max_avg_sales:
            max_avg_sales = current_avg
            top_salesperson_id = employee_id

        elif current_avg == max_avg_sales:
            if employee_id < top_salesperson_id:
                top_salesperson_id = employee_id
                
    return top_salesperson_id

def get_employees_in_region(sales_data, region_name):
    region_employees = []

    for employee_id, region, _ in sales_data:

        if region == region_name:
            region_employees.append(employee_id)

    region_employees.sort()
    return region_employees

def get_regional_sales_total(sales_data):
    # Lug'at o'rniga, natijani tuple'lar ro'yxatida saqlaymiz: 
    # [('Region', Total), ...]
    regional_summary = []
    
    for _, region, quarterly_sales_list in sales_data:
        employee_total_sales = sum(quarterly_sales_list)
        found = False
        for i in range(len(regional_summary)):
            current_region, current_total = regional_summary[i]
            
            if current_region == region:
                new_total = current_total + employee_total_sales
                regional_summary[i] = (region, new_total)
                found = True
                break
        if not found:
            regional_summary.append((region, employee_total_sales))
    regional_summary.sort()
    return regional_summary

def analyze_sales_data(sales_data):

    top_salesperson_id = find_top_salesperson(sales_data)
    north_region_employees = get_employees_in_region(sales_data, 'North')
    regional_summary = get_regional_sales_total(sales_data)
    return (top_salesperson_id, north_region_employees, regional_summary)

sales_data = [
    ('E101', 'North', [50000, 60000, 55000]),
    ('E201', 'South', [70000, 75000, 80000]),
    ('E102', 'North', [85000, 90000, 95000]),
    ('E301', 'West', [65000, 60000, 58000])  
]

summary = analyze_sales_data(sales_data)
print(summary)
