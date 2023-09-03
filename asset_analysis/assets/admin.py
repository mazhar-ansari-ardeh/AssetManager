from django.contrib import admin

from .models import Asset, Liability


class AssetAdmin(admin.ModelAdmin):
    def get_list_display(self, record):
        ld = ['id', 'title', 'owner', 'type']
        if record.user.is_superuser:
            ld += ['date']
        return ld

    def get_owner(rec):
        return rec.owner

    get_owner.short_description = 'Owner'


admin.site.register(Asset, AssetAdmin)
admin.site.register(Liability, AssetAdmin)

admin.site.site_header = 'ADMIN PANEL'
admin.site.site_title = 'SITE ADMIN'
admin.site.index_title = 'ADMINISTRATION'
