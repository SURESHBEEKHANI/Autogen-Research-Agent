import os
from autogen import AssistantAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ResearchAgents:
    def __init__(self, api_key):
        self.groq_api_key = api_key
        self.llm_config = {'config_list': [{'model': 'llama-3.3-70b-versatile', 'api_key': self.groq_api_key, 'api_type': "groq"}]}

        # Summarizer Agent - Summarizes research papers
        self.summarizer_agent = AssistantAgent(
            name="summarizer_agent",
            system_message="Summarize the retrieved research papers and present concise summaries to the user, JUST GIVE THE RELEVANT SUMMARIES OF THE RESEARCH PAPER AND NOT YOUR THOUGHT PROCESS.",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config=False
        )

        # Advantages and Disadvantages Agent - Analyzes pros and cons
        self.advantages_disadvantages_agent = AssistantAgent(
            name="advantages_disadvantages_agent",
            system_message="Analyze the summaries of the research papers and provide a list of advantages and disadvantages for each paper in a pointwise format. JUST GIVE THE ADVANTAGES AND DISADVANTAGES, NOT YOUR THOUGHT PROCESS",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config=False
        )

    def summarize_paper(self, paper_summary):
        """Generates a summary of the research paper."""
        try:
            if not paper_summary or paper_summary.strip() == "":
                return "No summary available for this paper."
                
            summary_response = self.summarizer_agent.generate_reply(
                messages=[{"role": "user", "content": f"Summarize this paper: {paper_summary}"}]
            )
            
            if isinstance(summary_response, dict):
                return summary_response.get("content", "Summarization failed!")
            else:
                return str(summary_response)
        except Exception as e:
            print(f"Error in summarize_paper: {e}")
            return f"Error generating summary: {str(e)}"

    def analyze_advantages_disadvantages(self, summary):
        """Generates advantages and disadvantages of the research paper."""
        try:
            if not summary or summary.strip() == "":
                return "No analysis available for this paper."
                
            adv_dis_response = self.advantages_disadvantages_agent.generate_reply(
                messages=[{"role": "user", "content": f"Provide advantages and disadvantages for this paper: {summary}"}]
            )
            
            if isinstance(adv_dis_response, dict):
                return adv_dis_response.get("content", "Advantages and disadvantages analysis failed!")
            else:
                return str(adv_dis_response)
        except Exception as e:
            print(f"Error in analyze_advantages_disadvantages: {e}")
            return f"Error generating analysis: {str(e)}"
