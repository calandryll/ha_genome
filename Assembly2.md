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

