# Import os to cwd to current directory
import os
path = os.getcwd()
os.chdir(path)

### Make genes.txt & SNPs.txt & genome.fasta easier to read through... ###

# Make gene list
genesList = []
# Store genes txt file contents as geneList
with open('genes.txt', 'r') as geneFile:
    next(geneFile, None) # Skip header
    for line in geneFile.readlines(): # Go over all the lines
        gene = line[:-1].split('\t') # Split line by '\t' and remove '\n'
        gene[2] = int(gene[2]) # Make columns 2,3 into integers for later use (start, end of gene)
        gene[3] = int(gene[3])
        genesList.append(gene) # Append each gene into list

# Make snp list
snpList = []
# Store snp txt file contents as snpList
with open('SNPs.txt', 'r') as SNPfile:
    next(SNPfile, None)  # Skip header in SNPfile
    for line in SNPfile.readlines(): # Go over every line
        SNP = line[:-1].split('\t')  # Split line by '\t' and remove '\n'
        snpList.append(SNP) # Append each SNP into list

# Make sequence dictionary so that each contig can be sliced out
from Bio import SeqIO # Import SeqIO in order to parse fas file
seq_dict = {rec.id : rec.seq for rec in SeqIO.parse("genome.fasta", "fasta")}

# Make lists that will be used to make the tableOutput.txt & incl 1st item (which will become the 'headers')
contig = ['contig']
snpPosition = ['snpPosition']
Type = ['Type']
Annotation = ['Annotation']
geneID = ['geneID']
referenceCodon = ['referenceCodon']
modifiedCodon = ['modifiedCodon']
referenceAA = ['referenceAA']
modifiedAA = ['modifiedAA']

# Make codon dictionary (codons : amino acid) # skip header by treating new lines as new lines
codon_dictionary = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*','TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W', '\n':'\n'}


# Make variables to count each contig's synonymous, non-syn, intergenic SNPs, which will be used for the Plot
contig1_synonymous = 0
contig1_nonsynonymous = 0
contig1_intergenic = 0
contig2_synonymous = 0
contig2_nonsynonymous = 0
contig2_intergenic = 0
contig3_synonymous = 0
contig3_nonsynonymous = 0
contig3_intergenic = 0

### INTERGENIC LOOP: Go through genes, snp lists to identify intergenic SNPs ###
# Note: I had to count/deal with Intergenic SNPs here as opposed to in the Intragenic loop because I couldn't make it work there with else, elif, etc.
for SNP in snpList: # Go through each SNP
    for gene in genesList: # Go through each gene
        if (SNP[0] == gene[0]): # Both Contig columns need to be the same btwn the 2 files
            if (gene[2] <= int(SNP[1]) <= gene[3]) or (gene[3] <= int(SNP[1]) <= gene[2]): # If SNP is intragenic on non-reverse or reverse strands
                SNP.append('Intragenic')
                break # In case a SNP is present in more than 1 gene
for SNP in snpList: # snpList will now have an extra 4th column for intragenic SNPs
    if len(SNP)==3: # this will isolate the intergenic SNPs, since they only have 3 columns, or items, in the list
        # Append all 9 column info for intergenic SNPs
        contig.append(SNP[0])
        snpPosition.append(SNP[1])
        Type.append('Intergenic')
        Annotation.append('-')
        geneID.append('-')
        referenceCodon.append('-')
        modifiedCodon.append('-')
        referenceAA.append('-')
        modifiedAA.append('-')
        # Do intergenic counts for each contig
        if SNP[0] == 'Contig_1':
            contig1_intergenic += 1 # Add 1 to count
        if SNP[0] == 'Contig_2':
            contig2_intergenic += 1 # Add 1 to count
        if SNP[0] == 'Contig_3':
            contig3_intergenic += 1 # Add 1 to count

### INTRAGENIC LOOP: Go through genes, snp lists and fasta file to count synonymous, non-synonymous SNPs ###

# Import bioseq for reverse complementing
from Bio.Seq import Seq
# Go through each SNP
for SNP in snpList:
    for gene in genesList: # Find at least one gene containing SNP
        if (SNP[0] == gene[0]): # Both Contig columns need to be the same btwn the 2 files
            if (gene[2] <= int(SNP[1]) <= gene[3]): # If SNP is between start and end of gene [note: the '=' is included bc it's possible for SNPs to be located at the start/end position - although rare]
                # Append contig, snpPosition, Annotation, geneID info from columns
                contig.append(SNP[0])
                snpPosition.append(SNP[1])
                Annotation.append(gene[4])
                geneID.append(gene[1])
                sequence = str(seq_dict[SNP[0]]) # Slice the sequence from the appropriate Contig, depending on first column info for the SNP
                # The particular gene from 5' to 3' is retrieved by slicing through sequence from start to end of gene
                 # Subtract gene start by -1 because python starts read at 0, gene end doesn't need to be subtracted since you need to grab the latter nucleotide
                gene5_3 = (sequence[(int(gene[2])-1):(int(gene[3]))])
                #Figure out which # codon (pos) has SNP: take SNP pos subtract by gene start, divide by 3, gene start needs to be -1 for same reason above
                Length_Start_SNPpos = ((int(SNP[1]))-(int(gene[2])-1))
                SNP_codon_no = Length_Start_SNPpos/3
               #If Length_Start_SNPpos divisible by 3, that means 3rd pos of SNP_codon_no
                if (Length_Start_SNPpos%3 ==0):
                   ## codon_ref_list note:
                   # Retrieve nucleotides of codon by slicing through the gene sequence
                    # Slice to SNP_codon_no^th nucleotide x3 since 3 nu.s/codon, then subtract by 1 because python starts count at 0
                    # This gives you the third nu., so -2 for second nu., and -3 for first nu.
                    # Insert nucleotides into a list so that they can be joined as a single string and manipulated later with the SNP nu.
                   codon_ref_list = [gene5_3[((int(SNP_codon_no))*3)-3], gene5_3[((int(SNP_codon_no))*3)-2], gene5_3[((int(SNP_codon_no))*3)-1]]
                   codon_ref = (''.join(codon_ref_list))
                   AA_ref = codon_dictionary[codon_ref]
                   codon_mod_list= codon_ref_list
                   codon_mod_list[2] = SNP[2] # Change codon_ref by replacing 3rd position of codon with nu. of the SNP
                   codon_mod = (''.join(codon_mod_list))
                   AA_mod = codon_dictionary[codon_mod]
               #If Length_Start_SNPpos + 2 is divisible by 3, that means 1st pos of SNP_codon_no+1
                if ((Length_Start_SNPpos+2)%3 ==0):
                   codon_ref_list = [gene5_3[((int(SNP_codon_no)+1)*3)-3], gene5_3[((int(SNP_codon_no)+1)*3)-2], gene5_3[((int(SNP_codon_no)+1)*3)-1]]
                   codon_ref = (''.join(codon_ref_list))
                   AA_ref = codon_dictionary[codon_ref]
                   codon_mod_list= codon_ref_list
                   codon_mod_list[0] = SNP[2] # Change codon_ref by replacing 1st position of codon with nu. of the SNP
                   codon_mod = (''.join(codon_mod_list))
                   AA_mod = codon_dictionary[codon_mod]
               #If Length_Start_SNPpos + 1 is divisible by 3, that means 2nd pos of SNP_codon_no+1
                if ((Length_Start_SNPpos+1)%3 ==0):
                   codon_ref_list = [gene5_3[((int(SNP_codon_no)+1)*3)-3], gene5_3[((int(SNP_codon_no)+1)*3)-2], gene5_3[((int(SNP_codon_no)+1)*3)-1]]
                   codon_ref = (''.join(codon_ref_list))
                   AA_ref = codon_dictionary[codon_ref]
                   codon_mod_list= codon_ref_list
                   codon_mod_list[1] = SNP[2] # Change codon_ref by replacing 1st position of codon with nu. of the SNP
                   codon_mod = (''.join(codon_mod_list))
                   AA_mod = codon_dictionary[codon_mod]
               # Append Type, ref/mod codon/AA, count syn & non-syn per contig
                if AA_ref == AA_mod:
                   Type.append('Synonymous')
                   if SNP[0] == 'Contig_1':
                       contig1_synonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_2':
                       contig2_synonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_3':
                       contig3_synonymous += 1 # Add 1 to count
                else:
                   Type.append('Non-synonymous')
                   if SNP[0] == 'Contig_1':
                       contig1_nonsynonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_2':
                       contig2_nonsynonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_3':
                       contig3_nonsynonymous += 1 # Add 1 to count
                referenceCodon.append(codon_ref)
                modifiedCodon.append(codon_mod)
                referenceAA.append(AA_ref)
                modifiedAA.append(AA_mod)
                break # In case a SNP is present in more than one gene (based on my analysis however, there is only one SNP in the whole SNP file, in contig3, that is present in 2 genes
    ## Handling the reverse complement SNPs ##
            if (gene[3] <= int(SNP[1]) <= gene[2]): # If SNP is between end and start of gene [note: the '=' is included bc it's possible for SNPs to be located at the start/end position - although rare]
                # Append contig, snpPosition, Annotation, geneID info from columns
                contig.append(SNP[0])
                snpPosition.append(SNP[1])
                Annotation.append(gene[4])
                geneID.append(gene[1])
                sequence = str(seq_dict[SNP[0]]) # Slice the sequence from the appropriate Contig, depending on first column info for the SNP
                # The particular gene from 3' to 5' is retrieved by slicing through sequence from start to end of gene
                    # Subtract gene start by -1 because python starts read at 0, gene end doesn't need to be subtracted since you need to grab the latter nucleotide
                gene3_5 = (sequence[(int(gene[3])-1):(int(gene[2]))])
                gene5_3 = str((Seq(gene3_5)).reverse_complement()) # Reverse complement the gene to get gene seq from 5' to 3'
                #Figure out which # codon (pos) has SNP: take SNP pos, subtract by start of gene, divide by 3, take absolute value since this will be a negative no., gene start needs to be +1 (instead of -1 since this is the reverse strand) for same reason above
                Length_Start_SNPpos = abs(int(SNP[1])-(int(gene[2])+1))
                SNP_codon_no = Length_Start_SNPpos/3
                #If Length_Start_SNPpos_divisible by 3, that means 3rd pos of SNP_codon_no
                if (Length_Start_SNPpos%3 ==0):
                   ## codon_ref_list note:
                   # Retrieve nucleotides of codon by slicing through the gene sequence
                    # Slice to SNP_codon_no^th nucleotide x3 since 3 nu.s/codon, then subtract by 1 because python starts count at 0
                    # This gives you the third nu., so -2 for second nu., and -3 for first nu.
                    # Insert nucleotides into a list so that they can be joined as a single string and manipulated later with the SNP nu.
                   codon_ref_list = [gene5_3[((int(SNP_codon_no))*3)-3], gene5_3[((int(SNP_codon_no))*3)-2], gene5_3[((int(SNP_codon_no))*3)-1]]
                   codon_ref = (''.join(codon_ref_list))
                   AA_ref = codon_dictionary[codon_ref]
                   codon_mod_list= codon_ref_list
                   codon_mod_list[2] = str((Seq(SNP[2]).reverse_complement())) # Change codon_ref by replacing 3rd position of codon with reverse complement of nu. of the SNP
                   codon_mod = (''.join(codon_mod_list))
                   AA_mod = codon_dictionary[codon_mod]
               #If Length_Start_SNPpos + 2 divisible  by 3, that means 1st pos of SNP_codon_no+1
                if ((Length_Start_SNPpos+2)%3 ==0):
                   codon_ref_list = [gene5_3[((int(SNP_codon_no)+1)*3)-3], gene5_3[((int(SNP_codon_no)+1)*3)-2], gene5_3[((int(SNP_codon_no)+1)*3)-1]]
                   codon_ref = (''.join(codon_ref_list))
                   AA_ref = codon_dictionary[codon_ref]
                   codon_mod_list= codon_ref_list
                   codon_mod_list[0] = str((Seq(SNP[2]).reverse_complement())) # Change codon_ref by replacing 1st position of codon with reverse complement of nu. of the SNP
                   codon_mod = (''.join(codon_mod_list))
                   AA_mod = codon_dictionary[codon_mod]
               #If Length_Start_SNPpos + 1 divisible by 3, that means 2nd pos of SNP_codon_no+1
                if ((Length_Start_SNPpos+1)%3 ==0):
                   codon_ref_list = [gene5_3[((int(SNP_codon_no)+1)*3)-3], gene5_3[((int(SNP_codon_no)+1)*3)-2], gene5_3[((int(SNP_codon_no)+1)*3)-1]]
                   codon_ref = (''.join(codon_ref_list))
                   AA_ref = codon_dictionary[codon_ref]
                   codon_mod_list= codon_ref_list
                   codon_mod_list[1] = str((Seq(SNP[2]).reverse_complement())) # Change codon_ref by replacing 1st position of codon with reverse complement of nu. of the SNP
                   codon_mod = (''.join(codon_mod_list))
                   AA_mod = codon_dictionary[codon_mod]
               # Append Type, ref/mod codon/AA, count syn & non-syn per contig
                if AA_ref == AA_mod:
                   Type.append('Synonymous')
                   if SNP[0] == 'Contig_1':
                       contig1_synonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_2':
                       contig2_synonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_3':
                       contig3_synonymous += 1 # Add 1 to count
                else:
                   Type.append('Non-synonymous')
                   if SNP[0] == 'Contig_1':
                       contig1_nonsynonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_2':
                       contig2_nonsynonymous += 1 # Add 1 to count
                   if SNP[0] == 'Contig_3':
                       contig3_nonsynonymous += 1 # Add 1 to count
                referenceCodon.append(codon_ref)
                modifiedCodon.append(codon_mod)
                referenceAA.append(AA_ref)
                modifiedAA.append(AA_mod)
                break # In case a SNP is present in more than one gene

