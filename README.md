## Projeto 4 - Conversor de moedas desenvolvido em COBOL + API REST

## Clique abaixo para testar a API em tempo real:

[![Abrir Testador](https://img.shields.io/badge/Abrir%20Testador%20Interativo-3270%20Terminal-brightgreen)](https://heriberto-junior.github.io/PRJ-4-conversor-responsivo/)

---

## Descrição

Projeto que demonstra como integrar **COBOL clássico** com **tecnologias modernas**:

- **Backend:** COBOL GNU (lógica de conversão)
- **API:** REST em Python (Flask)
- **Deployment:** Google Cloud Run (Servidor disponível até 05/06/2026)
- **Frontend:** HTML/CSS/JavaScript (GitHub Pages)
- **Containerização:** Docker

---

## Fluxo do Projeto

**1.** Usuário acessa https://heriberto-junior.github.io/PRJ-4-conversor-responsivo/ (GitHub Pages)  
**2.** Navegador baixa index.html (HTML + CSS + JavaScript)  
**3.** Usuário digita por exemplo: 100 BRL → USD  
**4.** JavaScript faz fetch para API:  
   POST https://conversor-responsivo-437617461453.us-central1.run.app/converter  
   { "valor": "100", "moeda": "USD" }  
**5.** API (app.py) recebe requisição  
**6.** app.py executa COBOL:  
   ./coin 100 USD  
**7.** COBOL processa (lê cotacao.txt, calcula)  
**8.** COBOL retorna:  
   Resultado:  19330.000 USD  
**9.** app.py converte para JSON:  
   {  
     "resultado": "Resultado:  19330.000 USD",  
     "sucesso": true  
   }  
**10.** JavaScript recebe JSON  
**11.** index.html mostra resultado:  
    ✓ Conversão Realizada  
    Resultado:  19330.000 USD  
**12.** Usuário vê resultado em tempo real  


---

## Desenvolvedor

**Heriberto** - Mainframe Developer
