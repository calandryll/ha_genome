# Heterosimga Genome Assembly

## Genome Assembly

### 150 Mbp Estimated Genome Size

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