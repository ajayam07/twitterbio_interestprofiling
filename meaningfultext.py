import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


textline = "A holiday destination management company, travel consultants. https://t.co/x15bSxzIX0"
# print(sorted(word_tokenize(textline,language='english'),reverse=True))
stop_words = set(stopwords.words("english"))
words = word_tokenize(textline)

# filtered after stop words
filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
#
# # word stemming using PorterStemmer
# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# for w in words:
#     print(ps.stem(w))

# POS tagging using PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()
    except Exception as e:
        print(str(e))
process_content()