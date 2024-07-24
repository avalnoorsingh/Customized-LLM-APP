import gradio as gr
from huggingface_hub import InferenceClient
from typing import List, Tuple
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util
import numpy as np
import faiss

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

# Placeholder for the app's state
class MyApp:
    def __init__(self) -> None:
        self.documents = []
        self.embeddings = None
        self.index = None
        self.load_pdf("pilot_guide.pdf")
        self.build_vector_db()

    def load_pdf(self, file_path: str) -> None:
        """Extracts text from a PDF file and stores it in the app's documents."""
        doc = fitz.open(file_path)
        self.documents = []
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            self.documents.append({"page": page_num + 1, "content": text})
        print("PDF processed successfully!")

    def build_vector_db(self) -> None:
        """Builds a vector database using the content of the PDF."""
        model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = model.encode([doc["content"] for doc in self.documents])
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
        print("Vector database built successfully!")

    def search_documents(self, query: str, k: int = 3) -> List[str]:
        """Searches for relevant documents using vector similarity."""
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode([query])
        D, I = self.index.search(np.array(query_embedding), k)
        results = [self.documents[i]["content"] for i in I[0]]
        return results if results else ["No relevant documents found."]

app = MyApp()

def respond(
    message: str,
    history: List[Tuple[str, str]],
    system_message: str,
    max_tokens: int,
    temperature: float,
    top_p: float,
):
    system_message = "Knowledgeable DBT (Dialectical Behavior Therapy) coach Focuses on one topic/option at a time Uses friendly greetings and asks thoughtful questions like a human counselor Keeps responses concise and avoids long-winded answers Listens attentively and provides accurate, helpful information Treats users with respect, considering their emotional state Refers to external resources (e.g. DBT workbooks) when relevant Asks one clarifying question at a time to guide the conversation Avoids suggesting anything potentially dangerous and advises seeking emergency help if needed." 
    messages = [{"role": "system", "content": system_message}]

    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    messages.append({"role": "user", "content": message})

    # RAG - Retrieve relevant documents
    retrieved_docs = app.search_documents(message)
    context = "\n".join(retrieved_docs)
    messages.append({"role": "system", "content": "Relevant documents: " + context})

    response = ""
    for message in client.chat_completion(
        messages,
        max_tokens=100,
        stream=True,
        temperature=0.98,
        top_p=0.7,
    ):
        token = message.choices[0].delta.content
        response += token
        yield response

demo = gr.Blocks()

with demo:
    gr.Markdown(
        "‼️Disclaimer: This chatbot is based on a DBT exercise book that is publicly available. and just to test RAG implementation.‼️"
    )
    
    chatbot = gr.ChatInterface(
        respond,
        examples=[
            ["What does effective flight management refer to?"],
            ["Explain the concept of situational awareness in the context of flight management."],
            ["What aspects of airmanship are evaluated during a flight test?"],
            ["How would you select the most favorable and appropriate cruising altitudes, considering weather, terrain, and equipment capabilities?"],
            ["How should the pilot secure the aircraft properly after parking, considering the existing or forecast weather conditions?"],
            ["After landing, what are the steps the pilot should take to clear the runway and taxi the aircraft to a suitable parking/refueling area?"],
            ["Why is it important for the pilot to position the flight controls appropriately based on the actual or simulated wind conditions during taxiing?"]
        ],
        title='AIR BUDDY 🛩️👩‍💻'
    )

if __name__ == "__main__":
    demo.launch()