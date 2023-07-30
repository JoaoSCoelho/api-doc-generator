----------------- time.struct_time(tm_year=2023, tm_mon=7, tm_mday=30, tm_hour=19, tm_min=1, tm_sec=54, tm_wday=6, tm_yday=211, tm_isdst=0) -----------------

<details>
 <summary><strong>POST</strong> | <code>/api/users</code> | Cria��o de usu�rios</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Nenhuma`


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
 <summary><strong>GET</strong> | <code>/api/users/:id</code> | Busca um usu�rio espec�fico</summary>

> **Permiss�es necess�rias**: `ADMIN`, `MANTAINER`, `STAFF`

> **Autentica��o necess�ria**: `Bearer`


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