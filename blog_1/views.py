from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog_Table

# Create your views here.

def index(request):
    dict_table_value = Blog_Table.objects.all()
    dict_pass_value = {'dict_table_value':dict_table_value}
    return render(request, 'index.html', dict_pass_value)

def Entry_on_table(request):
    return render(request, 'Entry_on_table.html')

def save(request):
    Title_1 = request.POST.get('Title_tabel')
    description_1 = request.POST.get('discription_tabel')
    save_value_to_tabel=Blog_Table(Title = Title_1, description = description_1)
    save_value_to_tabel.save()
    return render(request, 'Entry_on_table.html')

def details_page(request, pk):
    get_details = Blog_Table.objects.get(id=pk)
    context12 = {'get_details':get_details}
    return render(request, 'details_page.html', context12)


def see_details_monna(request):

    get_id = request.POST.get('get_id')
    print(get_id)
    get_details = Blog_Table.objects.get(id=get_id)
    context12 = {'get_details': get_details}
    return render(request, 'details_page.html', context12)