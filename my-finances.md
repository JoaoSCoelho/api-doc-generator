----------------- time.struct_time(tm_year=2023, tm_mon=7, tm_mday=30, tm_hour=11, tm_min=25, tm_sec=57, tm_wday=6, tm_yday=211, tm_isdst=0) -----------------

<details>
 <summary><strong>GET</strong> | <code>/api/confirmemail/:token</code> | Confirmar email</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Nenhuma`


##### Response
```ts
// Status 200 
![Confirmed email](resources/confirmed-email-screen.png)
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/users/me</code> | Busca os dados do usu�rio</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Bearer`


##### Response
```ts
// Status 200 
{
  user: {
    id: string,
    username: string,
    email: string,
    confirmedEmail: boolean,
    createdTimestamp: number,
    profileImageURL?: string
  }
}
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/bankaccounts/my</code> | Busca as contas banc�rias do usu�rio</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Bearer`


##### Response
```ts
// Status 200 
{
bankAccounts: {
    id: string,
    userId: string,
    createdTimestamp: number,
    name: string,
    initialAmount: number,
    imageURL?: string,
    totalAmount: number,
  }[]
}
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/transactions</code> | Busca todas as transa��es do usu�rio</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Bearer`


##### Response
```ts
// Status 200 
{
transactions: {
    id: string,
    bankAccountId?: string,
    giverBankAccountId?: string,
    receiverBankAccountId?: string,
    description?: string,
    spent?: number,
    gain?: number,
    amount?: number,
    createdTimestamp: number,
    title: string,
    type: 'expense' | 'income' | 'transfer',
  }[]
}
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/transactions/incomes</code> | Busca as transa��es de receita do usu�rio</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Bearer`


##### Response
```ts
// Status 200 
{
incomes: {
    id: string,
    bankAccountId: string,
    description?: string,
    gain: number,
    createdTimestamp: number,
    title: string,
  }[]
}
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/transactions/expenses</code> | Busca as transa��es de despesa do usu�rio</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Bearer`


##### Response
```ts
// Status 200 
{
expenses: {
    id: string,
    bankAccountId: string,
    description?: string,
    spent: number,
    createdTimestamp: number,
    title: string,
  }[]
}
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/transactions/transfers</code> | Busca as transa��es de transfer�ncia do usu�rio</summary>

> **Permiss�es necess�rias**: `NENHUMA`

> **Autentica��o necess�ria**: `Bearer`


##### Response
```ts
// Status 200 
{
transfers: {
    id: string,
    giverBankAccountId: string,
    receiverBankAccountId: string,
    description?: string,
    amount: number,
    createdTimestamp: number,
    title: string,
  }[]
}
```
</details>