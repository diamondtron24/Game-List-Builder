from django.contrib import admin
from .models import BaseShip
from .models import Squadron
from .models import Upgrade
from .models import Objective
from .models import Ship
from .models import SavedList
from .models import UpgradeImage

# Register your models here.
admin.site.register(BaseShip)
admin.site.register(Squadron)
admin.site.register(Upgrade)
admin.site.register(Objective)
admin.site.register(Ship)
admin.site.register(SavedList)
admin.site.register(UpgradeImage)