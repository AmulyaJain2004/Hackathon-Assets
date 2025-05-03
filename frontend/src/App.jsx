import { useState } from 'react'
import './App.css'
import Login from './pages/Login'
import SignUp from './pages/SignUp'
import Dashboard from './pages/Dashboard'

function App() {
  // Simple state-based routing for demo purposes
  const [currentPage, setCurrentPage] = useState('login')
  
  // Handle navigation between pages
  const navigateTo = (page) => {
    setCurrentPage(page)
  }

  // Render the appropriate component based on currentPage
  const renderPage = () => {
    switch (currentPage) {
      case 'login':
        return <Login navigateTo={navigateTo} />
      case 'signup':
        return <SignUp navigateTo={navigateTo} />
      case 'dashboard':
        return <Dashboard navigateTo={navigateTo} />
      default:
        return <Login navigateTo={navigateTo} />
    }
  }

  return (
    <div className="App">
      {renderPage()}
    </div>
  )
}

export default App
