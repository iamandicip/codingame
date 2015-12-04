import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

nodes = {}
gateways = []

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

#initiate a dictionary that will contain each node with all its links
for i in range(n):
    nodes[i] = []

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    #populate the nodes links
    nodes[n1].append(n2)
    nodes[n2].append(n1)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

# game loop
while 1:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    n2 # the two nodes of the link to be cut

    agent_options = nodes[si]
    for node in agent_options:
        n2 = node
        if(node in gateways):
            break

    print(str(si) + " " + str(n2))
