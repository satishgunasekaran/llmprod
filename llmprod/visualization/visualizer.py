import pandas as pd
import os
from langchain_together import Together
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

class Visualizer:
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
    
    def analyze_df(self, query):
        agent = create_pandas_dataframe_agent(self.llm, self.df, verbose=True) 
        prompt =  f"""
            You are a master visualization generator using plotly and create the plot for the following query:
            {query}
            
            Output 
            JSON format of the plotly figure
            
        """
        response = agent.run(prompt)
        
        return response
        
        
        
        
        
        
         
        
        
        
        
         
        
        
        
        
    
