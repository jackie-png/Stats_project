g = [[0,7,7,8],[6,7],[1],[5,1,7],[2,3,5,6],[1,2,3,4,5,6,7,8,9,0]] # rep answers

h = [1] # rep filter list

u = []

for elm in g:
    for elt in elm:
        if elt in h:
            if elm not in u:
                u.append(elm)
                break
            else:
                continue

print (u)