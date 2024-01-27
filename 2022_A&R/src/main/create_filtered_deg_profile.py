import sys
from os import path

sys.path.append('../../src/main')

import gene_set_handling as gsh

path = sys.argv[1]
output = sys.argv[2]

deg_dict = gsh.deg_file_to_dict_and_list(path, ",", 2, 0.01)
gsh.gene_dict_to_output(deg_dict, output)