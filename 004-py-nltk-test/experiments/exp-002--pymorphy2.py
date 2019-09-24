import nltk
import pymorphy2

text = "Мама мыла Раму, а Рама краснел от сраму. Наступила весна! А где скворцы?.. ждемс..."

morph = pymorphy2.MorphAnalyzer()

# ooo = morph.parse(text)

res = nltk.sent_tokenize(text)

for sentence in res:
    tokens = nltk.word_tokenize(sentence)
    tokens_norm = [morph.parse(word)[0].normal_form for word in tokens]
    tokens_norms_all = [morph.normal_forms(word) for word in tokens]
    pass



# words = ['грустно', 'зависимость', 'хорошему', 'приводит', 'альтернатив']
# for word in words:
#     p = morph.parse(word)[0]
#     print(p.normal_form)