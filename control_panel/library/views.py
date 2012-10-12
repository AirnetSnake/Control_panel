# Create your views here.

from myapp.models import Person
 
def get_last_person_name(request):
    last_person = Person.objects.all()[-1]
    return last_person.name