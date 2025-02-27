from django.shortcuts import render
from website import models
from django.shortcuts import redirect,get_object_or_404
from django.http import JsonResponse
from .models import Task
# Create your views here.

def home(req):
	data=models.Task.objects.all()
	obj={"produts":data}
	return render(req,"home.html", obj)

def Form(req):
	return render(req,"Form.html")

def save_form(req):
	data = models.Task(
		name=req.POST['name'],
		created_date=req.POST['created_date'],
		status=True if req.POST['status'] == "Active" else False ,
		expiry_date=req.POST['expiry_date'],
		priority=req.POST['priority']
	)
	data.save()
	return redirect("/home")


from django.http import JsonResponse
from .models import Task  

def list_task(req):
    query = list(Task.objects.all().values())  
    return JsonResponse(query, safe=False)  

def task_deleted(req):
    order_id = req.GET.get('id')
    task = get_object_or_404(models.Task, id=order_id)  
    task.delete()  
    return redirect("/home") 
