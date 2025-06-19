import React, { useState, useEffect } from 'react';
import { Zap, Brain, Database, Search, Shield } from 'lucide-react';
import { ApiInfo } from '../types';

const AboutSection: React.FC = () => {
  const [apiInfo, setApiInfo] = useState<ApiInfo | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Mock API info for now - in real app, fetch from API
    setApiInfo({
      name: "Virtual Research Assistant API",
      version: "1.0.0",
      description: "A FastAPI-based research assistant that fetches and analyzes research papers from multiple sources",
      features: [
        "Search research papers from ArXiv",
        "Search research papers from Google Scholar",
        "AI-powered paper summarization",
        "Advantages and disadvantages analysis",
        "Multiple data source support"
      ],
      technologies: [
        "FastAPI",
        "Python",
        "Groq API",
        "AutoGen",
        "ArXiv API",
        "Google Scholar"
      ]
    });
    setIsLoading(false);
  }, []);

  if (isLoading) {
    return (
      <div className="card">
        <div className="flex items-center justify-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Hero Section */}
      <div className="card bg-gradient-to-r from-primary-50 to-blue-50">
        <div className="text-center">
          <div className="flex items-center justify-center w-16 h-16 bg-primary-600 rounded-full mx-auto mb-4">
            <Zap className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl font-bold text-gray-900 mb-2">
            {apiInfo?.name}
          </h1>
          <p className="text-gray-600 max-w-2xl mx-auto">
            {apiInfo?.description}
          </p>
          <div className="mt-4">
            <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-primary-100 text-primary-800">
              v{apiInfo?.version}
            </span>
          </div>
        </div>
      </div>

      {/* Features Grid */}
      <div className="card">
        <h2 className="text-xl font-semibold text-gray-900 mb-6 flex items-center">
          <Brain className="w-5 h-5 mr-2 text-primary-600" />
          Key Features
        </h2>
        <div className="grid md:grid-cols-2 gap-4">
          {apiInfo?.features.map((feature, index) => (
            <div key={index} className="flex items-start space-x-3">
              <div className="flex-shrink-0 w-5 h-5 bg-primary-100 rounded-full flex items-center justify-center mt-0.5">
                <div className="w-2 h-2 bg-primary-600 rounded-full"></div>
              </div>
              <span className="text-gray-700">{feature}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Technologies */}
      <div className="card">
        <h2 className="text-xl font-semibold text-gray-900 mb-6 flex items-center">
          <Database className="w-5 h-5 mr-2 text-primary-600" />
          Technologies Used
        </h2>
        <div className="flex flex-wrap gap-2">
          {apiInfo?.technologies.map((tech, index) => (
            <span
              key={index}
              className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800"
            >
              {tech}
            </span>
          ))}
        </div>
      </div>

      {/* How It Works */}
      <div className="card">
        <h2 className="text-xl font-semibold text-gray-900 mb-6 flex items-center">
          <Search className="w-5 h-5 mr-2 text-primary-600" />
          How It Works
        </h2>
        <div className="space-y-4">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-semibold">
              1
            </div>
            <div>
              <h3 className="font-medium text-gray-900">Search Research Papers</h3>
              <p className="text-gray-600 text-sm mt-1">
                Enter your research topic and select data sources (ArXiv, Google Scholar)
              </p>
            </div>
          </div>
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-semibold">
              2
            </div>
            <div>
              <h3 className="font-medium text-gray-900">AI Analysis</h3>
              <p className="text-gray-600 text-sm mt-1">
                Our AI agents analyze each paper and generate comprehensive summaries
              </p>
            </div>
          </div>
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-semibold">
              3
            </div>
            <div>
              <h3 className="font-medium text-gray-900">Get Insights</h3>
              <p className="text-gray-600 text-sm mt-1">
                Review advantages, disadvantages, and key insights for each research paper
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* API Status */}
      <div className="card">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Shield className="w-5 h-5 text-green-500" />
            <div>
              <h3 className="font-medium text-gray-900">API Status</h3>
              <p className="text-sm text-gray-600">All systems operational</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            <span className="text-sm text-green-600 font-medium">Online</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutSection; 