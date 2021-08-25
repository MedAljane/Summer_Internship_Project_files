import pegasus_paraphrase
from pegasus_paraphrase import get_response
from textblob import TextBlob
from deep_translator import GoogleTranslator
from sentence_splitter import SentenceSplitter, split_text_into_sentences

def transPhrasing(text):
    splitter = SentenceSplitter(language=TextBlob(text).detect_language())
    sentence_list = splitter.split(text)
    translated_sentences = [GoogleTranslator(target='en').translate(element) for element in sentence_list]
    paraphrased_sentences = [get_response(e, 1, 1) for e in translated_sentences]
    cleaned_paraphrased_sentences = [e[0] for e in paraphrased_sentences]
    paraphrased_result_En = [' '.join(x for x in cleaned_paraphrased_sentences)]
    paraphrased_result_cleaned_En = str(paraphrased_result_En).strip('[]')
    
    sentences_to_french = [GoogleTranslator(target='fr').translate(e) for e in cleaned_paraphrased_sentences]
    paraphrased_result_fr = [' '.join(x for x in sentences_to_french)]
    paraphrased_result_cleaned_fr = str(paraphrased_result_fr).strip('[]').strip("'").strip('"')

    return [paraphrased_result_cleaned_En,paraphrased_result_cleaned_fr]