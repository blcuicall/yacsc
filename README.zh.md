# YACSC
[English](README.md) | 简体中文

YACSC (**Y**et **A**nother **C**hinese **S**pelling **C**heck Dataset) 是用于评估拼写检查模型在真实场景下性能的评估数据集。之前的Benchmark如 [SIGHAN](http://ir.itc.ntnu.edu.tw/lre/sighan8csc.html) 假设输入的句子只包含拼写错误，我们将其称为理想场景。然而，在真实应用场景中，拼写检查模型不可避免地会遇到带有语法错误的句子，这与理想场景的假设是有所偏离的。

为了在真实应用场景中测试现有拼写检查模型的性能以及拼写检查促进语法纠错任务效果的潜力，我们提出构建了真实场景下的中文拼写检查评估数据集 YACSC。它基于汉语学习者文本多维标注数据集 [YACLC](https://github.com/blcuicall/YACLC) 构建。YACLC 是一个基于中文学习者撰的大规模众包语法改错数据集，包含最小编辑修改和流畅性修改的二语学习者句子。我们直接对原始的、带语法错误的 YACLC 源句标注拼写错误，不对语法错误做任何修正，以在真实应用环境中更准确地评估拼写检查模型的性能。

YACSC 是一个两阶段数据集，包含2550个带标注的句对。数据集源句含有拼写错误的同时也可能含有语法错误，分两个阶段进行纠正。第一阶段纠正拼写错误，第二阶段纠正语法错误。我们还提供了YACSC的两个子集，YACSC-no\_GE和 YACSC-with\_GE。

- YACSC-with\_GE：用于在真实应用场景下评测拼写检查模型的性能，其源句子和目标句没有纠正语法错误。

- YACSC-with_GE：用于在理想场景下测试模型的性能，其源句子和目标句纠正了语法错误。

YACSC和这两个子集都放在 `YACSC`。

下面是YACSC数据集的相关统计信息:
| 描述 | 统计 |
| :--- | ---: |
| 句子数 | 2550 |
| 带拼写错误句子 (百分比) | 1275 (50\%) |
| 带语法错误句子 (百分比) | 1735 (68\%) |
| 平均句长 | 22.95 |
| 音近错误 | 967 |
| 形近错误 | 210   | 
| 音形近错误 | 312 |
| 拼写错误总数 | 1489 |

## SIGHAN-REVISED

原始的SIGHAN数据集是繁体中文数据集。前人研究都大多基于通过 [openCC](https://github.com/BYVoid/OpenCC) 转换为简体中文后使用。然而，转换的过程中会引入很多噪音：多个繁体中文字符在转换后可能对应一个简体中文字符，这会导致一对混淆字符在简化后可能变得无效。例如，"復習"和"複習"可以构成一个错误对"復-複"，但在转换过程中，"復"和"複"都会被转换为"复"。另外，我们还观察到SIGHAN基准数据集中存在一些不合理的标注，主要原因包括音近错误，形近错误和语法错误的漏标或误标。这些问题弱化了模型评估的可靠性。

为了缓解上面提及的SIGHAN测试集中的误标、漏标等问题。我们对SIGHAN测试集做了校对提高其评估结果的可靠性。下面是矫正前和矫正后的相关统计结果：

| 原始数据集 | 句子数 | 带错误句子数 | 错误数 |
| --- | ---: | ---: | ---: |
| SIGHAN13 | 1000 | 1000 | 1224 |
| SIGHAN14 | 1062 | 531 | 771 |
|SIGHAN15 | 1100 | 550 | 703 |
		
		 
| 矫正后 | 句子数 | 带错误句子数 | 错误数 |
| --- | ---: | ---: | ---: |
| SIGHAN13 | 1000 | 977 | 1483 |
| SIGHAN14 | 1062 | 602 | 932 |
| SIGHAN15 | 1100 | 618 | 858 |

所有校对后的SIGHAN测试集放在 `SIGHAN-REVISED`.

## Evaluation

我们提供了评测拼写检查模型输出的评测脚本，脚本计算句子级别的拼写错误检测和错误修正的精确率，召回率和F1值。

首先需要从源句和模型输出中抽取出模型的修改标签:
```
python ./evaluation/para2label.py --src input.txt --trg output.txt --out label.tsv
```
输入输出文件中数据格式为每行一个句子。

然后使用脚本 `metric_core.py` 计算精确率，召回率和F1值:
```
python ./evaluation/metric_core.py --input label.tsv --target gold.tsv
```

评测结果:
```
sent-detect-p: 76.38
sent-detect-r: 76.52
sent-detect-f1: 76.45
sent-correct-acc: 82.73
sent-correct-p: 75.83
sent-correct-r: 75.97
sent-correct-f1: 75.90
```

# 引用

如果您认为我们的工作对您的研究有帮助，请引用我们的论文:

```
@article{wang-etal-2021-yaclc,
  title={YACLC: A Chinese Learner Corpus with Multidimensional Annotation},
  author={Yingying Wang, Cunliang Kong, Liner Yang, Yijun Wang, Xiaorong Lu, Renfen Hu, Shan He, Zhenghao Liu, Yun Chen, Erhong Yang, Maosong Sun},
  journal={arXiv preprint arXiv:2112.15043},
  year={2021}
}

@article{wang-etal-2023-yaclc,
  title={汉语学习者文本多维标注语料库建设},
  author={王莹莹, 孔存良, 杨麟儿, 胡韧奋, 杨尔弘, 孙茂松},
  journal={语言文字应用},
  year={2023},
  number={1},
  pages={88-99}
}
```