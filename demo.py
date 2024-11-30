import requests
import json
import streamlit as st

# Define API endpoint and headers
url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}

history = []

# Response generation function
def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "Brainrot AI",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        actual_response = response_data.get('response', 'No response received.')
        return actual_response
    else:
        return f"Error: {response.text}"

st.title("Brainrot AI 🤖💻")
st.write("Explaining code like your chaotic bestie would!")

user_input = st.text_area("Enter your prompt:", placeholder="Ask me anything about code...")

if st.button("Generate Response"):
    if user_input.strip():
        response = generate_response(user_input)
        st.markdown(f"**Brainrot AI says:**\n\n{response}")
    else:
        st.warning("Please enter a prompt before clicking 'Generate Response'.")
