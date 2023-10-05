import React from 'react'
import logo from '../Images/logo.png'

function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-dark">
      <div className="container">
        <div className="d-flex align-items-center">
          <img
            src={logo}
            alt="Logo"
            className="navbar-brand mr-3"
            style={{ width: '40px', height: '40px' }}
          />
          <h1 className="navbar-brand mb-0">TextTracer</h1>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;