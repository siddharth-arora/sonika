from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
# import ListView 
from django.views.generic import ListView
# import model
from app1.models import school
# import DetailView
from django.views.generic import DetailView
# import CreateView
from django.views.generic.edit import CreateView
# import DeleteView
from django.views.generic.edit import DeleteView
# import reverse_lazy
from django.urls import reverse_lazy
# import UpdateView
from django.views.generic.edit import UpdateView

# Create your views here.
# function based view
#def index(request):
    # return render(request,'app1/first.html')

# class based view - method 1
# class index(View):
#     def get(self, request):
#         return HttpResponse("Class based view works")

# class based view - method 2
class index(TemplateView):
    template_name = 'app1/first.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_name'] = 'Jaiveer Vardhan'
        context['publisher'] = 'Tata McGraw Hill'
        return context

# class based view - ListView
class SchoolListView(ListView):
    # associate this view with the model
    # model = ModelClassName
    model = school
    # set the name of the list that we would be using in html
    # note: this list will hold all the data from the model
    # context_object_name = 'list_name'
    context_object_name = 'allschools'
    # give the template name in the template_name built in data member
    # template_name = 'app_name/HTML_file_name.html'
    template_name = 'app1/school_list.html'

# class based view - DetailView
class SchoolDetailView(DetailView):
    # associate this view with the model
    # model = ModelClassName
    model = school
    # set the name of the list that we would be using in html
    # note: this list will hold all the data from the model
    # context_object_name = 'list_name'
    context_object_name = 'school_detail'
    # give the template name in the template_name built in data member
    # template_name = 'app_name/HTML_file_name.html'
    template_name = 'app1/school_detail.html'

# class based view - CreateView
class SchoolCreateView(CreateView):
    # choose the fields to be present in the form
    # fields = ('field1','field2','field3')
    fields = ('name','principal','location')
    # associate this view with the model
    # model = ModelClassName
    model = school
    # give the template name in the template_name built in data member
    # template_name = 'app_name/HTML_file_name.html'
    template_name = 'app1/create_school.html'

# class based view - DeleteView
class SchoolDeleteView(DeleteView):
    # associate this view with the model
    # model = ModelClassName
    model = school
    # set the success_url
    # set the page where the control will go once the 
    # deletion is successful
    # success_url = reverse_lazy('name_of_the_target_url')
    success_url = reverse_lazy('list')

# function based view - school_updation_success
def school_updation_success(request):
    return render(request,'app1/school_updation_success.html')

# class based view - UpdateView
class SchoolUpdateView(UpdateView):
    # choose the fields to be present in the updation form
    # fields = ('field1','field2','field3')
    fields = ('name','principal','location')
    # associate this view with the model
    # model = ModelClassName
    model = school
    # set the success_url
    # set the page where the control will go once the 
    # updation is successful
    # success_url = reverse_lazy('name_of_the_target_url')
    success_url = reverse_lazy('school_updation_success')