import nltk

#text = "At eight o'clock on Thursday morning Arthur didn't feel very good."
text = "Мама мыла Раму, а Рама краснел от сраму. Наступила весна! А где скворцы?.. ждемс..."

text = "Мама _12_345 мыла Раму, а Рама краснел от сраму. Наступила весна! А где скворцы?.. ждемс..."

res = nltk.sent_tokenize(text)

for sentence in res:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    pass

#tagset = nltk.help.upenn_tagset()

pass
