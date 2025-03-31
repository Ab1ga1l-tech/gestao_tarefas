from django.contrib import admin
from django.urls import path
from .views import listar_tarefas, criar_tarefa, atualizar_tarefa, deletar_tarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', listar_tarefas, name='listar_tarefas'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
    path('atualizar/<int:tarefa_id>/', atualizar_tarefa, name='atualizar_tarefa'),
    path('deletar/<int:tarefa_id>/', deletar_tarefa, name='deletar_tarefa'),
]
