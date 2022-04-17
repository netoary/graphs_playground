import gurobipy as gp
from gurobipy import GRB

def is_path_of_length_five(edges):
    H = Graph(edges)
    if not H.is_connected():
        return False
    if not H.is_forest():
        return False
    return True

def mycallback(model, where):
    """
    This function checks whether the incumbent solution found by Gurobi has a
    cycle or not. If a cycle was found, then this function adds a constraint
    that is violated by the current solution.

    To be more precise, if a cycle C is found in the current solution,
    then this function adds the following constraint

      ∑ x_{e, 0} ≤ |E(C)| - 1
    e ∈ E(C)
    """

    if where == GRB.Callback.MIPSOL:
        print("entrou no callback")

        vals = model.cbGetSolution(x)

        dic = {}
        print(numero_de_cores)
        for c in range(numero_de_cores):
            dic[c] = []
            
        for (triple, val) in vals.items():
            if val > 0:
                u, v, c = triple
                dic[c].append((u, v, c))
        
        for c in range(numero_de_cores):
            edges = dic[c]
            #print(is_path_of_length_five(edges))
            if not is_path_of_length_five(edges):
                equation = 0
                for e in edges:
                    u, v, c = e
                    equation += x[u, v, c]
                model.cbLazy(equation <= 4)
        model.update()
        print(model)

G = graphs.RandomRegular(5,10)

model = gp.Model("5-path decomposition")

model.setParam('OutputFlag', 0)

numero_de_cores = G.size()/5

indices = [(u, v, c) for u, v, label in G.edges() for c in range(numero_de_cores)]
x = model.addVars(indices, lb=0.0, ub=1.0, vtype=GRB.BINARY, name="x")

model.update()

cont = 0

for u in G.vertices():
    for c in range(numero_de_cores):
        equation = 0
        for e in G.edges_incident(u):
            a, b, _ = e
            equation += x[a, b, c]
        cont += 1        
        _ = model.addConstr(equation<=2, name='each color has maximum degree at most 2')

print(cont)

model.update()

cont = 0
for c in range(numero_de_cores):
    equation = 0
    for e in G.edges():
        a, b, _=e
        equation += x[a, b, c]
    cont += 1
    _ = model.addConstr(equation==5, name='each color has five edges')

print(cont)

model.update()

for e in G.edges():
    equation = 0
    a, b, _ = e
    for c in range(numero_de_cores):
        equation += x[a, b, c]

    _ = model.addConstr(equation==1, name='each edge has one color')
model.update()

model.write("modelo_debug.lp")
model.Params.lazyConstraints = 1
model.optimize(mycallback)





def show(model, G, numero_de_cores, x):

    if model.status != GRB.OPTIMAL:
        return []

    edges=[]
    for e in G.edges():
        u,v,label=e
        for c in range(numero_de_cores):
            if x[u,v,c].x > 0.1:
                G.set_edge_label(u,v,c)
    G.show(color_by_label=True, layout="circular")

dix = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
cont=0
for e in G.edges():
    u,v,label=e
    for c in range(numero_de_cores):
        if x[u,v,c].x > 0.1:
            print(f"x {u,v,c} = {x[u,v,c].x}")
            cont+=1
            dix[c] += 1
print(cont)