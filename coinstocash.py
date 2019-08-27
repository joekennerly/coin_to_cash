def calc_dollars():
    dollar_amount = 0

    piggybank = {
        "quarters": 360,
        "nickles": 43,
        "dimes": 10,
        "pennies": 0,
    }

    for key, value in piggybank.items():
        if key == "quarters":
            dollar_amount += (value * .25)
        if key == "nickles":
            dollar_amount += (value * .05)
        if key == "dimes":
            dollar_amount += (value * .1)
        if key == "pennies":
            dollar_amount += (value * .01)

    print("dollar amt: ",dollar_amount)

calc_dollars()