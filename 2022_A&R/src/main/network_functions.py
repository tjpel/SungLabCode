import pandas as pd

def topology_file_to_dict(topo_file: str) -> dict:
    """
    Input - path to topology file
    """
    print("Function :: topology_file_to_dict > This might take time.")
    topo_dict = {}
    tdf = pd.read_csv(topo_file, sep="/t", header=0)

    for _, row in tdf.iterrows():
        source_node = row[0]
        target_node = row[1]

        if source_node in topo_dict.keys():
            topo_dict[source_node].append(target_node)
        else:
            topo_dict[source_node] = [target_node]

    return topo_dict

def create_sub_topology(features: list, topo_dict: dict) -> dict:
    print("Function :: create_sub_topology")
    print(f"Info :: Feature list size > {len(features)}")
    print(features)

    sub_topo_dict = {}
    for source_node in topo_dict.keys():
        pass



