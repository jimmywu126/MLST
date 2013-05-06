from graph import *
from graph_helper import *
from constants import *
from input_output import *
from solver_algorithms import *

"""
This file extracts leafy spanning trees from graphs, for part 2 of the MLST project.
"""

our_graphs = []
our_trees = []

# Takes a list of graphs and returns the leafiest spanning tree we can find
# by running them through all of our algorithms
def find_leafy_spanning_trees(graphs):

	# Initialize our graph-tree pairs
	our_graphs = input_graphs_from_file(OUR_GRAPHS)
	for graph in our_graphs:
		graph.search()
	our_trees = input_graphs_from_file(OUR_TREES)
	for tree in our_trees:
		tree.search()

	leafy_spanning_trees = []

	for graph in graphs:
		best_tree = find_leafy_spanning_tree(graph)
		leafy_spanning_trees.append(best_tree)

	return leafy_spanning_trees




# Takes a graph and returns the leafiest spanning tree we can find by running
# it through all of our algorithms
def find_leafy_spanning_tree(graph):

	# Maintain a record of bests so far
	best_tree = None
	best_leaf_count = 0
	best_algorithm = ''

	# Test for graph generated by us
	for i in range(len(our_graphs)):
		if are_equivalent_graphs(graph, our_graphs[i]):
			best_tree = our_trees[i]
			best_leaf_count = our_trees[i].num_leaves
			best_algorithm = 'our own solution'


	# Test for line
	if is_line(graph):
		print('Best solution:\tLeaves: ' + str(len(get_leaves(graph))) + '\t/\t' + str(len(get_nodes(graph))) + '\tAlgorithm: detected line')
		return graph

	# Test for tree
	if is_tree(graph):
		print('Best solution:\tLeaves: ' + str(len(get_leaves(graph))) + '\t/\t' + str(len(get_nodes(graph))) + '\tAlgorithm: detected tree')
		return graph

	# Test for small input size
	number_of_edges = len(get_edges(graph))
	if number_of_edges < 25:
		print('Graph contains only ' + str(number_of_edges) + ' edges. Recommend manually solving.')

	# Try all algorithms and record the best one
	for algorithm_name, algorithm in ALGORITHMS:
		tree = algorithm(graph)
		tree.search()

		if tree.num_leaves > best_leaf_count:
			best_tree = tree
			best_leaf_count = tree.num_leaves
			best_algorithm = algorithm_name

	# Log the best solution
	print('Best solution:\tLeaves: ' + str(best_leaf_count) + '\t/\t' + str(len(get_nodes(graph))) + '\tAlgorithm: ' + best_algorithm)

	return best_tree




