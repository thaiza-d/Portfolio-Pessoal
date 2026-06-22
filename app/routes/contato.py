from fastapi import APIRouter, Depends, BackgroundTasks
from ..schemas import ContatoCreate, ContatoResponse
from ..models import Contato
from ..dependencies import get_db
from sqlalchemy.orm import Session
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import resend

load_dotenv()

router = APIRouter(prefix="/contato", tags=["contato"])

resend.api_key = os.getenv("RESEND_API_KEY")

def enviar_email(nome, email, mensagem):
    resend.Emails.send({
        "from": os.getenv("RESEND_EMAIL"),
        "to": os.getenv("MEU_EMAIL"),
        "subject": f"Portfólio - mensagem de {nome}",
        "text": f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}"
    })    

@router.post("/")
def enviar_mensagem(
    envio: ContatoCreate,
    background_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    nova_mensagem = Contato(
        nome=envio.nome,
        email=envio.email,
        mensagem=envio.mensagem
    )

    db.add(nova_mensagem)
    db.commit()
    db.refresh(nova_mensagem)

    background_tasks.add_task(
        enviar_email,
        envio.nome,
        envio.email,
        envio.mensagem
    )

    return {"mensagem": "enviado com sucesso!"}