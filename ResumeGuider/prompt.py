from data import json
class Prompt:
    @staticmethod
    def extraction_prompt(context):
        agent_prompt=[{
            "role":"system","content":"Act as Resume/Cv Guider who extract data from the file or text user uploads"
          """
            You have to extract informations like this:
            1.Name
            2.Phone No
            3.Email Id
            4.Education
            5.Skills
            6.Experience
            7.GitHub Id
            8.Linkedin Id

            Always return a valid Json only

            Example:
            {

            "Name":"",
            "Phone No":123,
            "Email ID":"",
            "Education":"",
            "Skills":[],
            "Experience":"",
            "GitHub Id":"",
            "Linkedin Id":""

            }   
            """      
        },
        {
          "role":"user","content":context.user_input          
        }
        ]
        return agent_prompt
    @staticmethod
    def analyse_prompt(context):
        agent_prompt=[{
            "role":"system","content":"You are an Resume guider, analyse the strength,weakness and touchups required"
            """
            You have to analyse :
            1.Strength
            2.Weakness
            3.Touch Up
           
            Always return a valid Json only
            Example:
            {

            "Strength":[],
            "Weakness":[],
            "Touch Up":""
    
            }   
            """      
        },
        {
          "role":"user","content":json.dumps(context.extracted_data )         
        }
        ]
        return agent_prompt 
    @staticmethod
    def recommendation_prompt(context):
         agent_prompt=[{
            "role":"system","content":"You are an Resume guider, your task is to analyse the users's resume and recommend suitable jobs"
            """
            You have to recommend :
            1.Jobs
            2.Position
            3.Comapnies
           
            Always return a valid Json only

            Example:
            {

            "Jobs":[],
            "Position":[],
            "Companies":""
    
            }   
            """      
        },
        {
                    "role":"user","content":json.dumps(context.extracted_data)          
        
        }
        ]
         return agent_prompt
    @staticmethod
    def upskilling_prompt(context):
         agent_prompt=[{
            "role":"system","content":"You are an Resume guider, your task is to analyse the user's resume and recommend skills which will improve their carreer opertunities"
            """
           
                You have to recommend :
                Recommend:
                    1. Technical Skills to Learn
                    2. Soft Skills to Improve
                    3. Certifications
                    4. Projects to Build
                    5. Learning Resourc
            
                Always return a valid Json only

                Example:
                    {

                   "Technical_Skills": [],
                    "Soft_Skills": [],
                    "Certifications": [],
                    "Projects": [],
                    "Learning_Resources": []
                    }  

            """      
            
        },
        {
             "role":"user","content":json.dumps(context.extracted_data)          
       
        }
        ]
         return agent_prompt
    @staticmethod
    def ats_prompt(context):
        agent_prompt=[{
            "role":"system","content":"You are an Resume guider, your task is to analyse the user's resume and rate it on the scale of 0-100 and explain about the rating"
            """
           
                You have to recommend :
                Recommend:
                    1.Rating
                    2.Explanation
            
                Always return a valid Json only

                Example:
                    {
                    "Rating":45,
                    "Explanation:""
                    
                    }  

            """      
            
        },
        {
                   "role":"user","content":json.dumps(context.extracted_data    )             
        }
        ]
        return agent_prompt

    
        
