import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import yake

with open(r'D:\Python\Projects\BertAlgorithm\text.txt','r',encoding='utf-8') as f:
    lines=f.readlines()

txt=str(lines).split(",",1)[1]

dark=txt.split("\\n")

harsh=[]
for i in dark:
    temp=str(i).replace("\\","")
    harsh.append(temp)

while("" in harsh) :
    harsh.remove("")

harsh=harsh[:-1]

# search=input()
print(harsh)

text=input("Enter your Question: ")
language="en"
max_ngram_size=4
deduplication_threshold=0.9
numOfKeywords=20
custom_kw_extractor=yake.KeywordExtractor(lan=language,n=max_ngram_size,dedupLim=deduplication_threshold,top=numOfKeywords,features=None)
keywords=custom_kw_extractor.extract_keywords(text)
print("Extracted keywords are: ")
print(keywords)

# k=search.split()
dhokla=""
for i in range(0, len(harsh)):
    if set(keywords[0][0].split()).issubset(set(harsh[i].split())):
        # print("success")
        print(i)
        for j in range(i,i+27):
            # print("success")
            dhokla+=harsh[j+1]
        break
print(dhokla)

model=BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

tokenizer=BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

question = text
context = dhokla

input_ids = tokenizer.encode(question, context)

print('The input has a total of {:} tokens.'.format(len(input_ids)))

tokens = tokenizer.convert_ids_to_tokens(input_ids)

# For each token and its id...
for token, id in zip(tokens, input_ids):
    
    if id == tokenizer.sep_token_id:
        print('')
    
    print('{:<12} {:>6,}'.format(token, id))

    if id == tokenizer.sep_token_id:
        print('')

sep_index = input_ids.index(tokenizer.sep_token_id)

# The number of segment A tokens includes the [SEP] token istelf.
num_seg_a = sep_index + 1

# The remainder are segment B.
num_seg_b = len(input_ids) - num_seg_a

# Construct the list of 0s and 1s.
segment_ids = [0]*num_seg_a + [1]*num_seg_b

# There should be a segment_id for every input token.
assert len(segment_ids) == len(input_ids)

outputs = model(torch.tensor([input_ids]), # The tokens representing our input text.
                             token_type_ids=torch.tensor([segment_ids]), # The segment IDs to differentiate question from answer_text
                             return_dict=True) 

start_scores = outputs.start_logits
end_scores = outputs.end_logits

answer_start = torch.argmax(start_scores)
answer_end = torch.argmax(end_scores)

# Combine the tokens in the answer and print it out.
answer = ' '.join(tokens[answer_start:answer_end+1])

# print('Answer: "' + answer + '"')

answer = tokens[answer_start]

# Select the remaining answer tokens and join them with whitespace.
for i in range(answer_start + 1, answer_end + 1):
    
    # If it's a subword token, then recombine it with the previous token.
    if tokens[i][0:2] == '##':
        answer += tokens[i][2:]
    
    # Otherwise, add a space then the token.
    else:
        answer += ' ' + tokens[i]

print('Answer: "' + answer + '"')
