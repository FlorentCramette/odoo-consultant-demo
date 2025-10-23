# 📋 Cahier des Charges Fonctionnel - TechServices Pro

## 1. Contexte et Objectifs

### 1.1 Présentation de l'entreprise
**TechServices Pro** est une ESN (Entreprise de Services du Numérique) spécialisée dans le conseil et l'accompagnement IT.

- **Effectif** : 25 consultants (5 seniors, 15 confirmés, 5 juniors)
- **CA annuel** : ~2M€
- **Secteurs clients** : Banque, Assurance, Industrie
- **Prestations** : Conseil, développement, formation

### 1.2 Problématiques actuelles
❌ **Gestion projet** : Excel partagé, pas de vision consolidée  
❌ **Suivi temps** : Saisie manuelle, erreurs fréquentes  
❌ **Facturation** : Process manuel, délai 10-15 jours après livraison  
❌ **Pilotage** : Reporting hebdomadaire chronophage  
❌ **Planning** : Affectations consultants sur emails/Excel  

### 1.3 Objectifs du projet
✅ **Centraliser** : Une plateforme unique pour tous les processus  
✅ **Automatiser** : Facturation, alertes, reporting  
✅ **Piloter** : Visibilité temps réel sur projets et ressources  
✅ **Optimiser** : Réduire tâches admin de 40%  
✅ **Satisfaire** : Meilleure réactivité client  

---

## 2. Périmètre Fonctionnel

### 2.1 Modules inclus (Phase 1)

#### 🎯 Gestion Commerciale (CRM + Ventes)
- Gestion pipeline opportunités
- Création devis avec templates
- **Workflow approbation** si devis >10k€
- Conversion devis → projet automatique
- Historique interactions client

#### 📊 Gestion de Projets
- Création projet avec jalons/phases
- Affectation consultants par jalon
- Budgétisation par jalon (heures)
- **Alertes automatiques** si dépassement >90%
- Statuts jalon : À faire / En cours / Terminé / Facturé

#### ⏱️ Suivi du Temps
- Saisie feuille de temps quotidienne
- Sélection Projet > Jalon > Tâche
- Timer intégré (démarrer/arrêter)
- Validation chef de projet (hebdomadaire)
- Export Excel pour paie

#### 💰 Facturation
- Génération facture automatique à fin de jalon
- Calcul selon type contrat :
  - **Forfait** : montant fixe du jalon
  - **Régie** : heures réelles × TJM
- Workflow validation comptable
- Envoi automatique par email
- Relances impayés (J+30, J+45)

#### 📈 Reporting & Dashboards
- **Dashboard chef de projet** : mes projets actifs, consommation budget
- **Dashboard direction** : CA mensuel, taux occupation, projets en alerte
- **Rapport rentabilité** : marge par projet (heures budgétées vs réelles)

### 2.2 Modules exclus (Phase 2 ou ultérieur)
⏸️ Planning ressources avancé (vue Gantt interactif)  
⏸️ Portail client avec accès temps réel  
⏸️ Gestion des congés/absences  
⏸️ Evaluation/compétences consultants  
⏸️ Module RH complet (recrutement, entretiens)  

---

## 3. Exigences Fonctionnelles Détaillées

### 3.1 Gestion des Devis

#### REQ-F-001 : Création devis
**Description** : Le commercial crée un devis à partir d'un template.

**Workflow** :
1. Sélection client existant (ou création rapide)
2. Choix template : "Forfait projet" ou "Régie"
3. Ajout lignes de devis :
   - Forfait : Description jalon + montant fixe
   - Régie : Nombre jours × TJM
4. Conditions commerciales pré-remplies (délai paiement, pénalités)
5. Génération PDF automatique (logo, mentions légales)

**Champs obligatoires** :
- Client, contact
- Date validité devis (30 jours par défaut)
- Lignes de devis (min. 1)
- Conditions de paiement

#### REQ-F-002 : Workflow approbation devis
**Règle métier** : Tout devis >10k€ nécessite validation manager.

**Processus** :
1. Commercial soumet le devis → Statut "En attente approbation"
2. Email automatique au manager avec lien direct
3. Manager approuve/refuse/demande modification
4. Si refusé : commentaire obligatoire + retour au commercial
5. Si approuvé : passage statut "Approuvé" → envoyable au client

**SLA** : Validation manager sous 48h ouvrées

#### REQ-F-003 : Conversion devis en projet
**Déclencheur** : Confirmation du devis par le client

**Actions automatiques** :
1. Création projet avec nom du client
2. Création des jalons selon lignes du devis (1 ligne = 1 jalon)
3. Budget heures calculé : montant ligne / TJM moyen
4. Statut initial jalon : "À planifier"
5. Notification chef de projet assigné

