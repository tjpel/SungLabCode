import networkx as nx
import sys
import os

ppi_graph_file = sys.argv[1]
subgraph_file = sys.argv[2]
sub_topology_file = sys.argv[3]

graph = nx.Graph() #https://networkx.org/documentation/stable/tutorial.html

edges = nx.read_edgelist(ppi_graph_file)
graph.add_edges_from(edges.edges())
print(f"Number of Nodes in Current Network: {len(list(graph.nodes))}")

subgraph_gene_list = list(max(nx.connected_components(graph), key=len))
print(f"Number of Nodes in Largest Connected Components: {len(subgraph_gene_list)}")

with open(subgraph_file, 'w') as f:
    for gene in subgraph_gene_list:
        f.write(f"{gene}\n")

with open(sub_topology_file, 'w') as f:
    for node in subgraph_gene_list:
        edge_list = graph.edges(node)
        for edge_info in edge_list:
            source_node = edge_info[0]
            target_node = edge_info[1]
            f.write(f"{edge_info[0]}\t{edge_info[1]}\n") #edge_info[n] = source_node, target