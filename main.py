import load_data
import analyze_data 

def main():
    product_data = None

    while True:
        print("CSV Product Analyzer")
        print("1. Load Product Data from a CSV File")
        print("2. Analyze Product Data")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            filename = input("Enter the CSV filename: ")
            loaded_data = load_data.load_product_data(filename)
            if isinstance(loaded_data, str):
                print(f'Error Message: {loaded_data}')
            else:
                product_data = loaded_data
                print("Product data loaded.")
        elif choice == "2":
            analyzed_data = analyze_data.analyze_product_data(product_data)
            if analyzed_data is None:
                print(f'Error Message: Analyzed Data is None. Load data first by selecting option 1.')
            else:
                print(f'Analyzed Data:\n{analyzed_data}')
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()
