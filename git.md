# установка глобального пользователя Git (для всех проектов)
git config --global user.name "Pragmatic Programmer"

# установка глобального email пользователя Git (для всех проектов)
git config --global user.email "prag_prog@gmail.com"

# включение цветного вывода информации (в ряде случаев включено по умолчанию)
git config --global color.ui true

# вывод списка настроек
git config --list

# вывод имени пользователя/email из настроек
git config user.name
git config user.email

# вывод истории команд
history

# установка локальной настройки Git (для конкретного репозитория)
git config user.name "Pragmatic Programmer"
git config user.email "prag_prog@gmail.com"

# Расположение конфиг-файла

# 1. Системные настройки Git (для всех пользователей)
C:\Program Files\Git\etc\gitconfig

# 2. Глобальные настройки (для текущего пользователя)
%USERPROFILE%\.gitconfig

# 3. Локальные настройки (для конкретного репозитория)
<Путь_к_репозиторию>\.git\config

# создать каталог для проекта с именем 'first_project'
mkdir first_project

# вывести содержимое текущего каталога
ls

# перейти в созданный каталог
cd first_project/

# вывести путь к текущей локации
pwd

# вывести содержимое каталога в подробном (табличном виде), включая скрытые файлы и папки
ls -la

# (основная команда урока!) создать Git-репозиторий в текущей папке
git init

# перейти в папку '.git'
cd .git/

# вывести содержимое файла config
cat config

# задать локально (для текущего репозитория) имя пользователя Git
git config user.name "user22"

# вывести глобальное значение имени пользователя Git
git config --global user.name

# вывести локальное значение имени пользователя Git
git config user.name

# вывести список всех настроек Git
git config --list

# вывести список глобальных настроек Git
git config list --global

# вывести список локальных настроек Git
git config list --local

# переместиться в предыдущую локацию
cd -

# переместиться в домашний каталог пользователя
cd c:/Users/Pragmatic_Programmer

# вывести содержимое файла '.gitconfig'
cat .gitconfig

# вывести список ВСЕХ текущих настроек Git вместе с информацией о том, из какого файла конфигурации каждая настройка взята.
git config --show-origin --list

# посмотреть состояние файлов в индексе
git status

# посмотреть историю коммитов
git log

# вывести на экран содержимое указанного файла
cat page1.html

# добавить в индекс указанный файл
git add page1.html

# сделать коммит (требует ввода текстового сообщения)
git commit
