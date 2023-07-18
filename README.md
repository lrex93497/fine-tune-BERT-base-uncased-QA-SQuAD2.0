# Fine-tune-BERT-base-uncased-QA-SQuAD2.0
Fine tune bert-base-uncased for Queation answering on SQuAD 2.0

This set of program is written by referencing to quite a lot of sources, without them we probably not able to write this.

# What is inside the folder
This repository consisted of few things which is in each folder. Their name should already imply what they do.</br>
1. Training (fine tune)for bert Question and answering, from bert-base-uncased.</br>
They are in "train_bert_base_qa" folder. They are designed to run at colab. The model is trained at a a100 in colab. We trained for 4 epoch, batch size=32.

2. Training for aswerable/unaswerable classifier, which is also fine tuned from bert-base-uncased, it also test its accuracy on SQuAD2.0 dev set for classifier if question is aswerable/unaswerable.</br>
They are in "answerable_classifier" folder. They are designed to run at colab. The model is trained at a a100 in colab. We trained for 4 epoch, batch size=32.

3. Code for test the model on SQuAD2.0 dev set and give the respective .json output.</br>
They are in "combined" folder.

4. A light weight program for the model to gives answer from a given context.</br>
They are in "read_txt_and_answer" folder.

5. Program to convert .json dataset into .csv for the data needed in different part of the program. The dataset is in .json originally, but for easiler programing, it had been converted into .csv and is used in some of the program. These programs in in these folder in the respective program need it, they are named by convert_json_to_csv... something like this their name imply what they converted.

# The structure of the QA system
The QA program use two models, first is for the BERT Question answering, another one is for BERT classifier, which is for classifiering answerable and unanswerable question. For overall structure and for of how the QA program work, see below:
 <img src="image/flow.png" alt="flow.png"> </br>

# Performance 
We had tested the system on the dev set, at epoch 4 on both classifier and bert QA:
Exact Match (EM): 53.0784
f1: 59.1615

On the classifier alone, it can get 72.6899% of accuracy for classifing answerable and unanswerable question
On the QA bert alone, The F1 is 32.7591, EM is 24.9474. Since the QA bert alone has no ability to answer unanswerable question.

# Requirement
Below is the package and python we had used:
Python 	     3.7.9
Cuda 11.3, may need to change accord to GPU 
datasets                2.10.1
transformers            4.26.0.dev0
pandas                  1.3.5
numpy                   1.21.6
matplotlib              3.5.3
seaborn                 0.12.2
sklearn                 0.0.post1
torch                   1.12.1+cu113
tqdm                    4.64.1

# Reference
