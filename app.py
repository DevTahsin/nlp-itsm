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
        "question", "request", "problem", "incident", "improvement","ticket","trouble","difficult","hard","easy","error","failure","mistake","succcess","accomplishment","urgent","high priority","medium priority","low priority","network issue","hardware issue","software issue","account management","user access","security","data backup","performance","training","support request","bug report","feature request","configuration","integration","maintenance","outage","service request","account lockout","password reset","spam","phishing","virus","malware","ransomware","cybersecurity","compliance","encryption","cloud","virtualization","devops","agile","scrum","kanban","lean","six sigma","project management","resource allocation","time tracking","budgeting","procurement","contract management","legal","hr","payroll","benefits","recruiting","development","career growth","diversity","inclusion","culture","wellness","safety","environment","sustainability","quality control","quality assurance","testing","debugging","documentation","knowledge management","learning management","training management","performance management","succession planning","talent management","workforce planning","workforce development","workforce analytics","workforce optimization","workforce engagement","employee experience","employee satisfaction","employee retention","employee turnover","employee relations","employee development","employee performance","employee feedback","employee recognition","employee rewards","employee benefits","employee programs","employee services","employee support","employee resources","employee assistance","employee health","employee safety","employee wellness","employee culture","employee diversity","employee inclusion","employee equity","employee belonging","application","database","web","mobile","setup","server","vpn"
        ])
    resultData.append(resultDataToPush)
    print(resultDataToPush)

write_data('x.json', resultData)

