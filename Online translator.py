import openai
import streamlit as st
import time
from docx import Document
openai.api_key = ""

st.title(" Online Document Translater with OpenAI")
uploaded_documet = st.file_uploader("Upload your file",type=["docx"])

def read_docx_content(document):
    doc = Document(document)
    content = []
    
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    
    return '\n'.join(content)

def split_document_into_chunks(document_content, chunk_size):
    paragraphs = document_content.split('\n')
    chunks = []
    current_chunk = []

    for paragraph in paragraphs:
        current_chunk.append(paragraph + '\n')

        if sum(len(line) for line in current_chunk) > chunk_size:
            chunks.append(''.join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(''.join(current_chunk))

    return chunks

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if uploaded_documet is not None:
    target_language = st.text_input("Enter the language you want to translate to") 
    name_of_country = st.text_input("Enter the name of the country")
    chunk_size = 500  # Adjust the chunk size based on your token limit
    translate = st.button("Translate")
    if translate:
        st.write("Translating...")
        # Step 1: Read the DOCX file
        document_content = read_docx_content(uploaded_documet)

        # Step 2: Split the document into smaller chunks
        document_chunks = split_document_into_chunks(document_content, chunk_size)

        # Step 3: Translate each chunk using ChatGPT prompts
        translated_chunks = []
        chunks = []

        for chunk in document_chunks:
            prompt = f"""Translate the following text delimited by triple backticks to {target_language} and 
            change the people name present in the text to common name of {name_of_country} 
            Note: Always use the same names for future instances. For example, if "Alex Smith" is present in the text and you translate it, then use the same name whenever "Alex Smith" appears again.\n```{chunk}```
            display only the translated text.
            """
            response = get_completion(prompt, model="gpt-3.5-turbo")
            translated_chunk = response
            translated_chunks.append(translated_chunk)
            time.sleep(10)

            # Print or save the translated chunks
        for i, translated_chunk in enumerate(translated_chunks):
            st.write(f"{translated_chunk}\n")
            chunks.append(translated_chunk)

        # Step 4: Combine the translated chunks into a single document
        document = '\n\n'.join(chunks)
    
        st.download_button(label="Download Translated Document as docx",data= document,
                           file_name=f"document_translated_{target_language}.docx",
                           mime='application/octet-stream', key=321)
        st.download_button(label="Download Translated Document as txt",data= document)
                           
