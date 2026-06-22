from fastapi import APIRouter, Depends, BackgroundTasks
from ..schemas import ContatoCreate, ContatoResponse
from ..models import Contato
from ..dependencies import get_db
from sqlalchemy.orm import Session
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(prefix="/contato", tags=["contato"])

@router.get("/", response_model=list[ContatoResponse])
def receber_mensagem(db: Session=Depends(get_db)):
    result = db.query(Contato).all()
    return result

def enviar_email(nome, email, mensagem):
    msg = MIMEText(f"""
    Nome: {nome}
    Email: {email}
    Mensagem:
    {mensagem}
    """)

    msg["Subject"] = f"Portfólio - mensagem de {nome}"
    msg["From"] = os.getenv("MEU_EMAIL")
    msg["To"] = os.getenv("MEU_EMAIL")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as servidor:
        servidor.login(
            os.getenv("MEU_EMAIL"),
            os.getenv("SENHA_EMAIL")
        )
        servidor.send_message(msg)

@router.post("/")
def enviar_mensagem(
    envio: ContatoCreate,
    db: Session = Depends(get_db),
    background_tasks: BackgroundTasks = None
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