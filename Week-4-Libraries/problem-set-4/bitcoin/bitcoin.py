import sys
import requests
import json

def main():

    # Api key from coincap
    my_api_key = "d5fbc346207609105a884f65bb4d6771c78b229d3bf6d68cd1250ece830701fd"

    # Get number of bitcoins user wants
    number = get_number()

    # Get bitcoin price
    bitcoin_price = get_bitcoin(my_api_key)

    # print(type(number))
    # print(type(bitcoin_price))

    # Get value of n bitcoins
    value = number * bitcoin_price

    # Format number in four decimal places usin , as a thousands seperator
    formatted_number = format(value, ",.4f")

    # Print formatted number
    print(f"${formatted_number}")




# Function to check second argument get return it
def get_number():

    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command line argument!")
    except ValueError:
        sys.exit("Command line argument is not a number!")

    return n


def get_bitcoin(my_api_key):

    try:
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={my_api_key}")
    except requests.RequestException:
        sys.exit("Error getting request response: Provide correct API KEY!")

    # Get content in json format
    content = response.json()

    # Get dictionary of data
    data = content["data"]

    # Return value of priceUsd key
    return float(data["priceUsd"])


if __name__ == "__main__":
    main()
