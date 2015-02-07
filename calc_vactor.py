import math
v = (2, 3)
d_angle = math.radians(10)


v_new = (math.sin(d_angle)* math.sqrt(v[0]**2+ v[1]**2), math.cos(d_angle)* math.sqrt(v[0]**2+ v[1]**2) )
l = math.sqrt(v_new[0]**2 + v_new[1]**2) - math.sqrt(v[0]**2 + v[1]**2)
print(l)
