from data import time
from context import ActionContext
from file_reader import resume_read
from agent import Agent
from display import *
def main():
        print("--------------------------")
        print("--------------------------")
        time.sleep(1)
        print("Welcome to ResumeGuider")
        time.sleep(1)
        context=ActionContext()
        context.user_input=resume_read()

        agent=Agent
        agent.extract(context)
        agent.analyse(context)
        agent.recommend(context)
        agent.upskill(context)
        agent.rating(context)

        show_extracted_content(context)
        show_analysed_content(context)
        show_recom_content(context)
        show_upskilling_content(context)
        show_rating(context)

if __name__=="__main__":
    main()        

