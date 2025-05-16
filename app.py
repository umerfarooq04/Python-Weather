import argparse
from weather import get_weather
from utils import format_weather, save_to_history
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="Weather CLI App 🌤")
    parser.add_argument("--city", help="City name", required=False)
    parser.add_argument("--unit", help="Unit: C or F", default="C")
    args = parser.parse_args()

    unit = args.unit.upper()
    use_metric = unit == "C"

    if args.city:
        city = args.city
    else:
        city = input("Enter city name: ")

    while True:
        data = get_weather(city, use_metric)
        if data:
            result = format_weather(data, use_metric)
            print(Fore.CYAN + result)
            save_to_history(city, result)
            break
        else:
            print(Fore.RED + "City not found. Try again.")
            city = input("Enter city name: ")


if __name__ == "__main__":
    main()
