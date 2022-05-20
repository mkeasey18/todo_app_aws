from django.forms import NullBooleanField
from django.test import TestCase
import pytest
from models import ToDo
# Create your tests here.

def test_todo_task(db, ToDo):
    new_todo = ToDo(
        task = 'test task'
    )
    new_todo.save()
    assert ToDo.objects.get(task='test task') != None
