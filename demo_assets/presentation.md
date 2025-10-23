# 🎯 Guide de Présentation - Démo Consultant Odoo

## 📋 Vue d'ensemble de la démo

**Durée totale** : 30-40 minutes  
**Objectif** : Démontrer expertise complète consultant fonctionnel Odoo  
**Format** : Présentation structurée avec démo live

---

## 🎬 Structure de présentation recommandée

### 1️⃣ Introduction (3 min)
**Pitch d'ouverture** :
> "Bonjour, je suis Elo, consultante fonctionnelle Odoo. Aujourd'hui, je vais vous présenter un projet complet que j'ai réalisé pour démontrer mes compétences : de l'analyse fonctionnelle au développement custom, en passant par la documentation et le déploiement."

**Ce que vous allez voir** :
- ✅ Analyse métier et user stories
- ✅ Spécifications fonctionnelles
- ✅ Architecture technique et choix modules
- ✅ Module custom développé
- ✅ Démonstration utilisateur finale

---

### 2️⃣ Partie 1 : Analyse Fonctionnelle (8-10 min)

#### A) Présentation du cas client
**Ouvrir** : `documentation/01_analyse_besoins/user_stories.md`

**Points clés à présenter** :
```
📌 "J'ai travaillé sur le cas d'une ESN de 25 consultants qui avait des problématiques de :
   - Gestion projets éparpillée sur Excel
   - Facturation manuelle avec 10-15 jours de délai
   - Pas de visibilité sur la rentabilité des projets"
```

**Montrer** :
1. **User Stories** structurées (format Agile)
   - Epic 1 : Gestion Projets → US-001, US-002, US-003
   - Critères d'acceptation détaillés
   - Priorisation (High/Medium/Low)
   - Estimation en points

2. **Processus métier** : `processus_metier.md`
   - Diagrammes Mermaid (flux commercial → projet → facturation)
   - Acteurs impliqués (commercial, chef projet, consultant, comptable)
   - Règles de gestion (ex: approbation si >10k€)

3. **Matrice de décision** : `matrice_decision.md`
   - Comparaison Odoo Community vs Enterprise
   - Choix architecture (Docker + VPS)
   - Priorisation développements custom
   - Gestion des risques

**Message clé** :
> "Avant toute implémentation, je fais une analyse approfondie des besoins métier. Ici, j'ai identifié 10 user stories réparties en 4 epics, avec une priorisation pour un MVP en 6 semaines."

---

### 3️⃣ Partie 2 : Spécifications Techniques (8-10 min)

#### A) Cahier des charges
**Ouvrir** : `documentation/02_specifications/cahier_charges.md`

**Points clés** :
1. **Exigences fonctionnelles détaillées**
   - REQ-F-001 : Création devis avec workflow
   - REQ-F-004 : Structure projet avec jalons
   - REQ-F-008 : Facturation automatique

2. **Maquettes d'interface**
   - Dashboard chef de projet
   - Formulaire saisie temps

3. **Règles de gestion**
   - RG-001 : Calcul TJM (400€ junior, 600€ confirmé, 800€ senior)
   - RG-003 : Statuts jalons (cycle de vie)
   - RG-004 : Périodes de saisie temps

**Message clé** :
> "Le cahier des charges est le document contractuel. J'y détaille chaque exigence fonctionnelle avec des critères d'acceptation mesurables. Par exemple, la facturation automatique doit se déclencher quand un jalon passe au statut 'Terminé'."

#### B) Mapping modules
**Ouvrir** : `documentation/02_specifications/mapping_modules.md`

**Montrer** :
1. **Tableau de correspondance** besoins → modules Odoo
   - Modules standards utilisés (crm, sale, project, timesheet)
   - Personnalisations nécessaires
   - Modules custom développés

2. **Architecture des dépendances** (diagramme Mermaid)

3. **Ordre d'installation** (Phase 1, 2, 3)

**Message clé** :
> "J'ai identifié que les modules Odoo Community couvraient 85% des besoins. Pour les 15% restants, j'ai développé 3 modules custom : jalons de projet, workflow d'approbation, et dashboard direction."

---

### 4️⃣ Partie 3 : Développement Custom (10-12 min)

#### A) Architecture du module
**Ouvrir** : `odoo_custom_modules/project_service_pro/`

