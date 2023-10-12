#secret santa
import random
names = []
while True:
    names.append(input('Input a name: ').lower().strip())
    if names[-1] ==  '':
        names.pop()
        break

diction = {}
for i in names:
    diction[i] = names.copy()
    diction[i].remove(i)

while True:
    try:
        diction[input('Pick a name who can\'t get someone else ').lower().strip()].remove(input('Pick the person they can\'t get ').lower().strip())
    except:
        break
input('Ready? ')

outputs = []
worked = False
while worked == False:
    worked = True
    outs = []
    for i in range(len(names)):
        try:
            op = random.choice(diction[names[i]])
        except:
            worked = False
        outs.append([names[i],op])
        for j in names:
            try:
                diction[j].remove(op)
            except ValueError:
                pass
for ii in outs:
    input(ii[0]+' got: (enter to reveal)')
    print(ii[1].title())
