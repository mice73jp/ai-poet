from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from dotenv import load_dotenv
import streamlit as st

#load_dotenv()

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

prompt = ChatPromptTemplate.from_messages([
    ("system", "“You are a helpful assistant."),
    ("user", "{input}"),
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# st.title('This is a title')
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')

#제목
st.title('인공지능 시인')

#시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요")
st.write("시의 주제는", content )

# 시 작성 요청하기
if st.button("시 작성하기"):
    with st.spinner("시를 작성하는 중입니다..."):
        # 시 작성 요청
        result = chain.invoke({"input": content + "에 대한 시를 써줘."})
        st.write(result)
