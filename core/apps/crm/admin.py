from django.contrib import admin
from .models import Project, Task, Lead, Compte, Devise, Pays, DelaiDePaiement ,Invoice, Categorie # Register your models here
#
#
#.
admin.site.register(Project)
admin.site.register(Task)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'company')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

# Register the Lead model with the admin site using the LeadAdmin class
admin.site.register(Lead, LeadAdmin)

class CompteAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'type', 'devise', 'delai_de_paiement')
    list_filter = ('type', 'devise')
    search_fields = ('raison_sociale', 'responsable_email', 'adresse_facturation')
    # Customize other options as needed

# Register the Compte model with the admin site
admin.site.register(Compte, CompteAdmin)
admin.site.register(Devise)
admin.site.register(Pays)
admin.site.register(DelaiDePaiement)
admin.site.register(Categorie)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('project', 'invoice_number', 'invoice_date')

admin.site.register(Invoice, InvoiceAdmin)