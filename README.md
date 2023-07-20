# Fine-tune-BERT-base-uncased-QA-SQuAD2.0
Fine-tune bert-base-uncased for Question answering on SQuAD 2.0 by using BERT transformers

This set of programs is written by referencing some online sources like code templates, previous works by orders, documents etc., without them we are probably not able to write this.

# Index<br />
- [What is inside the folder](#what-is-inside-the-folder)
- [The structure of the QA system](#the-structure-of-the-qa-system)
- [Performance and link to trained model](#performance-and-link-to-trained-model)
- [light weight program for reading comprehension answering](#light-weight-program-for-reading-comprehension-answering)
- [How to use (Detailed description)](#how-to-use-detailed-description)
- [Requirement](#requirement)
- [Reference](#reference)

# What is inside the folder
This repository consisted of a few things which are in each folder. Their name should already imply what they do.</br>
1. Training for Bert Question and answering, from fine-tuning bert-base-uncased.</br>
They are in the "train_bert_base_qa" folder. They are designed to run at Google Colab and the model is trained with an a100. We trained for 4 epochs, batch size=32.

2. Training for answerable/unanswerable classifier, which is also fine-tuned from bert-base-uncased, it is also tested with its accuracy on SQuAD2.0 dev set for classifier if the question is answerable/unanswerable.</br>
They are in the "answerable_classifier" folder. They are designed to run at Colab. The model is trained at an a100 in Colab. We trained for 4 epochs, batch size=32.

3. Code for testing the system on SQuAD2.0 dev set and give the respective .json output.</br>
They are in the "combined" folder. ipynb file.

4. A lightweight program for the model to give an answer from a given context.</br>
They are in the "read_txt_and_answer" folder. It is a Python program, which can run on CUDA device or CPU.

5. Program to convert .json dataset into .csv for the data needed in different parts of the program. The dataset is in .json originally, but for easier programing, it had been converted into .csv and is used in some of the programs. These programs in this folder in the respective program need it, they are named by convert_json_to_csv... something like this name imply what they converted.

# The structure of the QA system
The QA program uses two models, the first is for the BERT Question answering, and the other is for the BERT classifier, which is for classifying answerable and unanswerable questions. For the overall structure and for how the QA program work, see below:
 <img src="image/flow.png" alt="flow.png"> </br>

# Performance and link to the trained model
We had tested the system on the dev set, at epoch 4 on both classifier and bert QA:</br>
Exact Match (EM): 53.0784</br>
f1: 59.1615</br>

On the classifier alone, it can get 72.6899% of accuracy for classifying answerable and unanswerable questions.</br></br>
On the QA bert alone, The F1 is 32.7591, EM is 24.9474. In the system, we do not use [CLS] output for unanswerable questions, since the QA bert alone has almost no ability to answer unanswerable questions, which also leads to low f1 and EM. However, for QA bert alone and counting answerable questions only,  F1: 62.0359, EM: 46.3900. </br>

The model is uploaded to hugging face, Bert QA at https://huggingface.co/lrex93497/bert_qa_pt_3, Classifier at https://huggingface.co/lrex93497/bert_qa_classifier_pt_3
</br>
# lightweight program for reading comprehension answering
The program is in the "Read_txt_and_answer" folder. Before use, please modify values "model_qa" and "classifier_model" inside the .py file to the respective model's location. Enter the context into the "context.txt" file, only in the first line. Then run "read_doc_and_answer.py" to wait it asks you to input a question. Then you can ask a question, if it finds the answer, it answers the answer. But it determines there is no answer, it output "". You can keep asking questions once it is loaded.</br>

Below is an example of running the program, using our trained model with context "Bert is a teacher, he teaches class a from Monday to Friday every week. Bert is an experienced teacher with 10 years of teaching experience.":</br>
 <img src="image/demo.PNG" alt="demo.PNG"> </br>

# How to use Detailed description
A detailed description of how to every thing in this repository is recorded in how_to_use.pdf.

# Requirement
Below is the package and Python we had used:</br></br>
Python 	     3.7.9</br>
Cuda 11.3, may need to change accord to GPU </br>
datasets                2.10.1</br>
transformers            4.26.0.dev0</br>
pandas                  1.3.5</br>
numpy                   1.21.6</br>
matplotlib              3.5.3</br>
seaborn                 0.12.2</br>
sklearn                 0.0.post1</br>
torch                   1.12.1+cu113</br>
tqdm                    4.64.1</br>

# Reference
https://github.com/ThaddeusSegura/BERT_on_SQuAD/blob/master/SE_classification.ipynb </br>
https://www.kaggle.com/code/peymaanalavi/questionanswering-on-squad </br>
