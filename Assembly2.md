# *Heterosigma akashiwo* assembly take 2

## Data clean-up
### Bacterial contamination read removal
[Deconseq](http://deconseq.sourceforge.net/) allows mapping of reads to a bacterial database, using their data set.  Default settings were used and removed all reads that mapped at least 80%.
```bash
./deconseq.pl -f ../heterosigma.fasta -dbs bact
mv 1515608796_clean.fa ../heterosigma_bac_clean.fasta
```

### Mapping of chloroplast genome
Bacterial cleaned reads were mapped to [*Heterosigma akashiwo* strain CCMP 452](https://www.ncbi.nlm.nih.gov/nuccore/EU168191.1) using [minimap2](https://github.com/lh3/minimap2).
```bash
rebaler /media/science/heterosigma/organelles/ha_mito.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta --keep > mito_452.fasta
```
```bash
rebaler /media/science/heterosigma/organelles/ha_chloroplast_452.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta --keep > rebaler4.fasta
```
