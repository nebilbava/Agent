def line():
        print("=" * 70)

def header(title):
        line()
        print(title.upper())    
        line()

def show_extracted_content(context):
        
        print("=" * 70)
        header('Resume Data')
        
        print("=" * 70)

        for key,value in context.extracted_data.items():
                print(f"{key}:{value}")
       
        print()
def show_analysed_content(context):
        
        print("=" * 70)
        header("Analaysed Data") 
        
        print()

        for key, value in context.analysed_data.items():
                print(f"{key}:{value}") 
     
        print()                     
def show_recom_content(context):
        
        print("=" * 70)
        header("Recommended Jobs")
        print("=" * 70)

        for key,value in context.recommendation_data.items():
                print(f"{key}:{value}")

        print()
def show_upskilling_content(context):
        
        print("=" * 70)
        header("Skill Can be Improved")  
        print("=" * 70)

        for key,value in context.upskilling_data.items():
                print(f"{key}:{value}")

        print()

def show_rating(context):

        print("=" * 70)
        header("Resume Score")
        print("=" * 70)   


        print(context.rating)
        print()                                               