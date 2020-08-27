import React from 'react';
import ReactDOM from 'react-dom';
import {Signin, Signup} from './components';

class AuthPage extends React.Component {
    render() {
        return (
            <div>
                Authentication Page
               <Signin/>
               <Signup/> 
            </div>
        );
    }
}

ReactDOM.render(<AuthPage />, document.getElementById("content"));