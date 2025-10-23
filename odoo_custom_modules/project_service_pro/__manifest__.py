# -*- coding: utf-8 -*-
{
    'name': 'Project Service Pro',
    'version': '17.0.1.0.0',
    'category': 'Services/Project',
    'summary': 'Professional Services Management - Milestones, Budget Tracking & Invoicing',
    'description': """
Project Service Pro - Démonstration Consultant Fonctionnel Odoo
================================================================

Extension du module Project pour la gestion de services professionnels :

Fonctionnalités principales :
------------------------------
* **Jalons de projet** : Découpage projet en phases facturables
* **Suivi budgétaire** : Alertes dépassement budget en temps réel
* **Calcul rentabilité** : Analyse marge par projet et jalon
* **Facturation automatique** : Génération factures depuis jalons
* **Dashboard chef de projet** : Vue consolidée avancement projets
* **Planning consultants** : Visualisation charge de travail

Modules techniques :
--------------------
* project_milestone : Gestion jalons
* project_budget_alert : Alertes automatiques
* project_profitability : Calcul rentabilité
* project_dashboard : Tableaux de bord

Cas d'usage :
-------------
Entreprise de services IT avec consultants facturés en régie ou forfait,
nécessitant un suivi précis des heures et budgets par phase de projet.

Auteur : Elo - Consultant Fonctionnel Odoo
Date : Octobre 2025
""",
    'author': 'Elo - Consultant Fonctionnel Odoo',
    'website': 'https://github.com/votre-username/odoo-consultant-demo',
    'license': 'LGPL-3',
    
    # Dépendances
    'depends': [
        'base',
        'project',
        'hr_timesheet',
        'sale_management',
        'sale_timesheet',
        'account',
        'portal',
    ],
    
    # Fichiers chargés
    'data': [
        # Sécurité
        'security/project_service_security.xml',
        'security/ir.model.access.csv',
        
        # Données de base
        'data/project_milestone_type_data.xml',
        'data/mail_template_data.xml',
        'data/ir_cron_data.xml',
        
        # Vues
        'views/project_milestone_views.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/hr_timesheet_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        
        # Wizards
        'wizards/project_milestone_invoice_wizard_views.xml',
        'wizards/project_profitability_report_wizard_views.xml',
        
        # Rapports
        'reports/project_milestone_report_templates.xml',
        'reports/project_profitability_report_templates.xml',
        
        # Menu
        'views/project_service_menus.xml',
        
        # Dashboard
        'views/project_dashboard_views.xml',
    ],
    
    # Démo data (pour tests)
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/project_project_demo.xml',
        'demo/project_milestone_demo.xml',
    ],
    
    # Assets (CSS, JS)
    'assets': {
        'web.assets_backend': [
            'project_service_pro/static/src/css/project_dashboard.css',
            'project_service_pro/static/src/js/project_dashboard.js',
        ],
    },
    
    # Configuration
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # Images (pour app store Odoo)
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
}
