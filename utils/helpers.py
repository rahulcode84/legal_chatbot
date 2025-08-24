import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("legal_assistant.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("legal_assistant")

def create_empty_files():
    """Create necessary directory structure and files"""
    directories = [
        'data',
        'logs',
        'models',
        'chains',
        'utils',
        'complaint_form'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")
    
    # Create empty __init__.py files in each directory
    for directory in directories:
        init_file = os.path.join(directory, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                pass
            logger.info(f"Created file: {init_file}")

def safe_invoke(chain, inputs, default_response="I apologize, but I encountered an error while processing your request. Please try again."):
    """Safely invoke a chain with error handling"""
    try:
        return chain.invoke(inputs)
    except Exception as e:
        logger.error(f"Error invoking chain: {str(e)}")
        return default_response