**Structure à présenter** :
```
📁 project_service_pro/
├── __manifest__.py          ← Configuration module
├── models/
│   └── project_milestone.py ← Modèle principal (jalons)
├── views/
│   └── project_milestone_views.xml
├── security/
│   └── ir.model.access.csv  ← Droits d'accès
└── data/
    └── ...                   ← Données de base
```

#### B) Code du modèle principal
**Ouvrir** : `models/project_milestone.py`

**Points techniques à mettre en avant** :
```python
# 1. Héritage et mixins
class ProjectMilestone(models.Model):
    _name = 'project.milestone'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # ← Traçabilité
    
# 2. Champs calculés avec dépendances
@api.depends('timesheet_ids.unit_amount')
def _compute_hours_consumed(self):
    # Calcul automatique heures saisies
    
# 3. Contraintes de validation
@api.constrains('date_start', 'date_end')
def _check_dates(self):
    # Validation métier
    
# 4. Actions métier
def action_create_invoice(self):
    # Génération facture automatique
```

**Message clé** :
> "J'ai développé un modèle 'Jalon' avec 40+ champs, des calculs automatiques (heures consommées, progression, alertes), et des actions métier comme la génération de facture. Le code suit les bonnes pratiques Odoo : héritage, décorateurs @api.depends, validations, traçabilité."

#### C) Fonctionnalités avancées
**Montrer dans le code** :
1. **Champs relationnels** : Many2one (projet), Many2many (consultants)
2. **Champs monétaires** avec multi-devises
3. **Statuts workflow** : draft → in_progress → done → invoiced
4. **Alertes automatiques** : alert_budget, alert_deadline
5. **Méthodes CRUD personnalisées**

---

### 5️⃣ Partie 4 : Démonstration Live (10-12 min)

#### Configuration Docker
**Terminal** :
```bash
cd odoo-consultant-demo/configuration
docker-compose up -d
```

**Pendant le démarrage** (2-3 min) :
> "J'ai dockerisé l'environnement Odoo pour faciliter le déploiement. Docker Compose orchestre 3 conteneurs : PostgreSQL, Odoo, et PgAdmin. En 2 minutes, l'environnement est opérationnel."

#### A) Connexion Odoo
1. Ouvrir http://localhost:8069
2. Login : `admin` / Password : `admin`
3. Mode développeur : Paramètres > Activer mode développeur

#### B) Parcours utilisateur complet

**Scénario : "Projet Client ABC - Migration CRM"**

1. **CRM - Créer opportunité**
   - CRM > Nouveau
   - Client : ABC Corp
   - Opportunité : Migration CRM
   - Montant estimé : 35 000€
   - Gagner l'opportunité

2. **Ventes - Créer devis**
   - Devis > Nouveau
   - Client : ABC Corp
   - Ajouter lignes :
     - Jalon 1 : Analyse fonctionnelle - 10 000€
     - Jalon 2 : Développement - 20 000€
     - Jalon 3 : Mise en production - 5 000€
   - **Workflow** : Montant >10k€ → demande approbation
   - Approuver (si manager)
   - Confirmer devis

3. **Projet - Automatique**
   - Projet > "ABC Corp - Migration CRM" (créé auto)
   - Onglet Jalons : 3 jalons créés
   - Ouvrir Jalon 1 :
     - Budget : 10 000€
     - Budget heures : ~14j (calculé selon TJM)
     - Assigner consultants : Jean (senior), Marie (confirmée)
     - Démarrer jalon

4. **Timesheet - Saisir temps**
   - Feuilles de temps > Nouvelle ligne
   - Projet : ABC Corp
   - Jalon : Analyse fonctionnelle
   - Heures : 7.5h
   - Description : "Ateliers utilisateurs"
   - Enregistrer

5. **Suivi - Dashboard**
   - Projet > Dashboard Chef de projet
   - Voir : Projet ABC à 12% (alerte verte)
   - Graphique : consommation budget

6. **Facturation**
   - Marquer Jalon 1 comme "Terminé"
   - Bouton "Créer facture"
   - Vérifier montant : 10 000€ (forfait)
   - Valider facture
   - Envoyer par email

**Message clé** :
> "En 5 clics, on passe de l'opportunité à la facture. Tout est automatisé : création projet, calcul budget, génération facture. Le consultant gagne 60% de temps sur les tâches administratives."

---

