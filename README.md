# YACSC
English | [简体中文](README.zh.md)

YACSC (**Y**et **A**nother **C**hinese **S**pelling **C**heck Dataset) is an evaluation dataset used to assess the performance of spell check models in real-world scenarios. Previous benchmarks like [SIGHAN](http://ir.itc.ntnu.edu.tw/lre/sighan8csc.html) assume input sentences contain only spelling errors, which we refer to as ideal scenarios. However, in real-world applications, spell check inevitably encounters sentences with grammatical errors, which deviates from the assumptions made in ideal scenarios. 

To test the effectiveness of existing CSC models in real-world scenarios and their potential to improve grammar correction, we propose YACSC. It is based on the Chinese learner corpus [YACLC](https://github.com/blcuicall/YACLC#introduction), a large-scale crowd-sourced corpus of annotated sentences written by Chinese language learners, which includes both grammatical and fluency corrections. We made annotations directly from the original, ungrammatical input of YACLC, without any modifications, to provide a more accurate evaluation of CSC performance in real-world conditions.

YACSC is a two-stage corpus for evaluating the performance of CSC models, including 2,550 annotated sentences. The corpus consists of sentences with both spelling and grammatical errors, which are then corrected in two stages. The first stage corrects the spelling errors, while the second stage corrects grammatical errors. We also provide two subsets of YACSC, YACSC-no\_GE and YACSC-with\_GE. In YACSC-with\_GE, the source sentences and target sentences do not correct grammatical errors, which are used to test the performance of the CSC model under real-world scenarios. In YACSC-with\_GE, the source sentences and target sentences have corrected grammatical errors, which are used to test the performance of the model under ideal scenarios. Both the YACSC dataset and the two subsets can be found in `YACSC`. 

Following is an overview of the statistics for YACSC:
| Description | Statistics |
| :--- | ---: |
| Sentences | 2,550 |
| Sentences with spelling errors (percentage) | 1,275 (50\%) |
| Sentences with grammatical errors (percentage) | 1,735 (68\%) |
| Avg length | 22.95 |
| Phonetic errors | 967 |
| Graphic errors | 210   | 
| Both phonetic and graphic errors | 312 |
| Total errors | 1,489 |

## SIGHAN-REVISED

Originally, the SIGHAN datasets are in traditional Chinese. Most prior studies are based on the converted simplified Chinese version by [openCC](https://github.com/BYVoid/OpenCC). However, the conversion to simplified Chinese introduces a lot of noise. Multiple traditional Chinese characters may correspond to a single Simplified Chinese character after conversion. Thus, a confusion pair may become invalid after simplification. For example, "復習(review)" and "複習(review)" could have constituted an error pair "復-複", but both "復" and 複" are converted to "复" in Simplified Chinese. And we also observed that there are some unreasonable annotations in the SIGHAN benchmarks. Some of the main reasons include similarity in sound, similarity in form, and grammatical errors. These issues undermine the reliability of the model evaluation.

To address the above-mentioned issues in the SIGHAN test sets, including mislabeling and omission, etc., we conducted a revision to improve the confidence of evaluation results. Following are the before-and-after revision statistics of the SIGHAN test sets:

| Original | \# Sent | \# Sent w/ errs | \# Errors |
| --- | ---: | ---: | ---: |
| SIGHAN13 | 1,000 | 1,000 | 1,224 |
| SIGHAN14 | 1,062 | 531 | 771 |
|SIGHAN15 | 1,100 | 550 | 703 |
		
		 
| Revised | \# Sent | \# Sent w/ errs | \# Errors |
| --- | ---: | ---: | ---: |
| SIGHAN13 | 1,000 | 977 | 1,483 |
| SIGHAN14 | 1,062 | 602 | 932 |
| SIGHAN15 | 1,100 | 618 | 858 |

All revised SIGHAN test sets can be found in `SIGHAN-REVISED`.

## Evaluation

We provide an evaluation script to evaluate the metric of CSC systems, including the f1-score of detection and correction at the sentence level.

We need to extract the edits from the input sentences and model output sentences:
```
python ./evaluation/para2label.py --src input.txt --trg output.txt --out label.tsv
```
Note that the input file and output file should contain source sentences and output sentences line by line.

Then we use the `metric_core.py` to calculate precision, recall, and F1 score:
```
python ./evaluation/metric_core.py --input label.tsv --target gold.tsv
```

Report preview:
```
sent-detect-p: 76.38
sent-detect-r: 76.52
sent-detect-f1: 76.45
sent-correct-acc: 82.73
sent-correct-p: 75.83
sent-correct-r: 75.97
sent-correct-f1: 75.90
```

# Citation

If you find this work useful for your research, please cite our paper:

```
@article{wang-etal-2021-yaclc,
  title={YACLC: A Chinese Learner Corpus with Multidimensional Annotation},
  author={Yingying Wang, Cunliang Kong, Liner Yang, Yijun Wang, Xiaorong Lu, Renfen Hu, Shan He, Zhenghao Liu, Yun Chen, Erhong Yang, Maosong Sun},
  journal={arXiv preprint arXiv:2112.15043},
  year={2021}
}

@article{wang-etal-2023-yaclc,
  title={The Construction of Chinese Multi-dimensional Learner Corpus: YACLC},
  author={Yingying Wang, Cunliang Kong, Liner Yang, Renfen Hu, Erhong Yang, Maosong Sun},
  journal={Applied Linguistics},
  year={2023},
  number={1},
  pages={88-99}
}
```