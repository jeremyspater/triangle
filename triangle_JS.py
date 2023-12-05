#Program to classify triangle, based on side lengths

from typing import List
import math #for 'isclose'

def tri_clas(sides: List[float]):

    #Input validation:
    if not isinstance(sides, list):
        raise ValueError("Input must be a list of numbers.")
    
    if not len(sides) == 3:
        raise ValueError("Input must contain three numbers.")
    
    if not all(isinstance(num, (int, float)) and num > 0 for num in sides):
        raise ValueError("All elements in the list must be positive numbers (integer or float).")

    if not ((sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[0] + sides[2] > sides[1])): #Condition for a triangle
        raise ValueError("Input must correspond to a valid triangle: one length cannot exceed sum of other two")
    
    #Logic for classifying triangle:
    if math.isclose(sides[0], sides[1]) and math.isclose(sides[1], sides[2]): 
        return('Equilateral')
    
    elif math.isclose(sides[0], sides[1]) or math.isclose(sides[1], sides[2]) or math.isclose(sides[0], sides[2]): 
        return('Isoceles')
    
    else:
        return('Scalene')

#Testing cases:

#Basic cases:
print(tri_clas([1,1,1]))
#print(tri_clas([2,2,3]))
#print(tri_clas([3,2,2]))
#print(tri_clas([2,3,2]))
#print(tri_clas([2,3,4]))

#Illegitimate cases:
#print(tri_clas(['a','b','c'])) 
#print(tri_clas(['a', 2, 3])) 
#print(tri_clas([1,2,3,4]))
#print(tri_clas([1, 1, -1]))
#print(tri_clas([1, 1, 0]))
#print(tri_clas([1, 2, 1]))
#print(tri_clas([3, 1, 1]))
#print(tri_clas([1, 1, 3]))
#print(tri_clas([1E99, 1E99, 3E99]))
#print(tri_clas([1, 1, 1+1j])) 

#Alternative number specifications:
#print(tri_clas([1.5, 3/2, 1.5]))
#print(tri_clas([0.3, 0.1+0.2, 0.3])) #'isclose' prevents floating-point rounding error here
#print(tri_clas([1E99, 1E99, 1E99]))
#print(tri_clas([1.,1.,1.]))
#print(tri_clas([1.,1,1]))
#print(tri_clas([True,1,1]))



