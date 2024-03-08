import flet as ft
from datetime import datetime

def main(pagina):
    chat = ft.Column()
    hoje = datetime.now()
    horario = hoje.strftime('%d/%m/%Y %H:%M:%S')

    def enviar_mensaem_tunel(mensagem):
        chat.controls.append(mensagem)
        pagina.update()
        pass

    pagina.pubsub.subscribe(enviar_mensaem_tunel)

    def enviar_mensagem (evento):
        texto_mensagem=ft.Text (f"{horario} - {nome_usuario.value}: {campo_mensagem.value}")
        pagina.pubsub.send_all(texto_mensagem)
        campo_mensagem.value=0
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar=ft.IconButton(on_click=enviar_mensagem,icon="send")
    linha_enviar=ft.Row([campo_mensagem,botao_enviar])

    texto = ft.Text("Bem vindo ao chat")

    def entrar_chat (evento):
        popup.open="False"
        pagina.remove(texto)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.pubsub.send_all(ft.Text(f"{horario} - {nome_usuario.value} entrou no chat"))
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

ft.app(target=main, view=ft.WEB_BROWSER)