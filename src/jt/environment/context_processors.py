from django.conf import settings

from .client import ClientConfig


def client_config(request):
    """
    Provides client-side configuration to templates.
    
    Creates a structured configuration object that gets injected into
    JavaScript as JtClientConfig, providing a single source of truth for
    all client configuration needs.
    
    Fails fast on missing required data - no masking of interface problems.
    
    Returns:
        dict: Context variables for templates
    """
    config = ClientConfig(
        DEBUG = settings.DEBUG,
        ENVIRONMENT = settings.ENV.environment_name,
        VERSION = settings.ENV.VERSION,
        JOURNAL_ID = request.view_parameters.journal_id,
    )
    
    return {
        'jt_client_config': config
    }
