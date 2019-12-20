from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact

class ContactList(ListView): 
    model = Contact
    fields = '__all__'

class ContactDetail(DetailView): 
    model = Contact
    fields = '__all__'

class ContactCreate(CreateView): 
    model = Contact
    fields = '__all__'

class ContactUpdate(UpdateView): 
    model = Contact
    fields = '__all__'

class ContactDelete(DeleteView): 
    model = Contact
    fields = '__all__'