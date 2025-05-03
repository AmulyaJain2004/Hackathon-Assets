# Hackathon Hub Frontend

A modern, responsive React application for hackathon event management built with React and Tailwind CSS.

## Features

- **User Authentication**: Login and signup pages with form validation
- **Dashboard**: Overview of user's hackathon activities and statistics
- **Responsive Design**: Mobile-first approach with responsive components
- **Reusable Components**: Modular components for forms, buttons, and layouts

## Tech Stack

- React 
- Tailwind CSS
- Vite

## Setup Instructions

### Prerequisites

- Node.js (v18 or higher recommended)
- npm or yarn

### Installation

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd hackathon-hub/frontend
   ```

2. Install dependencies
   ```bash
   npm install
   # or with yarn
   yarn
   ```

3. Install Tailwind CSS dependencies (if not already installed)
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   # or with yarn
   yarn add -D tailwindcss postcss autoprefixer
   ```

### Development

Run the development server:
```bash
npm run dev
# or with yarn
yarn dev
```

The application will be available at http://localhost:5173

### Build for Production

```bash
npm run build
# or with yarn
yarn build
```

## Project Structure

```
src/
├── components/
│   ├── common/         # Reusable UI components
│   │   ├── Button.jsx
│   │   └── FormInput.jsx
│   └── layout/         # Layout components
│       ├── Navbar.jsx
│       └── Footer.jsx
├── pages/              # Page components
│   ├── Login.jsx
│   ├── SignUp.jsx
│   └── Dashboard.jsx
├── App.jsx             # Main application component
├── main.jsx            # Entry point
├── index.css           # Global styles (Tailwind imports)
└── App.css             # App-specific styles
```

## License

MIT
