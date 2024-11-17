document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Récupérer les fichiers
    const fileInput1 = document.getElementById('file-input-1').files[0];
    const fileInput2 = document.getElementById('file-input-2').files[0];
    const fileInput3 = document.getElementById('file-input-3').files[0];

    // Vérifier si le fichier obligatoire est présent
    if (!fileInput1) {
        document.getElementById('error-message').textContent = "Les fichiers 1 et 2 sont obligatoires.";
        return;
    }

    // Effacer le message d'erreur si tout est bon
    document.getElementById('error-message').textContent = "";

    // Fonction pour envoyer un fichier via POST
    const uploadFile = (file, index) => {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("filename", `file_${index}`);

        return fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur lors de l'envoi du fichier ${index}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(`Fichier ${index} envoyé avec succès`, data);			
        })
        .catch(error => {
            console.error(`Erreur avec le fichier ${index}:`, error);
            document.getElementById('error-message').textContent = `Erreur lors de l'envoi du fichier ${index}.`;
        });
    };

    // Tableau pour les fichiers à envoyer
    const files = [fileInput1, fileInput2, fileInput3];
    let uploadPromises = [];

    // Envoyer chaque fichier un par un
    files.forEach((file, index) => {
        if (file) { // Si le fichier existe
            uploadPromises.push(uploadFile(file, index + 1));
        }
    });

    // Une fois tous les fichiers envoyés, afficher "Ok reçu"
    Promise.all(uploadPromises)
        .then(() => {
            document.getElementById('ram-management').innerHTML = " Tous les fichiers ont été envoyés avec succès.";
			//lance la page plan de remisage
            window.location.href = "http://" + window.location.hostname + ":5500/front/plan.html";
            
		})
        .catch(error => {
            console.error("Erreur générale:", error);
            document.getElementById('error-message').textContent = "Une erreur est survenue lors de l'envoi des fichiers.";
        });
});
