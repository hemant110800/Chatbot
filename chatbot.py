from datetime import date
import time
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def chatbot(quest):
    cnt=0
    update=[]
    
    punct = {'what','?','there', 'having', 'few', 'both', 's', 'are', 'myself', 'further', 'haven', 'herself', "you've",
         'just', 'ma', 'he', 'between', 'again', 'hadn', 'couldn', 'on', 'any', 'other', 'some', 'too', 'have', 'when',
          'wasn', "won't", 'didn', 'did', 'who', "haven't", 'before', 'most', 'under', 'ourselves', 'aren', 'is', 'were',
         "should've", "couldn't", 'ours', 'a', 'the', 'these', 'own', 'shouldn', 'yourselves', 'through', 'how', "you're",
        'until', 'or', 'y', 'below', 'you', 'out', "mustn't", "you'll", "wouldn't", 'now', 'then', 'doesn', 'won', 'nor',
         "it's", 'hers', 'than', 'its', 'me', 'their', 'wouldn', 'where', 'mightn', 'itself', "hadn't", 'mustn', 'had', 
        'doing','of', 'not', 'your', "don't", 'does', 're', 'yours', 'over','more', 'should', 'o', 'only', 'd', "weren't",
            "needn't", 'can', 'all', "she's", 'was', 'by', 'm', "shouldn't", 'my', 'isn', 'as', 'this', 'been', 'for', 
            'here', 'once', 'yourself', "aren't", 'them', 'into', "mightn't", 'i', "isn't", 'hasn', 'his', "that'll", 
            'ain', 'weren', 'we', 'after', 'themselves', 'do', 'himself', 'while', 'those', 'such', "hasn't", 'will', 
            'from', 'her', 'in', 'shan', 'off', 'they', 'whom', 'about', 'up', "wasn't", 'down', 've', 'very', 'to',
             'our', 'll', 'she', 'so', 'with', 'being', 'at', 'because', 'why', 'if', 'no', 'during', 'an', 'and',
              'which', 'each', 'be', 'above', 'theirs', "shan't", 't', 'has', 'it', 'but', 'same', "you'd", "didn't", 
              "doesn't", 'needn', 'against', 'am', 'don', 'him', 'that'}
    
    for word in quest:
        if word.lower() not in punct:
            update.append(word.lower())


    synonym={"thanks":"ok",
             "made":"originator",
             "type":"kind",
             "season":"weather",
             "dear":"friend",
             "surname":"name",
             "helper":"help",
             "goodwisher":"help",
             "imaginary":"real",
             "really":"ok",
             "okay":"ok",
             "called":"call",
             "aim":"goal",
             "study":"studies",
             "learning":"studies",
             "chatbot":"name",
             "field":"domain",
             "area":"domain",
             "interest":"domain",
             "stop":"terminate",
             "break":"terminate",
             "end":"terminate",
             "guy":"friend"
            }

    answer={"help":"Yeah I am always ready to help you!But i don't know what you want.Please ask questions",
             "friend":"Yeah!I am always with you friend",
             "date":date.today(),
             "time":time.asctime(),
             "problems":"i try my best to solve all your problems",
             "name":"I am your chatbot.I try to answer your questions",
             "call":"I am your friend only.So just call me friend",
             "ok":"No problem!Welcome",
             "about":"I am always happy.Dont worry about me",
             "real":"If you are real then I am also real.",
             "originator":"I am your assistant which is created by Hemant Bhati",
             "kind":"I am just learning from you.As a starter ask only basic questions on my particular domain,If i am capable then I will give your answer",
             "weather":"Be Ready to welcome Cold days,Take out your coats and rajai",
             "goal":"To give all answers in accurate manner",
             "studies":"Study is very important for everyone!Study hard because it shapes your future.",
             "domain":"I tell you about Social Media",
             "terminate":"How you end your conversation with your friend.Just say bye",
             }


    for i in update:
        if i in answer.keys():
            return(answer[i])
        elif i in synonym.keys():
            return(answer[synonym[i]])
        else:
            cnt+=1
    if(cnt==len(update)):
        return("I am sorry.I don't have an answer for this.")

print("Hello friends!How can I help you!")
#print("Enter -'stop' to break the conversation")
while(True):
    question=input()
    if(question.lower()=="bye"):
        print("Bye friend")
        break
    if(question.lower()=="hi" or question.lower()=="hello" or question.lower()=="hey"):
        print("Hi!How can i help you")
        continue
    l1=list(question.split(' '))
    #print(l1)
    print(chatbot(l1))
print("See you soon!friend")