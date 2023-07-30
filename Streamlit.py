#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import pickle


# In[6]:


model = pickle.load(open(r"C:\Users\easil\Downloads\logisticregression.pkl",'rb'))


# In[7]:


def main():
    st.title("Cardio Heart Disease")

    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    smoking = st.selectbox("is_smoking_YES", ["1", "0"])
    prevalentHyp = st.selectbox(" prevalentHyp", ["1", "0"])
    diabetes= st.selectbox(" diabetes", ["1", "0"])
    totChol = st.number_input("totChol", min_value=0, max_value=300, step=1)
    sysBP = st.number_input("sysBP", min_value=0, max_value=200, step=1)
    glucose = st.number_input("glucose", min_value=0, max_value=200, step=1)
    
    # Convert categorical features to numeric values
    sex = 1 if sex == "Male" else 0
    
    user_data =pd.DataFrame ({'age': [age],
                 'sex': [sex],
                 'smoking': [smoking],
                 'prevalentHyp': [prevalentHyp],
                 'diabetes': [diabetes],
                 'totChol': [totChol],
                 'sysBP': [sysBP],
                 'glucose': [glucose]})

  
    user_df = pd.DataFrame(user_data, index=[0])

    prediction = model.predict(user_df)
    
    if st.button("Predict"):
        if prediction[0] == 0:
            st.error("The model predicts that you are not likely to have heart disease after 10 years.")
        else:
            st.success("The model predicts that you are likely to have heart disease after 10 years.")


if __name__ == "__main__":
    main()
    


# In[ ]:





# In[ ]:





# In[ ]:




