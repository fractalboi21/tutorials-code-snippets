import React from "react";
import ReactDOM from "react-dom";
//jsx syntax
  function Welcome(props) {
    return <h1>hello {props.name}</h1>;
  }

  function App() {
    return(
      <div>
        <Welcome name="aakash" />
        <Welcome name="kash" />
        <Welcome name="mddie" />
      </div>
    );
  }

  ReactDOM.render(<App />, document.getElementById('root'));


