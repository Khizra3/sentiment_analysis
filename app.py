import streamlit as st
import pickle 
import sklearn
# load model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# create title
st.title('Sentiment Analysis')

review = st.text_input('Enter a Sentence to Predict:')

submit = st.button('Run')

if submit:
    prediction = model.predict([review])

    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('Positive')
    else:
        st.warning('Negative')
