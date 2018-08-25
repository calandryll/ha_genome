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

### Removal of contamination reads

```bash
python /media/science/heterosigma/scripts/fasta_cleaner.py /media/science/heterosigma/originals/heterosigma.fasta /media/science/heterosigma/cleanup/bacterial_ids.txt /media/science/heterosigma/originals/heterosigma_cleaned.fasta
python /media/science/heterosigma/scripts/fasta_cleaner.py /media/science/heterosigma/originals/heterosigma.fasta /media/science/heterosigma/cleanup/organelles_ids.txt /media/science/heterosigma/originals/heterosigma_final.fasta
```

## Genome Assembly

### 150 Mbp Estimated Genome Size

Reading discussion on the canu github, several suggestions to make changes for better assembly.  See [#254](https://github.com/marbl/canu/issues/254), [#221](https://github.com/marbl/canu/issues/221), and [FAQ](https://canu.readthedocs.io/en/latest/faq.html#my-assembly-continuity-is-not-good-how-can-i-improve-it).  Based on the Assembled Total Length (bp), an estimated genome size between 110 and 170 Mbp is probably appropriate to use.  Previous attempts at assembly of the genome resulted in missing/non-assembled genes that were verified by qPCR in the transcriptome.  Additionally, increased number of rounds for correction may increase quality [see here](https://canu.readthedocs.io/en/latest/faq.html#what-parameters-should-i-use-for-my-reads).

#### Correction of Reads

```bash
canu \
	-correct \
	-d ha-150-r1 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/originals/heterosigma_final.fasta \
	corMinCoverage=0 \
	corMhapSensitivity=high \
	corOutCoverage=500 \
	genomeSize=150m
```

```bash
canu \
	-correct \
	-d ha-150-r2 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/assemblies/ha-150-r1/heterosigma.correctedReads.fasta.gz \
	corMinCoverage=0 \
	corMhapSensitivity=high \
	corOutCoverage=500 \
	genomeSize=150m
```

```bash
canu \
	-correct \
	-d ha-150-r3 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/assemblies/ha-150-r2/heterosigma.correctedReads.fasta.gz \
	corMinCoverage=0 \
	corMhapSensitivity=high \
	corOutCoverage=500 \
	genomeSize=150m
```

```bash
canu \
	-correct \
	-d ha-150-r4 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/assemblies/ha-150-r3/heterosigma.correctedReads.fasta.gz \
	corMinCoverage=0 \
	corMhapSensitivity=high \
	corOutCoverage=500 \
	genomeSize=150m
```

```bash
canu \
	-correct \
	-d ha-150-r5 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/assemblies/ha-150-r4/heterosigma.correctedReads.fasta.gz \
	corMinCoverage=0 \
	corMhapSensitivity=high \
	corOutCoverage=500 \
	genomeSize=150m
```

#### Assembly from Corrected Reads

```bash
canu \
	-d ha-150 \
	-p heterosigma \
	-pacbio-raw /media/science/heterosigma/assemblies/ha-150-r5/heterosigma.correctedReads.fasta.gz \
	genomeSize=150m \
	minReadLength=500 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=500
```

The above command generated an assembly missing several 'known' genes that were verified via qPCR, i.e. peroxidase, etc.  A decrease in the coverage after trimming may be the cause of this.

```bash
canu \
	-trim-assemble \
	-d ha-150-t1 \
	-p ha-e105 \
	-pacbio-corrected /media/science/heterosigma/assemblies/ha-150/heterosigma.correctedReads.fasta.gz \
	genomeSize=150m \
	minReadLength=500 \
	correctedErrorRate=0.105 \
	corMhapSensitivity=high \
	corMinCoverage=0 \
	corOutCoverage=500
```

* corOutCoverage=100
  * Option to get more correct sequences
* minReadLength=500
  * Minimum read length to be loaded into the assembler
* corMhapSensitivity=high
  * Set the correction Mhap to high
* correctedErrorRate=0.105
  * Increase the error rate for overlaps