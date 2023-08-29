# GRIFFINGGIST

## Overview
The purpose of this code is to create an application that summarizes PDF documents using the OpenAI API. It reads a PDF file, extracts the text, and then uses the OpenAI language model to generate a summary. The code uses the Gradio library to create a web interface for the application.

## API Key
To use GriffinGist, you must have an API key from OpenAI. This key is used to authenticate requests to OpenAI. Refer to OpenAI's documentation for information on how to obtain an API key. Once obtained, create a file named apikey.txt in the same directory as the Python files and store the API key in this file.

## Key Features and Capabilities
The code consists of the following main parts:
* Loading the OpenAI API key: The code reads the API key from a file, sets it, and then initializes the OpenAI language model.
* Summarizing the PDF: The custom_summary function takes a PDF file path and an optional custom prompt as input, extracts the text from the PDF, and then generates a summary using the OpenAI language model. It returns both a regular summary and a custom summary if a custom prompt is provided.
* User Interface: The main function creates a web interface using the Gradio library. The interface consists of two text boxes for the user to input the PDF file path and an optional custom prompt, and two text boxes to display the summary and custom summary.

## Technology Stack
* OpenAI: Used for generating the summary of the PDF document using the OpenAI language model.
* LangChain: This comprehensive framework was chosen for developing the application powered by the OpenAI language model.
* Gradio: Gradio offers a quick and user-friendly way to create web interfaces for machine learning models, which is why it was chosen to create the web interface for this application.

## Install required packages
Use the command below to install the packages according to the configuration file `requirements.txt`.

```
$ pip install -r requirements.txt
```

## Usage
To use the griffingist.py script, follow these steps:
* Open a terminal and navigate to the griffingist directory.
* Run the script using the following command:
```
$ python3 ./griffingist.py
```
* Open a web browser and navigate to http://localhost:7860/.
* Enter the absolute path to the PDF file and an optional custom prompt for summarization.
* Click the "Submit" button to generate the summary and custom summary (if a custom prompt is supplied).