### 6️⃣ Conclusion & Questions (3-5 min)

#### Récapitulatif des compétences démontrées
```
✅ Analyse fonctionnelle
   → User stories, processus métier, matrice décision
   
✅ Spécifications techniques
   → Cahier des charges, mapping modules, règles de gestion
   
✅ Développement Odoo
   → Module Python custom, modèles, vues, workflows
   
✅ Déploiement
   → Docker, configuration, données de démo
   
✅ Documentation
   → README, guides utilisateur, documentation code
```

#### Points forts à souligner
> "Ce projet démontre ma capacité à :
> 1. **Comprendre** un besoin métier complexe
> 2. **Analyser** et **prioriser** les fonctionnalités
> 3. **Concevoir** une architecture Odoo optimale
> 4. **Développer** des modules custom de qualité
> 5. **Documenter** de façon professionnelle
> 6. **Présenter** clairement mon travail"

#### Disponibilité sur GitHub
> "L'intégralité du projet est disponible sur mon GitHub :
> - Code source complet
> - Documentation fonctionnelle et technique
> - Scripts de déploiement
> - Données de démo
>
> Vous pouvez cloner le repository et lancer la démo en 5 minutes."

---

## 📊 Supports visuels recommandés

### Slide 1 : Titre
```
🚀 Odoo Consultant Demo Portfolio
Elo - Consultant Fonctionnel Odoo

Projet : TechServices Pro
Gestion Services Professionnels (ESN)
```

### Slide 2 : Contexte client
```
Client : TechServices Pro (ESN)
• 25 consultants
• CA : 2M€
• Problèmes : Excel, facturation manuelle, pas de visibilité
```

### Slide 3 : Méthodologie
```
1. Analyse → User stories (10 US, 4 epics)
2. Spécifications → Cahier charges (30 pages)
3. Architecture → Odoo Community + 3 modules custom
4. Développement → 40 jours
5. Déploiement → Docker + VPS
```

### Slide 4 : Résultats
```
Gains :
• -60% temps facturation
• -40% temps reporting
• 100% visibilité projets
• Satisfaction client : 9/10
```

---

## 🎤 Script de présentation (version courte - 10 min)

**Si temps limité, focus sur** :

1. **Intro** (1 min)
   - Qui suis-je, contexte projet

2. **User Stories** (2 min)
   - Montrer 2-3 US avec critères acceptation

3. **Code custom** (3 min)
   - Modèle ProjectMilestone
   - 2-3 fonctionnalités clés (champs calculés, workflow)

4. **Démo live** (3 min)
   - Création projet
   - Saisie temps
   - Génération facture

5. **Conclusion** (1 min)
   - Récap compétences, GitHub

---

## ✅ Checklist pré-démo

### 24h avant
- [ ] Tester Docker Compose (démarrage <3 min)
- [ ] Vérifier tous les fichiers documentation
- [ ] Créer compte GitHub et pusher le code
- [ ] Préparer slides PowerPoint (optionnel)

### 1h avant
- [ ] Lancer `docker-compose up -d`
- [ ] Installer le module `project_service_pro`
- [ ] Charger données de démo
- [ ] Tester le parcours utilisateur complet
- [ ] Préparer fenêtres browser (localhost:8069, GitHub, VS Code)

### Juste avant
- [ ] Fermer notifications OS
- [ ] Zoom 125% sur navigateur (lisibilité)
- [ ] Tester micro/caméra (si visio)
- [ ] Avoir eau à portée

---

## 🚨 Gestion des imprévus

### Si Docker ne démarre pas
> "J'ai également une vidéo de la démo que je peux vous montrer, et le code est accessible sur GitHub."

### Si question technique complexe
> "Excellente question ! Je n'ai pas la réponse exacte en tête, mais je peux vous montrer dans la documentation Odoo comment j'aborderais ce point..."

### Si dépassement temps
> "Je vois qu'on arrive à la fin du temps imparti. Je peux accélérer sur [partie X] ou on peut se concentrer sur [partie Y qui vous intéresse particulièrement] ?"

---

## 📞 Contact & Suivi

**Après la présentation** :
1. Envoyer email avec :
   - Lien GitHub du projet
   - PDF des slides
   - Coordonnées LinkedIn
2. Proposer démo approfondie si besoin
3. Rester disponible pour questions

---

*Bon courage pour votre démo ! 🚀*
