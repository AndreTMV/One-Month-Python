sub_total = float(input("What is your bill sub-total?").strip('$'))

print("Tip sugestions:")
print("-------------------------------------------------------------------")
print(f"15% is ${sub_total * .15:.2f}")
print(f"18% is ${sub_total * .18:.2f}")
print(f"20% is ${sub_total * .20:.2f}")

tip_total = float(input("How much do you want to tip?").strip('%'))

print(f"The total is: ${sub_total + ((tip_total / 100)*sub_total)}")
