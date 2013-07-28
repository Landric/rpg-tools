from random import randint

def roll(dice_string):
    dice_string = dice_string.replace(" ", "")
    
    try:
        dice, sides = dice_string.split("d")
        if not dice:
            dice = 1
        else:
            dice = int(dice)
    except:
        print "Dice must be in the form XdY+Z"
        return 0
    
    try:
        sides, modifier = sides.split("+")
        modifier = int(modifier)
    except ValueError:
        try:
            sides, modifier = sides.split("-")
            modifier = int(modifier) * -1
        except ValueError:
            modifier = 0
            
    sides = int(sides)
    
    if dice == 1:
        result = randint(1, sides) + modifier
        print, "Rolled: "
        return result
    else:
        results = []
        for die in range(dice):
            results.append(randint(1, sides))
        
        total = sum(results)+modifier
        
        print "Rolled {0})".format(', '.join(map(str, results)))
        print, "Total: "
        return total
