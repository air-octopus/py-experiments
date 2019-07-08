# coding=utf-8

import nltk


# def load_sentence(text_id, sentence, db):
#     db.add_sentence(text_id, sentence)


def load_text(db, text_path):

    text_id = db.find_text(text_path)
    if text_id:
        return text_id[0]

    with open(text_path) as f:
        text = f.read()
        text = text                                             \
            .replace('...', '$$$$$triplept')                    \
            .replace('\n\n\n', '\n\n')                          \
            .replace('\n\n\n', '\n\n')                          \
            .replace('\n\n\n', '\n\n')                          \
            .replace('\n\n\n', '\n\n')                          \
            .replace('\n\n\n', '\n\n')                          \
            .replace('\n\n', '.$$$$$par')                       \
            .replace('\n    ', '.$$$$$par')                     \
            .replace('\n', ' ')                                 \
            .replace('..', '.')                                 \
            .replace('..', '.')                                 \
            .replace('..', '.')                                 \
            .replace('..', '.')                                 \
            .replace('$$$$$triplept.', '$$$$$triplept')         \
            .replace('  ', ' ')                                 \
            .replace('  ', ' ')                                 \
            .replace('  ', ' ')                                 \
            .replace('  ', ' ')                                 \
            .replace('  ', ' ')                                 \
            .replace('  ', ' ')                                 \
            .replace('  ', ' ')                                 \
            .replace('$$$$$triplept.', '$$$$$triplept')         \
            .replace('$$$$$par ', '$$$$$par')                   \
            .replace('$$$$$triplept', '...')                    \
            .replace('$$$$$par', '\n')

    text_id = db.add_text(text_path)

    sentences = nltk.sent_tokenize(text)
    db.add_sentences(text_id, sentences)
    # for sentence in sentences:
    #     db.add_sentence(text_id, sentence)

    # parsed_text = (text, text_id, [parse_sentence(sentence) for sentence in sentences])

    return text_id

