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


if __name__ == "__main__":
    main()
