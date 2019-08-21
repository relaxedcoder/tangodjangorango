
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
django.setup()


from rango.models import Category, Page
def Populate():
    python_pages = [{"title": "Official tutrorial", "url": "http://python.html"},
                    {"title": "How to Think like a Computer Scientist",
                     "url": "http://www.greenteapress.com/thinkpython/"},
                    {"title": "Learn Python in 10 Minutes",
                     "url": "http://www.korokithakis.net/tutorials/python/"}]
    django_pages = [{"title": "Official Django Tutorial",
                     "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
                    {"title": "Django Rocks",
                     "url": "http://www.djangorocks.com/"},
                    {"title": "How to Tango with Django",
                     "url": "http://www.tangowithdjango.com/"}]
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}]
    cat = {"Python": {"Pages": python_pages,"views":"128","likes":"64"},
           "Django": {"Pages": django_pages,"views":"64","likes":"32"},
           "Other Pages": {"Pages": other_pages,"views":"32","likes":"16"}}
    for k, v in cat.items():
        c = add_cat(k,v["views"],v["likes"])
        for p in v["Pages"]:
            add_pages(c, p["title"], p["url"])
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0} -{1}".format(str(c), str(p)))


def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c


def add_pages(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


if __name__ == "__main__":
    print("Starting Rango population Script......")
    Populate()
