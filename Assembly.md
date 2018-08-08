# Heterosimga Genome Assembly

## Bacterial and Organelle Cleanup

Removal of bacterial reads will be carried out by using minimap2 to map to a combined fasta of all assembled bacterial genomes from NCBI.

### Bacterial mapping

```bash
minimap2 -ax map-pb /media/science/databases/bacterial.fasta /media/science/heterosigma/originals/heterosigma.fasta > bacterial_reads.sam
samtools view -ht /media/science/databases/bacterial.fasta.fai bacterial_reads.sam > bacterial_reads_wheader.sam
samtools view -S -F4 bacterial_reads_wheader.sam > bacterial.mapped.sam
cut -f1 bacterial.mapped.sam | sort | uniq > bacterial_ids.txt
```

### Chloroplast and mitochondria mapping

```bash
minimap2 -ax map-pb /media/science/heterosigma/organelles/organelles.fasta /media/science/heterosigma/originals/heterosigma.fasta > organelles_reads.sam
samtools view -S -F4 organelle_reads.sam > organelle.mapped.sam
cut -f1 organelle.mapped.sam | sort | uniq > organelle_ids.txt
```

## Genome Assembly

### 150 Mbp Estimated Genome Size

Reading discussion on the canu github, several suggestions to make changes for better assembly.  See [#254](https://github.com/marbl/canu/issues/254), [#221](https://github.com/marbl/canu/issues/221), and [FAQ](https://canu.readthedocs.io/en/latest/faq.html#my-assembly-continuity-is-not-good-how-can-i-improve-it).  Based on the Assembled Total Length (bp), an estimated genome size between 110 and 170 Mbp is probably appropriate to use.  Previous attempts at assembly of the genome resulted in missing/non-assembled genes that were verified by qPCR in the transcriptome.

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