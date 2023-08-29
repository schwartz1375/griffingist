import sys

import gradio as gr
import openai
from langchain import OpenAI, PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Read API Key from file
try:
    with open('apikey.txt', 'r') as f:
        openai.api_key = f.read().strip()

    if not openai.api_key:
        raise ValueError("API key not found in the file.")

    print("API key loaded successfully.")
except FileNotFoundError:
    print("The file 'apikey.txt' was not found.")
    sys.exit(1)
except ValueError as ve:
    print(ve)
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

# Initialize the OpenAI language model with a temperature of 0 to make the output completely deterministic
llm = OpenAI(openai_api_key=openai.api_key, temperature=0)
# Initialize a text splitter that splits the text into chunks based on character count
text_splitter = CharacterTextSplitter()


def custom_summary(pdf_file_path, custom_prompt=""):
    # Load and split the PDF document
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()
    # Load the summarize chain
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    # Run the chain and get the regular summary
    summary = chain.run(docs)
    # Create the custom summary if a custom prompt is provided
    if custom_prompt:
        # Create the prompt template
        prompt_template = custom_prompt + """

        {text}

        SUMMARY:"""
        PROMPT = PromptTemplate(template=prompt_template,
                                input_variables=["text"])
        # Load the summarize chain with the custom prompt
        chain = load_summarize_chain(llm, chain_type="map_reduce",
                                     map_prompt=PROMPT, combine_prompt=PROMPT)
        # Run the chain and get the custom summary
        custom_summary = chain({"input_documents": docs}, return_only_outputs=True)[
            "output_text"]
    else:
        custom_summary = ""

    return summary, custom_summary


def main():
    # Create the Gradio interface
    input_pdf_path = gr.inputs.Textbox(label="Enter the PDF file path")
    input_custom_prompt = gr.inputs.Textbox(label="Enter your custom prompt")
    output_summary = gr.outputs.Textbox(label="Summary")
    output_custom_summary = gr.outputs.Textbox(label="Custom Summary")

    iface = gr.Interface(
        fn=custom_summary,
        inputs=[input_pdf_path, input_custom_prompt],
        outputs=[output_summary, output_custom_summary],
        title="GRIFFINGGIST - PDF Summarizer",
        description="Enter the path to a PDF file and get its summary.",
    )

    # Launch the Gradio interface
    iface.launch()


if __name__ == "__main__":
    main()
