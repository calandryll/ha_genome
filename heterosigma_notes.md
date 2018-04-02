# *Heterosigma akashiwo* Genome assembly
According to Roseann Catalico genome size should be approximately half of the human genome or 1500 Mbp

## Software installation
```
sudo apt-get install openjdk-8-jre-headless build-essential gnuplot
git clone https://github.com/marbl/canu.git
cd canu/src
make -j 64
```

## Data acquisition
```
mkdir ~/originals
cd originals
wget --no-check-certificate -i files.txt
```

## Canu usage
```
screen -S canu
~/canu/*/bin/canu genomeSize=1500k -pacbio-raw originals/*.fastq -p heterosigma [heterosigma_default]
```
Used the incorrect genomeSize, should have been 1500m

## Correct canu usage
```
~/canu/*/bin/canu -pacbio-raw ~/originals/*.fastq -p heterosigma genomeSize=1500m minMemory=900
```

## Redoing subread files
```
bash5tools.py --outFilePrefix ha --readType subreads --outType fastq --minReadScore 0.75 m170304_055253_42157_c101187342550000001823278408081750_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha1 --readType subreads --outType fastq --minReadScore 0.75 m170309_223211_42157_c101187412550000001823278408081753_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha2 --readType subreads --outType fastq --minReadScore 0.75 m170310_045026_42157_c101187412550000001823278408081754_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha3 --readType subreads --outType fastq --minReadScore 0.75 m170310_110930_42157_c101187412550000001823278408081755_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha4 --readType subreads --outType fastq --minReadScore 0.75 m170310_172852_42157_c101187412550000001823278408081756_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha5 --readType subreads --outType fastq --minReadScore 0.75 m170412_080127_42157_c101187522550000001823244205011707_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha6 --readType subreads --outType fastq --minReadScore 0.75 m170412_143440_42157_c101182882550000001823244205011700_s1_p0.bas.h5
bash5tools.py --outFilePrefix ha7 --readType subreads --outType fastq --minReadScore 0.75 m170412_210519_42157_c101182882550000001823244205011701_s1_p0.bas.h5
cat ha* > ../heterosigma.fastq
```

