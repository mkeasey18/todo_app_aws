from django.shortcuts import render
from todo_app.models import ToDo
from django.shortcuts import redirect

# Create your views here.
def todo_list(request):
    if request.method == "POST":
        new_task = ToDo()
        new_task.task = request.POST["taskField"]
        new_task.due_date = request.POST["dueDateField"]
        new_task.save()

    all_todos = ToDo.objects.all()
    context = {'tasks': all_todos}
    return render(request, 'todo_app/todo_list.html', context)

def delete_task(request, id):
    task_to_delete = ToDo.objects.get(id=id)
    task_to_delete.delete()
    response = redirect('todo_list')
    return response
