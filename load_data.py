import csv

def load_product_data(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            product_data = list(reader)
            
            # Validate data
            for product in product_data:
                product_name = product.get('Name')
                price = float(product.get('Price'))
                
                if not product_name or price < 0:
                    return "Invalid data found in the CSV file."
            
            return product_data
    except FileNotFoundError:
        return "File not found"

