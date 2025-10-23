# 🎯 Matrice de Décision - Choix Modules et Architecture

## Contexte décisionnel

**Objectif** : Sélectionner les modules Odoo et l'architecture optimale pour répondre aux besoins de TechServices Pro.

**Contraintes** :
- Budget limité → Odoo Community prioritaire
- Déploiement rapide → Maximum modules standards
- Évolutivité → Architecture modulaire
- Maintenance → Minimiser les customisations lourdes

---

## 📊 Matrice 1 : Odoo Community vs Enterprise

| Critère | Poids | Community | Enterprise | Choix retenu |
|---------|-------|-----------|------------|--------------|
| **Coût** | 30% | ⭐⭐⭐⭐⭐ (0€) | ⭐⭐ (€€€) | ✅ Community |
| **Fonctionnalités projet** | 25% | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Community suffisant |
| **Planning ressources** | 20% | ⭐⭐ (custom) | ⭐⭐⭐⭐⭐ | ⚠️ Limité Community |
| **Support officiel** | 15% | ⭐⭐ | ⭐⭐⭐⭐⭐ | Community acceptable |
| **Dashboard avancé** | 10% | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Community OK |

**Score pondéré** :
- 🏆 **Community** : 3.9/5 (78%)
- Enterprise : 4.2/5 (84%)

**Décision** : ✅ **Odoo Community** pour MVP Phase 1
- Migration vers Enterprise possible ultérieurement si besoin Planning avancé
- Économie ~15k€/an pour 25 utilisateurs

---

## 📦 Matrice 2 : Sélection Modules Standards

| Besoin fonctionnel | Module Odoo | Édition | Couverture | Customisation | Décision |
|-------------------|-------------|---------|------------|---------------|----------|
| CRM opportunités | `crm` | Community | 95% | ❌ Aucune | ✅ Installer |
| Devis & commandes | `sale` | Community | 90% | ⚠️ Templates | ✅ Installer |
| Gestion projets | `project` | Community | 85% | ⚠️ Jalons custom | ✅ Installer |
| Feuilles de temps | `hr_timesheet` | Community | 95% | ❌ Aucune | ✅ Installer |
| Facturation temps | `sale_timesheet` | Community | 80% | ⚠️ Règles calcul | ✅ Installer |
| Comptabilité | `account` | Community | 90% | ⚠️ Workflow appro | ✅ Installer |
| Planning ressources | `project_forecast` | ⛔ Enterprise | 0% | 🔴 Module custom | ⏸️ Phase 2 |
| Portail client | `portal` | Community | 95% | ❌ Aucune | ✅ Installer |
| Reporting BI | `spreadsheet` | ⛔ Enterprise | 0% | 🔴 Dashboards custom | ⚠️ Alternative |

**Légende** :
- ✅ Module utilisé tel quel ou légère config
- ⚠️ Customisation légère nécessaire (champs, vues)
- 🔴 Développement custom significatif
- ⏸️ Reporté à Phase 2

---

## 🔧 Matrice 3 : Niveau de Customisation

| Fonctionnalité | Standard Odoo | Config Odoo Studio | Développement Python | Choix technique |
|----------------|---------------|-------------------|---------------------|-----------------|
| **Workflow approbation devis** | ❌ | ⚠️ Possible | ✅ Recommandé | 🐍 Module custom |
| **Alertes dépassement budget** | ❌ | ⚠️ Limité | ✅ Flexible | 🐍 Actions serveur + custom |
| **Dashboard direction** | ⚠️ Basique | ✅ Suffisant | ⚠️ Si complexe | 🎨 Studio + QWeb |
| **Calcul rentabilité projet** | ❌ | ❌ | ✅ Nécessaire | 🐍 Champs calculés custom |
| **Templates devis** | ✅ | ✅ | ❌ | ⚙️ Configuration standard |
| **Règles facturation** | ⚠️ | ⚠️ | ✅ Règles métier | 🐍 Module custom |
| **Planning consultants** | ❌ | ❌ | ✅ Vue custom | 🐍 Module custom complet |
| **Export Excel** | ✅ | ✅ | ⚠️ Si format spécifique | ⚙️ Standard Odoo |

