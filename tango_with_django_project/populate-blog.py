import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
django.setup()
from blog.models import blogg

def populate():
    blog=[{"text":"Slicing. As explained in Limiting QuerySets, a QuerySet can be sliced, using Python’s array-slicing syntax",
            "author":"Adi","email":"wert@gfjdk.com","title":"hey"},{"text":"Slicing. As explained in Limiting QuerySets, a QuerySet can be sliced, using Python’s array-slicing syntax",
        "author":"Adi","email":"wert@gfjd.com","title":"hello"},{"text":"Slicing. As explained in Limiting QuerySets, a QuerySet can be sliced, using Python’s array-slicing syntax",
            "author":"Adi","email":"wert@gfjk.com","title":"how"}]
    for v in blog:
        add_blog(v["title"],v["author"],v["text"],v["email"])
    for p in blogg.objects.all():
        print(str(p))
def add_blog(title,author,text,email):
    p=blogg.objects.get_or_create(title=title,email=email)[0]
    p.author=author
    p.text=text
    p.save()
    return p
if __name__ == "__main__":
    print("Populating blog.......")
    populate()