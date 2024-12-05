# Importing Libraries
import requests
import json
import gradio as gr
import streamlit


url = "http://localhost:11434/api/generate"

# header
headers = {

    'Content-Type':'application/json'
}

history=[]

# response generation
def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"gid30n",
        "prompt":final_prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)
        
# gradio UI
interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch(share = True)