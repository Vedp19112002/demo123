def greet():
   print ("Hi")
   print("This is AI Doc")

def takeinput():
    name=input("What is your name? ")
    print("Hello "+name)
    abc=input("What are your Symptoms? ")
    print(abc)
    return abc

#we can add multiple llm options like gemini, gpt, claude etc. and based on user choice we can call the respective llm to generate response
     

class ChatGpt_LLM:    
    def __init__(self,model):               
         self.model=model
    def generate_response(self,prompt):
        # open ai api get response from model using prompt
        # openai url
        # openaikey 
        # make http call
        return "This is a dummy response to the prompt: "+prompt+" using model: "+self.model

class Gemini_LLM:    
    def __init__(self,model):               
         self.model=model
    def generate_response(self,prompt):
        # gemini api get response from model using prompt
        # gemini url
        # geminikey 
        # make http call
        return "This is a dummy response to the prompt: "+prompt+" using model: "+self.model


class Practo_Tool:
    def __init__(self,name):
        self.name=name

    def useTool(self,input):
        #Api url
        #Api key
        #make http call to book appointment
        print("Using the tool "+self.name+" to book appointment for symptom: "+input)
    
class Messenger_Tool:
    def __init__(self,name):
        self.name=name

    def useTool(self,input):
        #Api url
        #Api key
        #make http call to send message
        print("Using the tool "+self.name+" to send message for symptom: "+input)    


class Agent:
    def __init__(self,name,llm,tool):
        self.name=name
        self.llm=llm
        self.tool=tool
    # user input
    def giveadvice(self,symptom):
    #    llm=ChatGpt_LLM("GPT2.0")
       response=llm.generate_response("What advice would you give to a patient with the symptom of "+symptom)
       print(response)
    def takeaction(self,input):
        
        tool.useTool(input)

    # autonomous
    def giveadviceandtakeaction(self,symptom):
        self.giveadvice(symptom)
        self.takeaction(symptom)



class AutoAgent:
    def __init__(self,name,llm,tool,prompt):
        self.name=name
        self.llm=llm
        self.tool=tool
        self.prompt=prompt
    def decidetousetool(self,response):
        #logic to decide if the tool is needed based on response from llm
        if "severe" in response:
            return True
        else:
            return False
    
    def execute(self):
        response=self.llm.generate_response(self.prompt)
        print("Advice for "+symptom+": "+response)
        if self.decidetousetool(response):
            self.tool.useTool(symptom)
        else:
            print("No need to visit doctor")
            
chatMessages=[]
enquiryAgent=AutoAgent("EnquiryHealthbot",Gemini_LLM("gemini-1"),Messenger_Tool("MessengerAPI"),"Ask questions to understand the problem in detail "+chatMessages)
enquiryAgent.execute()

advisorAgent=AutoAgent("AutoHealthbot",ChatGpt_LLM("gpt-4"),Practo_Tool("PractoAPI"),"Provide advice for the problem: "+chatMessages)
advisorAgent.execute()
    
class Manager:
        def __init__(self,name,agents):
            self.name=name
            self.agents=agents
        def coordinate(self,symptom):
            for agent in self.agents:
                agent.execute()

greet()


# name="Ramesh"
# age=30;

# symptomlist=[{
#     "name":"Cough",
#     "Severity":"mild",
#     "duration":"2 days",
#     "priority": 1
# },{
#     "name":"Fever",
#     "Severity":"High",
#     "duration":"1 day",
#     "priority": 2
# },{
#     "name":"Headache",
#     "Severity":"Low",
#     "duration":"1 day",
#     "priority": 2
# }]

# print("Hi")
# print(name)
# #print(symptomlist[1])

# for symptom in symptomlist:
#         if symptom["priority"]==2:
#             print(symptom["name"],symptom["Severity"])
#             print(symptom["priority"])
# greet()



symptom=takeinput()
# instance of LLMs
llm=ChatGpt_LLM("gpt-4") # or Gemini_LLM("gemini-1") based on user choice
tool=Practo_Tool("PractoAPI")
agent= Agent("AI Doc",llm,tool)
agent.giveadvice(symptom)
