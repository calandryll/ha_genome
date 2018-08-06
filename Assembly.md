# Heterosimga Genome Assembly

## Genome Assembly

### 150 Mbp Estimated Genome Size

Reading discussion on the canu github, several suggestions to make changes for better assembly.  See [#254](https://github.com/marbl/canu/issues/254), [#221](https://github.com/marbl/canu/issues/221), and [FAQ](https://canu.readthedocs.io/en/latest/faq.html#my-assembly-continuity-is-not-good-how-can-i-improve-it).  Based on the Assembled Total Length (bp), an estimated genome size between 110 and 170 Mbp is probably appropriate to use.  Previous attempts at assembly of the genome resulted in missing/non-assembled genes that were verified by qPCR in the transcriptome.

Following [Du et al. 2017](https://www.nature.com/articles/ncomms15324), all reads will be used to assemble the genome followed by a clean up using BWA-MEM to remove assembled bacterial contigs.  A general FASTA was created from all available completed genomes from NCBI.

```bash
canu \
	-d ha-150 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma.fasta \
	genomeSize=150m \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=100
```

* corOutCoverage=100
  * Option to get more correct sequences
* minReadLength=500
  * Minimum read length to be loaded into the assembler
* corMhapSensitivity=high
  * Set the correction Mhap to high