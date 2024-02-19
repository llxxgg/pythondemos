def make_pizza(*toppings):
    """*标识创建一个空元组"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
