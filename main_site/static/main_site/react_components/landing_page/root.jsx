import React from 'react';
import ReactDOM from 'react-dom';

class LandingPage extends React.Component {

  componentDidMount() {

  }
  render() {
    return (
      <div>
        <div class="alert alert-danger" role="alert">Something went wrong</div>
      </div>
    );
  }
}

ReactDOM.render(<LandingPage />, document.getElementById("content"));