folder -> project -> (app1,app2,app3...) -> installapp -> app1

app1:
model name: Example
var_name:first_name | field_type:char(100)

# things to google
how to insert something in a middle of file

# models

#queries
Retrieving all objects
Entry.objects.all()

Retrieving specific objects with filters¶
Entry.objects.filter(pub_date__year=2006)

Chaining filters¶
Entry.objects.filter(headline__startswith='What'.exclude(pub_date__gte=datetime.date.today())
.filter(pub_date__gte=datetime.date(2005, 1, 30))

Filtered QuerySets are unique¶
q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=datetime.date.today())
q3 = q1.filter(pub_date__gte=datetime.date.today())

Retrieving a single object with get()¶
one_entry = Entry.objects.get(pk=1)

Limiting QuerySets¶
Entry.objects.all()[:5]
Entry.objects.order_by('headline')[0]

Field lookups¶
Entry.objects.filter(pub_date__lte='2006-01-01')  => SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';

Entry.objects.filter(blog_id=4)

Entry.objects.get(headline__exact="Cat bites dog") => SELECT ... WHERE headline = 'Cat bites dog';

For example, the following two statements are equivalent:
Blog.objects.get(id__exact=14)
Blog.objects.get(id=14)   

A case-insensitive match. So, the query: `iexact`
Blog.objects.get(name__iexact="beatles blog")

`contains` Case-sensitive containment test. For example:
Entry.objects.get(headline__contains='Lennon') -> SELECT ... WHERE headline LIKE '%Lennon%';

Lookups that span relationships¶
Entry.objects.filter(blog__name='Beatles Blog')

Blog.objects.filter(entry__headline__contains='Lennon')
Blog.objects.filter(entry__authors__name='Lennon')
Blog.objects.filter(entry__authors__name__isnull=True)

To select all blogs that contain an entry with “Lennon” in the headline as well as an entry that was published in 2008, we would write:
Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)

Blog.objects.exclude(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008,
)

Aggregation Cheat sheet¶
Book.objects.count()
Book.objects.filter(publisher__name='BaloneyPress').count()
Book.objects.all().aggregate(Max('price'))

# Each publisher, with a separate count of books with a rating above and below 5
>>> from django.db.models import Q
>>> above_5 = Count('book', filter=Q(book__rating__gt=5))
>>> below_5 = Count('book', filter=Q(book__rating__lte=5))
>>> pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
>>> pubs[0].above_5
23
>>> pubs[0].below_5
12

Search
Standard textual queries¶
Author.objects.filter(name__contains='Terry')
Entry.objects.filter(body_text__search='cheese')
Entry.objects.annotate(
...     search=SearchVector('blog__tagline', 'body_text'),
... ).filter(search='cheese')


# Field types¶
AutoField
BooleanField
CharField(max_length=None, **options)¶

class DateField(auto_now=False, auto_now_add=False, **options)¶
 DateField.auto_now¶
 DateField.auto_now_add¶
 
 class DateTimeField(auto_now=False, auto_now_add=False, **options)¶
 
 DecimalField
 class DecimalField(max_digits=None, decimal_places=None, **options)¶
 
 DurationField
 
  class DurationField(**options)¶
  
  EmailField¶
  
   class EmailField(max_length=254, **options)¶
   
   FileField¶
   
    class FileField(upload_to=None, max_length=100, **options)¶
    
    JSONField
     class JSONField(encoder=None, decoder=None, **options)¶
     
     SlugField
     
     TextField
     
     TimeField
     class TimeField(auto_now=False, auto_now_add=False, **options)¶
     
     URLField
      class URLField(max_length=200, **options)¶
      
      UUIDField
      
      import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields


Relationship fields¶
ForeignKey¶

class ForeignKey(to, on_delete, **options)¶
models.ForeignKey('self', on_delete=models.CASCADE).


     
 




# django model pattern
from django.db import models
class <ModelName>(models.Model):
    <var_name> = models.<FieldType>(params=args)
    +
    +
    +
    +
    +
    
    def __str__(self):
        return self.<var_name>