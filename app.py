from data.datajson import get_data, write_data
from learning.huggingface_transformers.language_detector import detect_language
from learning.huggingface_transformers.tr_to_en_translate import translate
from learning.huggingface_transformers.en_zero_shot_classification import zero_shot_classification

dataArray = get_data('b.json')
resultData = []


for data in dataArray[1:3]:
    resultDataToPush = {}
    resultDataToPush['text'] = data
    # trim 512 chars
    lan = detect_language(data)
    if lan == 'tr':
        data = translate(data)
        resultDataToPush['textTranslated'] = data
    elif lan != 'en':
        continue
    resultDataToPush['classification'] = zero_shot_classification(data, [
        'question', 'request', 'problem', 'incident', 'improvement', 
        'urgent', 'important', 'asset','positive','negative',
        'ticket','trouble','difficult','hard','easy',
        'error','failure','mistake','succcess','accomplishment',
        ])
    resultData.append(resultDataToPush)
    print(resultDataToPush)

write_data('x.json', resultData)

