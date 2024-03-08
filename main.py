import flet as ft

def main(pagina):
    texto = ft.Text("Oi")

    def entrar_chat (evento):
        popup.open="False"
        pagina.update()
        pagina.remove=texto
        pagina.remove=botao
        pagina.update()

    titulo_popup = ft.Text("Bem vindo")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton ("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title= titulo_popup,
        content= nome_usuario,
        actions=[botao_entrar],
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton(text = "Iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao)

ft.app(target=main)