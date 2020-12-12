import sys
import networkx

acc = 0
intr = []
g = networkx.DiGraph()
i = 0
for line in sys.stdin:
    op, amt = line.strip().split()
    sign, amt = amt[0], int(amt[1:])
    if sign == '-':
        amt *= -1

    g.add_node(i, type_=op)
    intr.append((op, amt))
    if op == 'acc':
        g.add_edge(i, i+1, weight=amt)
    elif op == 'nop':
        g.add_edge(i, i+1, weight=0)
    elif op == 'jmp':
        g.add_edge(i, i+amt, weight=0)
    i += 1

cycle = networkx.find_cycle(g)

def find_cost(g):
    acc = 0
    i = 0
    while g.succ[i]:
        j = 0
        for nbr, datadict in g.succ[i].items():
            acc += datadict.get('weight',0)
            j += 1
            if j == 2:
                raise Exception
            i = nbr
    return acc

for edge in cycle:
    node = edge[0]
    if intr[node][0] == 'nop':
        new = g.copy()
        new.remove_edge(node, edge[1])
        new.add_edge(node, node + intr[node][1])
        try:
            networkx.find_cycle(new)
        except:
            print(find_cost(new))
            break
    elif intr[node][0] == 'jmp':
        new = g.copy()
        new.remove_edge(node, edge[1])
        new.add_edge(node, node+1)
        try:
            networkx.find_cycle(new)
        except:
            print (find_cost(new))
            break
