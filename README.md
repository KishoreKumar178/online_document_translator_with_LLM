# Online Document Translator with OpenAI

## Project Description
The "Online Document Translator with OpenAI" is a web-based application that utilizes OpenAI's GPT-3.5 Turbo model to translate text from a DOCX file into the desired target language while also replacing specific names in the text with common names associated with a given country.

## Key Features
- User-Friendly Interface
- DOCX File Upload
- Target Language Selection
- Name Replacement
- Chunking for Translation
- Real-Time Translation
- GPT-3.5 Turbo Translation
- Download Translated Document

## How It Works
1. **Upload Document:** Users upload a DOCX file containing the text they want to translate.
2. **Specify Target Language:** Users enter the target language into which they want the document translated.
3. **Provide Country Name:** Optionally, users can specify the name of a country to be used for replacing specific names in the text for more contextually relevant translations.
4. **Translate:** Users click the "Translate" button to initiate the translation process.
5. **Real-Time Translation:** The application divides the document into smaller chunks and translates each chunk using the OpenAI GPT-3.5 Turbo model.
6. **Display Translated Text:** The translated text from each chunk is displayed in real-time on the web interface.
7. **Download:** Once the entire document is translated, users can download the translated document in both DOCX and plain text formats.

## Installation
To run this project locally, follow these steps:
1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set your OpenAI API key in the `openai.api_key` variable.
4. Run the application with `streamlit run app.py`.

## Acknowledgements
- This project uses the [OpenAI GPT-3.5 Turbo](https://beta.openai.com/signup/) model for language processing.

## Author
Kishore Kumar M
