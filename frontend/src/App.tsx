import { useState } from 'react';
import { Toaster } from 'react-hot-toast';
import Header from './components/Header';
import SearchForm from './components/SearchForm';
import ResultsSection from './components/ResultsSection';
import AboutSection from './components/AboutSection';
import { ResearchQuery, ResearchResponse } from './types';
import { researchApi } from './services/api';
import toast from 'react-hot-toast';

function App() {
  const [activeTab, setActiveTab] = useState('search');
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState<ResearchResponse | null>(null);

  const handleSearch = async (query: ResearchQuery) => {
    setIsLoading(true);
    setResults(null);

    try {
      const response = await researchApi.searchPapers(query);
      setResults(response);
      toast.success(`Found ${response.total_papers} papers for "${query.query}"`);
    } catch (error) {
      console.error('Search error:', error);
      toast.error('Failed to search papers. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Toaster
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: '#363636',
            color: '#fff',
          },
          success: {
            duration: 3000,
            iconTheme: {
              primary: '#10B981',
              secondary: '#fff',
            },
          },
          error: {
            duration: 4000,
            iconTheme: {
              primary: '#EF4444',
              secondary: '#fff',
            },
          },
        }}
      />

      <Header onTabChange={setActiveTab} activeTab={activeTab} />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'search' ? (
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Search Form */}
            <div className="lg:col-span-1">
              <SearchForm onSubmit={handleSearch} isLoading={isLoading} />
            </div>

            {/* Results */}
            <div className="lg:col-span-2">
              <ResultsSection results={results} isLoading={isLoading} />
            </div>
          </div>
        ) : (
          <AboutSection />
        )}
      </main>
    </div>
  );
}

export default App; 