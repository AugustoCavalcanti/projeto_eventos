from django.db import models

class Evento(models.Model):
    sigla = models.CharField('Sigla', max_length=10)
    nome = models.CharField('Nome do evento', max_length=128)
    data_de_inicio = models.DateField('Data de início do evento', blank=True, null=True)
    data_de_termino = models.DateField('Data de término do evento', blank=True, null=True)
    prazo_para_submicao_de_artigos = models.DurationField('Prazo para submissão de artigos', blank=True, null=True)
    url_do_site_do_evento = models.URLField()