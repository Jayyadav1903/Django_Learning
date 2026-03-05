from django.contrib import admin
from.models import biryani_variety,review,store,Biryani_Certificate
# Register your models here.
class BiryaniReviewInline(admin.TabularInline):
    model=review
    extra=2

class BiryaniVarietyAdmin(admin.ModelAdmin):
    list_display=('name','types','date_added')
    inlines=[BiryaniReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('biryani',)     
    
class BiryaniCertificateAdmin(admin.ModelAdmin):
    list_display=('biryani','certificate_number','date_issued','valid_until')    

admin.site.register(biryani_variety,BiryaniVarietyAdmin)
admin.site.register(review)
admin.site.register(store,StoreAdmin)
admin.site.register(Biryani_Certificate,BiryaniCertificateAdmin)
