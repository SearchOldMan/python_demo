from django.contrib import admin

from logview.models import OperatingSystem,Service,HardwareComponent,Server,IPAddress

admin.site.register(OperatingSystem)
admin.site.register(Service)
admin.site.register(HardwareComponent)
admin.site.register(Server)
admin.site.register(IPAddress)

# Register your models here.
