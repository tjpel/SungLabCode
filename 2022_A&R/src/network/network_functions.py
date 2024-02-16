import pandas as pd

def topology_file_to_dict(topo_file: str) -> dict:
    """
    Input - path to topology file
    """
    print("Function :: topology_file_to_dict > This might take time.")
    topo_dict = {}
    tdf = pd.read_csv(topo_file, sep="\t", header=0)

    for _, row in tdf.iterrows():
        source_node = row["source_gene"]
        target_node = row["target_gene"]

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
        if source_node in topo_dict:
            print(f"Source Node Found: {source_node}")
            for target_node in topo_dict[source_node]:
                if target_node in features:
                    print(f"Target Node Found: {target_node}")

                    if source_node in sub_topo_dict.keys():
                        sub_topo_dict[source_node].append(target_node)
                    else:
                        sub_topo_dict[source_node] = [target_node]

    return sub_topo_dict

def topology_dict_to_output(topo_dict: dict, output_path: str):
    print("Function :: topology_dict_to_output")

    with open(output_path, 'w') as f:
        for source_node in list(topo_dict.keys()):
            for target_node in topo_dict[source_node]:
                f.write(f"{source_node}\t{target_node}\n")

    print ("Info :: topology output creation complete")
    print(f"Info :: > {output_path} <")