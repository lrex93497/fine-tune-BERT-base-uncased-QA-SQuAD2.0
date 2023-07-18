# fine-tune-BERT-base-uncased-QA-SQuAD2.0
Fine tune bert-base-uncased for Queation answering on SQuAD2.0

This set of program is written by referencing to quite a lot of sources, without them I probably not able to write this.

This repository consisted of few things which is in each folder. </br>
1. Training (fine tune)for bert Question and answering.</br>
They are in "train_bert_base_qa" folder.

2. Training for aswerable/unaswerable classifier, it also test its accuracy on SQuAD2.0 dev set for classifier if question is aswerable/unaswerable.</br>
They are in "answerable_classifier" folder.

4. Code for test the model on SQuAD2.0 dev set and give the respective .json output.</br>
They are in "combined" folder.

6. A light weight program for the model to gives answer from a given context.</br>
They are in "read_txt_and_answer" folder.

The QA answer program consisted of two part, first is for the BERT Question answering, another one is for BERT classifier, which is for classifiering answerable and unanswerable question. For overall structure, see below:


