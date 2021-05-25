from os import read
from flask import Flask,render_template,request,jsonify
import pandas as pd
import pickle as pkl
import random

app = Flask(__name__)

model_data={}
with open('model.pkl','rb') as f:
    model_data=pkl.loads(f.read())

rdf=pd.read_csv('bot_response_dataset.csv')

def predict_tag(txt="Hello World",binarizer=None,model=None,vectorizer=None,*args,**kwargs):
    input_vector=vectorizer.transform([txt])
    result=model.predict(input_vector)
    output_tag=binarizer.inverse_transform(result)
    return output_tag[0]

def get_bot_reply(predicted_tag):
    result_df=rdf[rdf['tag']==predicted_tag]
    responses=result_df.bot_response.to_list()
    return random.choice(responses)


@app.route('/')
def index():
    return render_template('index.html',title='Skillshop Chatbot')

@app.route('/predict')
def predict():
    if request.args.get('query'):
        query=request.args.get('query')
        tag=predict_tag(query,**model_data)
        if tag:
            response=get_bot_reply(tag)
        else:
            response="sorry i'm still learning.Call us for more info"
    else:
        response="please ask me a question"
    return jsonify({'botreply': response,'query': query})


if __name__ == '__main__':
    app.run()