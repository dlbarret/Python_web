from modelo import obtener_libros

def renderizar_template(libros):
  # simular la caracterizacion de un template de Libros
  html = "<h1>Lista de libros</h1>"
  for libro in libros:
    html += f"<p>ID: {libro['id']}, <br>Titulo: {libro['titulo']}, <br> Autor : {libro['autor']}</p>"
    return html

#Integrar la visya y el template
def mostrar_libros_con_template():
  libros = obtener_libros()
  html = renderizar_template(libros)
  print(html)

 mostrar_libros_con_template()
  