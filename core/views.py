from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1>'.format(nome, idade))

def operacao(request, op, valor1, valor2):
    if op == 'soma':
        total = valor1 + valor2
    elif op == 'subtracao':
        total = valor1 - valor2
    elif op == 'multiplicacao':
        total = valor1 * valor2
    elif op == 'divisao':
        total = valor1 / valor2

    return HttpResponse('<h1>A {} de {} e {} é igual a: {}.</h1>'.format(op, valor1, valor2, total))
