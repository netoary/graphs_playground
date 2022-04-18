# -*- coding: utf-8 -*-

import time

load("utils.sage")

def solve_direct_ILP(G):
	inicio = time.time()
	p = MixedIntegerLinearProgram(maximization=True,solver="GUROBI")
	#p = MixedIntegerLinearProgram(maximization=True,solver=GurobiBackend)
	count = 0
	w = p.new_variable(binary=True)
	constraint = 0
	dic={}
	for e in G.edges():
		dic[e]=[]
	for x in Subsets(G.edges(),5):
		H = Graph()
		H.add_edges(x)
		if isPath(H):
			constraint=constraint+w[x]
			for e in x:
				dic[e].append(x)
			count+=1
	m = G.order()/2
	p.add_constraint(constraint<=m)
	p.add_constraint(constraint>=m)			
	for y in dic:
		constraint=0
		for x in dic[y]:
			constraint=constraint+w[x]
		p.add_constraint(constraint<=1)

	p.solve()
	sol=p.get_values(w).items()
	setted=[]
	for x in sol:
		if x[1]==1.0:
			setted.append(x[0])
	cor=0
	for x in setted:
		for e in x:
			G.set_edge_label(e[0],e[1],cor)
		cor+=1
	fim = time.time()
	print('tempo de execução ' + str(fim-inicio))
	return setted, fim-inicio




# Acho que esse de baixo retorna as soluções intermediarias, mas não lembro pra que

def solve_direct_ILP_full(G):
	inicio = time.time()
	all_graphs = []
	p = MixedIntegerLinearProgram(maximization=True,solver="GUROBI")
	#p = MixedIntegerLinearProgram(maximization=True,solver=GurobiBackend)
	count = 0
	w = p.new_variable(binary=True)
	constraint = 0
	dic={}
	for e in G.edges():
		dic[e]=[]
	for x in Subsets(G.edges(),5):
		H = Graph()
		H.add_edges(x)
		if isPath(H):
			constraint=constraint+w[x]
			for e in x:
				dic[e].append(x)
			count+=1
	m = G.order()/2
	p.add_constraint(constraint<=m)
	p.add_constraint(constraint>=m)			
	for y in dic:
		constraint=0
		for x in dic[y]:
			constraint=constraint+w[x]
		p.add_constraint(constraint<=1)

	while(True):
		try:
			p.solve()
		except:
			break
		sol=p.get_values(w).items()
		setted=[]
		constraint=0
		for x in sol:
			if x[1]==1.0:
				setted.append(x[0])
				constraint=constraint+w[x[0]]
		print(setted)
		all_graphs.append(setted)
		p.add_constraint(constraint<=m)
		p.add_constraint(constraint>=m)
	return all_graphs

	# ADICIONAR LOOP, dúvida até quando?
	 

	fim = time.time()
	print('tempo de execução ' + str(fim-inicio))


