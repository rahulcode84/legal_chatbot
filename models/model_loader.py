from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv
import logging

# Set up logging
logger = logging.getLogger("legal_assistant")

# Load environment variables
load_dotenv()

def load_models():
    """Initialize and return LLM models"""
    
    # Initialize OpenAI models with GPT-4 for maximum accuracy
    try:
        # Use the latest GPT-4 model for maximum accuracy on legal questions
        openai_model = ChatOpenAI(
            model="gpt-4-turbo", 
            temperature=0.2,  # Lower temperature for more factual responses
            max_tokens=4000    # Allow for detailed responses
        )
        logger.info("Successfully loaded GPT-4 model")
    except Exception as e:
        # Fallback to default ChatGPT if specific model isn't available
        logger.warning(f"Failed to load GPT-4, falling back to default: {str(e)}")
        openai_model = ChatOpenAI(temperature=0.2)
    
    # Use Ollama for local LLM if available
    try:
        llama_model = OllamaLLM(
            model='llama3.1',
            temperature=0.1  # Lower temperature for classification tasks
        )
        logger.info("Successfully loaded Llama model")
    except Exception as e:
        logger.warning(f"Failed to load Llama model: {str(e)}")
        # Fallback to OpenAI if Ollama isn't available
        llama_model = openai_model

    # Load Phi-3 model
    try:
        phi3_model = OllamaLLM(
            model='phi3',
            temperature=0.1
        )
        logger.info("Successfully loaded Phi-3 model")
    except Exception as e:
        logger.warning(f"Failed to load Phi-3 model: {str(e)}")
        # Fallback to OpenAI if Phi-3 isn't available
        phi3_model = openai_model
    
    return {
        "openai": openai_model,  # Primary model for detailed legal responses
        "llama": llama_model,    # Used for classification
        "phi3": phi3_model       # Alternative model
    }