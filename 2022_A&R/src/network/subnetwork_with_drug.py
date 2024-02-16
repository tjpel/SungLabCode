import pandas as pd

import sys
sys.path.insert(1, "../../src/main")
import gene_set_handling as GSH

disease_df = pd.read_csv(sys.argv[1], sep='\t')
subcluster_topo_df = pd.read_csv(sys.argv[2], sep='\t')
gene_list = GSH.gene_file_to_gene_list(sys.argv[3], '\t', 0)

output_file = sys.argv[4]

subcluster_topo_dict = {}
drug_list = []

for _, row in subcluster_topo_df.iterrows():
    try: subcluster_topo_dict[row[0]].append(row[1])#row[0] = source, row[1] = target
    except KeyError: subcluster_topo_dict[row[0]] = [row[1]]

for _, row in disease_df.iterrows():
    if row[3] in gene_list: #row[3] is gene, row[4] is drug
        drug_list.append(row[4])
        try: subcluster_topo_dict[row[3]].append(row[4])#row[3] = gene, row[4] = drug
        except KeyError: subcluster_topo_dict[row[3]] = [row[4]]

print(f"Total parsed drug: {len(drug_list)}")
drug_list = list(set(drug_list))
print(f"Unique drugs: {len(drug_list)}")

temp_dict = {}
with open(output_file, 'w') as f:
    for source in subcluster_topo_dict.keys():
        for target in subcluster_topo_dict.get(source, []):
            if target in drug_list:
                drug = target
                target = f'{source}_drug'
                try: temp_dict[drug].append(target)
                except KeyError: temp_dict[drug] = [target]
            
            f.write(f'{source}\t{target}\n')


output_file_preface = output_file.split('.tsv')[0]
with open(str(output_file_preface)+'.drug_info.tsv', 'w') as f:
    for gene in temp_dict.keys():
        f.write(f'{gene}\t{len(temp_dict[gene])}')
        for drug in temp_dict[gene]:
            f.write(f'\t{drug}')
        f.write('\n')