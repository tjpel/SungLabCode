#No changes to the start

library(DESeq2)

args <- commandArgs(trailingOnly = TRUE) #get args

#read in args tables and filenames
input_data <- read.csv(args[1], sep = "\t", row.names = 1, header = TRUE) 
input_meta_data <- read.csv(args[2], sep = "\t", row.names = 1, header = TRUE)
output_file <- args[3]

#make sure row names in input_data match column names
all(colnames(input_data) %in% rownames(input_meta_data))
#check if they are in the same order
all(colnames(input_data) == rownames(input_meta_data))

cts <- as.matrix(input_data)

dds <- DESeqDataSetFromMatrix(countData = cts,
                                colData = input_meta_data,
                                design = ~ condition)

dds <- estimateSizeFactors(dds)
norm_counts <- counts(dds, normalized = TRUE)
deseq_result <- DESeq(dds)

res <- results(deseq_result, contrast = c("condition", "case", "control"))

pvalue_order <- res[order(res$pvalue), ]
write.csv(as.data.frame(pvalue_order), file = output_file, quote = FALSE)