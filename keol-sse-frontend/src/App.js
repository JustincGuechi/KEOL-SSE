import React, { useState } from 'react';
import TramManagement from './TramManagement';
import UploadForm from './UploadForm';
import './App.css';

function App() {
  const [isUploaded, setIsUploaded] = useState(false);

  const handleUpload = () => {
    setIsUploaded(true);
  };

  return (
    <div className="App">
      {!isUploaded ? (
        <UploadForm onUpload={handleUpload} />
      ) : (
        <TramManagement />
      )}
    </div>
  );
}

export default App;
