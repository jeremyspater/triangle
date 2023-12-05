from typing import List
import math #for 'isclose'

def tri_clas(sides: List[float]):

    #Input validation:
    if not isinstance(sides, list):
        raise ValueError("Input must be a list of numbers.")
    
    if not len(sides) == 3:
        raise ValueError("Input must contain three numbers.")
    
    if not (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[0] + sides[2] > sides[1]): #Condition for a triangle
        raise ValueError("Input must correspond to a valid triangle: one length cannot exceed sum of other two")
    
    if not all(isinstance(num, (int, float)) and num > 0 for num in sides):
        raise ValueError("All elements in the list must be positive numbers (integer or float).")

    #Logic for classifying triangle:
    if math.isclose(sides[0], sides[1]) and math.isclose(sides[1], sides[2]):
        return('Equilateral')
    
    elif math.isclose(sides[0], sides[1]) or math.isclose(sides[1], sides[2]) or math.isclose(sides[0], sides[2]): #using isclose
        return('Isoceles')
    
    else:
        return('Scalene')
    
#print(tri_clas([1,1,1]))
#print(tri_clas([1,1,2]))
#print(tri_clas([1,2,3]))
#print(tri_clas(['a','b','c']))
#print(tri_clas([1,2,3,4]))
#print(tri_clas([1, 1, -1]))
#print(tri_clas([1.5, 3/2, 1.5]))
#print(tri_clas([0.3, 0.1+0.2, 0.3]))
#print(tri_clas([0.3, 0.1+0.2, 1]))
print(tri_clas([1, 2, 1]))
#print(tri_clas([1, 1, 1E6]))
