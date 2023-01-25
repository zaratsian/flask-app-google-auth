import React from "react";
import axios from "axios";

class App extends React.Component {
  state = {
    data: null,
  };

  componentDidMount() {
    // Make a GET request to the backend
    axios.get("https://5000-cs-45357632014-default.cs-us-east1-pkhd.cloudshell.dev/data").then((res) => {
      this.setState({ data: res.data });
    });
  }

  render() {
    return (
      <div>
        {this.state.data ? (
          <div>{this.state.data.message}</div>
        ) : (
          <div>Loading...</div>
        )}
      </div>
    );
  }
}

export default App;
