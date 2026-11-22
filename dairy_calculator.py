"""
Dairy Co-op Payment Calculator - v1.0
Kiambu Dairy Co-op, 30 farmer members

Usage:
    python dairy_calculator.py

Config:
    Edit price.txt to update weekly rate. No code change needed.
    Example price.txt contains: 55.0
"""

def get_current_price():
    """Read current price from price.txt, fall back to default."""
    try:
        with open("price.txt", "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        print("⚠ price.txt not found. Using default KES 55.00")
        return 55.0
    except ValueError:
        print("⚠ price.txt is invalid. Using default KES 55.00")
        return 55.0


def calculate_payment(litres, price_per_litre):
    return litres * price_per_litre


def run():
    print("Kiambu Dairy Co-op Payment Calculator")
    print("--------------------------------------")
    price = get_current_price()
    print(f"Current buying price: KES {price:.2f} per litre")
    print()

    name = input("Farmer name: ").strip()
    if not name:
        print("❌ Name is required.")
        return

    try:
        litres_input = input("Litres supplied today: ").strip()
        litres = float(litres_input)
        if litres <= 0:
            print("❌ Litres must be greater than zero.")
            return
    except ValueError:
        print("❌ Please enter a valid number for litres. Example: 12.5")
        return

    total = calculate_payment(litres, price)

    print()
    print(f"Farmer : {name}")
    print(f"Litres : {litres}")
    print(f"Price  : KES {price:.2f}/litre")
    print(f"Total  : KES {total:,.2f}")
    print()
    print("Thank you! Please collect payment from the co-op office.")


if __name__ == "__main__":
    run()
