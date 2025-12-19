from src import calculate_price

def test_calculate_price_with_one_item():
    expected = 5.0
    items: dict[str, float] = [
        {
        "price": 5,
        "name": "product"
        }
    ]
    result = calculate_price(items)
    print(f"Result 'calculate_price' function: {result}\nExpected: {result}")
    assert  result == expected

def test_calculate_price_with_one_item_and_discount():
    expected = 4.5
    items: dict[str, float] = [
        {
        "price": 5,
        "name": "product",
        "discount": 0.10
        }
    ]
    result = calculate_price(items)
    print(f"Result 'test_calculate_price_with_one_item_and_discount' function: {result}\nExpected: {result}")
    assert  result == expected

def test_calculate_price_with_multiples_item():
    expected = 24.5
    items: dict[str, float] = [
        {
        "price": 5,
        "name": "product1"
        },
        {
        "price": 7.5,
        "name": "product2"
        },
        {
        "price": 12,
        "name": "product2"
        }
    ]
    result = calculate_price(items)
    print(f"Result 'calculate_price' function: {result}\nExpected: {result}")
    assert  result == expected

def test_calculate_price_with_multiples_item_and_discount():
    expected = 18.0
    items: dict[str, float] = [
        {
        "price": 5,
        "name": "product1",
        "discount": 0.10
        },
        {
        "price": 7.5,
        "name": "product2"
        },
        {
        "price": 12,
        "name": "product2",
        "discount": 0.50
        }
    ]
    result = calculate_price(items)
    print(f"Result 'test_calculate_price_with_multiples_item_and_discount' function: {result}\nExpected: {result}")
    assert  result == expected

def test_calculate_invalid_properties_in_item():
    items: dict[str, float] = [
        {
        "price": 5,
        }

    ]
    result = calculate_price(items)
    assert  type(result) ==  ValueError
    print("Result: 'test_calculate_invalid_properties_in_item' return a 'ValueError' has expected when object does not have the 'price' or 'name' properties")

def test_calculate_invalid_price():
    items: dict[str, float] = [
        {
        "price": -5,
        "name": "product"
        }
    ]

    result = calculate_price(items)
    assert  type(result) ==  ValueError
    print("Result: 'test_calculate_invalid_properties_in_item' return a 'ValueError' has expected when value 'price' is less than zero(0).")

if __name__ == "__main__":
    print("Init tests: ")
    test_calculate_price_with_one_item()
    test_calculate_price_with_multiples_item()
    test_calculate_invalid_properties_in_item()
    test_calculate_invalid_price()
    test_calculate_price_with_one_item_and_discount()
    test_calculate_price_with_multiples_item_and_discount()