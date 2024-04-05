from django.shortcuts import render
from django.views import View
from django.utils.translation import ngettext, gettext as _
from django.utils import timezone
import random
from django.conf import settings


class HomeView(View):
    def get(self, request):
        lan = settings.LANGUAGES
        template = 'app/home.html'
        number = random.randint(1, 2)
        message = ngettext(
            "There is %(count)s apple.",  # Singular form
            "There are %(count)s apples.",  # Plural form
            number
        ) % {'count': number}

        context = {
            'greeting': _("Welcome to our Localization Project!"),
            'View_Pluralization_Message': message,
            'template_pluralization_message': number,
            'current_date': timezone.now()
        }
        return render(request, template, context)
