# GPT Audio Script Editor

This Streamlit application serves as an interactive platform for editing and proofreading audio scripts using OpenAI's GPT models. Users can upload their scripts, select sections of text, and employ GPT models to refine the content, enhancing readability and overall quality.

## Features

- **GPT Audio Script**: Load your scripts from `.xlsx` or `.csv` files, select the column containing the text, and let the GPT model improve the content.
- **Single Text Editing**: Input individual text snippets for quick edits.
- **Model Selection**: Choose between different GPT models, including `gpt-4-0125-preview`, `gpt-4`, `gpt-3.5-turbo`, and `gpt-4-turbo-preview` for text generation and editing.
- **Interactive Chat**: Engage in a chat-like interface with GPT, providing queries and receiving responses in real-time.

## How to Run

1. **Set up your environment**:
   Ensure you have Python installed on your machine and install the required dependencies via pip:

   ```sh
   pip install openai streamlit pandas


2. **Add your OpenAI API key:**:
    The application requires an OpenAI API key to interact with GPT models. Add your API key in the     Streamlit secrets management system or directly in the code.

3. **Launch the application:**:
    Run the Streamlit application with the following command:
   ```sh
    streamlit run gpt-audio-script.py



## Usage
**Upload a Script:**
Click on the "Choose a file" button to upload your .xlsx or .csv file containing the script(s) you wish to edit.
Select Text for Editing: Use the provided dropdown menus to select the GPT model and the column(s) of text you want to process.
**Process & Review:**
Click on the "GPT" or "Script GPT" button to initiate the editing process. Review the generated outputs directly within the application interface.
**Contributing**
Contributions to enhance the application's functionality or to improve user experience are welcome. Please follow standard open-source contribution guidelines, including creating issues for bugs or feature requests and submitting pull requests for code changes.