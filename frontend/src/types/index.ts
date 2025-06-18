export interface ResearchQuery {
  query: string;
  sources: string[];
  num_results: number;
}

export interface PaperSummary {
  title: string;
  link: string;
  summary: string;
  advantages_disadvantages: string;
}

export interface ResearchResponse {
  papers: PaperSummary[];
  total_papers: number;
  query: string;
  sources_used: string[];
}

export interface ApiInfo {
  name: string;
  version: string;
  description: string;
  features: string[];
  technologies: string[];
}

export interface AvailableSources {
  available_sources: string[];
  description: string;
}

export interface LoadingState {
  isLoading: boolean;
  message?: string;
} 