window.enviar = async function () {

    const nome = document.getElementById("nome")
    const email = document.getElementById("email")
    const mensagem = document.getElementById("mensagem")
    const btnEnviar = document.getElementById("btn-enviar")

    limparErros()
    let valido = true

    if (nome.value.trim() === "") {
        mostrarErro(nome, "erro-nome", "Por favor, informe seu nome.")
        valido = false
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email.value.trim())) {
        mostrarErro(email, "erro-email", "Informe um e-mail válido.")
        valido = false
    }
    if (mensagem.value.trim() === "") {
        mostrarErro(mensagem, "erro-mensagem", "Por favor, escreva sua mensagem.")
        valido = false
    }
    if (!valido) return

    try {

        btnEnviar.disabled = true
        btnEnviar.textContent = "Enviando..."

        const resposta = await fetch(
            "http://127.0.0.1:8000/contato/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    nome: nome.value,
                    email: email.value,
                    mensagem: mensagem.value
                })
            }
        )

        if (resposta.ok) {

            nome.value = ""
            email.value = ""
            mensagem.value = ""

            document
                .getElementById("modal")
                .classList.add("aberto")
        } else {
            alert("Não foi possível enviar a mensagem.")
        }

    } catch (erro) {

        console.error(erro)
        alert("Erro ao enviar. Tente novamente.")

    } finally {

        btnEnviar.disabled = false
        btnEnviar.textContent = "Enviar mensagem"

    }
}

window.fechar = async function() {
    document
        .getElementById("modal")
        .classList.remove("aberto")
}
