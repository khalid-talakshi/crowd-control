import React from 'react';
import ReactDOM from 'react-dom';
import 'normalize.css/normalize.css'
import './styles/styles.scss';
import Dashboard from './components/Dashboard';

// Renders App onto Public HTML File 
ReactDOM.render(<Dashboard />, document.getElementById('app'));