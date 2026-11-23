"""Small, reproducible educational experiment. See README for limitations."""
import json
from pathlib import Path
import numpy as np

def save(result, output):
    Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
TRAIN={
"billing":["why was my card charged twice","please explain the invoice amount","I need a refund for this payment","where can I download my receipt","update my billing address","my payment has failed","the subscription price is wrong","cancel the automatic renewal","I was overcharged this month","how do I change my card"],
"access":["I cannot log into my account","reset my password please","the login code is not arriving","my account is locked","I forgot my username","two factor authentication failed","the sign in screen rejects my password","help me regain account access","I lost my recovery code","my authentication token expired"],
"technical":["the application crashes on launch","uploading a file causes an error","the page freezes when I click save","the app runs very slowly","the download is stuck","my screen goes blank","the software will not install","a server error appears","the export button is broken","the search function returns no results"]}
TEST={"billing":["my invoice has an extra charge","I want a payment refund","change the subscription card","send me the billing receipt"],"access":["the password reset link failed","I cannot access my locked account","my login authentication code is missing","please help with sign in"],"technical":["the app crashes during file upload","the save button freezes the page","download shows a server error","installation is stuck on a blank screen"]}
def corpus(data):
    return [t for label in sorted(data) for t in data[label]],[label for label in sorted(data) for t in data[label]]
def run(output="results.json"):
    texts,y=corpus(TRAIN); test,yt=corpus(TEST)
    model=make_pipeline(TfidfVectorizer(ngram_range=(1,2)),LogisticRegression(C=4,max_iter=1000,random_state=42))
    pred=model.fit(texts,y).predict(test)
    return save({"seed":42,"train_rows":len(y),"test_rows":len(yt),"accuracy":float(accuracy_score(yt,pred)),"macro_f1":float(f1_score(yt,pred,average="macro")),"majority_accuracy":1/3,"labels":sorted(TRAIN),"confusion_matrix":confusion_matrix(yt,pred,labels=sorted(TRAIN)).tolist(),"predictions":[{"text":t,"actual":a,"predicted":str(p)} for t,a,p in zip(test,yt,pred)]},output)

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
