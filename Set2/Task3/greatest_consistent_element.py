from sys import argv



def next_nb(ls, visited, iterator, element):
    for i in range(len(ls[iterator])):
        #print(f"{visited} {ls[iterator][i]}")
        if  visited[ls[iterator][i] - 1] == 0:
            visited[ls[iterator][i] - 1] = element
            next_nb(ls, visited, ls[iterator][i] - 1, element)




if len(argv) < 2:
    print("Podaj input")
    exit()

# whole graph
ls = []
# contains information about every consistent element - 
#value of given element of the array equals the index of consistent element
visited = []
vertices = 0


# read graph from file
with open(argv[1]) as f:
    line = (str(f.readline()).rstrip())
    if line != "LS":
        print("Podaj liste sasiedztwa")
    for line in f:
        ls.append(line.rstrip().split(' '))
        vertices += 1

for i in range(len(ls)):
    if len(ls[i]) > 0 and ls[i][0] != '':
        ls[i] = list(map(int, ls[i]))
    else:
        ls[i].remove('')
f.close()


# set visited list to work
for i in range(vertices):
    visited.append(0)


element = 1
i = 0


# while there's any unvisited vertex 
while 0 in visited:
    # if not visited, start recursively from this vertex
    if visited[i] == 0:
        # set visited value to next element index
        visited[i] = element
        next_nb(ls, visited, i, element)
    if element in visited:
        element += 1
    i += 1



# creating new graph out of the greatest element
max_count = 0
max_index = 0
for i in visited:
    current_count = 0
    for j in visited:
        if j == i:
            current_count += 1
    if current_count > max_count:
        max_count = current_count
        max_index = i


# greatest consistent element
#gce = [[j for j in ls[i]]  for i in range(len(visited)) if visited[i] == max_index]
gce = [[j for j in ls[i]] if visited[i] == max_index else [0] for i in range(len(visited)) ]


#print(max_count, max_index)
#print(ls)
#print(gce)
#print(visited)


with open("graph_out.txt", 'w') as f:
    f.write("LS\n")
    for i in range(len(gce)):
        for j in gce[i]:
            f.write(f"{j} ")
        f.write('\n')
f.close()

if (max_count == len(ls)):
    print("graf spojny")
else:
    print("graf niespojny")