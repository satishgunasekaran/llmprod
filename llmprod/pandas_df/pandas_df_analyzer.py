import pandas as pd
import os
from langchain_together import Together
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

class PandasDFAnalyzer:
    def __init__(self,  df: pd.DataFrame,
                 
                 together_api_key: str,
                    llm = None
                 ):
        self.df = df
        self.llm = llm
        if not self.llm:
            self.llm = Together(
                model="Phind/Phind-CodeLlama-34B-v2",
                    temperature=0.7,
                    max_tokens=128,
                    top_k=1,
                    together_api_key=together_api_key,
                )
    def optimize_query(self, query):

        agent = create_pandas_dataframe_agent(self.llm, self.df, verbose=True) 
        prompt =  f"""
            You are a master prompt generator and generate the optimised prompt for the following query:
            {query}
            
            - the prompt should be optimised for the agent to understand the query
            - the prompt should be optimised for the agent to generate the correct code

            Output 
            Return Only the optimised prompt 
            
            
        """
        response = agent.run(prompt)
        
        return  response
    
    def analyze_df(self, query):
        
        agent = create_pandas_dataframe_agent(self.llm, self.df, verbose=True) 
        query = self.optimize_query(query)
        response = agent.run(query)
        
        return response
    
        
    def generate_prompts(self,  n_prompts=8):
        # agent = create_pandas_dataframe_agent(self.llm, self.df, verbose=True) 

        prompt =  f"""
            You are a master prompt generator and generate {n_prompts} prompts for the provided dataframe 

            - These are the datatypes of the columns
            - {self.df.dtypes}

            Output
            Return the prompts seperated by a new line don't generate coode
            """
        response = self.llm.invoke(prompt)
        #make it to return it is separated by a new line and remove the numbers at the start
        response = response.split("\n")
        #for each response take the element after the dot
        response = [r.split(".")[1] for r in response]
        return response
        
        
        
        
         
        
        
        
        
         
        
        
        
        
    
