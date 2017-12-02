# *Heterosigma akashiwo* Genome assembly
According to Roseann Catalico genome size should be approximately half of the human genome or 1500m

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

Species | Genome Size
--------|------------
*Ectocarpus siliculosus* | ~214 Mbp (haploid)
*Volvox* | ~131 Mbp
*Chondrus crispus* | ~105 Mbp
*Chlamydomonas reinhardtii* | ~111 Mbp
*Micromonas* | ~22 Mbp
*Ostreococcus* | ~13 Mbp

Est. Genome Size | Coverage
-----------------|---------
1500 Mbp | 5X
1500 kbp | 5400X
200 Mbp | 40X
175 Mbp | 46X
150 Mbp | 54X
100 Mbp | 80X