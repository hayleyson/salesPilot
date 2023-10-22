import openai
import streamlit as st
import requests

st.title("DistilGPT-based chatbot")

# openai.api_key = st.secrets["OPENAI_API_KEY"]

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # messages = [f"{m['content']}" for m in st.session_state.messages]
        # messages = "\n".join(messages)
        
        input_obj = {"input_text": prompt}
        print(input_obj)
        res = requests.post("http://127.0.0.1:5000/api/request_answer", data=input_obj)
        print(res.content.decode('utf-8'))
        
        if res.status_code == 200:
            res = eval(res.content.decode('utf-8'))['response_text']
                
            for token in res.split(" "):
                full_response += f" {token}"
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        else:
            message_placeholder.markdown("Error: Unable to fetch data from the API.")
        
        
        # for response in openai.ChatCompletion.create(
        #     model=st.session_state["openai_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # ):
        #     full_response += response.choices[0].delta.get("content", "")
        #     message_placeholder.markdown(full_response + "▌")
        # message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})