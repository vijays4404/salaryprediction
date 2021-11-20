import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt





def clean_experience(x):
    if x=='More than 50 years':
        return 50
    if x=='Less than 1 year':
        return 0.5
    return float(x)




@st.cache
def load_data():
    df=pd.read_csv('survey_results_public.csv')
    df=df[['Country','EdLevel','YearsCodePro','Employment','ConvertedComp']]
    df=df.rename({'ConvertedComp':'Salary'},axis=1)
    df=df[df['Salary'].notnull()]
    df=df[df['Employment']=='Employed full-time']
    #df['EdLevel']=df['EdLevel'].apply(clean_education)
    df['YearsCodePro']=df['YearsCodePro'].apply(clean_experience)
    #df['EdLevel']=df['EdLevel'].apply(clean_education)
    return df

df=load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salary")
    st.write(
        """
        Stock OverFlow Developer Survey 2020
        
        """
    )
    data=df['Country'].value_counts()
    fig1,ax1=plt.subplots()
    ax1.pie(data,labels=data.index)
    ax1.axis('equal')

    st.write("""
    
    Numnber of Data from different countries
    
    
    """)
    st.pyplot(fig1)



    st.write("""
    
   Mean Salary based on country
    
    
    """)
    data=df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)
  

    
    st.write("""
    
   Mean Salary based on experience
    
    
    """)
    data=df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)