### Make tableOutput.txt ###

# Import numpy for transforming the nested_list
import numpy as np
# Make a nested_list using lists made for tableOutput
nested_list = [contig, snpPosition, Type, Annotation, geneID, referenceCodon, modifiedCodon, referenceAA, modifiedAA]
transformed_nested_list = (np.transpose(nested_list)) # transform nested_list so that each row becomes a column
# Make and write tableOutput.txt using transformed_nested_list
with open('tableOutput - Mouly Rahman.txt', 'w') as file:
    file.writelines('\t'.join((i)) + '\n' for i in transformed_nested_list) # join lines with tabs and a new line

### Make Plot.pdf ###

# Import matplot to make Plot (numpy required as well)
import matplotlib.pyplot as plt
# Set width of bars
barWidth = 0.24
btwn_barWidth = 0.3
# Contig1: nonsyn, syn, intergenic
bar1 = [contig1_nonsynonymous, contig1_synonymous, contig1_intergenic]
# Contig2: nonsyn, syn, intergenic
bar2 = [contig2_nonsynonymous, contig2_synonymous, contig2_intergenic]
# Contig3: nonsyn, syn, intergenic
bar3 = [contig3_nonsynonymous, contig3_synonymous, contig3_intergenic]
# Set regions on x-axis for the 3 groups (nonysyn, syn, intergenic) for each contig
region1 = np.arange(len(bar1))
    # Shift over by length of x (bars), btwn_barWidth for each bar
region2 = [x + btwn_barWidth for x in region1]
    # Shift over 2x by length of x (bars), btwn_barWidth for each bar
region3 = [x + btwn_barWidth for x in region2]
# Plot the bars for each contig 1-3, with colour order of green, red, blue, black outline, and labels that will be used for the legend
plt.bar(region1, bar1, color='green', width=barWidth, edgecolor='black', label='1')
plt.bar(region2, bar2, color='red', width=barWidth, edgecolor='black', label='2')
plt.bar(region3, bar3, color='blue', width=barWidth, edgecolor='black', label='3')
# y-axis label
plt.ylabel('Number of SNPs', size=10)
# graph title
plt.title('Mutation profile', size=10)
# x-axis ticks for each region, or set of bars, fontsize 10, at centre of each region
plt.xticks([tick + btwn_barWidth for tick in range(len(bar1))], ['Non-synonymous', 'Synonymous', 'Intergenic'], size=10)
# add a legend, with title, fontsize and legend size 10
plt.legend(title = 'Contig', loc='upper right', fontsize=10, prop={'size':10})
# Save plot
plt.savefig("Plot - Mouly Rahman.pdf", format="pdf")
# Show plot
plt.show()

### End of script ###
