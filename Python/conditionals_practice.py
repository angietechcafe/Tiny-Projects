

def first_example(temp, neutrons_sent):
    
    NEW_PRODUCT = temp * neutrons_sent
    
    return temp < 900 and neutrons_sent > 400 and NEW_PRODUCT < 600000

def second_example(volt, curr, max_power):
    
    power = (volt * curr / max_power) * 200
    
    if power >= 90:
        return "purple"
    elif power >= 70:
        return "yellow"
    elif power >= 20:
        return "grey"
    return "silver"
    

def last_example(temp, neutrons_made_per_sec, container):
    
    value = temp * neutrons_made_per_sec * 100 / container
    
    ninety = 90
    
    return "LOW" if value < ninety  else "NORMAL" if ninety <= value <= 110 else "DANGER"
