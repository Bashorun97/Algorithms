from __future__ import print_function

def pythagoras(hyp, opp, adj):
    try:
        if hyp == str('?'):
            return ("Hypotenuse = " + int(((opp**2) + (adj**2))**0.5))
        elif opp == str('?'):
            return ("Opposite = " + int(((hyp**2) - (adj**2))**0.5))
        elif adj == str('?'):
            return ("Adjacent = " + int(((hyp**2) - (opp**2))**0.5))
        else:
            return "You already know the answer!"
    except:
        print ("Error, check your input. You must know 2 of the 3 variables.")

print(pythagoras(4, 3, '?'))