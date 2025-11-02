
car = {
    "brand": "Tesla",
    "model": "Cyber Truck",
    "year": 2023,
    "color": "Silver"
}
print(f"Original car info: {car}")

# Print the keys, values, and items of the dictionary
print(f"Key: {car.keys()}")
print(f"Values: {car.values()}")
print(f"Items: {car.items()}")

# Get the value for "model" using using get()
print(f"Model (get): {car.get("model")}")

# Try to get "engine" key with the get(). If it doesn't exist, show "Not available"
print(f"Engine (get): {car.get("engine", "Not available")}")