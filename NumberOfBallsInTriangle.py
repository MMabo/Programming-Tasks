total = 0
def NumberOfBallsInTriangle(NoAlongSide):

    if NoAlongSide == 1:
        return 1

    else:
        return NoAlongSide + NumberOfBallsInTriangle(NoAlongSide-1)

print(NumberOfBallsInTriangle(993))
print(NumberOfBallsInTriangle(994))
