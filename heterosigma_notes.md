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

## Canu 100 Mbp
```
~/bin/canu/*/bin/canu -correct -d canu-100 -p heterosigma -pacbio-raw originals/heterosigma.fastq genomeSize=110m maxMemory=31
```