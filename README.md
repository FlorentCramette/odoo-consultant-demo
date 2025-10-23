# 🚀 Odoo Consultant Demo Portfolio

## 📋 Vue d'ensemble
Ce repository démontre mes compétences en tant que **Consultant Fonctionnel Odoo**, incluant :
- 📝 Analyse fonctionnelle et rédaction de spécifications
- 👥 Gestion des user stories et besoins métier
- 🔧 Paramétrage et customisation Odoo Community
- 📊 Modélisation de processus métier
- 🐳 Déploiement et documentation technique

## 🎯 Cas d'usage : Gestion de Services Professionnels
Ce projet illustre l'implémentation d'une solution Odoo pour une entreprise de services IT, couvrant :
- Gestion de projets client avec jalons
- Suivi du temps et facturation
- Workflow d'approbation de devis
- Reporting personnalisé

## 📁 Structure du projet
```
odoo-consultant-demo/
├── 📄 README.md                          # Ce fichier
├── 📂 documentation/
│   ├── 01_analyse_besoins/              # Analyse métier
│   │   ├── user_stories.md              # User stories détaillées
│   │   ├── processus_metier.md          # Diagrammes de flux
│   │   └── matrice_decision.md          # Critères et choix techniques
│   ├── 02_specifications/               # Spécifications fonctionnelles
│   │   ├── cahier_charges.md            # Document de référence
│   │   ├── mapping_modules.md           # Modules Odoo utilisés
│   │   └── regles_gestion.md            # Règles métier
│   └── 03_technique/                    # Documentation technique
│       ├── architecture.md              # Architecture solution
│       ├── personnalisations.md         # Custom développés
│       └── guide_deploiement.md         # Procédure déploiement
├── 📂 odoo_custom_modules/
│   └── project_service_pro/             # Module custom exemple
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       ├── views/
│       ├── security/
│       ├── data/
│       └── README.md
├── 📂 configuration/
│   ├── docker-compose.yml               # Environnement Odoo
│   ├── odoo.conf                        # Configuration Odoo
│   └── requirements.txt                 # Dépendances Python
└── 📂 demo_assets/
    ├── screenshots/                     # Captures d'écran
    └── presentation.md                  # Support de démo
```

## 🛠️ Technologies utilisées
- **Odoo Community 17.0**
- **Python 3.10+**
- **PostgreSQL 15**
- **Docker & Docker Compose**
- **Git & GitHub**

## 🚀 Quick Start

### Prérequis
- Docker Desktop installé
- Git
- 4 GB RAM minimum

### Installation
```bash
# 1. Cloner le repository
git clone https://github.com/votre-username/odoo-consultant-demo.git
cd odoo-consultant-demo

# 2. Lancer l'environnement Odoo
docker-compose up -d

# 3. Attendre le démarrage (2-3 minutes)
# Odoo sera accessible sur http://localhost:8069

# 4. Se connecter
# Email: admin
# Password: admin
```

### Configuration de la démo
```bash
# Installer le module custom
# 1. Activer le mode développeur dans Odoo
# 2. Apps > Mettre à jour la liste des apps
# 3. Rechercher "Project Service Pro"
# 4. Installer
```

## 📖 Parcours de démonstration

### 1️⃣ Documentation fonctionnelle (15 min)
- Présentation des user stories
- Analyse des processus métier
- Matrice de décision pour choix modules

### 2️⃣ Configuration Odoo (10 min)
- Modules standards configurés
- Workflow personnalisé
- Règles de gestion implémentées

### 3️⃣ Développement custom (10 min)
- Module Python développé
- Modèles, vues, et logique métier
- Bonnes pratiques Odoo

### 4️⃣ Démonstration utilisateur (10 min)
- Parcours utilisateur complet
- Cas d'usage métier réel
- Reporting et analyses

## 💼 Compétences démontrées

### Analyse Fonctionnelle
✅ Recueil et formalisation des besoins  
✅ Rédaction de user stories (format Agile)  
✅ Modélisation de processus métier (BPMN)  
✅ Rédaction de cahier des charges  

### Expertise Odoo
✅ Connaissance approfondie modules Odoo  
✅ Paramétrage et configuration  
✅ Développement modules custom Python  
✅ Gestion des workflows et automatisations  

### Gestion de Projet
✅ Méthodologie Agile/Scrum  
✅ Documentation technique et fonctionnelle  
✅ Communication client (specs claires)  
✅ Déploiement et mise en production  

### Outils & Techniques
✅ Git & GitHub (versioning)  
✅ Docker (containerisation)  
✅ Markdown (documentation)  
✅ Diagrammes (Mermaid, BPMN)  

## 📞 Contact
**Flo - Consultant Fonctionnel Odoo**  
📧 [Votre email]  
💼 [LinkedIn]  
🐙 [GitHub]

## 📄 Licence
Ce projet est à usage de démonstration professionnelle.

---

*Dernière mise à jour : Octobre 2025*
