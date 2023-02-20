# START
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# PRICES
spc = 18
mpc = 24
lpc = 29
sp = 17
mp = 23
lp = 28
sc = 16
mc = 21
lc = 26
s = 15
m = 20
l = 25
if (size == "S") and (add_pepperoni == "Y") and (extra_cheese == "Y"):
    print(f"Your final bill is: ${spc}.")
elif (size == "S") and (add_pepperoni == "Y") and (extra_cheese == "N"):
    print(f"Your final bill is: ${sp}.")
elif (size == "S") and (add_pepperoni == "N") and (extra_cheese == "Y"):
    print(f"Your final bill is: ${sc}.")
elif (size == "S") and (add_pepperoni == "N") and (extra_cheese == "N"):
    print(f"Your final bill is: ${s}.")
elif (size == "M") and (add_pepperoni == "Y") and (extra_cheese == "Y"):
    print(f"Your final bill is: ${mpc}.")
elif (size == "M") and (add_pepperoni == "Y") and (extra_cheese == "N"):
    print(f"Your final bill is: ${mp}.")
elif (size == "M") and (add_pepperoni == "N") and (extra_cheese == "Y"):
    print(f"Your final bill is: ${mc}.")
elif (size == "M") and (add_pepperoni == "N") and (extra_cheese == "N"):
    print(f"Your final bill is: ${m}.")
elif (size == "L") and (add_pepperoni == "Y") and (extra_cheese == "Y"):
    print(f"Your final bill is: ${lpc}.")
elif (size == "L") and (add_pepperoni == "Y") and (extra_cheese == "N"):
    print(f"Your final bill is: ${lp}.")
elif (size == "L") and (add_pepperoni == "N") and (extra_cheese == "Y"):
    print(f"Your final bill is: ${lc}.")
elif (size == "L") and (add_pepperoni == "N") and (extra_cheese == "N"):
    print(f"Your final bill is: ${l}.")
