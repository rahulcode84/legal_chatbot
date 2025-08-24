from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda
import json

class ContentType(BaseModel):
    content_type: str = Field(description="Classification of the query as either 'legal' or 'non-legal'.")
    confidence: float = Field(description="Confidence score between 0.0 and 1.0")
    reasoning: str = Field(description="Brief explanation for the classification")

def create_classifier_chain(llm):
    """Create and return the classifier chain"""
    str_parser = StrOutputParser()
    
    # Enhanced Classification prompt with Indian law specifics
    legal_classifier_template = PromptTemplate(
        template="""
        You are an AI model specialized in classifying queries as legal or non-legal, with particular expertise in Indian law.
        
        LEGAL queries include any questions or requests related to:
        - Laws, statutes, or legal codes (especially Indian law)
        - Indian Constitution and constitutional articles
        - Supreme Court of India and High Court cases or legal precedents
        - Indian legal procedures or processes
        - Legal rights, obligations, or liabilities in India
        - Government regulations or compliance with Indian law
        - Constitutional matters of India
        - Criminal or civil law in India
        - Legal documents or contracts under Indian law
        - Legal advice or interpretation of Indian laws
        - Indian legal systems or institutions
        
        NON-LEGAL queries are anything not directly related to the legal topics above, such as:
        - General knowledge questions
        - Technical support requests
        - Personal advice unrelated to legal matters
        - Entertainment queries
        - Mathematics or science questions
        - Travel, food, or general lifestyle questions
        
        Analyze the following query carefully:
        
        Query: {user_input}
        
        Return ONLY a simple JSON object with these three fields, nothing else:
        {{"content_type": "legal or non-legal", "confidence": 0.0-1.0, "reasoning": "brief explanation"}}
        
        No additional formatting, markdown, explanation, or properties wrappers.
        """,
        input_variables=['user_input']
    )
    
    # Functions for processing LLM output
    def fix_json(text_output):
        """Extract valid JSON from model output which might contain formatting issues"""
        try:
            # Find the first { and last } to extract just the JSON part
            start = text_output.find('{')
            end = text_output.rfind('}') + 1
            if start >= 0 and end > 0:
                json_str = text_output[start:end]
                # Parse the extracted JSON
                parsed = json.loads(json_str)
                return parsed
            return {"content_type": "non-legal", "confidence": 0.0, "reasoning": "Failed to parse output"}
        except json.JSONDecodeError:
            return {"content_type": "non-legal", "confidence": 0.0, "reasoning": "Failed to parse output"}

    def convert_to_pydantic(json_dict):
        """Convert dictionary to ContentType object"""
        return ContentType(**json_dict)
    
    # Build the classification chain
    classifier_chain = (
        legal_classifier_template
        | llm
        | str_parser
        | RunnableLambda(fix_json)
        | RunnableLambda(convert_to_pydantic)
    )
    
    return classifier_chain