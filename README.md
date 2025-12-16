
# Sistema de Ouvidoria

Projeto acadêmico desenvolvido em **Python**, com integração ao **MySQL**, que simula o funcionamento de uma **Ouvidoria Institucional**. O sistema permite o cadastro, consulta, listagem, contagem e remoção de manifestações, organizadas por tipo.

---

## 🎯 Objetivo do Projeto

Aplicar conceitos de **lógica de programação**, **funções**, **estruturas condicionais**, **laços de repetição** e **integração com banco de dados**, por meio do desenvolvimento de um sistema funcional de ouvidoria.

---

## ⚙️ Funcionalidades

* Registrar novas manifestações
* Listar manifestações por tipo ou todas
* Consultar manifestação por código
* Contar o total de manifestações cadastradas
* Remover manifestações pelo código
* Menu interativo via terminal

---

## 🗂️ Tipos de Manifestações

* Elogio
* Reclamação
* Sugestão
* Denúncia

---

## 🧠 Estrutura do Código

O sistema é organizado em funções responsáveis por cada operação:

* `adicionarManifestacao()` → registra uma nova manifestação
* `listarManifestacoes()` → lista manifestações por tipo ou todas
* `pesquisarManifestacoesCodigo()` → consulta manifestação pelo código
* `quantidadeManifestacao()` → exibe o total de manifestações
* `removerManifestacao()` → remove uma manifestação pelo código

As operações de banco de dados são realizadas por meio do módulo **operacoesbd**, responsável pelas funções de conexão e execução de comandos SQL.

---

## 🛠️ Tecnologias Utilizadas

* Python
* MySQL
* SQL
* Git e GitHub

---

## ▶️ Como Executar o Projeto

1. Clone este repositório
2. Configure o banco de dados MySQL e crie a tabela `Manifestacoes`
3. Configure o arquivo de conexão com o banco no módulo `operacoesbd`
4. Execute o arquivo principal do sistema pelo terminal ou PyCharm

```bash
python main.py
```

---

## 📚 Finalidade

Projeto desenvolvido com **finalidade acadêmica e educacional**, voltado para prática de programação e banco de dados.

---

👨‍💻 Desenvolvido por

