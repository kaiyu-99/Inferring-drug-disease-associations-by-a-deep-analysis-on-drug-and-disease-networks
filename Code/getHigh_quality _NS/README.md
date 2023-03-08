1.	***getFinalNS_1path*** /: Scores for unlabeled samples are calculated using the given drug and its direct neighbors in the network.
2.	***getFinalNS_2path*** /: Calculate the weights of paths connecting one drug and its 2-neighbors in the network.
3.	***4_add1path.py***: A package to calculate the final scores for unlabeled samples by combining the results in folders in "getFinalNS_1path" and "getFinalNS_2path".
4.	***5_getFinalSamples.py***: A package to select high-quality negative samples under different thresholds and proportions to positive samples.<br>
![筛选负样本流程图]( https://github.com/kaiyu-99/Inferring-drug-disease-associations-by-a-deep-analysis-on-drug-and-disease-networks/blob/master/IMG/High_quality_NS.png)
