import React, { useEffect, useState } from 'react';

const NavBar = () => (
  <nav>
    <a href="#home">Accueil</a>
    <a href="#tram">Gestion des Rames</a>
    <a href="#contact">Contact</a>
  </nav>
);

const TableCell = ({ place, cleanTime }) => {
  let backgroundColor = '#ffffff'; // Blanc par défaut
  if (place) {
    switch (place.couleur) {
      case 'L':
        backgroundColor = '#a8e6a6'; // Vert pastel
        break;
      case 'N':
        backgroundColor = '#ffd699'; // Orange pastel
        break;
      case 'T':
        backgroundColor = '#ffcccb'; // Rouge pastel
        break;
      default:
        backgroundColor = '#ffffff'; // Blanc par défaut
    }
  }

  return (
    <td className="cell-container" style={{ backgroundColor }}>
      {place && (
        <>
          <div className="ligne-badge">{place.ligne_id}</div>
          <div className="place-badge">{place.place_id}</div>
          <div className="top-section">
            <span className="rame" contentEditable>{place.rame}</span>
          </div>
          <div className="time-grid">
            <div className="time-box">{cleanTime(place.horaire_depart)}</div>
            <div className="time-box">{cleanTime(place.horaire_arrivee)}</div>
            {place.horaire_depart_bis && <div className="time-box">{cleanTime(place.horaire_depart_bis)}</div>}
            {place.horaire_arrivee_bis && <div className="time-box">{cleanTime(place.horaire_arrivee_bis)}</div>}
          </div>
        </>
      )}
    </td>
  );
};

const Table = ({ data, cleanTime }) => (
  <div className="table-container" id="tableau">
    <table>
      <tbody>
        {data && Array.from({ length: 7 }).map((_, rowIndex) => (
          <tr key={rowIndex}>
            {Array.from({ length: 5 }).map((_, colIndex) => {
              const index = rowIndex * 5 + colIndex;
              const place = data.places[index];
              return <TableCell key={colIndex} place={place} cleanTime={cleanTime} />;
            })}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

const MaintenanceList = ({ data }) => (
  <div id="atelier">
    {data && data.maintenances.map((maintenance, index) => (
      <div key={index} contentEditable>{maintenance.numero}</div>
    ))}
  </div>
);

const TramManagement = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/getjson?year=2024&month=11&day=18')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Erreur :', error));
  }, []);

  const cleanTime = (time) => {
    if (time && time.includes(':')) {
      const parts = time.split(':');
      return parts[1] + ":" + parts[2];
    }
    return '—';
  };

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
    });
  };

  return (
    <div className="TramManagement">
      <NavBar />
      <main>
        <h1>Gestion des Rames de Tram</h1>
        <button onClick={sendJSON}>Envoyer la Validation</button>
        <Table data={data} cleanTime={cleanTime} />
        <MaintenanceList data={data} />
      </main>
      <footer>
        &copy; 2024 Gestion des Rames de Tram - Tous droits réservés.
      </footer>
    </div>
  );
};

export default TramManagement;