
infile = open('input2.txt','r')

total = 0
for line in infile:
    dimensions = line.strip().split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    
    perim = []
    perim.append(l+l+w+w)
    perim.append(w+w+h+h)
    perim.append(h+h+l+l)
    perimeter = min(perim)
    
    vol = l*w*h
    box = vol+perimeter
    total += box
print(total)
