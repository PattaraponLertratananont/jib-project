from django.views import View
from django.http import HttpResponse
from .models import Worker
# class-base view
class WorkerListView(View):
    def get(self, req):
        workers = Worker.objects.all()
        html=''
        for worker in workers:
            html += f'<li>{worker.first_name}</li>'
        return HttpResponse(html)