Snap Memories Downloader
Un script simple pour récupérer automatiquement tes Memories Snapchat en local à partir de l’export officiel de tes données, sans payer le stockage cloud de Snapchat.​

Fonctionnalités
Parcourt l’archive des données Snapchat exportées.​

Récupère les Memories (photos/vidéos) et les enregistre en local.​

Permet de sauvegarder tes souvenirs sans dépendre du cloud payant de Snapchat.​

Prérequis
Python 3 installé.​

Un compte Snapchat avec l’option de téléchargement des données activée.​

Télécharger tes données Snapchat (obligatoire)
Avant d’utiliser ce script, tu dois d’abord télécharger tes données Snapchat au format dossier zip :​

Va dans les paramètres de ton compte Snapchat (application ou site web).​

Demande une copie de tes données (option « Télécharger mes données »).​

Attends de recevoir l’email de Snapchat avec le lien de téléchargement.​

Télécharge l’archive de tes données au format .zip.​

Place ce fichier .zip dans le dossier du projet ou note bien son chemin complet.​

Ce fichier zip est la source que le script va utiliser pour retrouver et télécharger tes Memories.​

Installation
Cloner le dépôt :​

bash
git clone https://github.com/saadyaq/snap_mem.git
cd snap_mem
(Optionnel) Créer un environnement virtuel.​

Installer les dépendances si un requirements.txt est ajouté plus tard :​

bash
pip install -r requirements.txt
Utilisation
Assure-toi d’avoir téléchargé tes données Snapchat en .zip comme indiqué plus haut.​

Place le fichier .zip dans le dossier du projet ou adapte le chemin dans main.py si nécessaire.​

Lance le script :​

bash
python main.py
Les Memories seront téléchargées / copiées dans un dossier de sortie (par exemple memories/).​

Si le script accepte des arguments (chemin du zip, dossier de sortie, etc.), précise-les dans la commande ou dans le code, puis mets à jour cette section en conséquence.​

Avertissement
Projet à usage strictement personnel.​

Respecte les conditions d’utilisation de Snapchat et les lois en vigueur.​

L’auteur n’est pas affilié à Snapchat et n’est pas responsable d’un usage abusif de cet outil.
