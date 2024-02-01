import math
x=math.pi/4
y=math.pi/3
a=math.tan(x)
b=math.tan(y)
c=math.sin(y)
numerator=math.sqrt(a+1)
denominator=math.sqrt(b+c)
value=numerator/denominator
print("The value is", value)
