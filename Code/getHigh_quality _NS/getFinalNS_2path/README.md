1.	***csv_files*** /: Obtain the input and output files for path weights of target drug path length 2 in potential negative samples.
2.	***example_2*** /: This document mainly takes 10 drugs as an example, constructs a drug 
network, and then calculates the path weight of the drug's neighbor's neighbor drug.
3.	***1_CreateNetwork.py***: Construction of drug network, the weight between drug nodes is the similarity score between the two drugs. 
4.	***2_countExtrascore.py***: Calculate all possible path weights for the target drug and its neighbor's neighbor drug.
5.	***3_addIndex.py***: Add exponent to all possible path lengths, choosing the maximum path length as the final path weight of length 2 for this target drug.
