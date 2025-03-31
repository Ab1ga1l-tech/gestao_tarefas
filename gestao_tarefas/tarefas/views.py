from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Tarefa

@csrf_exempt
@login_required
def listar_tarefas(request):
    if request.method == "GET":
        tarefas = Tarefa.objects.filter(usuario=request.user).values()
        return JsonResponse(list(tarefas), safe=False)

@csrf_exempt
@login_required
def criar_tarefa(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nova_tarefa = Tarefa.objects.create(
            usuario=request.user,
            titulo=data.get("titulo"),
            descricao=data.get("descricao", ""),
            prioridade=data.get("prioridade", "M"),
            data_vencimento=data.get("data_vencimento", None)
        )
        return JsonResponse({"id": nova_tarefa.id, "mensagem": "Tarefa criada com sucesso!"}, status=201)

    # Resposta para requisições GET ou métodos não permitidos
    return JsonResponse({"erro": "Método não permitido. Use POST."}, status=405)


@csrf_exempt
@login_required
def atualizar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    if request.method == "PUT":
        data = json.loads(request.body)
        tarefa.titulo = data.get("titulo", tarefa.titulo)
        tarefa.descricao = data.get("descricao", tarefa.descricao)
        tarefa.concluida = data.get("concluida", tarefa.concluida)
        tarefa.prioridade = data.get("prioridade", tarefa.prioridade)
        tarefa.data_vencimento = data.get("data_vencimento", tarefa.data_vencimento)
        tarefa.save()
        return JsonResponse({"mensagem": "Tarefa atualizada com sucesso!"})

@csrf_exempt
@login_required
def deletar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    if request.method == "DELETE":
        tarefa.delete()
        return JsonResponse({"mensagem": "Tarefa deletada com sucesso!"})

