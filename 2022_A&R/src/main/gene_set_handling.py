import pandas as pd

def deg_file_to_dict_and_list(path: str, delimiter: str, abs_log2_thresh: float, padj_thresh: float) -> dict:
    """
    Function Requirements: DESeq2 outputs as tsv
    Note: Says specified to handle Vasculitis project, ask for unspeced version
    """

    print(f"Info :: abs log2 threshold set to {abs_log2_thresh}")
    print(f"Info :: adj p-value threshold set to {padj_thresh}")

    df = pd.read_csv(path, sep=delimiter, header=0)

    #abs(df["log2fc"]) > abs_log2_thresh indictates big movement of reglation of gene
    #float(df["padj"]) < float(padj_thresh) meets a certain p-val threshold for multiple testing
    gene_interest = df[(abs(df["log2FoldChange"]) > abs_log2_thresh) & (df["padj"] < float(padj_thresh))]

    deg_dict = {}
    for _, row in gene_interest.iterrows():
        gene = row.iloc[0]
        log2fc = float(row['log2FoldChange'])
        padj = float(row['padj'])

        deg_dict[gene] = [log2fc, padj]

    print(f"Info :: Total Number of DEGs = { len(deg_dict.keys()) }")

    return deg_dict


def gene_dict_to_output(deg_dict: dict, output_path: str):
    with open(output_path, 'w') as f:
        f.write("gene\tlog2fc\tpadj\n")

        for gene, value in deg_dict.items(): #key = gene name, value = [log2fc, padj]
            f.write(f"{gene}\t{value[0]}\t{value[1]}\n")


