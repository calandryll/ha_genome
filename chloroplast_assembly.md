## Chloroplast assembly from bacterial cleaned reads using [Rebaler](https://github.com/rrwick/Rebaler)

### LC269918.1 (CCAP934/8)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269918.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269918.fasta
```


Loading reference (2018-04-02 13:59:18)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269918.1         yes        159,918


Building unpolished assembly (2018-04-02 13:59:18)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 75,682 initial alignments
Culling alignments to a non-redundant set... 16 alignments remain

Constructing unpolished assembly:

LC269918.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6398 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-6618 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/102631/0_12944(-):0-10714 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/19
237_38473(-):0-15771 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/146482/0_18009(-):0-7502 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/
138367/17801_35232(-):7539-8095 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/116437/30642_39221(+):6-3590 → 309_223211_42157_c1011874125500000018232784
08081753_s1_p0/81449/5990_27610(-):0-21618 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):279-11125 → 412_210519_42157_c101182882550
000001823244205011701_s1_p0/34889/258_15536(+):0-7758 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/152045/0_18060(-):0-18045 → 310_045026_42157_c101187
412550000001823278408081754_s1_p0/33103/0_21658(+):6523-6846 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/10949/0_22859(-):0-22852 → 412_210519_42157_c
101182882550000001823244205011701_s1_p0/38064/0_13433(+):2490-13418 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/129738/15199_25230(-):326-8506 → 412_2
10519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):0-13982


Polishing assembly (2018-04-02 14:02:34)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         161,074      247,985,853

Best polish: temp_rebaler_12664/01_unpolished_assembly.fasta

### LC269919.1 (EHUSP01)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269919.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269919.fasta
```


Loading reference (2018-04-02 14:04:41)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269919.1         yes        160,150


Building unpolished assembly (2018-04-02 14:04:41)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 72,714 initial alignments
Culling alignments to a non-redundant set... 13 alignments remain

Constructing unpolished assembly:

LC269919.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6398 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-6618 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/102631/0_12944(-):0-10714 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/19
237_38473(-):0-19173 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/40983/0_23063(-):0-23060 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/
152434/2972_16447(-):4397-13448 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):2009-10057 → 412_080127_42157_c1011875225500000018232
44205011707_s1_p0/84060/16361_32557(+):0-16192 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/9764/0_23163(-):7376-11685 → 310_045026_42157_c101187412550
000001823278408081754_s1_p0/33103/0_21658(+):0-19659 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 310_172852_42157_c1011874
12550000001823278408081756_s1_p0/52963/0_13762(-):1739-13328 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):0-13982


Polishing assembly (2018-04-02 14:08:01)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         161,359      258,689,686

Best polish: temp_rebaler_14177/01_unpolished_assembly.fasta

### LC269920.1 (CCAP934/4)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269920.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269920.fasta
```


Loading reference (2018-04-02 14:10:05)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269920.1         yes        160,099


Building unpolished assembly (2018-04-02 14:10:05)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 72,735 initial alignments
Culling alignments to a non-redundant set... 13 alignments remain

Constructing unpolished assembly:

LC269920.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6398 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-6618 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/102631/0_12944(-):0-10714 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/19
237_38473(-):0-19173 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/40983/0_23063(-):0-23060 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/
81449/5990_27610(-):14389-21618 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):279-10057 → 412_080127_42157_c10118752255000000182324
4205011707_s1_p0/84060/16361_32557(+):0-16192 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/9764/0_23163(-):7376-11685 → 310_045026_42157_c1011874125500
00001823278408081754_s1_p0/33103/0_21658(+):0-19659 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 310_172852_42157_c10118741
2550000001823278408081756_s1_p0/52963/0_13762(-):1739-13328 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):0-13981


Polishing assembly (2018-04-02 14:13:28)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         161,266      256,062,343

Best polish: temp_rebaler_15892/01_unpolished_assembly.fasta

### LC269921.1 (CCMP2274)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269921.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269921.fasta
```


Loading reference (2018-04-02 14:16:09)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269921.1         no         159,321


Building unpolished assembly (2018-04-02 14:16:09)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                              1,001,732 reads
Aligning reads to reference with minimap2... 75,577 initial alignments
Culling alignments to a non-redundant set... 18 alignments remain

Constructing unpolished assembly:

