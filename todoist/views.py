from django.shortcuts import render
from django.views.generic import TemplateView


class StartPageView(TemplateView):
    template_name = 'todoist/start_page/start_page.html'

class TodoistView(TemplateView):
    template_name = 'todoist/todoist.html'

