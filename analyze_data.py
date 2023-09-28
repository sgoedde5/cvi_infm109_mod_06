def analyze_product_data(product_data):
    if product_data is not None:
        total_products = len(product_data)
        
        # Calculate average price
        total_price = sum(float(product['Price']) for product in product_data)
        average_price = total_price / total_products

        # Find the most expensive and least expensive products
        sorted_products = sorted(product_data, key=sort_by_price)
        most_expensive_product = sorted_products[-1]
        least_expensive_product = sorted_products[0]

        result = (
                  f"Total products: {total_products}\n"
                  f"Average price: ${average_price:.2f}\n"
                  f"Most expensive product: {most_expensive_product['Name']} (Price: ${most_expensive_product['Price']})\n"
                  f"Least expensive product: {least_expensive_product['Name']} (Price: ${least_expensive_product['Price']})\n"
                 ) 

        return result
    else:
        print("Product data is empty. Please load data first.")
        return None

def sort_by_price(product):
    return float(product['Price'])

