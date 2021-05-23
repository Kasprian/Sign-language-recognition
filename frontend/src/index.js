import React from 'react';
import ReactDOM from 'react-dom';
import { CameraFeed } from './components/camera-feed';

import './styles.css';

// Upload to local seaweedFS instance
const uploadImage = async file => {
    const formData = new FormData();
    formData.append('picture', file);
    formData.append("type", 'image/jpeg')
    var link = document.createElement("a");
    link.download = "image.png";
    link.href = URL.createObjectURL(file);
    link.click()
    console.log(link.href);
    const requestOptions = {
        method: 'POST',
        body: formData
    };
    fetch('http://localhost:8000/recognize/', requestOptions)
        .then(response => response.json())
        .then(function (response) {
            console.log('response')
            console.log(response)
        });

};


function App() {
    return (
        <div className="App">
            <h1>Image capture test</h1>
            <p>Capture image from USB webcamera and upload to form</p>
            <CameraFeed sendFile={uploadImage} />
        </div>
    );
}

const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
