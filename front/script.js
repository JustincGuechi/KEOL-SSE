/*// Fonction pour afficher la section active
function showSection(sectionId) {
	// Masque toutes les sections
	const sections = document.querySelectorAll('.section');
	sections.forEach(section => section.classList.remove('active'));
	
	// Affiche la section demandée
	document.getElementById(sectionId).classList.add('active');
}
*/
// Fonction pour charger le JSON à partir du fichier local
function loadJSON() {
    // Utiliser fetch() pour charger le fichier JSON
    fetch('http://localhost:5000/plans')  // Le fichier JSON local dans le même répertoire que votre HTML
        .then(response => {
			console.log("test2");
            // Vérifier si le fichier JSON est bien récupéré
            if (!response.ok) {
                throw new Error('Erreur de récupération du JSON');
            }
            return response.json();  // Convertir la réponse en objet JavaScript
        })
        .then(data => {
			console.log(data);
            // Remplir la grille avec les données du premier plan
            if (data.places.length >0) {
                generateTable(data); // Passe les places du premier plan à la fonction
            } else {
                console.error('Données JSON invalides ou structure inattendue.');
            }
        })
        .catch(error => {
            console.error('Erreur :', error);
        });
}

function cleanTime(time) {
    if (time && time.includes(':')) {
        // Supprime la première partie avant les deux-points (par exemple "01:06:23" -> "06:23")
        const parts = time.split(':');
		return parts[1]+":"+parts[2];
    }
    return '—'; // Retourne un tiret si la donnée est invalide ou vide
}

function generateTable(jsonData) {
    const tableContainer = document.getElementById('tableau');
    const table = document.createElement('table');

    for (let row = 0; row < 7; row++) {
        const tr = document.createElement('tr');

        for (let col = 0; col < 5; col++) {
            const td = document.createElement('td');
            
            // Calcul de l'index
            const index = row * 5 + col;

            if (jsonData.places[index]) {
                const place = jsonData.places[index];

                // Appliquer la couleur de fond selon la valeur de 'couleur'
                let backgroundColor = '#fff'; // Par défaut, blanc

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

                // Appliquer la couleur de fond à la cellule
                td.style.backgroundColor = backgroundColor;

                // Création du conteneur principal
                const container = document.createElement('div');
                container.className = 'cell-container';

                // Badge pour ligne_id (en haut à gauche)
                if (place.ligne_id !== 'nan') {
                    const ligneBadge = document.createElement('div');
                    ligneBadge.className = 'ligne-badge';
                    ligneBadge.textContent = place.ligne_id;
                    td.appendChild(ligneBadge);
                }

                // Badge pour place_id (en haut à droite)
                if (place.place_id !== 'nan') {
                    const placeBadge = document.createElement('div');
                    placeBadge.className = 'place-badge';
                    placeBadge.textContent = place.place_id;
                    td.appendChild(placeBadge);
                }

                // Section supérieure (Rame mise en valeur)
                const topSection = document.createElement('div');
                topSection.className = 'top-section';
                topSection.innerHTML = `
                    <span class="rame">${place.rame !== 'nan' ? place.rame : ''}</span>
                `;

                // Section des horaires (4 blocs : 2 en haut et 2 en bas)
                const timeGrid = document.createElement('div');
                timeGrid.className = 'time-grid';
                timeGrid.innerHTML = `
                    <div class="time-box">${cleanTime(place.horaire_depart)}</div>
                    <div class="time-box">${cleanTime(place.horaire_arrivee)}</div>
                    <div class="time-box">${cleanTime(place.horaire_depart_bis)}</div>
					<div class="time-box">${cleanTime(place.horaire_arrivee_bis)}</div>
                `;

                // Ajouter les sections au conteneur
                container.appendChild(topSection);
                container.appendChild(timeGrid);
                td.appendChild(container);
            } else {
                td.classList.add('empty');
            }

            tr.appendChild(td);
        }

        table.appendChild(tr);
    }

    tableContainer.appendChild(table);
}








// Remplir la grille lorsque le DOM est prêt
//document.addEventListener("DOMContentLoaded", fillGrid);
/*
// Affiche la section Accueil par défaut
document.addEventListener('DOMContentLoaded', function() {
	showSection('home');
});*/
// Charger les données dès que la page est prête
window.onload = loadJSON;