**Légende** :
- ⚙️ Configuration standard (paramétrage Odoo)
- 🎨 Odoo Studio (Enterprise) ou configuration avancée
- 🐍 Développement Python (module custom)

**Estimation effort** :
- Configuration standard : 2-5 jours
- Odoo Studio : 5-10 jours (si disponible)
- Développement custom : 15-25 jours

---

## 🏗️ Matrice 4 : Architecture Technique

### Option A : Déploiement Cloud (Odoo.sh / SaaS)
| Critère | Score | Commentaire |
|---------|-------|-------------|
| Coût initial | ⭐⭐⭐ | Abonnement mensuel |
| Maintenance | ⭐⭐⭐⭐⭐ | Gérée par Odoo |
| Personnalisation | ⭐⭐⭐ | Limitée selon offre |
| Performance | ⭐⭐⭐⭐ | Bonne |
| Données | ⭐⭐⭐ | Hors site |
| **Total** | **18/25** | |

### Option B : Serveur dédié (VPS)
| Critère | Score | Commentaire |
|---------|-------|-------------|
| Coût initial | ⭐⭐⭐⭐ | VPS ~30€/mois |
| Maintenance | ⭐⭐ | À gérer (sauvegardes, MAJ) |
| Personnalisation | ⭐⭐⭐⭐⭐ | Totale |
| Performance | ⭐⭐⭐⭐ | Configurable |
| Données | ⭐⭐⭐⭐⭐ | Contrôle total |
| **Total** | **20/25** | |

### Option C : Docker local (développement) + Cloud (production)
| Critère | Score | Commentaire |
|---------|-------|-------------|
| Coût initial | ⭐⭐⭐⭐⭐ | Docker gratuit + VPS |
| Maintenance | ⭐⭐⭐ | Gestion VPS prod |
| Personnalisation | ⭐⭐⭐⭐⭐ | Totale (environnements isolés) |
| Performance | ⭐⭐⭐⭐ | Excellente en dev |
| Données | ⭐⭐⭐⭐ | Flexibilité |
| **Total** | **21/25** | |

**Décision** : ✅ **Option C - Docker + VPS**
- 🐳 Docker pour développement et démo
- ☁️ VPS pour production (ex: OVH, DigitalOcean)
- 🔄 CI/CD possible avec Git

---

## 🚀 Matrice 5 : Priorisation Développements Custom

| Module / Feature | Valeur métier | Complexité | Dépendances | Priorité | Sprint |
|-----------------|---------------|------------|-------------|----------|--------|
| **Workflow approbation devis** | 🔥🔥🔥 Haute | ⚙️⚙️ Moyenne | sale | 🔴 P1 | Sprint 1 |
| **Alertes budget jalons** | 🔥🔥🔥 Haute | ⚙️ Faible | project | 🔴 P1 | Sprint 1 |
| **Calcul rentabilité projet** | 🔥🔥 Moyenne | ⚙️⚙️⚙️ Élevée | project, hr_timesheet | 🟡 P2 | Sprint 2 |
| **Dashboard direction** | 🔥🔥 Moyenne | ⚙️⚙️ Moyenne | account, project | 🟡 P2 | Sprint 2 |
| **Planning consultants** | 🔥🔥🔥 Haute | ⚙️⚙️⚙️⚙️ Très élevée | hr, project | 🟠 P3 | Sprint 3+ |
| **Portail client avancé** | 🔥 Faible | ⚙️⚙️ Moyenne | portal | 🟢 P4 | Phase 2 |
| **Facturation automatique** | 🔥🔥🔥 Haute | ⚙️⚙️ Moyenne | account, project | 🔴 P1 | Sprint 1-2 |
| **Templates email** | 🔥 Faible | ⚙️ Faible | mail | 🟢 P4 | Configuration |

**Légende complexité** :
- ⚙️ Faible : 1-3 jours
- ⚙️⚙️ Moyenne : 3-7 jours
- ⚙️⚙️⚙️ Élevée : 7-15 jours
- ⚙️⚙️⚙️⚙️ Très élevée : 15-30 jours

