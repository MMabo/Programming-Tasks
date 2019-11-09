def mortgage_repayment(A,Y,R):
    top = A * (R/1200) * ((1 + R/1200)**(12*Y))
    bottom = ((1 + R/1200)**(12*Y)) - 1
    return top/bottom

print(mortgage_repayment(12,5000,13))
