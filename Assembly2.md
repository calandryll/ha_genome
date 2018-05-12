# *Heterosigma akashiwo* assembly take 2

## Data clean-up
### Bacterial contamination read removal
[Deconseq](http://deconseq.sourceforge.net/) allows mapping of reads to a bacterial database, using their data set.  Default settings were used and removed all reads that mapped at least 80%.
```bash
./deconseq.pl -f ../heterosigma.fasta -dbs bact
mv 1515608796_clean.fa ../heterosigma_bac_clean.fasta
```

### Mapping of chloroplast genome
Bacterial cleaned reads were mapped to [*Heterosigma akashiwo* strain CCMP 452](https://www.ncbi.nlm.nih.gov/nuccore/EU168191.1) using [Rebaler](https://github.com/rrwick/Rebaler).  See [chloroplast assembly notes](https://github.com/calandryll/ha_genome/blob/master/chloroplast_assembly.md) or [mitochondria assembly notes](https://github.com/calandryll/ha_genome/blob/master/mito_assembly.md) for more information.

#### Removing reads
Reads associated with organelle assemblies, NIES293, were removed from **heterosigma_bac_clean.fasta** using [fasta_cleaner.py](https://github.com/calandryll/ha_genome/blob/master/scripts/fasta_cleaner.py).
```bash
python scripts/fasta_cleaner.py originals/heterosigma_bac_clean.fasta assemblies/mito/temp_rebaler_14091/02_1_alignments.paf originals/heterosigma_wout_bac_mito.fasta
```

```bash
python scripts/fasta_cleaner.py originals/heterosigma_wout_bac_mito.fasta assemblies/chloroplast/temp_rebaler_27405/02_1_alignments.paf originals/heterosigma_wout_bac_organelles.fasta
```


A total of 52,255 reads were removed from **heterosigma.fasta** for all data clean-up.

## Genome Assembly
[canu](https://github.com/marbl/canu) was updated to 1.7 before being run.

### 150 Mbp Estimated Genome Size
```bash
canu \
	-d ha-150-cor80 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=150m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```
A minimum read length of 500 was added to decrease the number of reads tossed from analysis, from ~9% to ~3%.

### 110 Mbp Estimated Genome Size
```bash
canu \
	-d ha-110-cor80 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=110m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 300 Mbp Estimated Genome Size
```bash
canu \
	-d ha-300-cor80 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=300m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 350 Mbp Estimated Genome Size
```bash
canu \
	-d ha-350-cor80 \
	-p heterosigma \
	-pacbio-raw /medi/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=350m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 375 Mbp Estimated Genome Size
```bash
canu \
	-d ha-375-cor80 \
	-p heterosigma \
	-pacbio-raw /medi/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=375m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 400 Mbp Estimated Genome Size
```bash
canu \
	-d ha-400-cor80 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=400m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 500 Mbp Estimated Genome Size
```bash
canu \
	-d ha-500-cor80 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=500m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 1500 Mbp Estimated Genome Size
```bash
canu \
	-d ha-1500-cor80 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=1500m \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### 375 Mbp Estimated Genome Size
```bash
canu \
	-d ha-375-cor100 \
	-p heterosigma \
	-pacbio-raw /medi/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=375m \
	corOutCoverage=100 \
	corMhapSensitivity=normal \
	minReadLength=500
```

### Assembly Statistics

| Assembly      | # of Contigs |  N50   | Longest Contig | Est. Genome Size |
|:--------------|:------------:|:------:|:--------------:|-----------------:|
| Ha-110-cor80  |    14,429    | 12,093 |     94,712     |          110 Mbp |
| Ha-150-cor80  |    14,429    | 12,093 |     94,712     |          150 Mbp |
| Ha-300-cor80  |    14,406    | 12,096 |     94,712     |          300 Mbp |
| Ha-350-cor80  |    14,405    | 12,096 |     94,712     |          350 Mbp |
| Ha-375-cor80  |    17,111    | 14,378 |    108,460     |          375 Mbp |
| Ha-400-cor80  |    17,111    | 14,378 |    108,460     |          400 Mbp |
| Ha-500-cor80  |    17,111    | 14,378 |    108,460     |          500 Mbp |
| Ha-1500-cor80 |    17,103    | 14,378 |    108,460     |         1500 Mbp |

### Assembly Statistics

| Run           | Assembled<br> Contigs | Assembled<br>Total Length (bp) | Unassembled<br> Contigs | Unassembled<br>Total Length (bp) |
|:--------------|:---------------------:|:------------------------------:|:-----------------------:|:--------------------------------:|
| Ha-110-cor80  |        14,429         |          117,019,216           |         226,606         |           815,546,757            |
| Ha-150-cor80  |        14,429         |          117,019,214           |         226,606         |           815,546,757            |
| Ha-300-cor80  |        14,406         |          116,912,066           |         226,610         |           815,719,009            |
| Ha-350-cor80  |        14,405         |          116,910,303           |         226,611         |           815,751,413            |
| Ha-375-cor80  |        17,111         |          167,636,982           |         271,448         |          1,067,751,062           |
| Ha-400-cor80  |        17,111         |          167,636,982           |         271,448         |          1,067,751,062           |
| Ha-500-cor80  |        17,111         |          167,634,515           |         271,448         |          1,067,751,062           |
| Ha-1500-cor80 |        17,103         |          167,632,582           |         271,551         |          1,067,964,418           |

### 120 Mb Estimate Genome Size
Reading discussion on the canu github, several suggestions to make changes for better assembly.  See [#254](https://github.com/marbl/canu/issues/254), [#221](https://github.com/marbl/canu/issues/221), and [FAQ](https://canu.readthedocs.io/en/latest/faq.html#my-assembly-continuity-is-not-good-how-can-i-improve-it).  Based on the Assembled Total Length (bp), an estimated genome size between 110 and 170 Mbp is probably appropriate to use.

```bash
canu \
	-d ha-120 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=120m \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=100
```

A test run using all reads at 150 Mbp.  Trying to increase the size of the mitochondrial assembly, now that I know what to look for and do afterwards.
```bash
canu \
	-d ha-150-2 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_bac_clean.fasta \
	genomeSize=150m \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=100
```
Keeping the chloroplast reads in the original file may lead to excluding some of the known primers from the transcriptome.  A test at 150 Mbp without the chloroplast but including the mitochondria reads will be tested.
```bash
canu \
	-d ha-150-3 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_chloroplast.fasta \
	genomeSize=150m \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=100
```

### 150 Mbp 
Keeping any organelle reads within the original files seems to create several contigs for the 18S/ribosomal structure, in addition exclude the Glutathione Peroxidase gene.
```bash
canu \
	-d ha-150-4 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.fasta \
	genomeSize=150m \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=100
```

| Assembly                             | # of Contigs |   NG50/N50    | Longest Contig | Est. Genome Size |
|:-------------------------------------|:------------:|:-------------:|:--------------:|-----------------:|
| Ha-120<sup>[1](#myfootnote1)</sup>   |    15,760    | 15,708/13,551 |    124,956     |          120 Mbp |
| Ha-150-2<sup>[2](#myfootnote2)</sup> |    15,706    | 12,836/13,410 |    189,811     |          150 Mbp |
| Ha-150-3<sup>[3](#myfootnote3)</sup> |    15,936    | 13,108/13,503 |    105,178     |          150 Mbp |
| Ha-150-4<sup>[4](#myfootnote4)</sup> |    15,837    | 13,080/13,512 |     99,628     |          150 Mbp |



## Organelle Assembly using [canu](https://github.com/marbl/canu)
Reads selected during test assembly using [Rebaler](https://github.com/rrwick/Rebaler) were used for assembly using canu.

```bash
canu \
	-d ha-chloro \
	-p chloroplast \
	-pacbio-raw /media/science/heterosigma/originals/chloroplast_reads.fasta \
	genomeSize=160000 \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=100
```
For the chloroplast reads: Out of 43517 reads, 43111 are greater than 250 bp, 41862 are greater than 500 bp.

```bash
canu \
	-d ha-mito \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/mito_reads.fasta \
	genomeSize=38690 \
	corOutCoverage=80 \
	corMhapSensitivity=normal \
	minReadLength=500
```
Only 8 reads less than 500 bp.

| Assembly | Assembly Size | Median Assembly Size | N50 |
| -------- | :-----------: | :------------------: | :-: |
| ha-chloro | 187,350 | 159,918 | 187,350 |
| ha-mito | 35,951 | 38,690 | 35,951 |

In the [canu](https://canu.readthedocs.io/en/latest/faq.html#my-circular-element-is-duplicated-has-overlap) FAQ, for overlap for circular constructs to user MUMmer.

#### Chloroplast Overlap

```bash
nucmer -maxmatch -nosimplify heterosigma.contigs.fasta heterosigma.contigs.fasta
show-coords -lrcTH out.delta
```

The first 27,929 bp will be removed from the contig.


### Polishing of Genome
Bax files for each run were merged into a single bam file.
```bash
bamtools merge -in ha.subreads.bam -in ha1.subreads.bam -in ha2.subreads.bam -in ha3.subreads.bam -in ha4.subreads.bam -in ha5.subreads.bam -in ha6.subreads.bam -out heterosigma.bam
```

Reads associated with bacteria and organelles were filtered from the combined bam file.
```bash
samtools view -h bas/heterosigma.bam | grep -vf bac_mito_chloro_reads.txt | samtools view -bS -o heterosigma_wout_bac_organelles.bam -
```

#### Align using pbalign
```bash
pbalign /media/science/heterosigma/originals/heterosigma_wout_bac_organelles.bam /media/science/heterosigma/assemblies/fasta/ha-375-cor80.fasta heterosigma_aligned.bam --nproc 24
```

#### Polishing using arrow
```bash
arrow align/heterosigma_aligned.bam -r /media/science/heterosigma/assemblies/fasta/ha-375-cor80.fasta -o ha-375-consensus.fasta -o ha-375-variants.gff -j 24
```

## Validation of Genome Assembly
Validation will be done using Benchmarking Universal Single-Copy Orthologs ([BUSCO](http://busco.ezlab.org/)) and Quality Assessment Tool for Genome Assemblies ([QUAST](http://quast.sourceforge.net/quast)), using Ha-375-consensus files.

### BUSCO

```bash
busco \
	-i ../fasta/ha-375-consensus.fasta \
	-o eukaryotes \
	-m geno \
	-l /media/science/busco/eukaryota_odb9 \
	-c 20 \
	--long
```

Approximately 3% are complete for the eukaryotic data set.  Running the assembled transcriptome (14,025 contigs) yields 45.8% complete, or the MMETSP0292 transcriptome assembly (30,419 contigs) is 54.8% complete.

### QUAST
```bash
quast -o quast -t 24 ../polishing/ha-375-consensus.fasta -e -f --glimmer
quast -o quast_gm -t 24 ../polishing/ha-375-consensus.fasta -e -f
```

## Annotation
Assembly from the [transcriptome project](https://github.com/calandryll/transcriptome2) were used to aid in annotation of the genome (N50: 1399, # of contigs: 14025).  Additionally the current release (2018_03) of the [Uniprot/Swiss-Prot](http://www.uniprot.org/) database was used.

```bash
cat Control_2_unmapped.fastq Control_3_unmapped.fastq Control_4_unmapped.fastq > Control_unmapped.fastq
seqtk seq -A Control_unmapped.fastq > Control_unmapped.fasta
```

### Footnotes
<a name="myfootnote1">1</a>: Missing Plasma membrane permase and glutathione peroxidase.

<a name="myfootnote2">2</a>: Missing glutathione peroxidase.

<a name="myfootnote3">3</a>: Missing Plasma membrane permase and glutathione peroxidase.

<a name="myfootnote4">4</a>: Missing Plasma membrane permase and glutathione peroxidase.
