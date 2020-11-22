# crear ambiente
python -m venv venv

### para linux
source venv/bin/activate

## para win 
> venv\Scripts\activate.bat

## para salir del entorno
> deactivate

## activar entorno virtual power shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


## para importar las dependencias
pip freeze > requirements.txt

# dkjango run project
python manage.py runserver  || python manage.py runserver 9000

## genera tablas temporales a sql
python manage.py migrate

## para crear un modulo autores
python manage.py startapp editoriales

## genera sql
python manage.py makemigrations autores
python manage.py makemigrations editoriales


## para migrar a la db
python manage.py migrate

## ver historial de migraciones
python manage.py showmigrations

## crear superuser
python manage.py createsuperuser

## en appcreada/admin.py agregar la sig linea
from autores.models import Autor
admin.site.register(Autor)

## crear una consola pero con django
python manage.py shell

## ejemplo de como acceder a su shell
python manage.py shell

### luego podemos interacturar
> from autores.models import Autor
> Autor

> autores = Autor.objects.all() # retorna todos los registros de DB

> Autor.objects.get(id=1) #solo busca 1 valor si se repite, sera un >error, por lo q se recomienda solo para buscar id

> Autor.objects.filter(nombre="dixroby") #filtra y debuelve un arrary

> autorJoven = Autor.objects.filter(edad__lt = 30) #un filtro de 30 para abajo
> autorViejo = Autor.objects.filter(edad__gt = 30) #de 30 para arriba

# CRUD

## add
nuevo_autor = Autor.objects.create(nombre = "name",telefono = "23234", correo = "gg",edad = 19)

## update
autor = Autor.objects.get(id=1)
autor.nombre = "new name"
autor.save()

## delete 
Autor.objects.get(id=1).delete()

## recorrer con un for 
> exec("for c in cursos: print ('{0} - {1} - {2}'.format(c.id, c.nombre,c.creditos))")

## eliminar 
libro.autores.remove(Autor.objects.get(id=1))

## agregar
libros.autores.add(Autor.Autor.objects.get(id=1))