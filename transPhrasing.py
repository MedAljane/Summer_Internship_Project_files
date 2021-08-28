import pegasus_paraphrase
from pegasus_paraphrase import get_response
from textblob import TextBlob
from deep_translator import GoogleTranslator
from sentence_splitter import SentenceSplitter, split_text_into_sentences


def sentence_is_valid(sentence) -> bool:
    """
    Determine if a generated sentence is valid or not
    :param sentence: String
    :return: Bool
    """
    words = sentence.split(' ')
    for element in words:
        if len(element) > 3 and words.count(element) > 7:
            return False
        else:
            continue
    return True


def trans_phrasing(text) -> list:
    """
    Translate a text, split it to sentences and generates paraphrased sentences using the generating function,
    returns a list containing the paraphrased text in both English and French languages
    :param text: String
    :return: List
    """
    splitter = SentenceSplitter(language=TextBlob(text).detect_language())
    sentence_list = splitter.split(text)
    translated_sentences = [GoogleTranslator(target='en').translate(element) for element in sentence_list]

    paraphrased_sentences = []

    for e in translated_sentences:
        result = get_response(e, 1, 1)
        if sentence_is_valid(result[0]):
            paraphrased_sentences.append(result[0])
        else:
            paraphrased_sentences.append(e)

    paraphrased_result_en = [' '.join(x for x in paraphrased_sentences)]
    paraphrased_result_cleaned_en = str(paraphrased_result_en).strip('[]').strip("'").strip('"')
    
    sentences_to_french = [GoogleTranslator(target='fr').translate(e) for e in paraphrased_sentences]
    paraphrased_result_fr = [' '.join(x for x in sentences_to_french)]
    paraphrased_result_cleaned_fr = str(paraphrased_result_fr).strip('[]').strip("'").strip('"')

    return [paraphrased_result_cleaned_en, paraphrased_result_cleaned_fr]
