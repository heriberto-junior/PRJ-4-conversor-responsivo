## Projeto 4 - Conversor de moedas desenvolvido em COBOL responsivo (em andamento)

# Conversor de Moedas - COBOL + API REST

## Testador Interativo

**[👉 Clique aqui para testar a API](https://heribertonsjr.github.io/PRJ-4-conversor-responsivo/)**

---

## API em Produção

**URL:** https://conversor-moedas-437617461453.us-central1.run.app

## Endpoints

### GET /health
```bash
curl https://conversor-moedas-437617461453.us-central1.run.app/health
```

### POST /converter
```bash
curl -X POST https://conversor-moedas-437617461453.us-central1.run.app/converter \
  -H "Content-Type: application/json" \
  -d '{"valor":"100","moeda":"USD"}'
```

## Tecnologias

- **COBOL** - Lógica de conversão
- **Python** - Framework Flask
- **Google Cloud Run** - Hosting
- **Docker** - Containerização
- **GitHub Pages** - Interface web

## Desenvolvedor

**Heriberto** - Mainframe Developer
