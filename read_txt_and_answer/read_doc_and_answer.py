#First, we do prediction, then we do classifier by other classifier for unanswerable question
#as we find by finding [CLS] output for unanswerable question has low accuracy to idenify it.

from tqdm.auto import tqdm  # for showing progress bar
from datasets import load_dataset
import json
import pandas as pd
import numpy as np
import torch
from transformers import BertForQuestionAnswering, BertForSequenceClassification
from transformers import BertTokenizerFast, BertTokenizer
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler

device = torch.device('cpu')
#Using torch by GPU
if torch.cuda.is_available():
    device = torch.device('cuda:0')
    print("Use cuda device:", torch.cuda.get_device_name(0))
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device('cpu')
    print("use cpu")


try:
    #load model
    model_qa = BertForQuestionAnswering.from_pretrained('./bert_qa_pt_3/', local_files_only=True)
    tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
    classifier_model = BertForSequenceClassification.from_pretrained(
        './bert_qa_classifier_pt_3/', # 12-layer BERT
        num_labels = 2, #0:false 1:true
        output_attentions = False, # no attention output
        output_hidden_states = False, # no need for classifier
    )
except:
    while True:
        print("Cannot find model, you sure model is in the folder same as this program?")
        print("If yes, close this program and reload it")
        input("\n")



f = open("context.txt", "r")

context = f.readline()
model_qa.to(device)
classifier_model.to(device)


print("Context readed, what is your question?")

while True:
    question = input("Please input question\n")

    #QA model first

    #do two times as by one line cannot get all values
    input_ids = tokenizer.encode(context,question,truncation=True,padding='max_length')
    tokenized = tokenizer.encode_plus(context,
                            question,
                            add_special_tokens=True,    # Add `[CLS]` and `[SEP]`
                            truncation=True,
                            return_attention_mask=True,  # Construct attn. masks.
                            padding='max_length',
                            return_tensors='pt')
    #find location of sep
    sep_index = input_ids.index(tokenizer.sep_token_id)

    #segment a which contains sep itself
    segment_a_no = sep_index + 1

    #segment b the rest of the ids
    segment_b_no = len(input_ids) - segment_a_no

    #make a list, 0 for segment a, 1 for segment b.
    segment_ids = [0] * segment_a_no + [1] * segment_b_no
    #padding is handled by attention mask
    #check if segment_ids is normal
    assert len(input_ids) == len(segment_ids)

    type_id = segment_ids
    input_ids = tokenized['input_ids']
    mask = tokenized['attention_mask']
    
    input_ids = input_ids.tolist()
    
    tokens = tokenizer.convert_ids_to_tokens(input_ids[0])

    type_id = torch.Tensor(type_id)
    input_ids = torch.Tensor(input_ids)


    input_ids = input_ids.int()
    input_ids = input_ids.to(device)
    mask = mask.int()
    mask = mask.to(device)
    type_id = type_id.int()
    type_id = type_id.to(device)


    result = model_qa(input_ids = input_ids, attention_mask=mask, token_type_ids=type_id)       #use ids and mask and type to get result
    answer_start = torch.argmax(result.start_logits)    #get start position by argmax
    answer_end = torch.argmax(result.end_logits)        #get end position by argmax
    # join the break word
    if answer_end >= answer_start:
        answer = tokens[answer_start]
        for i in range(answer_start + 1, answer_end + 1):
            if tokens[i][0:2] == "##":
                answer = ""
            else:
                answer += " " + tokens[i]

    #answer is the answer


    #now pass to classifier
    tokenized = tokenizer.encode_plus(question,context,
                            add_special_tokens=True,    # Add `[CLS]` and `[SEP]`
                            truncation=True,
                            return_attention_mask=True,  # Construct attn. masks.
                            padding='max_length',       #512
                            max_length=512,
                            return_tensors='pt')
    
    input_ids = tokenized['input_ids']
    mask = tokenized['attention_mask']
    
    #input_ids = torch.Tensor(input_ids)
    #mask = torch.Tensor(mask)

    input_ids = input_ids.int()
    input_ids = input_ids.to(device)
    mask = mask.int()
    mask = mask.to(device)
    
    output = classifier_model(input_ids=input_ids, 
                                token_type_ids=None, 
                                attention_mask=mask 
                                )
    
    logit = output['logits']
    logit = logit.detach().cpu().numpy()

    result_0_or_1 = np.argmax(logit, axis=None).flatten()      #0 false 1 true

    if result_0_or_1[0] == 0:
        answer = ''      #0 means unanswerable question, so ''

    print("Answer: " + answer)
    answer=""       #reset answer