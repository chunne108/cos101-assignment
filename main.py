def maths_and_physics_formula_options():
    print('nMaths and physics formula option:')
    print('a. frequency ')
    print('b. momentum')
    print('c. perimeter of a rectangle')
    print('d. impulse')
    print('e. area of a parallelogram')
    print('f. finished')


maths_and_physics_formula_options()


options = input(' pick an option from a to f  ')
print(options)
if options == 'a':
    number_of_cycles = int(input('enter number  '))
    time = int(input('enter number  '))
    frequency = number_of_cycles / time
    print(frequency)

elif options == 'b':
    mass = int(input('enter value for mass  '))
    velocity = int(input('enter value for velocity  '))
    momentum = mass * velocity
    print(momentum)

elif options == 'c':
    breadth = int(input('enter value of breadth  '))
    length = int(input('enter value of length  '))
    perimeter_of_a_rectangle = (length + breadth) * 2
    print(perimeter_of_a_rectangle)

elif options == 'd':
    force = int(input('enter value of force  '))
    time = int(input('enter value of time  '))
    impulse = force * time
    print(impulse)

elif options == 'e':
    base = int(input('enter value of base  '))
    height = int(input('enter value of height  '))
    area_of_a_parallelogram = base * height
    print(area_of_a_parallelogram)

elif options == 'f':
    close = "thank you for using chunne's code  "
    matric = "matric no bhu/24/04/05/0116"
    end = close + matric
    print(end)

else :
    print('you are only allowed to pick options from a to f ')