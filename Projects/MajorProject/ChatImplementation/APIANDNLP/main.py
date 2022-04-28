import yake

text=input("Enter your Question: ")
language="en"
max_ngram_size=5
deduplication_threshold=0.9
numOfKeywords=24
custom_kw_extractor=yake.KeywordExtractor(lan=language,n=max_ngram_size,dedupLim=deduplication_threshold,top=numOfKeywords,features=None)
keywords=custom_kw_extractor.extract_keywords(text)
print("Extracted keywords are: ")
print(keywords)
