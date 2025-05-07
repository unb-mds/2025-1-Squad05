# 🔐 Voice Biometrics API

Este projeto implementa uma **API de reconhecimento biométrico por voz** em um modelo de login já existente utilizando **SpeechBrain** e **FastAPI**. A API permite que usuários registrem sua voz e, posteriormente, sejam autenticados com base em suas características vocais únicas.

## 📎Links Úteis

- [Figma - Projeto (StoryMap)](https://www.figma.com/board/b3El7KviXHzQEFS7IuhGyo/Projeto-MDS--Copy-?node-id=0-1&t=bZuBbWs4QZgYPwbc-1)
- [Figma - Protótipo](https://www.figma.com/proto/QTXFDiqQfiVNi7GRcvbs1q/Tela-de-login?node-id=1-2&t=HCUUayChkonQImLr-1&starting-point-node-id=1%3A2)
- [GitHub Page](https://unb-mds.github.io/Sonorus-2025.1/)
- [Arquitetura](./docs/arquitetura_software/)
- [Requisitos](./docs/requisitos.md)

## 🧠 Tecnologias Utilizadas

**Frontend**
    - HTML
    - CSS
    - TailwindCSS
    - JavaScript
    - ReactJs

**Backend**
    - Python
    - SpeechBrain
    - FastAPI

**Banco de dados**
    - Oracle Database

## 📁 Estrutura do Projeto

```
Biometria-Vocal-2025.1/
├── src
    ├── backend/
        ├── api/
        ├── database/
        ├── models/
        ├── services/
        ├── utils/
        ├── main.py
        └── requirements.txt
    ├── frontend/
        ├── CSS/
        ├── HTML/
        └── JS/
├── LICENSE
├── README.md
├── docs/
    ├── arquitetura_software/
    ├── atas/
    └── estudos/
└── .gitignore
```

## 🚀 Como Executar
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/unb-mds/Biometria-Vocal-2025.1.git
   cd Biometria-Vocal-2025.1
   ```

2. **Navegue até o diretório do backend:**
   ```bash
   cd src/backend
   ```

3. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Inicie o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Acesse a API:**
   - Acesse a documentação interativa no navegador em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Ou veja a documentação alternativa em: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

7. **Encerrar o servidor:**
   - Pressione `Ctrl + C` no terminal para parar o servidor.


## 🔊 Como Usar


### ▶️ Registro


### ✅ Verificação


## 🧪 Modelo Usado
ECAPA-TDNN do speechbrain/spkrec-ecapa-voxceleb

## 📂 Armazenamento

## Contribuidores

| Nome                | GitHub        |
|---------------------|-------------------------|
|Douglas Wilson       | [Dodgelinhass](https://github.com/Dodgelinhass) |
|Daniel Teles         | [dtdanielteles](https://github.com/dtdanielteles) |
|José Joaquim         | [Joaquim-SNeto](https://github.com/Joaquim-SNeto) |
|Luan Vinícius        | [luannvi](https://github.com/luannvi) |
|Matheus Lemes        | [matheuslemesam](https://github.com/matheuslemesam) |
|Paulo Henrique       | [Pauloswimming](https://github.com/Pauloswimming) |
|Paulo Nery           | [Pnery2004](https://github.com/Pnery2004) |
|Rafael Barbosa       | [rafaelbdmelo117](https://github.com/rafaelbdmelo117) |
