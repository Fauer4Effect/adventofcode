inputfile = open('input7.txt','r')
'''
the trick to this one is we are going to try to run all of the rules
if the necessary input for the rules are defined
we are just going to keep running all of the rules as long
as necessary until we finally reach the end and the values stabalize
'''
wires = {}
def dorules(rules):
    for commandlist in rules:

        if commandlist[0] =='NOT':
            if commandlist[1] in wires:
                wires[commandlist[2]] = ~wires[commandlist[1]]
        
        elif 'AND' in commandlist:
            if commandlist[0] in wires and commandlist[2] in wires:
                in1 = wires[commandlist[0]]
                in2 = wires[commandlist[2]]
                wires[commandlist[3]] = in1 & in2
            elif commandlist[2] in wires:
                try:
                    in1 = int(commandlist[0])
                    in2 = wires[commandlist[2]]
                    wires[commandlist[3]] = in1 & in2
                except ValueError:
                    pass
        
        elif 'OR' in commandlist:
            if commandlist[0] in wires and commandlist[2] in wires:
                in1 = wires[commandlist[0]]
                in2 = wires[commandlist[2]]
                wires[commandlist[3]] = in1 | in2
            elif commandlist[2] in wires:
                try:
                    in1 = int(commandlist[0])
                    in2 = wires[commandlist[2]]
                    wires[commandlist[3]] = in1 | in2
                except ValueError:
                    pass
        
        elif 'LSHIFT' in commandlist:
            if commandlist[0] in wires:
                in1 = wires[commandlist[0]]
                shift = int(commandlist[2])
                wires[commandlist[3]] = in1 << shift
        
        elif 'RSHIFT' in commandlist:
            if commandlist[0] in wires:
                in1 = wires[commandlist[0]]
                shift = int(commandlist[2])
                wires[commandlist[3]] = in1 >> shift
        
        elif len(commandlist) == 2:
            try:
                wires[commandlist[1]] = int(commandlist[0])
            except ValueError:
                if commandlist[0] in wires:
                    wires[commandlist[1]] = wires[commandlist[0]]

rules = []
for line in inputfile:
        commandlist = line.strip().split(' ')
        commandlist.remove('->')
        rules.append(commandlist)

while 'a' not in wires:
        dorules(rules)
        
print(wires['a'])

