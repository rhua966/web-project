import React, { useState } from "react";
import { Button, FormGroup, FormControl, FormLabel } from "react-bootstrap";
import { NavLink } from 'react-router-dom'

export default function LoginPage() {
    
    
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function validateForm() {
        return username.length > 0 && password.length > 0;
    }

    function handleSubmit(event) {
        console.log(`${username}${password}`)
        event.preventDefault();
    }

    return (
        <div className="Login">
            <form onSubmit={handleSubmit}>
                <FormGroup controlId="username" bsSize="large">
                <FormLabel>Username</FormLabel>
                <FormControl
                    autoFocus
                    type="username"
                    value={username}
                        onChange={e => { setUsername(e.target.value); }}
                />
                </FormGroup>
                <FormGroup controlId="password" bsSize="large">
                <FormLabel>Password</FormLabel>
                <FormControl
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    type="password"
                />
                </FormGroup>
                <Button block bsSize="large" disabled={!validateForm()} type="submit">
                    Login
                </Button>
                <br></br>
                <NavLink to='/register'>Don't have an account?</NavLink>
            </form>
            
        </div>
    );
}