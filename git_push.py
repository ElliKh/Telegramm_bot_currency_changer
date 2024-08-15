#git@github.com:ElliKh/Osnova.git

from os import system


ssh_url = 'git@github.com:ElliKh/Telegramm_bot_currency_changer.git'
branch = 'master'
commit_message = 'update'

system('clear')
system('git init')
system('git add .')
system(f'git commit -m {commit_message}')
system(f'git remote add origin {ssh_url}')
system(f'git push -u origin {branch}')

print('Процесс успешно выполнен')

