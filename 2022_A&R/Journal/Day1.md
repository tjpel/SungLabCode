### Day 1
1:58pm Today I want to work on the first part of this according to the readme, which is Differentially Expressed Genes and Volcano Plot.

2:01 ```analysis_with3Meta/gene_set/01_run_deseq_multi_level.sh``` just runs ```../../src/RNAseqPipeline_SungLab/deseq2_multi_level.r $data_file $meta_file $output_file``` with ```data_file=aortitis.tsv
meta_file=aortitis.meta.tsv
output_file=aortitis.deg.tsv.t2t2```.

2:05 Moving to ```../../src/RNAseqPipeline_SungLab/deseq2_multi_level.r```. Looks like this a well used pipeline for the lab? Files look drag-and-dropped ("/RNASseqPipeline_SungLab/"). Code all makes sense and I'm not sure it could be optimized any more, but I don't know waht DESeqDataSetFromMatrix is. Time to look at documentation for DESeq2.

2:08 Found a good 25-min video on DESeq2 as a whole, going to watch that as the documentation was a little unintuitive.
Notes:
    - Input format: A table with genes as rows, samples as columns, and counts (reads of that gene in that sample) as values.