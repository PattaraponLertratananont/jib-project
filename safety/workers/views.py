from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from .models import Worker

# class-base view
class WorkerListView(View):
    def get(self, req):
        workers = Worker.objects.all()
        # html=''
        # for worker in workers:
        #     html += f'<li>{worker.first_name}</li>'
        # return HttpResponse(html)
        worker_list = []
        for worker in workers:
            worker_list.append(worker.first_name)
        return render(req, 'worker_list.html',{'workers':worker_list})