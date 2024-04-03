import numpy, math

def magnetude2d(vec): # POP POP
    return (math.sqrt(vec[0]**2 + vec[1]**2))

def dotproduct2d(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]

arr1 = [0, -1]
arr2 = [0, 1]

print(numpy.degrees(numpy.arccos(dotproduct2d(arr1, arr2)/(magnetude2d(arr1) * magnetude2d(arr2)))))
