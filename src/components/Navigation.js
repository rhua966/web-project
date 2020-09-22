import React from 'react'
import { Nav, Navbar } from 'react-bootstrap'
// import { NavLink } from 'react-router-dom'
// import '../App.css'

export default function Navigation() {

    return (
        <Navbar className='sticky-top' collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Navbar.Brand href="/home">Dunedin Dairy</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="/products">Products</Nav.Link>
            <Nav.Link href="/news">News</Nav.Link>
            <Nav.Link href="/comments">Comments</Nav.Link>
            <Nav.Link href="/about">About Us</Nav.Link>
          </Nav>
          <Nav>
            <Nav.Link href='/login'>Login</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
}