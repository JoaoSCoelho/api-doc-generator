from pick import pick
import keyboard
import time

print('------------ REST API Routes Documentation Generator ------------')

savefile = input('Nome do arquivo a ser salvo (ex: something.md): ')
baseroute = input('Rota base (ex: /api): ')
apipermissions = input('Quais são todas as permissões existentes na sua API? ').upper().split(' ')

# Create the save file and put the current datetime
file = open(savefile, 'a')
file.write(f'\n\n----------------- {time.localtime()} -----------------')
file.close()

def exec():
  method = pick(['GET', 'POST', 'PUT', 'DELETE'], 'Método:', '→')[0]
  print(f'Método: {method}')
  route = baseroute + input('Rota: ')
  shortdescription = input('Descrição curta: ')
  authtype = pick(['Nenhuma', 'Bearer'], 'Tipo de autenticação:', '→')[0]
  print(f'Autenticação necessária: {authtype}')
  oldPermissions = pick(apipermissions, 'Permissões necessárias: (selecione com o ESPAÇO, confirme com ENTER)', '→', 0, True)
  permissions = []

  # Transform oldPermissions on a list in permissions
  for permission in oldPermissions:
    permissions.append(permission[0])

  print(f'Permissões necessárias: {permissions}')

  body = ''
  havebody = 'NÃO'

  if (method == 'POST' or method == 'PUT'):
    havebody = pick(['SIM', 'NÃO'], 'Tem body?', '→')[0]
    print(f'Tem corpo? {havebody}')

    if (havebody == 'SIM'):
      print('Digite o modelo de body abaixo:')
      while (True): # allow multiline input
        event = keyboard.read_event()

        if (event.is_keypad and event.name == 'enter'): 
          break
        else:
          body += '\n' + input()

  responsestatus = input('Successfully status code: ')

  print('Digite o modelo de response abaixo:')

  response = ''
  while (True): # allow multiline input
    event = keyboard.read_event()

    if (event.is_keypad and event.name == 'enter'): 
      break
    else:
      response += '\n' + input()

  returnvalue = f"""<details>
 <summary><strong>{method}</strong> | <code>{route}</code> | {shortdescription}</summary>

> **Permissões necessárias**: `{'`, `'.join(permissions) if permissions else 'NENHUMA'}`

> **Autenticação necessária**: `{authtype}`
{
  f'''

##### Body
```ts{body}
```
''' if havebody == 'SIM' else ''
}

##### Response
```ts
// Status {responsestatus} {response}
```
</details>"""

  # Each concluded route is saved on savefile
  file = open(savefile, 'a')
  file.write('\n\n' + returnvalue)
  file.close()

  repeat = pick(['SIM', 'NÃO'], 'Quer criar outra rota?', '→')[0]
  print(f'Repetir? {repeat}')

  if (repeat == 'SIM'):
    return returnvalue + '\n\n' + exec()

  return returnvalue

documentation = exec()

file = open(savefile, 'w')
file.write(f'----------------- {time.localtime()} -----------------\n\n{documentation}')
file.close()

print('-------------------- RESULTADO --------------------\n')
print(documentation)
print('\n---------------------------------------------------')



