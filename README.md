# KEOL-SSE (KEOLÏSSE)

## Description
**KEOLÏSSE** est une application conçue pour automatiser la planification de la flotte de tramway de la ville de Dijon. Elle permet, à partir de fichiers Excel renseignant diverses contraintes (maintenance des rames, équipements spécifiques tels que les brosses et pantos, etc.), ainsi que les particularités des journées/périodes, de produire un fichier Excel final contenant : 
- La planification des rames en circulation,
- Les horaires de départ et d’arrivée (à voir),
- Les quais attribués.

Ce projet a été réalisé principalement en Python dans le cadre d’un Hackathon, en réponse aux besoins du porteur de projet, **Keolis**.

---

## Fonctionnalités
- Lecture des fichiers Excel contenant les contraintes et informations.
- Prise en compte des particularités journalières et saisonnières.
- Génération automatique d’un fichier Excel consolidé avec la planification optimisée.

---

## Installation
### Pré-requis
- Python 3.x (A voir)
- Bibliothèques Python nécessaires :
  A confirmer

### Étapes
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/JustincGuechi/KEOL-SSE.git
   cd keolisse
   pip install -r requirements.txt
   ```
2. Assurez-vous d'avoir les fichiers Excel de contrainte et de configuration à jour avant d'utiliser l’application.

---

## Utilisation
1. Renseignez les fichiers Excel contenant les contraintes et les informations nécessaires (ex. : maintenance, caractéristiques des rames).
2. Lancez le script principal pour générer la planification :
   ```bash
   docker build -t keol-sse .
   docker run -it --rm -p 5000:5000 keol-sse
   ```
3. Le fichier Excel final contenant la planification sera généré dans le répertoire de sortie.

---

## Contribuer
Les contributions sont les bienvenues ! Voici comment vous pouvez participer :
- Signalez des bugs en ouvrant une issue.
- Soumettez des pull requests pour des améliorations ou nouvelles fonctionnalités.
- Contactez-nous pour toute suggestion.

---


## Remerciements
Merci à **Keolis** pour leur confiance et à l'équipe du Hackathon pour leur soutien et leurs idées.
