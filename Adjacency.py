import sys

# make set and put all Vs in it
def edge_to_adjacency(edge_list):
    vs = set()
    for e in edge_list:
        vs.add(e[1])
        vs.add(e[0])

# Vs <--> Is
    v_to_i = {v: i for i, v in enumerate(sorted(vs))}

# start adj mtrx but put in all 0s
    num_vs = len(vs)
    adj_mtrx = [[0] * num_vs for i in range(num_vs)]

# replace 0s w/ wghts
    for e in edge_list:
        from_v, to_v, wght = e
        from_i = v_to_i[from_v]
        to_i = v_to_i[to_v]
        adj_mtrx[from_i][to_i] = wght

    return adj_mtrx

# remove formatting and convert to list of tokens
# do not change this method
def clean(text):
    text = text.strip()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("”", "")
    text = text.replace(" ", "")
    text = text.replace("\"", "")
    text = text.split(",")
    return text


''' DRIVER CODE '''

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('adjacency.in')
else:
    in_data = sys.stdin

# get line of input, remove formatting, convert to list of tokens
input_text = in_data.readline()
input_text = clean(input_text)

# convert one string to 2D list of edge data
edges = []
for i in range(0, len(input_text), 3):
    newList = [input_text[i], input_text[i+1], int(input_text[i+2])]
    edges.append(newList)

# convert the 2D list to an adjacency matrix
adj_matrix = edge_to_adjacency(edges)

print('\n'.join([' '.join([str(cell) for cell in row]) for row in adj_matrix]))
