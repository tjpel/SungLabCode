library(ggplot2)
library(ggrepel)

#cmd: Rscript DEG_to_VolcanoPlot.adj.r [input] [output_prefix]

args <- commandArgs(trailingOnly = TRUE)
input_file <- read.csv(args[1], sep = ",", header = TRUE, row.names = 1)
output_prefix <- args[2]

#make a new df
x_axis <- input_file$log2FoldChange #x is the log2foldchange
y_axis <- -log10(input_file$padj) #y is -log10 of the padj value
gene_list <- rownames(input_file)
df <- do.call(rbind, Map(data.frame, "log2FC" = x_axis, "padj" = y_axis)) #map() creates a dataframe of log2FC, padj pairs, then r bind concats them into one # nolint: line_length_linter.
rownames(df) <- gene_list
df$genes <- row.names(df)

#create subsets
#adj pvalue 0.05 = 1.30103 (-log10 padj)
#adj pvalue 0.01 = 2 (-log10 padj)
sig_subset <- subset(df, padj > 1.30103)
sig_red_subset <- subset(sig_subset, log2FC > 2)
sig_blue_subset <- subset(sig_subset, log2FC < -2)
sig_red_text_subset <- subset(sig_subset, log2FC > 2)
sig_blue_text_subset <- subset(sig_subset, log2FC < -2)

output_pdf_label <- paste(output_prefix, ".volcano.label.pdf", sep="")
pdf(output_pdf_label)
ggplot(df, aes(x=log2FC, y=padj))+ coord_cartesian(xlim=c(-8,8), ylim=c(0,30))+ geom_point(colour="grey") +
geom_point(data = sig_red_subset, colour="red") +
geom_point(data = sig_blue_subset, colour="blue") +
geom_text_repel(data = sig_red_text_subset, aes(log2FC, padj, label=genes), colour="red", size=2) +
geom_text_repel(data=sig_blue_text_subset, aes(log2FC, padj, label=genes), colour="blue", size=2) +
ylab("-Log_10 (adj pvalue)")
dev.off()