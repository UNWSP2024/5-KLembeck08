def km_to_miles(km):
    return km * 0.6214

def main():
    km = float(input("Enter distance in kilometers: "))
    miles = km_to_miles(km)
    print(f"{km} kilometers is {miles:.2f} miles.")

main()
