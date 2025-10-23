# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta


class ProjectMilestone(models.Model):
    """
    Modèle représentant un jalon (milestone) dans un projet.
    Un jalon est une phase facturable avec budget heures et montant défini.
    """
    _name = 'project.milestone'
    _description = 'Project Milestone'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, date_start, name'
    
    # === CHAMPS DE BASE ===
    name = fields.Char(
        string='Nom du jalon',
        required=True,
        tracking=True,
        help="Ex: Phase 1 - Analyse fonctionnelle"
    )
    
    sequence = fields.Integer(
        string='Séquence',
        default=10,
        help="Ordre d'affichage des jalons"
    )
    
    description = fields.Html(
        string='Description',
        help="Description détaillée du jalon et livrables attendus"
    )
    
    # === RELATIONS ===
    project_id = fields.Many2one(
        'project.project',
        string='Projet',
        required=True,
        ondelete='cascade',
        tracking=True,
        index=True
    )
    
    partner_id = fields.Many2one(
        'res.partner',
        string='Client',
        related='project_id.partner_id',
        store=True,
        readonly=True
    )
    
    company_id = fields.Many2one(
        'res.company',
        string='Société',
        related='project_id.company_id',
        store=True,
        readonly=True
    )
    
    sale_line_id = fields.Many2one(
        'sale.order.line',
        string='Ligne de commande',
        help="Ligne de commande origine (si créé depuis devis)",
        tracking=True
    )
    
    sale_order_id = fields.Many2one(
        'sale.order',
        string='Commande',
        related='sale_line_id.order_id',
        store=True,
        readonly=True
    )
    
    # === DATES ===
    date_start = fields.Date(
        string='Date début',
        tracking=True,
        default=fields.Date.context_today
    )
    
    date_end = fields.Date(
        string='Date fin',
        tracking=True
    )
    
    date_deadline = fields.Date(
        string='Deadline',
        help="Date limite de livraison (alerte si dépassée)"
    )
    
    # === BUDGET ET FACTURATION ===
    currency_id = fields.Many2one(
        'res.currency',
        string='Devise',
        related='project_id.currency_id',
        store=True,
        readonly=True
    )
    
    amount = fields.Monetary(
        string='Montant facturable',
        currency_field='currency_id',
        tracking=True,
        help="Montant à facturer pour ce jalon (forfait ou estimé)"
    )
    
    budget_hours = fields.Float(
        string='Budget heures',
        tracking=True,
        help="Nombre d'heures budgétées pour ce jalon"
    )
    
    pricing_type = fields.Selection(
        [
            ('fixed', 'Forfait'),
            ('timesheet', 'Régie (heures réelles)')
        ],
        string='Type de tarification',
        default='fixed',
        required=True,
        tracking=True
    )
    
    # === HEURES CONSOMMÉES (CALCULÉES) ===
    hours_consumed = fields.Float(
        string='Heures consommées',
        compute='_compute_hours_consumed',
        store=True,
        help="Total des heures saisies sur ce jalon"
    )
    
    hours_remaining = fields.Float(
        string='Heures restantes',
        compute='_compute_hours_remaining',
        store=True
    )
    
    progress = fields.Float(
        string='Progression (%)',
        compute='_compute_progress',
        store=True,
        group_operator='avg'
    )
    
    # === AFFECTATION ===
    user_ids = fields.Many2many(
        'res.users',
        'project_milestone_user_rel',
        'milestone_id',
        'user_id',
        string='Consultants assignés',
        tracking=True
    )
    
    user_id = fields.Many2one(
        'res.users',
        string='Responsable',
        tracking=True,
        default=lambda self: self.env.user
    )
    
    # === TÂCHES ET TEMPS ===
    task_ids = fields.One2many(
        'project.task',
        'milestone_id',
        string='Tâches'
    )
    
    task_count = fields.Integer(
        string='Nombre de tâches',
        compute='_compute_task_count'
    )
    
    timesheet_ids = fields.One2many(
        'account.analytic.line',
        'milestone_id',
        string='Feuilles de temps'
    )
    
    timesheet_count = fields.Integer(
        string='Nombre de timesheets',
        compute='_compute_timesheet_count'
    )
    
    # === FACTURATION ===
    invoice_id = fields.Many2one(
        'account.move',
        string='Facture',
        readonly=True,
        copy=False,
        help="Facture générée pour ce jalon"
    )
    
    invoice_status = fields.Selection(
        [
            ('no', 'Rien à facturer'),
            ('to_invoice', 'À facturer'),
            ('invoiced', 'Facturé')
        ],
        string='Statut facturation',
        compute='_compute_invoice_status',
        store=True,
        tracking=True
    )
    
    # === STATUT ===
    state = fields.Selection(
        [
            ('draft', 'Brouillon'),
            ('planned', 'Planifié'),
            ('in_progress', 'En cours'),
            ('done', 'Terminé'),
            ('validated', 'Validé client'),
            ('invoiced', 'Facturé'),
            ('cancel', 'Annulé')
        ],
        string='Statut',
        default='draft',
        required=True,
        tracking=True,
        group_expand='_expand_states'
    )
    
    # === ALERTES ===
    alert_budget = fields.Boolean(
        string='Alerte budget',
        compute='_compute_alert_budget',
        store=True,
        help="True si dépassement budget >90%"
    )
    
    alert_deadline = fields.Boolean(
        string='Alerte deadline',
        compute='_compute_alert_deadline',
        store=True,
        help="True si deadline dépassée"
    )
    
    # === CALCULS ===
    @api.depends('timesheet_ids.unit_amount')
    def _compute_hours_consumed(self):
        """Calcul des heures totales saisies sur le jalon"""
        for milestone in self:
            milestone.hours_consumed = sum(milestone.timesheet_ids.mapped('unit_amount'))
    
    @api.depends('hours_consumed', 'budget_hours')
    def _compute_hours_remaining(self):
        """Calcul des heures restantes"""
        for milestone in self:
            milestone.hours_remaining = milestone.budget_hours - milestone.hours_consumed
    
    @api.depends('hours_consumed', 'budget_hours')
    def _compute_progress(self):
        """Calcul du pourcentage d'avancement basé sur les heures"""
        for milestone in self:
            if milestone.budget_hours > 0:
                milestone.progress = (milestone.hours_consumed / milestone.budget_hours) * 100
            else:
                milestone.progress = 0.0
    
    @api.depends('hours_consumed', 'budget_hours')
    def _compute_alert_budget(self):
        """Alerte si dépassement budget >90%"""
        for milestone in self:
            if milestone.budget_hours > 0:
                milestone.alert_budget = (milestone.hours_consumed / milestone.budget_hours) >= 0.90
            else:
                milestone.alert_budget = False
    
    @api.depends('date_deadline', 'state')
    def _compute_alert_deadline(self):
        """Alerte si deadline dépassée et jalon non terminé"""
        today = fields.Date.today()
        for milestone in self:
            milestone.alert_deadline = (
                milestone.date_deadline 
                and milestone.date_deadline < today 
                and milestone.state not in ['done', 'validated', 'invoiced', 'cancel']
            )
    
    @api.depends('task_ids')
    def _compute_task_count(self):
        """Compte le nombre de tâches"""
        for milestone in self:
            milestone.task_count = len(milestone.task_ids)
    
    @api.depends('timesheet_ids')
    def _compute_timesheet_count(self):
        """Compte le nombre de timesheets"""
        for milestone in self:
            milestone.timesheet_count = len(milestone.timesheet_ids)
    
    @api.depends('state', 'invoice_id')
    def _compute_invoice_status(self):
        """Calcul du statut de facturation"""
        for milestone in self:
            if milestone.state == 'invoiced' or milestone.invoice_id:
                milestone.invoice_status = 'invoiced'
            elif milestone.state in ['done', 'validated']:
                milestone.invoice_status = 'to_invoice'
            else:
                milestone.invoice_status = 'no'
    
    # === CONTRAINTES ===
    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        """Validation : date fin après date début"""
        for milestone in self:
            if milestone.date_start and milestone.date_end:
                if milestone.date_end < milestone.date_start:
                    raise ValidationError(_("La date de fin doit être postérieure à la date de début."))
    
    @api.constrains('budget_hours')
    def _check_budget_hours(self):
        """Validation : budget heures positif"""
        for milestone in self:
            if milestone.budget_hours < 0:
                raise ValidationError(_("Le budget heures doit être positif."))
    
    # === ACTIONS ===
    def action_start(self):
        """Démarrer le jalon"""
        self.ensure_one()
        self.write({'state': 'in_progress', 'date_start': fields.Date.today()})
        self.message_post(body=_("Jalon démarré"))
    
    def action_complete(self):
        """Marquer comme terminé"""
        self.ensure_one()
        if self.hours_consumed == 0:
            raise UserError(_("Impossible de terminer un jalon sans heures saisies."))
        self.write({'state': 'done'})
        self.message_post(body=_("Jalon terminé - Prêt pour validation"))
        
        # Notification au responsable projet
        self.project_id.message_post(
            body=_("Le jalon '%s' a été marqué comme terminé.") % self.name,
            subtype_xmlid='mail.mt_note'
        )
    
    def action_validate(self):
        """Validation client"""
        self.ensure_one()
        self.write({'state': 'validated'})
        self.message_post(body=_("Jalon validé par le client - Prêt pour facturation"))
    
    def action_create_invoice(self):
        """Générer une facture pour ce jalon"""
        self.ensure_one()
        
        if self.state not in ['done', 'validated']:
            raise UserError(_("Le jalon doit être terminé ou validé pour être facturé."))
        
        if self.invoice_id:
            raise UserError(_("Une facture existe déjà pour ce jalon."))
        
        # Calcul du montant à facturer
        if self.pricing_type == 'timesheet':
            # Régie : heures × TJM moyen
            amount_to_invoice = self._compute_amount_from_timesheet()
        else:
            # Forfait : montant fixe
            amount_to_invoice = self.amount
        
        # Création de la facture
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [(0, 0, {
                'name': f"{self.project_id.name} - {self.name}",
                'quantity': self.hours_consumed if self.pricing_type == 'timesheet' else 1,
                'price_unit': amount_to_invoice / self.hours_consumed if self.pricing_type == 'timesheet' and self.hours_consumed else amount_to_invoice,
                'product_id': self.env.ref('product.product_product_1').id,  # Service générique
            })]
        })
        
        self.write({
            'state': 'invoiced',
            'invoice_id': invoice.id
        })
        
        self.message_post(body=_("Facture %s créée") % invoice.name)
        
        return {
            'type': 'ir.actions.act_window',
            'name': _('Facture'),
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'target': 'current',
        }
    
    def _compute_amount_from_timesheet(self):
        """Calcul montant depuis timesheet (régie)"""
        self.ensure_one()
        # Simplification : utilise le montant configuré / heures * heures réelles
        if self.budget_hours > 0:
            rate = self.amount / self.budget_hours
            return self.hours_consumed * rate
        return self.amount
    
    # === VUES ===
    def action_view_tasks(self):
        """Ouvrir les tâches du jalon"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Tâches du jalon'),
            'res_model': 'project.task',
            'domain': [('milestone_id', '=', self.id)],
            'view_mode': 'tree,form',
            'context': {'default_milestone_id': self.id, 'default_project_id': self.project_id.id}
        }
    
    def action_view_timesheets(self):
        """Ouvrir les timesheets du jalon"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Temps saisi'),
            'res_model': 'account.analytic.line',
            'domain': [('milestone_id', '=', self.id)],
            'view_mode': 'tree,form',
            'context': {'default_milestone_id': self.id, 'default_project_id': self.project_id.id}
        }
    
    # === KANBAN GROUP EXPAND ===
    @api.model
    def _expand_states(self, states, domain, order):
        """Afficher tous les états dans la vue kanban"""
        return [key for key, _ in self._fields['state'].selection]
