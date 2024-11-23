
import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/getjson?year=2024&month=11&day=18')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Erreur :', error));
  }, []);

  const sendJSON = () => {
    fetch('http://127.0.0.1:5000/getexcel', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.blob())
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = url;
      a.download = 'data.xlsx';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
    })
    .catch(error => {
      console.error('Erreur :', error);
      const backupUrl = 'http://127.0.0.1:5500/data/20130304_SCH_DEX_Plan_de_remisage.xlsm';
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = backupUrl;
      a.download = '20130304_SCH_DEX_Plan_de_remisage.xlsm';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    });
  };

  return (
    <div className="App">
      <nav>
        <a href="#home">Accueil</a>
        <a href="#tram">Gestion des Rames</a>
        <a href="#contact">Contact</a>
      </nav>
      <main>
        <h1>Gestion des Rames de Tram</h1>
        <button onClick={sendJSON}>Envoyer la Validation</button>
        <div className="grid-container" id="tableau">
          {/* Render your table here using data */}
        </div>
        <div id="atelier"></div>
      </main>
      <footer>
        &copy; 2024 Gestion des Rames de Tram - Tous droits réservés.
      </footer>
    </div>
  );
}

export default App;