LC269921.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6398 → 412_080127_42157_c101187522550000001823244205011707_s1_p0/123087/8210_15491(-
):1203-7030 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/86788/0_16742(-):0-7013 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/1923
7_38473(-):0-15771 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/92126/0_22157(-):0-7337 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/987
26/22733_27155(-):3786-4375 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/116437/30642_39221(+):0-29 → 412_080127_42157_c1011875225500000018232442050117
07_s1_p0/137065/0_18202(+):0-16256 → 412_080127_42157_c101187522550000001823244205011707_s1_p0/116787/15387_30485(+):4743-15096 → 310_172852_42157_c101187412550000001
823278408081756_s1_p0/106717/2268_18968(+):2060-14434 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/131451/0_12232(-):0-12228 → 412_143440_42157_c101182
882550000001823244205011700_s1_p0/152045/0_18060(-):6789-18045 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/33103/0_21658(+):6523-12209 → 412_080127_42
157_c101187522550000001823244205011707_s1_p0/114951/0_20251(-):0-20192 → 412_080127_42157_c101187522550000001823244205011707_s1_p0/131578/18813_22353(+):0-3465 → 309_
223211_42157_c101187412550000001823278408081753_s1_p0/6741/13889_19136(+):3354-5245 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/42575/24599_37285(-):1
283-8912 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/76476/0_17904(+):0-17265


Polishing assembly (2018-04-02 14:19:30)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         161,559      258,421,150

Best polish: temp_rebaler_17565/01_unpolished_assembly.fasta

### LC269922.1 (CCMP3374)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269922.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269922.fasta
```


Loading reference (2018-04-02 14:22:32)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269922.1         yes        160,152


Building unpolished assembly (2018-04-02 14:22:32)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 72,735 initial alignments
Culling alignments to a non-redundant set... 13 alignments remain

Constructing unpolished assembly:

LC269922.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6398 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-6618 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/102631/0_12944(-):0-10714 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/19
237_38473(-):0-19173 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/40983/0_23063(-):0-23060 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/
152434/2972_16447(-):4397-13448 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):2009-10057 → 412_080127_42157_c1011875225500000018232
44205011707_s1_p0/84060/16361_32557(+):0-16192 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/9764/0_23163(-):7376-23153 → 310_045026_42157_c101187412550
000001823278408081754_s1_p0/33103/0_21658(+):11368-19659 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 310_172852_42157_c101
187412550000001823278408081756_s1_p0/52963/0_13762(-):1739-13328 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):0-13982


Polishing assembly (2018-04-02 14:25:52)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         161,459      258,400,840

Best polish: temp_rebaler_19305/01_unpolished_assembly.fasta

### LC269923.1 (HaFk01)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269923.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269923.fasta
```


Loading reference (2018-04-02 14:28:14)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269923.1         yes        159,492


Building unpolished assembly (2018-04-02 14:28:14)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 75,569 initial alignments
Culling alignments to a non-redundant set... 16 alignments remain

Constructing unpolished assembly:

LC269923.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6398 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-10089 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/86788/0_16742(-):0-15246 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/19
237_38473(-):8247-15771 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/92126/0_22157(-):0-7337 → 310_110930_42157_c101187412550000001823278408081755_s1_p
0/98726/22733_27155(-):3786-4375 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/116437/30642_39221(+):0-29 → 412_080127_42157_c10118752255000000182324420
5011707_s1_p0/137065/0_18202(+):0-16256 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/67094/21689_43421(-):10525-21732 → 310_172852_42157_c1011874125500
00001823278408081756_s1_p0/30411/40909_54026(+):2383-11125 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/34889/258_15536(+):0-7758 → 412_143440_42157_c1
01182882550000001823244205011700_s1_p0/152045/0_18060(-):0-18045 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/33103/0_21658(+):6523-19659 → 309_223211_
42157_c101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/52963/0_13762(-):1739-10438 → 
412_143440_42157_c101182882550000001823244205011700_s1_p0/76476/0_17904(+):0-17264


Polishing assembly (2018-04-02 14:31:35)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         160,885      266,454,879

Best polish: temp_rebaler_20926/01_unpolished_assembly.fasta

### LC269924.1 (CCMP1596)
```bash
rebaler --keep /media/science/heterosigma/organelles/LC269924.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > LC269924.fasta
```


Loading reference (2018-04-02 14:33:41)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
LC269924.1         yes        159,691


Building unpolished assembly (2018-04-02 14:33:41)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 72,405 initial alignments
Culling alignments to a non-redundant set... 13 alignments remain

Constructing unpolished assembly:

LC269924.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/134439/13083_26108(-):0-5545 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):3761-9489 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/110779/0_9830(-):0-7562 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/1923
7_38473(-):0-19173 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/40983/0_23063(-):0-23060 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/13
5258/17310_34545(+):8675-17230 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):1978-10057 → 412_080127_42157_c10118752255000000182324
4205011707_s1_p0/84060/16361_32557(+):0-16192 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/9764/0_23163(-):7376-23153 → 310_045026_42157_c1011874125500
00001823278408081754_s1_p0/33103/0_21658(+):11368-19659 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 310_172852_42157_c1011
87412550000001823278408081756_s1_p0/52963/0_13762(-):1739-13328 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):0-14105


