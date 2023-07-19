import pandas as pd

json_to_convert = pd.read_json('train-v2.0.json')

question_list = []
text_list = []      #this is context
id_list = []
answer_list = []
answer_start_list = []

for data in json_to_convert['data']:
    data_df = pd.DataFrame(data)
    for paragraphs in data_df['paragraphs']:
        paragraphs_df = pd.DataFrame(paragraphs)      #qas for 1 context in here,   df: qas context  
        for qas in paragraphs_df['qas']:
            try:
                qas_df = pd.DataFrame(qas)      #inside there two types of qa set so try&except for another type
                #^ df:  question    id  answers is_impossbile
                question_list.append(qas_df['question'][0])    #[0] as all are same
                id_list.append(qas_df['id'][0])        #[0] as all are same
                for answers in qas_df['answers']:
                    answer_list.append(answers['text'])
                    answer_start_list.append(answers['answer_start'])     
                    text_list.append(paragraphs_df['context'][0])
                    break   #only first answer is used
            except:
                continue
          
                    
#print(question_list)
#print(text_list)
#print(id_list)
#print(answer_list)

csv_df = percentile_list = pd.DataFrame(
    {'context': text_list,
     'question': question_list,
     'id': id_list,
     'answer_start': answer_start_list,
     'text': answer_list
    })

csv_df.to_csv('train-v2.0-no-imposs-q.csv')