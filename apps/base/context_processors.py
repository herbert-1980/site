# from page import models
from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext, Template

# Imprime um texto qualquer 
def context_social(request):
    return {'social': 'Exibir este contexto em qualquer lugar!'}


# Imprime a hora com data completo
def context_horario(request):
    # Obtém a data e hora atual
    data_e_hora_atual = timezone.now()

    # Formata a data e hora em uma string legível
    horario_formatado = data_e_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

    # Retorna um dicionário com a data e hora formatadas
    return {'horario': f"Agora é exatamente: {horario_formatado}"}

# Imprime o Ip do usuario
"""
def ip_address_processor(request):
    return {'ip_address': request.META["REMOTE_ADDR"]}

def cliente_ip_view(request):
    template = Template("{{ title }}: {{ ip_address }}")
    context = RequestContext(
        request,
        {
            "title": "Your Ip Address",
        },
        [ip_address_processor]
    )
    
    return HttpResponse(template.render(context))"""