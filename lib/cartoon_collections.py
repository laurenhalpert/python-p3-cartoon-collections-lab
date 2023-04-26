def roll_call_dwarves(names):
    for i in range(1,len(names)+1):
        print(f"{i}. {names[i-1]}")
    pass

def summon_captain_planet(calls):
    return [call.title() + "!" for call in calls]
    pass

def long_planeteer_calls(calls):
    number_long_calls = 0
    for call in calls:
        if len(call) >4:
            number_long_calls += 1
    return number_long_calls != 0
    pass

def find_the_cheese(snacks):
    for snack in snacks:
        if snack in ["cheddar", "gouda", "camembert"]:
            return snack
    return None
