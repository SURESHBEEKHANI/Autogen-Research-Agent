import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgents
from data_loader import DataLoader

load_dotenv()

# Move set_page_config() to be the first Streamlit command.
st.set_page_config(
    page_title="Autogen Agent",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Updated Custom CSS: Set professional type text styling
custom_css = """
<style>
    body {
        background-color: #f5f5f5;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #ffffff;
        font-size: 16px;
        line-height: 1.6;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: 600;
        color: #ffffff;
    }
    .css-18e3th9, .css-1d391kg {
        color: #ffffff;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: #ffffff;
        border-radius: 5px;
        border: none;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    .stMarkdown, .css-1d391kg {
        color: #ffffff;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit UI Title
st.title("📚 Virtual Research Assistant")

num_results = 5
source_choice = st.sidebar.multiselect("Select Data Sources", options=["ArXiv", "Google Scholar"], default=["ArXiv"])
# Sidebar with features and footer
with st.sidebar:
    st.divider()
    st.markdown("<h3 style='color: #ffffff;'>Key Features</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style='list-style: none; padding: 0; color: #ffffff; text-align: left;'>
        <li style='margin-bottom: 8px;'>🔍 <strong>Multi-Source Research Retrieval</strong></li>
        <li style='margin-bottom: 8px;'>🤖 <strong>Integrated Chatbot Interaction</strong></li>
        <li style='margin-bottom: 8px;'>✨ <strong>Advanced Summarization</strong></li>
        <li style='margin-bottom: 8px;'>🔄 <strong>Automatic Query Expansion & Refinement</strong></li>
        <li style='margin-bottom: 8px;'>📊 <strong>Visual Data Presentation</strong></li>
    </ul>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("<p style='text-align: center; color:#ffffff;'><em>Built with Groq | Autogen</em></p>", unsafe_allow_html=True)

# Retrieve the API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if API key is set, else stop execution
if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please set it in your environment variables.")
    st.stop()

# Initialize AI Agents for summarization and analysis
agents = ResearchAgents(groq_api_key)

# Initialize DataLoader for fetching research papers
data_loader = DataLoader()

# Use chat_input instead of text_input for entering the research topic.
query = st.chat_input("Enter a research topic:")

# Trigger the search automatically if a query is provided.
if query:
    with st.spinner("Fetching research papers..."):  # Show a loading spinner
        
        all_papers = []
        # Fetch from selected sources based on sidebar choices
        if "ArXiv" in source_choice:
            arxiv_papers = data_loader.fetch_arxiv_papers(query, limit=num_results)
            all_papers.extend(arxiv_papers)
        if "Google Scholar" in source_choice:
            google_scholar_papers = data_loader.fetch_google_scholar_papers(query)
            all_papers.extend(google_scholar_papers)

        # If no papers are found, display an error message
        if not all_papers:
            st.error("Failed to fetch papers. Try again!")
        else:
            processed_papers = []

            # Process each paper: generate summary and analyze advantages/disadvantages
            for paper in all_papers:
                summary = agents.summarize_paper(paper['summary'])  # Generate summary
                adv_dis = agents.analyze_advantages_disadvantages(summary)  # Analyze pros/cons

                processed_papers.append({
                    "title": paper["title"],
                    "link": paper["link"],
                    "summary": summary,
                    "advantages_disadvantages": adv_dis,
                })

            # Display the processed research papers
            st.subheader("Top Research Papers:")
            for i, paper in enumerate(processed_papers, 1):
                st.markdown(f"### {i}. {paper['title']}")  # Paper title
                st.markdown(f"🔗 [Read Paper]({paper['link']})")  # Paper link
                st.write(f"**Summary:** {paper['summary']}")  # Paper summary
                st.write(f"{paper['advantages_disadvantages']}")  # Pros/cons analysis
                st.markdown("---")  # Separator between papers
