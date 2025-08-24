from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda
import os
from typing import Dict, Any

# This file will provide specialized knowledge about Indian constitutional law

def create_indian_law_chain(models):
    """Create a chain specifically for handling Indian constitutional law queries"""
    
    # Parser for output
    str_parser = StrOutputParser()
    
    # Detailed prompt for Indian constitutional law
    indian_constitution_prompt = PromptTemplate(
        template="""
        You are an expert on the Indian Constitution and constitutional law.
        
        IMPORTANT KNOWLEDGE BASE:
        - The Constitution of India has 448 articles in 25 parts and 12 schedules.
        - The Constitution was adopted on 26 November 1949 and came into effect on 26 January 1950.
        - Part III of the Constitution covers Fundamental Rights (Articles 12-35).
        - Part IV covers the Directive Principles of State Policy (Articles 36-51).
        - The Supreme Court of India is the guardian of the Constitution.
        - Articles 14-18 deal with Right to Equality.
        - Articles 19-22 cover Right to Freedom.
        - Article 21 deals with Right to Life and Personal Liberty.
        - Articles 23-24 prohibit exploitation.
        - Articles 25-28 ensure Right to Freedom of Religion.
        - Articles 29-30 protect Cultural and Educational Rights.
        - Article 32 provides the Right to Constitutional Remedies.
        
        USER QUERY: {user_input}
        
        Provide a detailed, accurate, and well-structured answer about the Indian Constitution based on the query:
        """,
        input_variables=["user_input"]
    )
    
    # Function to check if the query is about Indian constitutional law
    def is_constitution_query(user_input: str) -> bool:
        constitution_keywords = [
            "indian constitution", "article", "fundamental right", "directive principle",
            "amendment", "preamble", "constitutional", "supreme court", "high court",
            "writ", "habeas corpus", "mandamus", "prohibition", "certiorari", "quo warranto"
        ]
        
        user_input_lower = user_input.lower()
        return any(keyword in user_input_lower for keyword in constitution_keywords)
    
    # Function to route queries
    def route_constitutional_query(inputs: Dict[str, Any]):
        user_input = inputs["user_input"]
        
        if is_constitution_query(user_input):
            # Use a more capable model for constitutional queries
            return models["llama"].invoke(indian_constitution_prompt.format(user_input=user_input))
        else:
            # Use the standard legal chain for other legal queries
            return None  # This will fall back to the standard legal chain
            
    return RunnableLambda(route_constitutional_query) | str_parser