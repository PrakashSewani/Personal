import yake
import wikipedia
import spacy

nlp=spacy.load("en_core_web_sm")

while(True):
    text=input("Enter your Question: ")
    language="en"
    max_ngram_size=3
    deduplication_threshold=0.9
    numOfKeywords=20
    custom_kw_extractor=yake.KeywordExtractor(lan=language,n=max_ngram_size,dedupLim=deduplication_threshold,top=numOfKeywords,features=None)
    keywords=custom_kw_extractor.extract_keywords(text)
    print("Extracted keywords are: ")
    print(keywords)
    try:
        for i in range(len(keywords)):
            text=wikipedia.summary(keywords[i][0])
            print(text)
            doc=nlp(text)
            print("Suggested Keywords: ")
            print(doc.ents)
            flag=input("Satisfied with current answer? Y/N: ")
            if flag=="y" or flag=="Y":
                break
    except wikipedia.exceptions.DisambiguationError as opt:
        print(opt)
