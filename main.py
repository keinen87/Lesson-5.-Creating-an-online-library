from livereload import Server
from render_website import on_reload

def rebuild():
    print("Site rebuilt")

server = Server()
server.watch('./templates/template.html', on_reload)
server.serve(root='index.html')