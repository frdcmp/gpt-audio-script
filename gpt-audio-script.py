from openai import OpenAI
import streamlit as st
import pandas as pd
import prompts

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def gpt(system_prompt, model):
    response = client.chat.completions.create(
    model = model,
    messages=[
        {"role": "system", "content": "You are a script editor and proofreader. You only reply with the correct text, and never write explanations."},
        {"role": "user", "content": system_prompt},
    ]
    )
    return (response.choices[0].message.content)


st.set_page_config(layout="wide")
st.title("GPT Audio Script")

# Input for the text to be synthesized
prompt_variables = {var: getattr(prompts, var) for var in dir(prompts) if not var.startswith("__")}
selected_prompt = st.selectbox("Select a prompt:", list(prompt_variables.keys()))
placeholder_text = prompt_variables[selected_prompt]

#placeholder_text = st.checkbox"Improve the script by adding commas and dots to enhance readibility. Only add commas without altering the script otherwise:"
prompt = st.text_area("Prompt:", value=placeholder_text)
model = st.selectbox("Select GPT model", ("gpt-4-0125-preview", "gpt-4", "gpt-3.5-turbo", "gpt-4-turbo-preview"))

with st.expander ("Try on single text", expanded=False):
    single_text = st.text_area("Text", value="なじみのない環境に行き長期間過ごすと ストレスがたまります 参加組織には別途メンタルウェルビーイング・アプリがあり セルフヘルプやプロの支援が提供されます")
    if st.button("GPT", type="primary", use_container_width = True):
        system_prompt = f"{prompt} \n`{single_text}`"
        df = pd.DataFrame([single_text], columns=["Text"])
        gpt = gpt(system_prompt, model)
        st.code(gpt)

with st.expander ("Audio script", expanded=True):
    uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "csv"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "xlsx":
            df = pd.read_excel(uploaded_file)
        elif file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload an Excel or CSV file.")
        st.dataframe(df, use_container_width=True, hide_index=True)
        # Let the user select the column for 'ID'
        column_select = st.multiselect("Select Column for Text", df.columns)

        if len(column_select) == 1:
            text_column = column_select[0]  # Only one column selected
        if len(column_select) == 2:
            text_column_1 = column_select[0]
            text_column_2 = column_select[1]

        if st.button ("Script GPT", type="primary", use_container_width = True):
            if len(column_select) == 1:
                with st.spinner('GPT in Progress...'):
                    my_bar = st.progress(0)
                    total_rows = len(df)
                    for index, row in df.iterrows():
                        script = row[text_column]
                        system_prompt = f"{prompt}:\n\n{script}"
                        #st.write(system_prompt)
                        df.at[index, 'GTP'] = gpt(system_prompt, model)
                        my_bar.progress((index + 1) / total_rows)
                st.dataframe(df, use_container_width=True, hide_index=True)

            if len(column_select) == 2:
                with st.spinner('GPT in Progress...'):
                    my_bar = st.progress(0)
                    total_rows = len(df)
                    for index, row in df.iterrows():
                        script_1 = row[text_column_1]
                        script_2 = row[text_column_2]
                        system_prompt = f"{prompt}:\n\nText 1:\n{script_1}\n\nText 2:\n{script_2}"
                        st.write(system_prompt)
                        df.at[index, 'GTP'] = gpt(system_prompt, model)
                        my_bar.progress((index + 1) / total_rows)
                st.dataframe(df, use_container_width=True, hide_index=True)
