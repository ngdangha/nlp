import spacy
from spacy.scorer import Scorer
from spacy.tokens import DocBin
from spacy.training import Example

txt = spacy.blank("vi")
test_file_path = "./data/test_syllable.spacy"
model_path = "./output/1/model-best"
score_path = model_path + "/score.txt"

def save_score(model_path, score_path, result):
    with open(score_path,'w') as file:
        file.write('Model: ' + str(model_path) + '\n\n')

        for score in result.items():
            file.write(str(score))
            file.write('\n')

    file.close()

#get test data
doc_bin = DocBin().from_disk(test_file_path)  # your file here
TEST_REVISION_DATA = []  # examples in Prodigy's format
for doc in doc_bin.get_docs(txt.vocab):
    spans = [[ent.start_char, ent.end_char, ent.label_] for ent in doc.ents]
    TEST_REVISION_DATA.append((doc.text,{'entities':spans}))

#use model to get scorer result
nlp = spacy.load(model_path)
examples = []
scorer = Scorer()
for text, annotations in TEST_REVISION_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    example.predicted = nlp(str(example.predicted))
    examples.append(example)

result = scorer.score(examples)

save_score(model_path, score_path, result['ents_per_type'])

# for item in result.items():
#     print(item)

# print(result['ents_per_type']['DATE'][0])