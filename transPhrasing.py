import pegasus_paraphrase
from pegasus_paraphrase import get_response
from textblob import TextBlob
from deep_translator import GoogleTranslator
from sentence_splitter import SentenceSplitter, split_text_into_sentences

def sentenceIsValid(sentence):
    words = sentence.split(' ')
    for element in words:
        if len(element) > 3 and words.count(element) > 7:
            return False
        else:
            return True

def transPhrasing(text):
    splitter = SentenceSplitter(language=TextBlob(text).detect_language())
    sentence_list = splitter.split(text)
    translated_sentences = [GoogleTranslator(target='en').translate(element) for element in sentence_list]


    paraphrased_sentences = []

    for e in translated_sentences:
        result = get_response(e, 1, 1)
        if sentenceIsValid(result[0]):
            paraphrased_sentences.append(result[0])
        else:
            paraphrased_sentences.append(e)

    paraphrased_result_En = [' '.join(x for x in paraphrased_sentences)]
    paraphrased_result_cleaned_En = str(paraphrased_result_En).strip('[]').strip("'").strip('"')
    
    sentences_to_french = [GoogleTranslator(target='fr').translate(e) for e in paraphrased_sentences]
    paraphrased_result_fr = [' '.join(x for x in sentences_to_french)]
    paraphrased_result_cleaned_fr = str(paraphrased_result_fr).strip('[]').strip("'").strip('"')

    return [paraphrased_result_cleaned_En,paraphrased_result_cleaned_fr]
