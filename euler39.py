import math

num_solutions = 0
answer = 0

for p in range(100, 1000):
  # p = a + b + c
  # a = P * ( P - 2 * b ) / ( 2 * ( P - b )
  solutions = 0
  for b in range(1, p):
    a = p * ( p - 2 * b ) / ( 2 * ( p - b ))
    if(a<1): break
    c = math.sqrt( a**2 + b**2 )
    if (c == int(c) and (a < b)):
      print "For Perimeter ", p, " {",a,",",b,",",c,"}"
      solutions = solutions + 1
      if(solutions > num_solutions):
        num_solutions = solutions
        answer = p
print "P=",answer," num: ",num_solutions
		