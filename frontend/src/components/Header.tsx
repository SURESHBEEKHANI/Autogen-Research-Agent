import React from 'react';
import { Search, BookOpen, Zap } from 'lucide-react';

interface HeaderProps {
  onTabChange: (tab: string) => void;
  activeTab: string;
}

const Header: React.FC<HeaderProps> = ({ onTabChange, activeTab }) => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo and Title */}
          <div className="flex items-center space-x-3">
            <div className="flex items-center justify-center w-10 h-10 bg-primary-600 rounded-lg">
              <BookOpen className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-gray-900">Research Agent</h1>
              <p className="text-sm text-gray-500">AI-Powered Research Assistant</p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <nav className="flex space-x-1">
            <button
              onClick={() => onTabChange('search')}
              className={`px-4 py-2 rounded-lg font-medium transition-colors duration-200 flex items-center space-x-2 ${
                activeTab === 'search'
                  ? 'bg-primary-100 text-primary-700'
                  : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
              }`}
            >
              <Search className="w-4 h-4" />
              <span>Search Papers</span>
            </button>
            <button
              onClick={() => onTabChange('about')}
              className={`px-4 py-2 rounded-lg font-medium transition-colors duration-200 flex items-center space-x-2 ${
                activeTab === 'about'
                  ? 'bg-primary-100 text-primary-700'
                  : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
              }`}
            >
              <Zap className="w-4 h-4" />
              <span>About</span>
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header; 