# 🚀 PortScanner

## English 🇬🇧

### Description

**PortScanner** is a web application that lets you scan TCP and UDP ports on a target host.  
The frontend uses **HTML**, **Tailwind CSS** 🎨, and **JavaScript**.  
The backend is powered by **Python (Flask)** 🐍.

### Features ✨

- Scan TCP and UDP ports.
- Select target IP address and protocol.
- See scan results in a user-friendly interface styled with Tailwind CSS.

### Requirements 🧰

- Python 3.9+
- Flask
- Node.js & npm (for Tailwind CSS build, if you want to customize styles)
- (Optional) Virtualenv for environment management

### Usage ⚡

1. **Clone the repository**
   ```bash
   git clone https://github.com/Briiice3R/PortScanner.git
   cd PortScanner
   ```

2. **Install Python dependencies**
   > The main dependency is Flask. Install it with:
   ```bash
   pip install flask
   ```
   Add other libraries as needed.

3. **Install Tailwind CSS dependencies (optional, only if you want to customize styles)**
   ```bash
   npm install
   npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
   ```
   If you only use the generated CSS, this step is not mandatory.

4. **Run the application**
   ```bash
   flask run
   ```
   By default, the app will run on `http://127.0.0.1:5000`.

5. **Open your browser** 🌐
   Visit `http://127.0.0.1:5000` and use the web interface to scan ports.

### Notes 📝

- UDP port scanning may not be reliable due to protocol limitations ⚠️.
- Make sure you have the necessary permissions to scan ports on target hosts 🔒.

---

## Français 🇫🇷

### Description

**PortScanner** est une application web permettant de scanner les ports TCP et UDP d’une machine cible.  
Le frontend utilise **HTML**, **Tailwind CSS** 🎨 et **JavaScript**.  
Le backend fonctionne avec **Python (Flask)** 🐍.

### Fonctionnalités ✨

- Scan des ports TCP et UDP.
- Sélection de l’adresse IP cible et du protocole.
- Affichage des résultats avec une interface moderne grâce à Tailwind CSS.

### Prérequis 🧰

- Python 3.9+
- Flask
- Node.js & npm (pour générer Tailwind CSS si tu veux personnaliser le style)
- (Optionnel) Virtualenv pour la gestion d’environnement

### Utilisation ⚡

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Briiice3R/PortScanner.git
   cd PortScanner
   ```

2. **Installer les dépendances Python**
   > La dépendance principale est Flask. Installe-la avec :
   ```bash
   pip install flask
   ```
   Ajoute les autres bibliothèques nécessaires au besoin.

3. **Installer Tailwind CSS (optionnel, seulement si tu veux personnaliser le style)**
   ```bash
   npm install
   npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
   ```
   Si tu utilises uniquement le CSS généré, cette étape n’est pas obligatoire.

4. **Lancer l’application**
   ```bash
   flask run
   ```
   Par défaut, l’application fonctionne sur `http://127.0.0.1:5000`.

5. **Ouvrir votre navigateur** 🌐
   Rendez-vous sur `http://127.0.0.1:5000` pour utiliser l’interface de scan de ports.

### Remarques 📝

- Le scan UDP peut être peu fiable à cause des limitations du protocole ⚠️.
- Assure-toi d’avoir les autorisations nécessaires pour scanner les ports des hôtes ciblés 🔒.
