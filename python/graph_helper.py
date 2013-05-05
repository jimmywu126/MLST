from graph import *
from constants import *
from random import shuffle

"""
This file contains convenient helper methods for graphs.
"""

# Returns a list of nodes in the graph
def get_nodes(graph):
	nodes = set()
	edges = get_edges(graph)

	for edge in edges:
		nodes.add(edge.ends[0])
		nodes.add(edge.ends[1])

	return list(nodes)


# Returns a list of edges in the graph
def get_edges(graph):
	number_of_nodes = len(graph.neighbors)
	edge_set = set()

	for current_node in range(0, number_of_nodes):
		for adjacent_node in graph.neighbors[current_node]:
			edge_set.add(Edge(current_node, adjacent_node))

	return list(edge_set)


# Returns a list of edges not used in the graph.
def get_unused_edges(graph):
	number_of_nodes = len(graph.neighbors)
	unused_edge_set = set()

	for current_node in range(0, number_of_nodes):
		current_node_neighbors = set(graph.neighbors[current_node])
		for other_node in range(0, number_of_nodes):
			if current_node != other_node:
				if other_node not in current_node_neighbors:
					unused_edge_set.add(Edge(current_node, other_node))

	return list(unused_edge_set)


# Returns a list of all nodes in the tree that are leaves (degree one)
def get_leaves(tree):
	leaves = []
	for node in range(0, len(tree.neighbors)):
		if len(tree.neighbors[node]) == 1:
			leaves.append(node)

	return leaves

def create_copy_of_graph(graph):
	edges = get_edges(graph)
	return make_graph(edges)


# Returns a random graph of given size
def create_sample_graph(number_of_nodes, number_of_edges):

	# For an undirected graph with n nodes, m = n(n-1)/2
	if number_of_edges > number_of_nodes * (number_of_nodes - 1) / 2:
		number_of_edges = number_of_nodes * (number_of_nodes - 1) / 2

	# Create empty graph
	sample_graph = Graph(number_of_nodes)

	# Maintain a random-order list of unused edges
	unused_edges = get_unused_edges(sample_graph)
	shuffle(unused_edges)

	# Add random edges to graph
	for _ in range(number_of_edges):
		sample_graph.add_edge(unused_edges.pop())

	return sample_graph


