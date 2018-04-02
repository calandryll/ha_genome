## Mitochondria assembly from bacterial cleaned reads using [Rebaler](https://github.com/rrwick/Rebaler)

| Strain | Mitochondria Size | Mapped Size | Mapping Quality |
| ------ | ---------------- | ----------- | --------------- |
| **Strain Y** | 38,690 | 39,364 | 10,643,447 |
| **CCMP452** | 38,724 | 39,058 | 10,507,179 |
| **NIES293** | 38,641 | 39,004 | 10,258,881 |


### Strain Y
```bash
rebaler --keep /media/science/heterosigma/organelles/AB546637.2.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > AB546637.fasta
```


Loading reference (2018-04-02 19:08:35)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular   Length
AB546637.2         yes        38,690


Building unpolished assembly (2018-04-02 19:08:35)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the corresponding read sequence. This creates an unpolished assembly made directly
from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 3,135 initial alignments
Culling alignments to a non-redundant set... 5 alignments remain

Constructing unpolished assembly:

AB546637.2:
309_223211_42157_c101187412550000001823278408081753_s1_p0/118583/0_11246(+):0-10882 → 304_055253_42157_c101187342550000001823278408081750_s1_p0/25087/19940_49075(-):6583-7026 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/48048/17590_32289(+):3-6101 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/101089/29977_44828(+):0-8948 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/36239/0_15573(+):0-12993


Polishing assembly (2018-04-02 19:09:24)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between rounds such that all parts (including the ends) are polished well. Assembly
quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin          39,364       10,643,447

Best polish: temp_rebaler_11866/01_unpolished_assembly.fasta

### CCMP452
```bash
rebaler --keep /media/science/heterosigma/organelles/ha_mito.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > GQ222228.fasta
```


Loading reference (2018-04-02 19:19:59)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular   Length
GQ222228.1         yes        38,724


Building unpolished assembly (2018-04-02 19:19:59)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the corresponding read sequence. This creates an unpolished assembly made directly
from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 3,166 initial alignments
Culling alignments to a non-redundant set... 2 alignments remain

Constructing unpolished assembly:

GQ222228.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/7159/0_18572(-):0-18362 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/40183/0_25495(+):1140-21836


Polishing assembly (2018-04-02 19:20:48)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between rounds such that all parts (including the ends) are polished well. Assembly
quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin          39,058       10,507,179

Best polish: temp_rebaler_17635/01_unpolished_assembly.fasta

### NIES293
```bash
rebaler --keep /media/science/heterosigma/organelles/GQ22227.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > GQ22227.fasta
```


Loading reference (2018-04-02 19:16:12)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular   Length
GQ222227.1         yes        38,641


Building unpolished assembly (2018-04-02 19:16:12)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the corresponding read sequence. This creates an unpolished assembly made directly
from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 3,138 initial alignments
Culling alignments to a non-redundant set... 4 alignments remain

Constructing unpolished assembly:

GQ222227.1:
412_080127_42157_c101187522550000001823244205011707_s1_p0/94965/0_14503(-):0-12970 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/118733/0_14549(-):12114-14459 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/73474/36266_39840(-):0-1856 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/40183/0_25495(+):0-21833


Polishing assembly (2018-04-02 19:17:01)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between rounds such that all parts (including the ends) are polished well. Assembly
quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin          39,004       10,258,881

Best polish: temp_rebaler_14091/01_unpolished_assembly.fasta