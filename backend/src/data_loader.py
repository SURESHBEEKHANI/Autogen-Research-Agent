import requests
import xml.etree.ElementTree as ET
from scholarly import scholarly

class DataLoader:
    def __init__(self):
        print("DataLoader Init")
        
    def fetch_arxiv_papers(self, query, limit=None):
        """
        Fetches research papers from ArXiv based on the user query.
        
        Args:
            query (str): Search query for papers
            limit (int): Maximum number of papers to return
            
        Returns:
            list: A list of dictionaries containing paper details (title, summary, link).
        """
        
        def search_arxiv(query, max_results=10):
            """Helper function to query ArXiv API."""
            try:
                url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    root = ET.fromstring(response.text)
                    papers = []
                    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                        try:
                            title_elem = entry.find("{http://www.w3.org/2005/Atom}title")
                            summary_elem = entry.find("{http://www.w3.org/2005/Atom}summary")
                            id_elem = entry.find("{http://www.w3.org/2005/Atom}id")
                            
                            if title_elem is not None and summary_elem is not None and id_elem is not None:
                                papers.append({
                                    "title": title_elem.text.strip(),
                                    "summary": summary_elem.text.strip(),
                                    "link": id_elem.text.strip()
                                })
                        except Exception as e:
                            print(f"Error parsing paper entry: {e}")
                            continue
                    return papers
                else:
                    print(f"ArXiv API returned status code: {response.status_code}")
                    return []
            except Exception as e:
                print(f"Error fetching from ArXiv: {e}")
                return []

        papers = search_arxiv(query)

        if limit is not None:
            papers = papers[:limit]
            
        return papers

    def fetch_google_scholar_papers(self, query):
        """
        Fetches research papers from Google Scholar.
        
        Args:
            query (str): Search query for papers
            
        Returns:
            list: A list of dictionaries containing paper details (title, summary, link)
        """
        try:
            papers = []
            search_results = scholarly.search_pubs(query)

            for i, paper in enumerate(search_results):
                if i >= 5:  # Limit to 5 papers
                    break
                try:
                    title = paper["bib"]["title"] if "title" in paper["bib"] else "No title available"
                    summary = paper["bib"].get("abstract", "No summary available")
                    link = paper.get("pub_url", "No link available")
                    
                    papers.append({
                        "title": title,
                        "summary": summary,
                        "link": link
                    })
                except Exception as e:
                    print(f"Error parsing Google Scholar paper: {e}")
                    continue
                    
            return papers
        except Exception as e:
            print(f"Error fetching from Google Scholar: {e}")
            return []
