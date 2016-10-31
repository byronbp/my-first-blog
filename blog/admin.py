from django.contrib import admin
from .models import Post

admin.site.register(Post) #Permite que el modelo Post
                          #sea visible en la pag. del administrador
