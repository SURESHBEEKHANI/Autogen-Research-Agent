import React from 'react';
import { BookOpen, Search, TrendingUp } from 'lucide-react';
import { ResearchResponse } from '../types';
import PaperCard from './PaperCard';

interface ResultsSectionProps {
  results: ResearchResponse | null;
  isLoading: boolean;
}

const ResultsSection: React.FC<ResultsSectionProps> = ({ results, isLoading }) => {
  if (isLoading) {
    return (
      <div className="card">
        <div className="flex items-center justify-center py-12">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto mb-4"></div>
            <p className="text-gray-600">Searching for research papers...</p>
            <p className="text-sm text-gray-500 mt-2">This may take a few moments</p>
          </div>
        </div>
      </div>
    );
  }

  if (!results) {
    return null;
  }

  return (
    <div className="space-y-6">
      {/* Results Header */}
      <div className="card">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-semibold text-gray-900 mb-2">
              Search Results
            </h2>
            <p className="text-gray-600">
              Found {results.total_papers} papers for "{results.query}"
            </p>
          </div>
          <div className="flex items-center space-x-4 text-sm text-gray-500">
            <div className="flex items-center space-x-1">
              <BookOpen className="w-4 h-4" />
              <span>{results.total_papers} papers</span>
            </div>
            <div className="flex items-center space-x-1">
              <Search className="w-4 h-4" />
              <span>{results.sources_used.join(', ')}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Papers Grid */}
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-1">
        {results.papers.map((paper, index) => (
          <PaperCard key={index} paper={paper} />
        ))}
      </div>

      {/* No Results */}
      {results.papers.length === 0 && (
        <div className="card text-center py-12">
          <BookOpen className="w-12 h-12 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No papers found</h3>
          <p className="text-gray-600">
            Try adjusting your search terms or selecting different data sources.
          </p>
        </div>
      )}
    </div>
  );
};

export default ResultsSection; 