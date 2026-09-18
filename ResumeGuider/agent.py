from context import ActionContext
from llm import LLm
from prompt import Prompt

class Agent():
    @staticmethod
    def extract(context):
        resume=context.user_input
        if resume:
            prompt=Prompt.extraction_prompt(context)
            response=LLm.generate_response(prompt)
            context.extracted_data=response
    @staticmethod
    def analyse(context):
        if context.extracted_data:
        
            prompt=Prompt.analyse_prompt(context)
            response=LLm.generate_response(prompt)
            context.analysed_data=response
    @staticmethod
    def recommend(context):
        if context.extracted_data:
            prompt=Prompt.recommendation_prompt(context)
            response=LLm.generate_response(prompt)
            context.recommendation_data=response
    @staticmethod  
    def upskill(context):
        if context.extracted_data:
            prompt=Prompt.upskilling_prompt(context)
            response=LLm.generate_response(prompt)
            context.upskilling_data=response
    @staticmethod
    def rating(context):
        if context.extracted_data:
            prompt=Prompt.ats_prompt(context)
            response=LLm.generate_response(prompt)
            context.rating=response


        