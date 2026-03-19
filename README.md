## Project 4 - Currency Converter built with COBOL + REST API [ENG]

## Click below to test the API in real time:

[![Open Tester](https://img.shields.io/badge/Open%20Interactive%20Tester-3270%20Terminal-brightgreen)](https://heriberto-junior.github.io/PRJ-4-conversor-responsivo/)

---

## Description

A project that demonstrates how to integrate **classic COBOL** with **modern technologies**:

- **Backend:** GNU COBOL (conversion logic)
- **API:** REST with Python (Flask)
- **Deployment:** Google Cloud Run (Server available until 06/05/2026)
- **Frontend:** HTML/CSS/JavaScript (GitHub Pages)
- **Containerization:** Docker

---

## Project Flow

**- 01.** User accesses https://heriberto-junior.github.io/PRJ-4-conversor-responsivo/ (GitHub Pages)  
**- 02.** Browser downloads index.html (HTML + CSS + JavaScript)  
**- 03.** User inputs e.g.: 100 BRL → USD  
**- 04.** JavaScript sends a fetch request to the API:  
          ```
          POST https://conversor-responsivo-437617461453.us-central1.run.app/converter
          ```  
          ```  
          { "valor": "100", "moeda": "USD" }
          ```  
**- 05.** API (app.py) receives the request  
**- 06.** app.py executes COBOL:  
         ```
         ./coin 100 USD
         ```  
**- 07.** COBOL processes the request (reads cotacao.txt, calculates)  
**- 08.** COBOL returns:  
          Result:  19330.000 USD  
**- 09.** app.py converts to JSON:  
         ```  
         {
         ```  
         ```  
            "resultado": "Resultado:  19330.000 USD",
         ```  
         ```  
            "sucesso": true
           ```  
           ```  
          }
          ```  
**- 10.** JavaScript receives the JSON  
**- 11.** index.html displays the result:  
       ```
       ✓ Conversion Successful
       ```  
       ```  
        Result:  19330.000 USD
        ```  
**- 12.** User sees the result in real time  

---

## Developer

**Heriberto** - Mainframe Developer

---
---

## Projeto 4 - Conversor de moedas desenvolvido em COBOL + API REST [PT-BR]

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

**- 01.** Usuário acessa https://heriberto-junior.github.io/PRJ-4-conversor-responsivo/ (GitHub Pages)  
**- 02.** Navegador baixa index.html (HTML + CSS + JavaScript)  
**- 03.** Usuário digita por exemplo: 100 BRL → USD  
**- 04.** JavaScript faz fetch para API:  
          ```
          POST https://conversor-responsivo-437617461453.us-central1.run.app/converter
          ```  
          ```  
          { "valor": "100", "moeda": "USD" }
          ```  
**- 05.** API (app.py) recebe requisição  
**- 06.** app.py executa COBOL:  
         ```
         ./coin 100 USD
         ```  
**- 07.** COBOL processa (lê cotacao.txt, calcula)  
**- 08.** COBOL retorna:  
          Resultado:  19330.000 USD  
**- 09.** app.py converte para JSON:  
         ```  
         {
         ```  
         ```  
            "resultado": "Resultado:  19330.000 USD",
         ```  
         ```  
            "sucesso": true
           ```  
           ```  
          }
          ```  
**- 10.** JavaScript recebe JSON  
**- 11.** index.html mostra resultado:  
       ```
       ✓ Conversão Realizada
       ```  
       ```  
        Resultado:  19330.000 USD
        ```  
**- 12.** Usuário vê resultado em tempo real  


---

## Desenvolvedor

**Heriberto** - Mainframe Developer