**Plan de release** :
- 🔴 **Phase 1 (MVP)** : P1 → 15-20 jours dev
- 🟡 **Phase 2** : P2 → 10-15 jours dev
- 🟠 **Phase 3** : P3 → 15-20 jours dev
- 🟢 **Phase 4** : P4 → Améliorations continues

---

## 📋 Matrice 6 : Gestion des Risques

| Risque | Probabilité | Impact | Mitigation | Responsable |
|--------|-------------|--------|------------|-------------|
| **Modules Community insuffisants** | 🟡 Moyenne | 🔥🔥 Moyen | POC validant besoins critiques avant | Consultant |
| **Customisations trop lourdes** | 🟡 Moyenne | 🔥🔥🔥 Élevé | Prioriser configuration vs code | Développeur |
| **Résistance au changement utilisateurs** | 🔴 Élevée | 🔥🔥🔥 Élevé | Formation, accompagnement, pilotes | Chef projet |
| **Performances insuffisantes** | 🟢 Faible | 🔥🔥 Moyen | Tests charge, indexation BDD | Tech lead |
| **Migration données existantes** | 🟡 Moyenne | 🔥🔥🔥 Élevé | Mapping détaillé, scripts validation | Consultant + Dev |
| **Bugs modules custom** | 🔴 Élevée | 🔥🔥 Moyen | Tests unitaires, code review, recette | Développeur |
| **Dépassement budget/délai** | 🟡 Moyenne | 🔥🔥🔥 Élevé | Sprints courts, revues régulières | Chef projet |

**Plan de contingence** :
1. ⚠️ Si Community trop limité → Budget Enterprise phase 2
2. ⚠️ Si custom trop lourd → Réduire périmètre fonctionnel
3. ⚠️ Si résistance forte → Déploiement progressif par service

---

## 🎯 Synthèse des Décisions

### Architecture retenue
```
┌─────────────────────────────────────────┐
│  Frontend : Odoo Web (Community 17.0)   │
├─────────────────────────────────────────┤
│  Modules Standards :                     │
│  • CRM, Sales, Project, Timesheet       │
│  • Account, Portal                       │
├─────────────────────────────────────────┤
│  Modules Custom :                        │
│  • project_service_pro (workflow, KPI)  │
│  • approval_workflow (devis)            │
├─────────────────────────────────────────┤
│  Base de données : PostgreSQL 15         │
├─────────────────────────────────────────┤
│  Infrastructure :                        │
│  • Dev : Docker Compose (local)         │
│  • Prod : VPS Ubuntu 22.04 (4GB RAM)    │
└─────────────────────────────────────────┘
```

### Budget estimé
| Poste | Montant |
|-------|---------|
| Licence Odoo Community | 0 € |
| VPS Production (1 an) | 360 € |
| Développement custom (40j) | 16 000 € |
| Formation utilisateurs (3j) | 2 400 € |
| Reprise données | 2 000 € |
| **TOTAL** | **20 760 €** |

### Planning prévisionnel
| Phase | Durée | Livrables |
|-------|-------|-----------|
| Analyse & POC | 2 semaines | Specs validées, POC docker |
| Sprint 1 (MVP) | 2 semaines | Modules P1 fonctionnels |
| Sprint 2 | 2 semaines | Modules P2 + reporting |
| Recette & formation | 1 semaine | Tests validation, formation |
| Déploiement prod | 1 semaine | Mise en production |
| **TOTAL** | **8 semaines** | Odoo opérationnel |

---

## ✅ Validation et Approbation

| Décision | Validé par | Date | Statut |
|----------|-----------|------|--------|
| Choix Community vs Enterprise | Direction | 15/10/2025 | ✅ |
| Architecture Docker + VPS | DSI | 17/10/2025 | ✅ |
| Budget 20k€ | DAF | 18/10/2025 | ✅ |
| Planning 8 semaines | Chef projet | 20/10/2025 | ✅ |

---

**Ce document constitue la base contractuelle pour le lancement du projet.**

*Rédigé par : Consultant Fonctionnel Odoo*  
*Dernière mise à jour : 23 octobre 2025*
