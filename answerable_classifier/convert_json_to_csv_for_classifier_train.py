import pandas as pd

json_to_convert = pd.read_json('train-v2.0.json')

question_list = []
text_list = []      #this is context
answerable_list = []    #0 false, 1 true

for data in json_to_convert['data']:
    data_df = pd.DataFrame(data)
    for paragraphs in data_df['paragraphs']:
        paragraphs_df = pd.DataFrame(paragraphs)      #qas for 1 context in here,   df: qas context  
        for qas in paragraphs_df['qas']:
            try:
                qas_df = pd.DataFrame(qas)      #inside there two types of qa set so try&except for another type
                #^ df:  question    id  answers is_impossbile
                question_list.append(qas_df['question'][0])    #[0] as all are same
                answerable_list.append(1)    
                for answers in qas_df['answers']:    
                    text_list.append(paragraphs_df['context'][0])
                    break   #only first answer is used
            except:
                qas_df = pd.json_normalize(qas)     #df: plausible_answer   question    id  answers is_impossible
                # this type of questio has no answer, so answer is''
                question_list.append(qas_df['question'][0])
                text_list.append(paragraphs_df['context'][0])
                answerable_list.append(0)  


                    
#print(question_list)
#print(text_list)
#print(id_list)
#print(answer_list)

csv_df = percentile_list = pd.DataFrame(
    {'context': text_list,
     'question': question_list,
     'answerable': answerable_list,
    })

csv_df.to_csv('train-classifier-v2.0.csv')