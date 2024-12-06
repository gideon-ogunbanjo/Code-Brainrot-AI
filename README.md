# Code-Brainrot-AI

Brainrot AI is an interactive, cutting-edge code assistant designed to answer all your programming questions with accuracy, precision, and a touch of Gen Z flair. The app interacts with a model ```gid30n``` powered by LLama, this assistant ensures your coding journey is insightful and engaging. Whether you're debugging, learning, or exploring new tech, Brainrot AI has your back!

✨ Features
- Interactive Chat: Continuously tracks your conversation history for contextual responses.
- Multi-Programming Language Support: Covers a broad range of programming languages and paradigms.
- Gen Z Personality: Explains code concepts with clarity and a hint of modern creative expression.
- Gradio-Powered Interface: Easy-to-use web-based interface for seamless interaction.
- Custom API Integration: Communicates with a local API for flexible, fast, and accurate code assistance.

🚀 Quick Start
* Requirements
To get started, ensure you have the following installed on your system:

- Python 3.10+
- Gradio (pip install gradio)
- Requests (pip install requests)
- You also need access to a local API service running at http://localhost:11434/api/generate (or a custom URL).

### Installation
1. Clone this repository:

```bash
git clone https://github.com/gideon-ogunbanjo/Code-Brainrot-AI
cd brainrot-ai
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the API URL (optional):
If you're using a custom API URL, set it as an environment variable:

```bash
export API_URL="http://your-api-url/api/generate"
```
4. Run the application:

``` bash
python app.py
```
Open your browser to the provided URL and start chatting with Brainrot AI!

🌟 How It Works
- User Input: Enter your coding-related questions in the Gradio textbox.
- API Interaction: The app sends your question (and conversation history) to a locally hosted API for processing.
- AI Response: Brainrot AI, powered by the Gid30n model, generates an insightful and Gen Z-styled answer, which is displayed in the Gradio interface.
- History Management: Tracks the conversation history to provide context-aware responses throughout the session.

🛠 Technologies
- Python: The foundation of the app.
- LLama: A powerful language model used for generating responses to programming-related queries
- Gradio: A simple and beautiful UI framework.
- Requests: Handles communication with the local API.

### Creator:
Gideon Ogunbanjo.
