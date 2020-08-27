import React from 'react';
import ReactDOM from 'react-dom';

class AuthPage extends React.Component {
 render() {
  return(
   <div>
    Authentication Page
   </div>
  );
 }
}

ReactDOM.render(<AuthPage />, document.getElementById("content"));