## Celera Assembler
```
PBcR -length 500 -partitions 200 -l heterosigma -s ha.spec -fastq ../originals/heterosigma.fastq genomeSize=1500000000
```
After examining the results from the 1500 Mbp, I think the correct estimated genome size is ~150 Mbp.  See [genome sizes](https://github.com/calandryll/ha_genome/blob/master/genome_size.md) for estimated genome sizes of other organisms.  A closely related species (*Ectocarpus siliculosus*) has approximately 200 Mbp for its genome size.  Being a multicellular organism, it can be assumed that *H. akashiwo*, a single cellular organism, would have a smaller genome size.  Looking at other single celled organisms shows a similar size of 100-150 Mbp.

## Canu Re-run
```
~/bin/canu/*/bin/canu -d canu -p heterosigma -pacbio-raw originals/heterosigma.fastq genomeSize=150m minMemory=24
```

## Higher Correction
```
~/bin/canu/*/bin/canu -d canu-high -p heterosigma -pacbio-raw originals/heterosigma.fastq genomeSize=150m corMhapSensitivity=high corMinCoverage=0 corOutCoverage=100
```

Between the two runs, low number of contigs 6744 and 3553 respecitively.  Compared to number of contigs generated via the transcriptome these seem low.  Additionally related organisms have closer to the number of contigs as derived by the transcriptome.  Will try a genome size of 100 Mbp as well as MECAT.

## MECAT
### Mapping and overlapping of reads
```
mecat2pw -j 0 -d originals/heterosigma.fastq -o mecat/heterosigma.fastq.pm.can -w tmp -t 4
```
### Correct Noisy Reads
```
mecat2cns -i 0 -t 4 mecat/heterosigma.fastq.pm.can originals/heterosigma.fastq mecat/corrected_heterosigma.fasta
```
### Extract high coverage of reads
```
extract_sequences mecat/corrected_heterosigma.fasta mecat/corrected_heterosigma_25x 150000000 25
extract_sequences mecat/corrected_heterosigma.fasta mecat/corrected_heterosigma_40x 150000000 40
```
All files are identical, not sure if step is needed.

### Assemble Reads
```
mecat2canu -trim-assemble -p heterosigma -d mecat genomeSize=150m ErrorRate=0.02 maxMemory=31 maxThreads=4 Overlapper=mecat2asmpw -pacbio-corrected mecat/corrected_heterosigma.fasta
```
Low number of assembled contigs.  Perhaps from issues with coverage?  Will try assembly with canu at 110 Mbp to see if that improves.

## Canu 110 Mbp
```
~/bin/canu/*/bin/canu -correct -d canu-110 -p heterosigma -pacbio-raw originals/heterosigma.fastq genomeSize=110m maxMemory=31
```

## Canu 75 Mbp
```
~/bin/canu/*/bin/canu -correct -d canu-75 -p heterosigma -pacbio-raw originals/heterosigma.fastq genomeSize=75m maxMemory=31
~/bin/canu/*/bin/canu -trim -d canu-75 -p heterosigma -pacbio-corrected canu-75/heterosigma.correctedReads.fasta.gz genomeSize=75m maxMemory=31
~/bin/canu/*/bin/canu -assemble -d canu-75 -p heterosigma -pacbio-corrected canu-75/heterosigma.trimmedReads.fasta.gz genomeSize=75m maxMemory=31 correctedErrorRate=0.105
~/bin/canu/*/bin/canu -assemble -d canu-75 -p heterosigma -pacbio-corrected canu-75-standard/heterosigma.trimmedReads.fasta.gz genomeSize=75m maxMemory=31
```

## Begin alignment and polishing
```
bax2bam m170304_055253_42157_c101187342550000001823278408081750_s1_p0.1.bax.h5 m170304_055253_42157_c101187342550000001823278408081750_s1_p0.2.bax.h5 m170304_055253_42157_c101187342550000001823278408081750_s1_p0.3.bax.h5 -o m170304_055253_42157_c101187342550000001823278408081750_s1_p0
pbalign --tmpDir=tmp --minAccuracy=0.75 --minLength=50 --minAnchorSize=12 --maxDivergence=30 --concordant --algorithm=blasr --algorithmOptions=--useQuality --maxHits=1 --hitPolicy=random --seed=1 --nproc=4 originals/bas/m170304_055253_42157_c101187342550000001823278408081750_s1_p0.subreads.bam canu/heterosigma.contigs.fasta ha.aln.bam
bamtools stats -in ha.aln.bam
**********************************************
Stats for BAM file(s):
**********************************************

Total reads:       135818
Mapped reads:      135818       (100%)
Forward strand:    67489        (49.6908%)
Reverse strand:    68329        (50.3092%)
Failed QC:         0    (0%)
Duplicates:        0    (0%)
Paired-end reads:  0    (0%)
samtools sort ha.aln.bam -o ha.sorted.bam
samtools index ha.sorted.bam ha.index
samtools faidx canu/heterosigma.contigs.fasta
arrow -j 4 --log-file arrow.log -r canu/heterosigma.contigs.fasta -o polish/canu_polished.fasta ha.aln.bam
arrow -j 4 --log-file arrow.log -r canu-high/heterosigma.contigs.fasta -o polish/canu-high_polished.fasta ha.aln.bam
arrow -j 4 --log-file arrow.log -r canu-75/heterosigma.contigs.fasta -o polish/canu-75_polished.fasta ha.aln.bam
```

## Canu using highest generated reads

```
~/bin/canu/*/bin/canu -d ha -p heterosigma -pacbio-raw originals/heterosigma_2.fastq genomeSize=150m minMemory=24
```

## [Racon](https://github.com/isovic/racon)
Adapted from [here](https://inf-biox121.readthedocs.io/en/2017/index.html)
### Overlapping with minimap
```
~/bin/racon/tools/minimap/minimap -Sw5 -L100 -m0 -t4 ../originals/heterosigma_2.fastq ../originals/heterosigma_2.fastq | gzip -1 > heterosigma_2.paf.gz
```
*Note:* During mapping, reads are mapped against themselves, hence being in the command twice.

### Assembly with miniasm
```
~/bin/racon/tools/miniasm/miniasm -f ../originals/heterosigma_2.fastq heterosigma_2.paf.gz > heterosigma_2.gfa
```
Convert GFA to fasta file:
```
awk '/^S/{print ">"$2"\n"$3}' heterosigma_2.gfa | fold > heterosigma.raw_assembly.fasta
```

### Correction with Racon
Map original reads against raw assembly:
```
~/bin/racon/tools/minimap/minimap heterosigma.raw_assembly.fasta ../originals/heterosigma_2.fastq > heterosigma.raw_assembly.reads_mapped.paf
```

Correcting with racon:
```
~/bin/racon/bin/racon -t 4 ../originals/heterosigma_2.fastq heterosigma.raw_assembly.reads_mapped.paf heterosigma.raw_assembly.fasta heterosigma.corrected.fasta
```
Very few contigs produced.

## Canu at 55 Mbp
```
~/bin/canu/*/bin/canu -d ha-55 -p heterosigma -pacbio-raw originals/heterosigma.fastq genomeSize=55m minMemory=24
```

## Current thoughts
It seems all assembly attempts, except RACON, make a chloroplast and mitochrondria genome for *Heterosigma* (~187,000 and ~37,000 bp).  Removing those reads from the assembly should yield a better assembly for the genome.  Data from Roseann Catalico will be used to remove those reads from the data (CCMP452, isolated Long Island Sound).

### Chloroplast removal
```
~/bin/Organelle_PBA/OrganelleRef_PBA -i /media/science/heterosigma/originals/heterosigma.fastq -r /media/science/heterosigma/organelles/ha_chloroplast.fasta -o /media/science/heterosigma/chloro_out
```

### Mitochonrida removal
```
~/bin/Organelle_PBA/OrganelleRef_PBA -i /media/science/heterosigma/originals/heterosigma.fastq -r /media/science/heterosigma/organelles/ha_mito.fasta -o /media/science/heterosigma/mito_out
```

Entire reads that mapped to the organelles were removed with the organelle_strip.py  Assembly at 150 Mbp will be attempted again with the cleaned data.

## Canu with Cleaned reads
```
~/bin/canu/*/bin/canu -d ha-150 -p heterosigma -pacbio-raw originals/heterosigma_cleaned.fasta genomeSize=150m minMemory=24
```

## Removal of bacterial contamination
Contigs from ha-150 will be blasted and results will be examined for bacterial contamination.  Any contigs will then be aligned using blasr against the reads and removed.  Organelles will be run again using Organelle_PBA to ensure no bacterial reads contaminated those assemblies, i.e. ~26,000 insert.

[Deconseq](http://deconseq.sourceforge.net/) allows mapping of reads to a bacterial database, using their data set.  Default settings were used and removed all reads that mapped at least 80%.
```
./deconseq.pl -f ../heterosigma.fasta -dbs bact
mv 1515608796_clean.fa ../heterosigma_bac_clean.fasta
```
## Chloroplast assembly
```
~/bin/Organelle_PBA/OrganelleRef_PBA -i /media/science/heterosigma/originals/heterosigma_bac_clean.fasta -r /media/science/heterosigma/organelles/ha_chloroplast_452.fasta -o /media/science/heterosigma/chloro_out -t fasta
```

```
~/bin/canu/*/bin/canu -d ha-150-cor80 -p heterosigma -pacbio-raw originals/heterosigma_cleaned.fasta genomeSize=150m minMemory=24 corOutCoverage=80 corMhapSensitivity=normal
```
Will need cleaning ever further for assembly