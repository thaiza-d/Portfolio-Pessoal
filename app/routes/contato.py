from fastapi import APIRouter, Depends
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

@router.post("/")
def enviar_mensagem(envio: ContatoCreate, db: Session= Depends(get_db)):
    nova_mensagem = Contato(
        nome=envio.nome,
        email=envio.email,
        mensagem=envio.mensagem
    )
    db.add(nova_mensagem)
    db.commit()
    db.refresh(nova_mensagem)

    try:
        nova_mensagem()
    except Exception as erro:
        print(erro)

    msg = MIMEText(
    f"""
    Nome: {envio.nome}
    Email: {envio.email}
    Mensagem:
    {envio.mensagem}
    """
    )

    msg["Subject"] = f"Portfólio - mensagem de {envio.nome}"
    msg["From"] = os.getenv("MEU_EMAIL")
    msg["To"] = os.getenv("MEU_EMAIL") 
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(
            os.getenv("MEU_EMAIL"),
            os.getenv("SENHA_EMAIL")
            )
        servidor.send_message(msg)
        print("FROM:", os.getenv("MEU_EMAIL"))
        print("TO:", os.getenv("MEU_EMAIL"))
        print(msg.as_string())

    return {"mensagem": "enviado com sucesso!"}