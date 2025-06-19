import React, { useState } from 'react';
import { ExternalLink, ChevronDown, ChevronUp, FileText, TrendingUp } from 'lucide-react';
import { PaperSummary } from '../types';

interface PaperCardProps {
  paper: PaperSummary;
}

const PaperCard: React.FC<PaperCardProps> = ({ paper }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="card hover:shadow-md transition-shadow duration-200">
      {/* Paper Header */}
      <div className="flex justify-between items-start mb-4">
        <h3 className="text-lg font-semibold text-gray-900 leading-tight">
          {paper.title}
        </h3>
        <a
          href={paper.link}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center space-x-1 text-primary-600 hover:text-primary-700 transition-colors duration-200"
        >
          <ExternalLink className="w-4 h-4" />
          <span className="text-sm">View Paper</span>
        </a>
      </div>

      {/* Summary Section */}
      <div className="mb-4">
        <div className="flex items-center space-x-2 mb-2">
          <FileText className="w-4 h-4 text-gray-500" />
          <h4 className="text-sm font-medium text-gray-700">Summary</h4>
        </div>
        <p className="text-gray-600 text-sm leading-relaxed">
          {isExpanded ? paper.summary : `${paper.summary.slice(0, 200)}...`}
        </p>
        {paper.summary.length > 200 && (
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="text-primary-600 hover:text-primary-700 text-sm font-medium mt-2 flex items-center space-x-1"
          >
            {isExpanded ? (
              <>
                <ChevronUp className="w-4 h-4" />
                <span>Show Less</span>
              </>
            ) : (
              <>
                <ChevronDown className="w-4 h-4" />
                <span>Read More</span>
              </>
            )}
          </button>
        )}
      </div>

      {/* Advantages and Disadvantages */}
      <div className="border-t border-gray-200 pt-4">
        <div className="flex items-center space-x-2 mb-3">
          <TrendingUp className="w-4 h-4 text-green-500" />
          <h4 className="text-sm font-medium text-gray-700">Analysis</h4>
        </div>
        <div className="bg-gray-50 rounded-lg p-3">
          <p className="text-gray-600 text-sm leading-relaxed">
            {paper.advantages_disadvantages}
          </p>
        </div>
      </div>
    </div>
  );
};

export default PaperCard; 