
import React from 'react';
import './App.css';

function UploadForm({ onUpload }) {
  return (
    <div className="container">
      <div className="image-container">
        <img src="tram_3.jpg" alt="Rames de Tram" className="background-image" />
      </div>
      <h1 className="title">Gestion du plan de remisage des tramways</h1>
      <p className="description">Chargez vos fichiers de contraintes Excel.</p>
      <form id="upload-form" className="upload-container" onSubmit={(e) => {
        e.preventDefault();
        onUpload();
      }}>
        <div className="file-input-group">
          <label htmlFor="file-input-1">Maintenance journalière (Obligatoire) :</label>
          <input type="file" id="file-input-1" accept=".xlsx" required />
        </div>
        <div className="file-input-group">
          <label htmlFor="file-input-2">KMs parcourus (Optionnel) :</label>
          <input type="file" id="file-input-2" accept=".xlsx" />
        </div>
        <div className="file-input-group">
          <label htmlFor="file-input-3">Template plan de remisage (Optionnel) :</label>
          <input type="file" id="file-input-3" accept=".xlsx" />
        </div>
        <button type="submit" id="upload-btn">Valider</button>
      </form>
      <p id="error-message" className="error-message"></p>
      <div id="ram-management" className="ram-management"></div>
    </div>
  );
}

export default UploadForm;