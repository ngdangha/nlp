import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("vi")
doc_bin = DocBin().from_disk("./data/test_syllable.spacy")  # your file here
examples = []  # examples in Prodigy's format
for doc in doc_bin.get_docs(nlp.vocab):
    spans = [{"start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents]
    examples.append({"text": doc.text, "spans": spans})