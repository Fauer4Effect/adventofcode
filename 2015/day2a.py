infile = open("input2.txt",'r')

total = 0
for line in infile:
    dimensions = line.strip().split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    side1 = 2*length*width
    side2 = 2*width*height
    side3 = 2*height*length


    sides =[side1,side2,side3]
    extra = min(sides)/2

    print(str(side1),str(side2),str(side3),str(extra))
    box =side1 + side2 + side3 + extra
    total += box
    print(box,total)
print(total)