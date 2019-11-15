gates = ['OR','AND','XOR','NOR','NAND']
precedence_order = []
for i in enumerate(gates):
    print(i)
    precedence_order.append(i)

gate1 = input()
gate2 = input()

#The precedence is NAND > NOR > NOT > XOR > AND > OR
# A gate1 B = C
# C gate2 D = E 
#output E

for a in range(2):
    for b in range(2):
        for c in range(2):
            print()
            

