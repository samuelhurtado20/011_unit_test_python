from typing import List, Dict, Any, Set

def calculate_price(items: list[dict[str, float, float]]):
    required_keys: Set[str] = {"name", "price"}
    total_price = 0.0

    for item in items:
        if not required_keys.issubset(item.keys()):
            return ValueError(f"The items must have 'price' and 'name' properties, 'discount' is optional. Fault item: {item}.")
        price = item.get("price")
        if price < 0:
            return ValueError(f"'price' value cannot be less than zero (0).")
        total_price += price - (price * item.get("discount", 0))
    return total_price