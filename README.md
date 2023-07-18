# fine-tune-BERT-base-uncased-QA-SQuAD2.0
Fine tune bert-base-uncased for Queation answering on SQuAD2.0

This set of program is written by referencing to quite a lot of sources, without them we probably not able to write this.

This repository consisted of few things which is in each folder. Their name should already imply what they do.</br>
1. Training (fine tune)for bert Question and answering.</br>
They are in "train_bert_base_qa" folder. They are designed to run at colab. The model is trained at a a100 in colab.

2. Training for aswerable/unaswerable classifier, it also test its accuracy on SQuAD2.0 dev set for classifier if question is aswerable/unaswerable.</br>
They are in "answerable_classifier" folder. 

3. Code for test the model on SQuAD2.0 dev set and give the respective .json output.</br>
They are in "combined" folder.

4. A light weight program for the model to gives answer from a given context.</br>
They are in "read_txt_and_answer" folder.

5. Program to convert .json dataset into .csv for the data needed in different part of the program. The dataset is in .json originally, but for easiler programing, it had been converted into .csv and is used in some of the program. These programs in in these folder in the respective program need it, they are named by convert_json_to_csv... something like this their name imply what they converted.

The QA answer program consisted of two models, first is for the BERT Question answering, another one is for BERT classifier, which is for classifiering answerable and unanswerable question. For overall structure, see below:


