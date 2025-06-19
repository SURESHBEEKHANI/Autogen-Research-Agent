import React, { useState, useEffect } from 'react';
import { Search, Database, Settings } from 'lucide-react';
import { ResearchQuery } from '../types';

interface SearchFormProps {
  onSubmit: (query: ResearchQuery) => void;
  isLoading: boolean;
}

const SearchForm: React.FC<SearchFormProps> = ({ onSubmit, isLoading }) => {
  const [query, setQuery] = useState('');
  const [selectedSources, setSelectedSources] = useState<string[]>(['ArXiv', 'Google Scholar']);
  const [numResults, setNumResults] = useState(5);
  const [availableSources, setAvailableSources] = useState<string[]>([]);

  useEffect(() => {
    // In a real app, you'd fetch this from the API
    setAvailableSources(['ArXiv', 'Google Scholar']);
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    const researchQuery: ResearchQuery = {
      query: query.trim(),
      sources: selectedSources,
      num_results: numResults,
    };

    onSubmit(researchQuery);
  };

  const toggleSource = (source: string) => {
    setSelectedSources(prev =>
      prev.includes(source)
        ? prev.filter(s => s !== source)
        : [...prev, source]
    );
  };

  return (
    <div className="card">
      <div className="flex items-center space-x-2 mb-6">
        <Search className="w-5 h-5 text-primary-600" />
        <h2 className="text-xl font-semibold text-gray-900">Research Paper Search</h2>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Search Query */}
        <div>
          <label htmlFor="query" className="block text-sm font-medium text-gray-700 mb-2">
            Research Topic
          </label>
          <input
            type="text"
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter your research topic (e.g., 'machine learning', 'quantum computing')"
            className="input-field"
            required
          />
        </div>

        {/* Data Sources */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            <Database className="w-4 h-4 inline mr-2" />
            Data Sources
          </label>
          <div className="grid grid-cols-2 gap-3">
            {availableSources.map((source) => (
              <label key={source} className="flex items-center space-x-2 cursor-pointer">
                <input
                  type="checkbox"
                  checked={selectedSources.includes(source)}
                  onChange={() => toggleSource(source)}
                  className="w-4 h-4 text-primary-600 border-gray-300 rounded focus:ring-primary-500"
                />
                <span className="text-sm text-gray-700">{source}</span>
              </label>
            ))}
          </div>
        </div>

        {/* Number of Results */}
        <div>
          <label htmlFor="numResults" className="block text-sm font-medium text-gray-700 mb-2">
            <Settings className="w-4 h-4 inline mr-2" />
            Number of Results per Source
          </label>
          <select
            id="numResults"
            value={numResults}
            onChange={(e) => setNumResults(Number(e.target.value))}
            className="input-field"
          >
            <option value={3}>3 papers</option>
            <option value={5}>5 papers</option>
            <option value={10}>10 papers</option>
            <option value={15}>15 papers</option>
          </select>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading || !query.trim() || selectedSources.length === 0}
          className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center space-x-2"
        >
          {isLoading ? (
            <>
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
              <span>Searching...</span>
            </>
          ) : (
            <>
              <Search className="w-4 h-4" />
              <span>Search Papers</span>
            </>
          )}
        </button>
      </form>
    </div>
  );
};

export default SearchForm; 