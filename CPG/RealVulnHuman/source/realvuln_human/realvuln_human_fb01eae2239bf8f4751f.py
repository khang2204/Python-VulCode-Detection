'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# }}}

# Debug Toolbar {{{

def show_toolbar(request):
    if request.GET.get('debug') or \
            request.POST.get('debug') or \
            request.COOKIES.get('debug'):
        return True
    return False

DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': 'badguys.settings.show_toolbar'
}

# }}}

# vim: set foldmethod=marker:
