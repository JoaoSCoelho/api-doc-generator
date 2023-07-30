----------------- time.struct_time(tm_year=2023, tm_mon=7, tm_mday=30, tm_hour=11, tm_min=25, tm_sec=57, tm_wday=6, tm_yday=211, tm_isdst=0) -----------------

<details>
 <summary><strong>GET</strong> | <code>/api/confirmemail/:token</code> | Confirmar email</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Nenhuma`


##### Response
```ts
// Status 200 
![Confirmed email](resources/confirmed-email-screen.png)
```
</details>

<details>
 <summary><strong>GET</strong> | <code>/api/users/me</code> | Busca os dados do usuário</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Bearer`


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
 <summary><strong>GET</strong> | <code>/api/bankaccounts/my</code> | Busca as contas bancárias do usuário</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Bearer`


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
 <summary><strong>GET</strong> | <code>/api/transactions</code> | Busca todas as transações do usuário</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Bearer`


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
 <summary><strong>GET</strong> | <code>/api/transactions/incomes</code> | Busca as transações de receita do usuário</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Bearer`


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
 <summary><strong>GET</strong> | <code>/api/transactions/expenses</code> | Busca as transações de despesa do usuário</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Bearer`


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
 <summary><strong>GET</strong> | <code>/api/transactions/transfers</code> | Busca as transações de transferência do usuário</summary>

> **Permissões necessárias**: `NENHUMA`

> **Autenticação necessária**: `Bearer`


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