# REST API Documentation Generator
 
Um script simples em Python para ajudar na criação da documentação de uma REST API em Markdown

## Tabela de conteúdos

- [REST API Documentation Generator](#rest-api-documentation-generator)
  - [Tabela de conteúdos](#tabela-de-conteúdos)
  - [Instalação](#instalação)
  - [Como usar](#como-usar)
      - [Veja vídeo de exemplo](#veja-vídeo-de-exemplo)
      - [Exemplo de criação da documentação de duas rotas](#exemplo-de-criação-da-documentação-de-duas-rotas)
        - [Resultado em Markdown](#resultado-em-markdown)
        - [Body](#body)
        - [Response](#response)
        - [Response](#response-1)
  - [Status](#status)
  - [Licença](#licença)
  - [Tecnologias e Libs](#tecnologias-e-libs)

## Instalação

1. Você precisa do [Git](https://git-scm.com) e do [Python3](https://python.org/) instalados na sua máquina.

```bash
# Clone este repositório
$ git clone <https://github.com/JoaoSCoelho/api-doc-generator>

# Acesse a pasta do projeto no terminal/cmd
$ cd api-doc-generator
```

2. Instale as dependências:
```python
from pick import pick
import keyboard
import time
``` 
```bash
$ pip install [deps]
```

## Como usar

```bash
# Rode o programa
$ python index.py
```

#### [Veja vídeo de exemplo](resources/usage.mp4)
![](resources/usage.mp4)
[https://youtu.be/XTlyknuiyhk](https://youtu.be/XTlyknuiyhk)

#### Exemplo de criação da documentação de duas rotas

```powershell
PS C:\api-doc-generator> python index.py
------------ REST API Routes Documentation Generator ------------
Nome do arquivo a ser salvo (ex: something.md): file.md
Rota base (ex: /api): /api
Quais são todas as permissões existentes na sua API? ADMIN PRO_USER SUPER_USER MANTAINER STAFF
Método: POST
Rota: /users
Descrição curta: Criação de usuários
Autenticação necessária: Nenhuma
Permissões necessárias: []
Tem corpo? SIM
Digite o modelo de body abaixo:
{
  username: string,
  email: string,
  password: string,
  nickname?: string,
  imageURL?: string,
}
Successfully status code: 201
Digite o modelo de response abaixo:
{
  username: string,
  email: string,
  nickname?: string,
  imageURL?: string,
  permissions: string[],
  confirmed_email: boolean,
  created_at: string,
  updated_at: string
}
Repetir? SIM
Método: GET
Rota: /users/:id
Descrição curta: Busca um usuário específico
Autenticação necessária: Bearer
Permissões necessárias: ['ADMIN', 'MANTAINER', 'STAFF']
Successfully status code: 200
Digite o modelo de response abaixo:
{
  username: string,
  email: string,
  nickname?: string,
  imageURL?: string,
  permissions: string[],
  confirmed_email: boolean,
  created_at: string,
  updated_at: string
}[]
Repetir? NÃO
-------------------- RESULTADO --------------------

<details>
 <summary><strong>POST</strong> | <code>/api/users</code> | Criação de usuários</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Nenhuma`


##### Body
```ts
{
  username: string,
  email: string,
  password: string,
  nickname?: string,
  imageURL?: string,
}
\```


##### Response
```ts
// Status 201
{
  username: string,
  email: string,
  nickname?: string,
  imageURL?: string,
  permissions: string[],
  confirmed_email: boolean,
  created_at: string,
  updated_at: string
}
\```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/users/:id</code> | Busca um usuário específico</summary>

> **Permissões necessárias**: `ADMIN`, `MANTAINER`, `STAFF`

> **Autenticação necessária**: `Bearer`


##### Response
```ts
// Status 200
{
  username: string,
  email: string,
  nickname?: string,
  imageURL?: string,
  permissions: string[],
  confirmed_email: boolean,
  created_at: string,
  updated_at: string
}[]
\```
</details>

---------------------------------------------------
```

##### Resultado em Markdown

<details>
 <summary><strong>POST</strong> | <code>/api/users</code> | Criação de usuários</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Nenhuma`


##### Body
```ts
{
  username: string,
  email: string,
  password: string,
  nickname?: string,
  imageURL?: string,
}
```


##### Response
```ts
// Status 201
{
  username: string,
  email: string,
  nickname?: string,
  imageURL?: string,
  permissions: string[],
  confirmed_email: boolean,
  created_at: string,
  updated_at: string
}
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/users/:id</code> | Busca um usuário específico</summary>

> **Permissões necessárias**: `ADMIN`, `MANTAINER`, `STAFF`

> **Autenticação necessária**: `Bearer`


##### Response
```ts
// Status 200
{
  username: string,
  email: string,
  nickname?: string,
  imageURL?: string,
  permissions: string[],
  confirmed_email: boolean,
  created_at: string,
  updated_at: string
}[]
```
</details>

## Status
> **Descontinuado** v0.1.0Alpha

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

## Tecnologias e Libs

* ![Python logo](resources/python.png) Python
* pick
* keyboard
* time