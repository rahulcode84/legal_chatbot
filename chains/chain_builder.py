from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from typing import Dict, Any
from indian_law_knowledge import create_indian_law_chain

def create_legal_chain(models, classifier_chain):
    """Create a chain that handles legal queries and gracefully handles non-legal queries"""
    
    # Parser for final output
    str_parser = StrOutputParser()
    
    # Create the Indian law specialized chain
    indian_law_chain = create_indian_law_chain(models)
    
    # General legal prompt
    legal_prompt = PromptTemplate(
        template="""
        You are an expert legal assistant specializing in Indian law and constitutional matters.
        
        IMPORTANT GUIDELINES:
        - When answering about Indian constitutional articles, cite the specific article numbers and provide accurate information.
        - Refer to relevant sections of laws, acts, and statutes when appropriate.
        - For questions about legal procedures, explain the steps clearly and in correct order.
        - If uncertain about a specific legal detail, acknowledge the limitations rather than providing potentially incorrect information.
        - Include references to relevant Indian legal precedents when applicable.
        
        USER QUERY: {user_input}
        
        CHAT HISTORY: {chat_history}
        
        Provide a clear, accurate, and helpful response about this legal question based on Indian law:
        """,
        input_variables=["user_input", "chat_history"]
    )
    
    # Template for non-legal responses
    non_legal_template = PromptTemplate(
        template="""
        I apologize, but I'm specifically designed to assist with legal queries related to law, constitutional matters, and legal procedures. 
        
        The query you provided appears to be unrelated to legal matters. I'd be happy to help if you have any questions about laws, legal rights, 
        court procedures, or other legal topics.
        
        Please feel free to ask a legal question, and I'll do my best to assist you.
        """,
        input_variables=[]
    )
    
    # Function to route based on classification
    def route_based_on_classification(inputs: Dict[str, Any]):
        user_input = inputs["user_input"]
        chat_history = inputs.get("chat_history", "")
        
        # Classify the input
        classification = classifier_chain.invoke({"user_input": user_input})
        
        # If it's a legal query, use the appropriate chain
        if classification.content_type.lower() == "legal":
            # Try the specialized Indian law chain first
            indian_law_result = indian_law_chain.invoke({"user_input": user_input})
            
            # If the specialized chain returned a result, use it
            if indian_law_result:
                return indian_law_result
            
            # Otherwise, fall back to the general legal chain
            return models["llama"].invoke(legal_prompt.format(
                user_input=user_input,
                chat_history=chat_history
            ))
        # If it's not a legal query, provide a polite rejection
        else:
            return non_legal_template.format()
    
    # Create the combined chain
    combined_chain = RunnableLambda(route_based_on_classification) | str_parser
    
    return combined_chain