---

### 3.2 Gestion des Projets et Jalons

#### REQ-F-004 : Structure projet
**Hiérarchie** :
```
Projet "Client XYZ - Migration CRM"
├── Jalon 1 : Analyse fonctionnelle (20j - 10k€)
│   ├── Tâche : Ateliers utilisateurs
│   ├── Tâche : Rédaction specs
│   └── Tâche : Validation client
├── Jalon 2 : Développement (40j - 20k€)
└── Jalon 3 : Mise en production (10j - 5k€)
```

**Champs jalon** :
- Nom
- Date début / fin prévisionnelle
- Budget heures
- Montant facturable (€)
- Consultant(s) assigné(s)
- Statut : À planifier / En cours / Terminé / Validé / Facturé

#### REQ-F-005 : Alertes dépassement budget
**Règle** : Alerte automatique si consommation heures >90% budget jalon

**Actions** :
1. Email automatique au chef de projet
2. Bandeau orange dans vue projet
3. Blocage saisie temps si >120% (configurable)

**Calcul en temps réel** : Somme(heures saisies) / Budget heures

---

### 3.3 Suivi du Temps

#### REQ-F-006 : Saisie feuille de temps
**Interface consultant** :
- Vue calendrier semaine
- Glisser-déposer pour saisie rapide
- Timer intégré (start/stop)
- Copie semaine précédente (bouton)

**Saisie ligne** :
- Date
- Projet > Jalon (sélection liée)
- Nombre d'heures (0.5, 1, 7.5...)
- Description (optionnelle)
- Type (Projet client / Interne / Formation / Commercial)

**Règles de validation** :
- Max 12h par jour
- Warning si semaine >40h
- Impossible de saisir sur jalon "Facturé" (verrouillé)

#### REQ-F-007 : Validation chef de projet
**Fréquence** : Hebdomadaire (chaque lundi)

**Processus** :
1. Chef de projet reçoit email "Temps à valider"
2. Vue récapitulative : toutes les lignes de ses consultants
3. Validation par lot ou ligne par ligne
4. Possibilité de refuser avec commentaire
5. Une fois validé → verrouillé, utilisable pour facturation

---

### 3.4 Facturation

#### REQ-F-008 : Génération facture automatique
**Déclencheur** : Chef de projet clique "Jalon terminé" → "À facturer"

**Process automatique** :
1. Système crée brouillon de facture
2. Lignes de facture :
   - **Si forfait** : 1 ligne avec montant jalon
   - **Si régie** : Somme(heures validées) × TJM
3. Conditions paiement reprises du devis
4. Échéance calculée (ex: 30 jours fin de mois)

**Ajustements manuels** : Comptable peut modifier avant validation

#### REQ-F-009 : Envoi et relances
**Actions automatiques** :
1. **J0 (validation facture)** : Email client avec PDF attaché
2. **J+30 (échéance)** : Si non payée → Relance niveau 1 (amical)
3. **J+45** : Relance niveau 2 (ferme)
4. **J+60** : Notification direction pour contentieux

**Templates email** : Personnalisables avec variables (n° facture, montant, etc.)

---

### 3.5 Reporting et Pilotage

#### REQ-F-010 : Dashboard chef de projet
**KPI affichés** :
- Mes projets actifs (nombre)
- Budget total vs consommé (%)
- Projets en alerte (rouge si >100%)
- Prochaines échéances (jalons à terminer cette semaine)

**Graphiques** :
- Évolution heures consommées par projet (ligne)
- Répartition temps par type (projet/interne/commercial) - camembert

#### REQ-F-011 : Dashboard direction
**KPI affichés** :
- CA du mois (vs objectif)
- CA prévisionnel à 3 mois (jalons planifiés)
- Taux d'occupation moyen consultants
- Nombre projets actifs
- Top 5 clients (CA)
- Impayés en cours (montant)

**Graphiques** :
- CA mensuel 12 derniers mois (histogramme)
- Évolution taux occupation (courbe)

#### REQ-F-012 : Rapport rentabilité projet
**Données calculées** :
| Projet | Heures budgétées | Heures réelles | Écart | CA facturé | Coût réel | Marge € | Marge % |
|--------|------------------|----------------|-------|------------|-----------|---------|---------|
| Client A | 100h | 120h | -20h | 15 000€ | 12 000€ | 3 000€ | 20% |

**Formules** :
- Coût réel = Σ(heures consultant × coût horaire)
- Marge € = CA facturé - Coût réel
- Marge % = Marge € / CA facturé

