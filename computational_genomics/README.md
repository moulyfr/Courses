Mutations within a gene can be classified as synonymous and non-synonymous substitutions. Synonymous substitutions are single base changes that modify a codon without a modification in its encoded amino acid. Non-synonymous mutations modify both the codon and the amino acid.

script_to_run.py contains a script which estimates the number of non-synonymous, synonymous and intergenic SNPs present in a sampled bacterial population (to be run in Python3).

Input files:
1. SNP file: a list of SNPs obtained by mapping the raw sequencing reads of individual bacterial isolates to a complete reference genome of the same species. The contig of origin, position in the contig and nucleotide change are displayed for every SNP.
2. Annotation file: contains the geneID, gene description, contig of origin and genome coordinates for every gene encoded in the reference genome.
3. Genome file: a .fasta file containing the complete genome of the reference sample.

Output files:
1. A text file with 9 columns separated by TAB: (1) contig of origin, (2) SNP position, (3) substitution type, (4) gene description, (5) gene ID, (6) the reference codon, (7) the modified codon, (8) the reference amino acid (single letter) and (9) the modified amino acid (single letter). 
2. A barplot.pdf showing the number of non-synonymous, synonymous and intergenic SNPs present in each contig. Please, check the example output file attached.
