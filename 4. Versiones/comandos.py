'''
Aqui se registrarán todos los comandos necesarios para el control de versiones en git:
1.- git init: Con este comando inicializamos el proyecto. Aquí se agrega una carpeta .git en el directorio y se registra toda la información necesaria para el manejo de versiones.
2.- git status -s: Con este comando visualizamos el estatus de los archivos del proyecto. Si éstos aparecen con '?' significa que aun no han sido agregados.
    Tenemos el seguiente ejemplo:
    $ git status -s
    ?? "1. Doctest/"
    ?? "2.- Assert/"
    ?? "3. Casos de pruebas/"
    ?? __pycache__/

    En este ejemplo podemos visualizar que ningun archivo ha sido agregado en el directorio de git ya que tiene el signo '??'.
    Si deseamos agregar un archivo o directorio ejecutamos el siguiente comando.
3.- git add nombre_archivo: Aquí pude ser directorios. En esta oportunidad esta creando una área de ensayo ó "Staging area" antes del reporsitorio local.
    Tambien podemos hacer uso de "git add ." con este comando preparamos el área de ensayo de todo el proyecto que estamos realizando.
4.- git commit -m "Comentario": Aquí lo que hace es crear la fotografía del proyecto y agregamos un comentario. En este punto si corremos el comando git status -s
    podemos ver que no lista la carpeta que agregamos a git.


    Si realizamos una modificación al archivo podemos ver Visual Studio Code ó ejecutando el comando git status -s que extsite un archivo modificado.
    Para ello debemos agregar el archivo al área de ensayo para prepararlo y hacerle el commit con su comentando la modificación que acabamos de realizar.
5.- git add test_shopping_cart.py
6.- git log --oneline: Con este comando podemos visualizar todas las copias realizadas en el proyecto identificadas con su id.
7.- git reset -- hard "codigo o id de la foto": Aquí podemos restaurar una version del proyecto ya agregada. Para ello hacemos uso del código de la foto.
    De igual manera, si queremos visualizar que se restauró la copia que queríamos podemos hacer uso del comando log para validar. En el caso de Visual Studio Code
    se modifica automaticamente el archivo (ALELUYA POR ESO :-) )
8.- Pero para la fortuna del programasdor existe un comando que agrega al a´rea de trabajo y realiza commit al mismo tiempor. Este comando es el siguiente:
    git commit am "comentario"
'''