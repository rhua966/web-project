import React from 'react';
import { Switch, Route } from 'react-router-dom';

import HomePage from './components/HomePage';
import ProductPage from './components/ProductPage'
import CommentsPage from './components/CommentsPage'
import NewsPage from './components/NewsPage'
import AboutPage from './components/AboutPage';
import LoginPage from './components/LoginPage'
import RegisterPage from './components/RegisterPage'
import ErrorPage from './components/ErrorPage'

export default function Main() {

    return (
        <Switch>
            <Route exact path='/' component={HomePage} /> 
            <Route exact path='/home' component={HomePage} />
            <Route exact path='/products' component={ProductPage} />
            <Route exact path='/news' component={NewsPage} /> 
            <Route exact path='/comments' component={CommentsPage} /> 
            <Route exact path='/about' component={AboutPage} /> 
            <Route exact path='/login' component={LoginPage} />
            <Route exact path='/register' component={RegisterPage} /> 
            <Route component={ErrorPage} />
        </Switch>
    )
}