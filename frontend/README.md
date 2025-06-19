# Research Agent Frontend

A modern React TypeScript frontend for the Autogen Research Agent API. This application provides a beautiful and intuitive interface for searching and analyzing research papers from multiple sources.

## Features

- 🔍 **Smart Search**: Search research papers from ArXiv and Google Scholar
- 🤖 **AI Analysis**: Get AI-powered summaries and analysis of research papers
- 📊 **Multiple Sources**: Support for multiple data sources with easy selection
- 🎨 **Modern UI**: Beautiful, responsive design with Tailwind CSS
- ⚡ **Fast Performance**: Built with Vite for optimal development experience
- 📱 **Mobile Friendly**: Responsive design that works on all devices

## Tech Stack

- **React 18** - Modern React with hooks
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API communication
- **Lucide React** - Beautiful icons
- **React Hot Toast** - Toast notifications

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running on `http://localhost:8000`

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   Navigate to `http://localhost:3000`

### Building for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

## Project Structure

```
src/
├── components/          # React components
│   ├── Header.tsx      # Navigation header
│   ├── SearchForm.tsx  # Search form component
│   ├── PaperCard.tsx   # Individual paper display
│   ├── ResultsSection.tsx # Results display
│   └── AboutSection.tsx # About page
├── services/           # API services
│   └── api.ts         # API client
├── types/             # TypeScript type definitions
│   └── index.ts       # API types
├── App.tsx            # Main app component
├── main.tsx           # App entry point
└── index.css          # Global styles
```

## API Integration

The frontend communicates with the backend API through the following endpoints:

- `POST /api/research` - Search and analyze research papers
- `GET /api/research/sources` - Get available data sources
- `GET /api/api-info` - Get API information
- `GET /api/health` - Health check

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Code Style

The project uses:
- **ESLint** for code linting
- **Prettier** for code formatting
- **TypeScript** for type safety

## Features in Detail

### Search Interface
- Clean, intuitive search form
- Source selection (ArXiv, Google Scholar)
- Configurable result count
- Real-time validation

### Results Display
- Card-based layout for papers
- Expandable summaries
- Direct links to papers
- AI-generated analysis

### Responsive Design
- Mobile-first approach
- Adaptive layouts
- Touch-friendly interactions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

This is the README for the frontend folder.
