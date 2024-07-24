---
title: SimpleRAGLLM
emoji: 🐨
colorFrom: red
colorTo: gray
sdk: gradio
sdk_version: 4.37.2
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
.....................................................................................................................................................................



AIR BUDDY - A professional flight attendant assistant
introduction
AIR BUDDY is a powerful flight management assistant that combines natural language processing, information retrieval, and deep learning to provide pilots with accurate and relevant information to enhance flight operations This service is designed to function as a knowledgeable and responsive partner

features
PDF Extraction and Indexing: AIR BUDDY PDF can extract information from aviation manuals and other related documents, creating a vector database for better information retrieval
Natural Language Search: Users can use natural language to query AIR BUDDY, and the application will search the indexed documents and provide the most relevant information.
Contextual responses: AIR BUDDY responses are tailored to the user’s question and conversation, ensuring that the information provided is accurate and helpful.
Structured Conversation: The program follows a structured conversation format, keeping the conversation going and providing clear, concise answers.
Research Sample Questions: AIR BUDDY provides a number of sample questions that users can explore to understand the breadth of the application's capabilities.

Detailed technical details
The AIR BUDDY application was developed using the following technology:

Gradio: A Python library for building interactive web applications.
Hugging Face Inference Client: An interactive library and language examples for Hugging Face.
PyMuPDF (fitz): Python binding for a PDF rendering library, used to extract text from PDF documents.
Sentence Transformers: A library for semantic embedding of text, for creating a vector database.
FAISS: A library for finding efficient similarities and aggregating dense vectors, used for vector database implementations.
The main features of the application are:

PDF extraction and indexing: the load_pdf and build_vector_db methods in the MyApp class handle extracting text from PDF files and creating a vector database, respectively
Natural Language Search: the search_documents method in the MyApp class searches for relevant documents based on the user’s query.
Context-sensitive response: The response service generates the final response to the user, taking into account the conversation history, the user query, and related documents received

Usage:
To use the AIR BUDDY application, just use the code provided. The application uses a Gradio-powered web interface, where users can interact with the chatbot and explore available sample questions.

Working with Python
Copy
if __name__ == "__main__": .
    demo.file() .
Future developments
Some potential areas for future growth include:

Integration of new data sources: Extending knowledge to include more aviation-related documents, such as regulations, advisory letters, and safety bulletins.
Individualized Recommendations: Create a system that provides personalized recommendations based on the user’s flight experience, aircraft type, and operating environment
More support: Enables the application to handle and respond to various input methods such as images, photos, and audio recordings.
Conversational capabilities: To enhance chatbots’ conversational capabilities to engage in natural contextual conversations.
Offline Accessibility: Look for ways to make the application offline, either by hiding context or by using a standalone desktop application.
conclusion
AIR BUDDY is a high-performance flight management assistant that uses natural language processing and advanced information retrieval techniques to provide pilots with the information they need to improve flight operations Provides powerful, contextual information combined with its user-friendly interface, AIR BUDDY aims to be an invaluable tool in the cockpit.
