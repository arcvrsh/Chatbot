import streamlit as st
import pandas as pd
import os

st.title("Skillshop Chatbot Admin")
choices=["View Dataset","Add Queries","Add Bot Responses"]
tags=["timing","delivery","offers","address","combo","menu","special day(wednesday)"]
userchoice=st.sidebar.selectbox("menu",choices)

Q_Dataset="query_dataset.csv"
R_Dataset="bot_response_dataset.csv"

qdf=None
rdf=None

if os.path.exists(Q_Dataset):
    qdf=pd.read_csv(Q_Dataset)

if os.path.exists(R_Dataset):
    rdf=pd.read_csv(R_Dataset)
   

if userchoice==choices[0]:
    #code for displaying data
    st.header("Select a dataset")
elif userchoice==choices[1]:
    #code for adding queries
    dataset=[]
    st.header("Add new customer queries")
    question=st.text_input("A customer query")
    tag=st.selectbox("select a tag",tags)
    clicked=st.button("save")

    if clicked and question:
        data={"query":question,"tag":tag}
        dataset.append(data)
        tempdf=pd.DataFrame(dataset)

        if isinstance(qdf,pd.DataFrame):
            # save to existing file
            qdf=qdf.append(tempdf)
            qdf.to_csv(Q_Dataset,index=False)
            st.success("query saved successfully")
        else:
            # only runs for very first time
            tempdf.to_csv(Q_Dataset,index=False)
            st.success("query saved successfully")
else:
    #code for adding responses
    dataset=[]
    st.header("Add new bot responses")
    tag=st.selectbox("select a tag",tags)
    response=st.text_input("Bot response")
    clicked=st.button("save")

    if clicked and response:
        data={"bot_response":response,"tag":tag}
        dataset.append(data)
        tempdf=pd.DataFrame(dataset)

        if isinstance(rdf,pd.DataFrame):
            rdf=rdf.append(tempdf)
            rdf.to_csv(R_Dataset,index=False)
            st.success("response saved successfully")
        else:
            tempdf.to_csv(R_Dataset,index=False)
            st.success("response saved successfully")