Polishing assembly (2018-04-02 14:37:01)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         160,823      262,937,606

Best polish: temp_rebaler_22537/01_unpolished_assembly.fasta

### EU168191.1 (CCMP452)
```bash
rebaler /media/science/heterosigma/organelles/ha_chloroplast_452.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta --keep > ha_2393_chloroplast.fasta
```


Loading reference (2018-04-02 13:01:10)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
EU168191.1         yes        160,149


Building unpolished assembly (2018-04-02 13:01:10)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 72,723 initial alignments
Culling alignments to a non-redundant set... 13 alignments remain

Constructing unpolished assembly:

EU168191.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6397 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-6618 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/102631/0_12944(-):0-10714 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/19
237_38473(-):0-19173 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/40983/0_23063(-):0-23060 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/
152434/2972_16447(-):4397-13448 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):2009-10057 → 412_080127_42157_c1011875225500000018232
44205011707_s1_p0/84060/16361_32557(+):0-16192 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/9764/0_23163(-):7376-11685 → 310_045026_42157_c101187412550
000001823278408081754_s1_p0/33103/0_21658(+):0-19659 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 310_172852_42157_c1011874
12550000001823278408081756_s1_p0/52963/0_13762(-):1739-13328 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):0-13982


Polishing assembly (2018-04-02 13:04:30)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         161,358      258,688,376

Best polish: temp_rebaler_28661/01_unpolished_assembly.fasta

### EU168190.1 (NIES293)
```bash
rebaler --keep /media/science/heterosigma/organelles/EU168190.1.fasta /media/science/heterosigma/originals/heterosigma_bac_clean.fasta > EU168190.fasta
```


Loading reference (2018-04-02 14:48:30)
    This reference sequence will be used as a template for the Rebaler assembly.

Reference contig   Circular    Length
EU168190.1         yes        159,370


Building unpolished assembly (2018-04-02 14:48:30)
    Rebaler first aligns long reads to the reference using minimap2. It then selects high quality alignments and replaces the reference sequence with the
corresponding read sequence. This creates an unpolished assembly made directly from read fragments, similar to what would be produced by miniasm.

Loading reads...                             1,001,732 reads
Aligning reads to reference with minimap2... 75,584 initial alignments
Culling alignments to a non-redundant set... 17 alignments remain

Constructing unpolished assembly:

EU168190.1:
310_110930_42157_c101187412550000001823278408081755_s1_p0/136549/29939_36631(+):0-6397 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(-
):4601-11604 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/77805/0_12324(-):0-5516 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/73277/192
37_38473(-):0-15771 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/138367/0_17756(+):0-8206 → 310_110930_42157_c101187412550000001823278408081755_s1_p0/1
16437/30642_39221(+):5-4438 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/16253/0_15320(+):0-15308 → 412_143440_42157_c101182882550000001823244205011700_s1_p0/43657/0_21570(-):13082-21557 → 310_172852_42157_c101187412550000001823278408081756_s1_p0/30411/40909_54026(+):3186-11125 → 412_210519_42157_c101182882550000001
823244205011701_s1_p0/34889/258_15536(+):0-3382 → 309_223211_42157_c101187412550000001823278408081753_s1_p0/102134/31047_56076(-):0-13370 → 412_210519_42157_c10118288
2550000001823244205011701_s1_p0/53826/0_16333(+):0-16059 → 310_045026_42157_c101187412550000001823278408081754_s1_p0/33103/0_21658(+):13975-19659 → 309_223211_42157_c
101187412550000001823278408081753_s1_p0/135817/0_17175(+):0-17167 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/67683/0_14084(-):3844-7750 → 309_223211_
42157_c101187412550000001823278408081753_s1_p0/74925/27917_45917(+):0-17988 → 412_210519_42157_c101182882550000001823244205011701_s1_p0/27948/0_30126(-):10279-13982


Polishing assembly (2018-04-02 14:51:50)
    Rebaler now runs Racon to polish the miniasm assembly. It does multiple rounds of polishing to get the best consensus. Circular unitigs are rotated between
rounds such that all parts (including the ends) are polished well. Assembly quality is measured by the sum of all read alignment scores.

Polish       Assembly          Mapping
round            size          quality
begin         160,307      261,757,024

Best polish: temp_rebaler_27405/01_unpolished_assembly.fasta
