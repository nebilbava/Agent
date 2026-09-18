def resume_read():
    filepath=input("Enter File Path Here: ")
    try:
        with open(filepath,"r",encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error:File Not Exist") 
        return None
    except Exception as e:
        print(f"Error:{e}") 
        return None  
    
