import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import pickle as pkl
import plotly
import plotly.graph_objects as go
from csv import writer


st.set_page_config(page_title="COVITALITY APP",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")

st.sidebar.header('User Input Parameters')

# load spreadsheet with data to be annotated
def get_data():
  return []

def score(risk):
    
    if risk<15:
      report = '<p style="font-family:sans-serif; color:Green; font-size: 20px;">Low Mortality Risk</p>'
      st.markdown(report, unsafe_allow_html=True)
      st.write("Mortality Risk Score is ",risk)
      #st.write("Low Mortality Risk")
    elif risk >= 15 and risk <=25:
      report = '<p style="font-family:sans-serif; color:Yello; font-size: 20px;">Moderate Mortality Risk</p>'
      st.markdown(report, unsafe_allow_html=True)
      st.write("Mortality Risk Score is ",risk)
      #st.write("Moderate Mortality Risk")
    else :
      report = '<p style="font-family:sans-serif; color:Red; font-size: 20px;">High Mortality Risk</p>'
      st.markdown(report, unsafe_allow_html=True)
      st.write("Mortality Risk Score is ",risk)
      #st.write("High Mortality Risk")


def preprocess(page,ss_dys,co_imm,ss_oxsa,img_xray):   
 
    risk = 0
    # Pre-processing user input   
    if page<60:
          risk = risk+0
    else :
          risk = risk+19

    if ss_dys=="Present":
          risk = risk+9
    else: 
          risk = risk+0

    if co_imm=="Yes":
          risk = risk+29
    else:  risk = risk+0

    if ss_oxsa>=92:
          risk = risk+0
    else :
          risk = risk+15

    if img_xray=="Abnormal":
          risk = risk+28
    else: risk = risk+0
    
   
    return risk

    

       
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:#7D0552;padding:13px"> 
    <h1 style ="color:white;text-align:center;">COVITALITY APP</h1> 
    </div> 
    """
      
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by MANUSREE BANERJEE ')
      
# following lines create boxes in which user can enter data required to make prediction
pname = st.sidebar.text_input('Patient Name')
pid = st.sidebar.text_input('Patient ID')
page=st.sidebar.slider("Age",1,100)
psex = st.sidebar.radio("Select Gender: ", ('male', 'female'))
ss_fev = st.sidebar.selectbox('Fever',("Present","Absent")) 
ss_cou = st.sidebar.selectbox('Cough', ("Present","Absent"))
ss_dys = st.sidebar.selectbox('Dyspnea', ("Present","Absent"))
ss_fa = st.sidebar.selectbox('Fatigue', ("Present","Absent"))
co_dime = st.sidebar.selectbox('Diabetes Mellitus', ("Present","Absent"))
co_bp = st.sidebar.selectbox('Hypertension', ("Present","Absent"))
co_kidis = st.sidebar.selectbox('Chronic kidney disease', ("Present","Absent"))
co_lidis = st.sidebar.selectbox('Chronic liver disease', ("Present","Absent"))
co_cadis = st.sidebar.selectbox('Chronic cardiac disease', ("Present","Absent"))
co_obs = st.sidebar.selectbox('Obesity', ("Present","Absent"))
co_ild = st.sidebar.selectbox('Chronic pulmonary disease ', ("Present","Absent"))
co_imm = st.sidebar.selectbox('Is patient on Immunosuppressant / Steroids ?', ("Yes","No"))
co_alc = st.sidebar.selectbox('Did patient drink alcohol within past 5 years ?', ("Yes","No"))
co_smk = st.sidebar.selectbox('Did patient smoke within past 5 years ?', ("Yes","No"))
ss_oxsa = st.sidebar.slider('Oxygen Saturation',0,100)
img_xray = st.sidebar.selectbox('X-ray report ', ("Normal","Abnormal"))
tr_chis = st.sidebar.selectbox('Contact/Travel history', ("Yes","No"))





risk = preprocess(page,ss_dys,co_imm,ss_oxsa,img_xray)

if st.button("Risk Strata Key"):
  # display table
  fig=go.Figure(data=go.Table(header=dict(values=['Risk Category', 'Risk Score'],fill_color='#FD8E72',font_size=18,align='center'),
                            cells=dict(values=[['Low','High'],['<36','>=36']],fill_color='#F9B7FF',font_color=['black'],font_size=14,align='center')))

  #fig.update_layout(autosize=True,margin=dict(l=0,r=0,b=0,t=0))
  fig.update_layout(autosize=False,
                  width=800,
                  height=350
                 )
  st.write(fig)

if st.button("Predict"):    
  mortality = score(risk)
  st.info("Don't forget to rate this app")
  
feedback = st.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)
  
if feedback:
    st.header("Thank you for rating the app!")


    
   

st.subheader("About App")

st.info("This web app is helps you to find out whether you are at a risk of mortality from COVID-19.")
st.info("Enter the required fields and click on the 'Predict' button to check your survival chances from COVID-19.")
st.info("Build using Extreme Gradient Boosting Model with AUC score of 94%.")


st.caption("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 