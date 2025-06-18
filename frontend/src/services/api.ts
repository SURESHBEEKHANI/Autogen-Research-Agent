import axios from 'axios';
import { ResearchQuery, ResearchResponse, ApiInfo, AvailableSources } from '../types';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const researchApi = {
  // Search and analyze research papers
  searchPapers: async (query: ResearchQuery): Promise<ResearchResponse> => {
    const response = await api.post<ResearchResponse>('/research', query);
    return response.data;
  },

  // Get available data sources
  getAvailableSources: async (): Promise<AvailableSources> => {
    const response = await api.get<AvailableSources>('/research/sources');
    return response.data;
  },

  // Get API information
  getApiInfo: async (): Promise<ApiInfo> => {
    const response = await api.get<ApiInfo>('/api-info');
    return response.data;
  },

  // Health check
  healthCheck: async (): Promise<{ status: string }> => {
    const response = await api.get<{ status: string }>('/health');
    return response.data;
  },
};

export default api; 