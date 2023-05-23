from django.shortcuts import render
import requests
from django.shortcuts import render, redirect


def ticket_list(request):
    search_term = request.GET.get('search')
    response = requests.get('http://localhost:8000/api/tickets/', params={'search': search_term})
    tickets = response.json()
    return render(request, 'ticket_list.html', {'tickets': tickets})


def create_ticket(request):
    if request.method == 'POST':
        ticket_data = {
            'description': request.POST.get('description'),
            'resolution_end_date': request.POST.get('resolution_end_date')
        }
        response = requests.post('http://localhost:8000/api/ticket/create/', data=ticket_data)
        if response.status_code == 200:
            return redirect('ticket:list')

    return render(request, 'create_ticket.html')


def view_ticket(request, id):
    response = requests.get(f'http://localhost:8000/api/ticket/{id}/')
    if response.status_code == 200:
        ticket = response.json()
        return render(request, 'view_ticket.html', {'ticket': ticket})

    return redirect('ticket:list')


def edit_ticket(request, id):
    response = requests.get(f'http://localhost:8000/api/ticket/{id}/')
    if response.status_code == 200:
        ticket = response.json()
        if request.method == 'PUT':
            ticket_data = {
                'description': request.PUT.get('description'),
                'resolution_end_date': request.PUT.get('resolution_end_date'),
                'status': request.PUT.get('status'),
            }
            response = requests.put(f'http://localhost:8000/api/ticket/{id}/update/', data=ticket_data)
            if response.status_code == 200:
                return redirect('ticket:list')
        return render(request, 'edit_ticket.html', {'ticket': ticket})

    return redirect('ticket:list')


def delete_ticket(request, id):
    response = requests.get(f'http://localhost:8000/api/ticket/{id}/')
    if response.status_code == 200:
        ticket = response.json()
        if request.method == 'DELETE':            
            response = requests.delete(f'http://localhost:8000/api/ticket/{id}/delete/')
            if response.status_code == 200:
                return redirect('ticket:list')
        return render(request, 'delete_ticket.html', {'ticket': ticket})
    return redirect('ticket:list')