import requests

def get_exchange_rates(base_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('rates', {})
        else:
            print(f"API returned status code: {response.status_code}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: API is not reachable. Details: {str(e)}")
        return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    if rates and to_currency in rates:
        converted_amount = amount * rates[to_currency]
        return converted_amount
    else:
        print(f"Currency {to_currency} is not supported.")
        return None

def main():
    print("Real-Time Currency Converter!")
    
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    from_currency = input("Enter the currency (e.g., USD, EUR, GBP): ").strip().upper()
    to_currency = input("Currency that you are converting to (e.g., NPR, JPY, INR): ").strip().upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Sorry, there is some issue with the conversion.")

if __name__ == "__main__":
    main()
