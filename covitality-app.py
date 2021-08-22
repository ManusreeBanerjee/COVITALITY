import streamlit as st
import base64
import sklearn
import pandas as pd
import numpy as np
import pickle as pkl
from csv import writer
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
#Load the saved model
#model=pkl.load(open("final_model.p","rb"))



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
    elif risk >= 15 and page <=25:
      report = '<p style="font-family:sans-serif; color:Yello; font-size: 20px;">Moderate Mortality Risk</p>'
      st.markdown(report, unsafe_allow_html=True)
      st.write("Mortality Risk Score is ",risk)
      #st.write("Moderate Mortality Risk")
    else :
      report = '<p style="font-family:sans-serif; color:Red; font-size: 20px;">High Mortality Risk</p>'
      st.markdown(report, unsafe_allow_html=True)
      st.write("Mortality Risk Score is ",risk)
      #st.write("High Mortality Risk")


    

def preprocess(page,psex,ss_fev,ss_cou,ss_dys,ss_fa,co_dime,co_bp,co_kidis,co_lidis,co_cadis,co_obs,co_ild,co_imm,co_alc,co_smk,ss_oxsa,img_xray,tr_chis):   
 
    risk = 0
    # Pre-processing user input   
    if page<50:
          risk = risk+1
    elif page >= 50 and page <=59:
          risk = risk+2
    else :
          risk = risk+3

    if psex=="male":
          risk = risk+2
    else: risk = risk+1

    if ss_fev=="Present":
          risk = risk+2
    else: risk = risk+0

    if ss_cou=="Present":
          risk = risk+1
    else: risk = risk+0

    if ss_dys=="Present":
          risk = risk+2
    else: risk = risk+0

    if ss_fa=="Present":
          risk = risk+1
    else:  risk = risk+0

    if co_dime=="Present":
          risk = risk+2
    else:  risk = risk+0

    if co_bp=="Present":
          risk = risk+3
    else: risk = risk+1

    if co_kidis=="Present":
          risk = risk+3
    else:  risk = risk+1

    if co_lidis=="Present":
          risk = risk+3
    else:  risk = risk+1

    if co_cadis=="Present":
          risk = risk+3
    else:  risk = risk+1

    if co_obs=="Present":
          risk = risk+3
    else:  risk = risk+0

    if co_ild=="Present":
          risk = risk+3
    else:  risk = risk+0

    if co_imm=="Yes":
          risk = risk+3
    else:  risk = risk+0

    if co_alc=="Yes":
          risk = risk+3
    else:  risk = risk+0

    if co_smk=="Yes":
          risk = risk+3
    else:  risk = risk+1

    if ss_oxsa<90:
          risk = risk+4
    elif ss_oxsa >= 90 and ss_oxsa <=95:
          risk = risk+2
    else :
          risk = risk+0

    if img_xray=="Abnormal":
          risk = risk+3
    else: risk = risk+2

    if tr_chis=="Yes":
          risk = risk+1
    else: risk = risk+0


    
    #user_input=np.array(user_input)
    #user_input=user_input.reshape(1,-1)
    #user_input=scal.fit_transform(user_input)
    return risk

    

       
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">COVITALITY APP</h1> 
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



#user_input=preprocess(psex,ss_fev,ss_cou,ss_dys,ss_fa,co_dime,co_bp,co_kidis,co_lidis,co_cadis,co_obs,co_ild,co_imm,co_alc,co_smk,img_xray,tr_chis)
#pred=preprocess(page,psex,ss_fev,ss_cou,ss_dys,ss_fa,co_dime,co_bp,co_kidis,co_lidis,co_cadis,co_obs,co_ild,co_imm,co_alc,co_smk,ss_oxsa,img_xray,tr_chis)
#probability_class_1 = pred.item(1)
#prob = round(probability_class_1*100,1)

risk = preprocess(page,psex,ss_fev,ss_cou,ss_dys,ss_fa,co_dime,co_bp,co_kidis,co_lidis,co_cadis,co_obs,co_ild,co_imm,co_alc,co_smk,ss_oxsa,img_xray,tr_chis)

if st.button("Predict"):    
  mortality = score(risk)
  st.info("Don't forget to rate this app")
  
feedback = st.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)
  
if feedback:
    st.header("Thank you for rating the app!")

#if st.button("Predict"):    
 # if pred[0] == 0:
  #  st.error('You have higher chances of surviving COVID-19.')
    
  #else:
   # st.success('Warning! You have lower chances of surviving COVID-19!')
    
   

st.subheader("About App")

st.info("This web app is helps you to find out whether you are at a risk of mortality from COVID-19.")
st.info("Enter the required fields and click on the 'Predict' button to check your survival chances from COVID-19.")
st.info("Build using Extreme Gradient Boosting Model with AUC score of 94%.")


st.caption("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 