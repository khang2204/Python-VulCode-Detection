@receiver(signal, **decorator_kwargs)...
if settings.SUSPEND_SIGNALS:
return
return func(sender, **kwargs)