---

## 4. Exigences Non Fonctionnelles

### 4.1 Performance
- **Temps de réponse** : <2s pour affichage page standard
- **Recherche** : <1s pour recherche client/projet
- **Export Excel** : <10s pour rapport 1000 lignes
- **Concurrence** : 25 utilisateurs simultanés sans dégradation

### 4.2 Sécurité
- **Authentification** : Login/password Odoo + 2FA (optionnel)
- **Droits d'accès** :
  - Consultant : voir ses projets, saisir temps
  - Chef de projet : voir ses projets, valider temps, créer jalons
  - Commercial : CRM, devis, lecture projets
  - Comptable : facturation, finance
  - Direction : accès total lecture
- **Audit** : Log des actions critiques (validation facture, modification budget)

### 4.3 Disponibilité
- **Uptime** : >99% (max 7h downtime/an)
- **Sauvegarde** : Quotidienne automatique (rétention 30 jours)
- **RTO** : <4h en cas de panne majeure
- **RPO** : <24h (perte données max)

### 4.4 Compatibilité
- **Navigateurs** : Chrome, Firefox, Edge (dernières versions)
- **Mobile** : Responsive design (tablette/smartphone)
- **Intégrations** : API REST pour futur (logiciel compta externe)

---

## 5. Règles de Gestion

### RG-001 : Calcul Taux Journalier Moyen (TJM)
- **Junior** : 400€/j
- **Confirmé** : 600€/j
- **Senior** : 800€/j

*Note : TJM paramétrable par consultant dans sa fiche*

### RG-002 : Budget heures jalon
**Si forfait** : Budget heures = Montant jalon / TJM moyen équipe

**Exemple** :
- Jalon 10 000€
- Équipe : 1 senior (800€) + 1 confirmé (600€)
- TJM moyen = 700€
- Budget = 10 000 / 700 = **14.3 jours** (~100h)

### RG-003 : Statuts jalons
- **À planifier** : Jalon créé, pas encore assigné
- **En cours** : Au moins 1h saisie
- **Terminé** : Chef projet valide livrable
- **Validé** : Client accepte (optionnel)
- **À facturer** : Prêt pour génération facture
- **Facturé** : Facture envoyée, jalon verrouillé

### RG-004 : Périodes de saisie temps
- Saisie possible J-7 à J+2 (pour corrections)
- Validation hebdomadaire chaque lundi 12h
- Après validation : modification nécessite déverrouillage manager

### RG-005 : Conditions de paiement
- **Standard** : 30 jours fin de mois
- **Grands comptes** : 45 jours fin de mois
- **PME** : 30 jours date facture

### RG-006 : Taux d'occupation cible
- **Consultant** : 70-85% (temps facturable)
- 15-30% restant : formation, commercial, interne

---

## 6. Interfaces et Maquettes

### 6.1 Écran principal - Dashboard Chef de Projet
```
┌─────────────────────────────────────────────────────────────┐
│  🏠 Accueil  │  📊 Mes Projets  │  ⏱️ Temps  │  ⚙️ Config  │
├─────────────────────────────────────────────────────────────┤
│  👋 Bonjour Jean Dupont (Chef de Projet)                    │
├─────────────────────────────────────────────────────────────┤
│  📈 Mes Indicateurs                                          │
│  ┌──────────────┬──────────────┬──────────────┬───────────┐ │
│  │ Projets actifs│ Budget total│ Conso moyenne│ En alerte│ │
│  │      8       │   150k€     │     68%      │     2    │ │
│  └──────────────┴──────────────┴──────────────┴───────────┘ │
│                                                               │
│  🚨 Projets nécessitant attention                            │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ 🔴 Client ABC - Migration CRM   │ 105% budget │ Voir   ││
│  │ 🟠 Client XYZ - Formation       │  92% budget │ Voir   ││
│  └─────────────────────────────────────────────────────────┘│
│                                                               │
│  📊 Mes Projets                                              │
│  ┌───┬──────────────┬──────────┬─────────┬─────────┬──────┐│
│  │ ✓ │ Projet      │ Client   │ Budget  │ Conso   │ %   ││
│  ├───┼──────────────┼──────────┼─────────┼─────────┼──────┤│
│  │ 🟢│ Refonte SI   │ Acme     │ 120h   │ 65h    │ 54% ││
│  │ 🟠│ Migration CRM│ TechCo   │ 80h    │ 74h    │ 92% ││
│  │ 🟢│ Audit sécu   │ FinanceX │ 40h    │ 12h    │ 30% ││
│  └───┴──────────────┴──────────┴─────────┴─────────┴──────┘│
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Formulaire Saisie Temps (consultant)
```
┌──────────────────────────────────────────────────┐
│  ⏱️ Saisie Temps - Semaine du 21/10/2025         │
├──────────────────────────────────────────────────┤
│  📅 Lun 21  Mar 22  Mer 23  Jeu 24  Ven 25      │
│  ┌──────────────────────────────────────────┐    │
│  │ Projet : [Client ABC - Migration ▼]     │    │
│  │ Jalon  : [Développement ▼]              │    │
│  │ Heures : [___] h   [⏱️ Timer: 2h34]    │    │
│  │ Description : ___________________________│    │
│  │ [➕ Ajouter ligne] [💾 Enregistrer]     │    │
│  └──────────────────────────────────────────┘    │
│                                                   │
│  📋 Temps saisi cette semaine                    │
│  ┌────┬──────────────┬──────┬─────┬───────┐    │
│  │Date│ Projet       │Jalon │Heures│Action │    │
│  ├────┼──────────────┼──────┼─────┼───────┤    │
│  │21/10│Client ABC   │Dev   │ 7.5h│ [✏️]  │    │
│  │22/10│Client ABC   │Dev   │ 6h  │ [✏️]  │    │
│  │22/10│Formation    │-     │ 2h  │ [✏️]  │    │
│  └────┴──────────────┴──────┴─────┴───────┘    │
│  Total semaine : 15.5h / 37.5h                  │
└──────────────────────────────────────────────────┘
```

---

## 7. Plan de Formation

### 7.1 Utilisateurs finaux (consultants)
**Durée** : 2h  
**Contenu** :
- Navigation interface Odoo
- Saisie feuille de temps
- Consultation planning personnel
- Accès documents projet

### 7.2 Chefs de projet
**Durée** : 4h  
**Contenu** :
- Création/gestion projets et jalons
- Affectation consultants
- Validation temps
- Suivi budgétaire et alertes
- Reporting

### 7.3 Service commercial
**Durée** : 3h  
**Contenu** :
- Gestion pipeline CRM
- Création devis (templates)
- Workflow approbation
- Conversion devis en projet

### 7.4 Service comptabilité
**Durée** : 3h  
**Contenu** :
- Validation factures
- Gestion paiements/relances
- Exports comptables
- Lettrage automatique

---

## 8. Critères d'Acceptation Globaux

### Phase Recette
✅ **Fonctionnel** : Toutes les US priorité 1 opérationnelles  
✅ **Performance** : Temps réponse <2s validé sur 25 utilisateurs  
✅ **Données** : Migration 100% clients + 50 projets historiques  
✅ **Formation** : 100% utilisateurs formés  
✅ **Documentation** : Guide utilisateur + guide admin livrés  

### Go/No-Go Production
- [ ] Validation recette par métiers (commercial, chef projet, compta)
- [ ] Tests charge OK
- [ ] Sauvegarde automatique configurée et testée
- [ ] Support niveau 1 formé (hotline interne)
- [ ] Plan de repli défini (retour ancien système si besoin)

---

## 9. Contraintes et Hypothèses

### Contraintes
- ⏰ **Délai** : Mise en production avant 31/12/2025
- 💰 **Budget** : Max 25k€ (licence + dev + formation)
- 👥 **Ressources** : 1 consultant fonctionnel + 1 dev Odoo
- 🖥️ **Infrastructure** : VPS existant (4GB RAM, Ubuntu)

### Hypothèses
- ✅ Consultants saisiront leur temps quotidiennement
- ✅ Chefs de projet valideront hebdomadairement
- ✅ Données historiques disponibles en CSV (export ancien système)
- ✅ Pas de changement majeur organisation pendant projet

---

## 10. Annexes

### A. Glossaire
- **TJM** : Taux Journalier Moyen (tarif consultant)
- **Jalon** : Phase facturable d'un projet
- **MVP** : Minimum Viable Product (version minimale fonctionnelle)
- **SLA** : Service Level Agreement (engagement qualité)

### B. Références
- [Documentation Odoo Community](https://www.odoo.com/documentation/17.0/)
- [Guide OCA (Odoo Community Association)](https://github.com/OCA)

---

**Document contractuel - Signature électronique**

| Rôle | Nom | Date | Signature |
|------|-----|------|-----------|
| Client - Direction | M. Martin | 20/10/2025 | ✅ Validé |
| Consultant Odoo | Elo | 23/10/2025 | ✅ Validé |
| Chef de Projet | Mme Dubois | 20/10/2025 | ✅ Validé |

---

*Version 1.0 - Document de référence pour développement*
