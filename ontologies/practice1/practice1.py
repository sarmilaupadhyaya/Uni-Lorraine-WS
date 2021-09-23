# 22 Sep 2021
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_lg')
nlp.add_pipe('sentencizer')
matcher = Matcher(nlp.vocab)
f = open("pos.txt","w")

def read_file(file_path):

    data = open(file_path, "r").read()
    data = nlp(data)
    for i,sent in enumerate(data.sents):
        f.write("==============================")
        f.write("\n")
        f.write("Sentence no "+str(i))
        f.write("\n")
        for word in data:
            f.write((word.text +"==========="+ word.pos_))
            f.write("\n")
    return data


def get_terminology(data):
    """
    """
    patterns = [[{"POS": "NOUN"}, {"POS": "NOUN"}], [{"POS": "ADJ"}, {"POS": "NOUN"}]]
    for pattern in patterns:
        matcher = Matcher(nlp.vocab)
        matcher.add("nlg", [pattern])
        print("==============================")
        print(pattern)
        print("***************************")

        matches = matcher(data)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = data[start:end]  # The matched span
            print(match_id, string_id, start, end, span.text)
            f.write(span.text)
        matcher.remove("nlg")

data = read_file("nlg_text")
get_terminology(data)
