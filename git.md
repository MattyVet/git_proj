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

# вывод списка настроек
git config list

# установить редактор по умолчанию для Git
git config core.editor nano

# добавить в индекс все файлы в текущей папке
git add .

# добавить в индекс указанный файл
git add page1.html

# посмотреть историю коммитов в компактном виде
git log --oneline

# "ленивый коммит" (без команды 'git add')
git commit -a

# добавить изменения в индексе в предыдущий коммит
git commit --amend

# показать детальную информацию о последнем коммите
git show

# показать детальную информацию об указанном коммите
git show <commit_id>

# вывести только имена файлов, участвовавших в коммите
git show --name-only <commit_id>

# переместить "голову" репозитория на 1 коммит назад
# (команда будет подробно рассмотрена в следующих уроках)
git reset HEAD~1

# выполнить коммит с указанным сообщением (после ключа -m)
git commit -m "add some new features"

# совместить ключи -a -m в коммите
# тем самым избавиться от отдельной команды git add и задать сообщение для коммита
git commit -am "add some new features"

# сбросить весь индекс\stage (сохраняя изменения в папке)
git reset

# убрать файл из индекса
git reset <file_name>

# вернуть к состоянию последнего коммита (если поломали код, например)
git reset --hard

# отменить последний коммит (сохраняя сами изменения)
git reset HEAD~1
git reset HEAD^

# отменить последние 2 коммита
git reset HEAD~2
git reset HEAD^^

# отменить последние 3 коммита
git reset HEAD~3
git reset HEAD^^^

# отменить последние 2 коммита (удаляя изменения)
git reset HEAD~2 --hard

# вывести предыдущее значение HEAD
cat .git/ORIG_HEAD

# вернуться к коммиту, на который указывает ORIG_HEAD
git reset ORIG_HEAD --hard

# вернуться к состоянию после указанного коммита
git reset --hard <commit_id>

# история коммитов в кратком виде
git log --oneline

# краткая справка по команде revert
git revert

# подробная справка по команде revert
git revert --help

# детали последнего коммита
git show

# откатить последний коммит (создавая новый `обратный коммит`)
git revert HEAD

# вывод содержимого файла styles.css на экран
cat styles.css

# откатить последний коммит без ввода сообщения для коммита
git revert HEAD --no-edit

# откатить коммит по его идентификатору (хэш-коду)
git revert 8ab14c

# откатить третий коммит с конца
git revert HEAD~3

# отменить незавершенный откат коммита
git revert --abort

# откатить серию коммитов
git revert 9e59768..4b2413e

# откатить коммит без создания нового коммита (изменения попадают в индекс)
git revert 9e59768 --no-commit

# вызов справки
git rm --help

# удаление файла из каталога (команда терминала)
rm page2.html

# удаление файла из Git-репозитория
git rm page2.html

# форсированное удаление файла (если есть изменения в индексе)
git rm page2.html -f
git rm page2.html --force

# удаление каталога
git rm my_folder -r
git rm my_folder --recursive

# вызов справки
git clean --help

# сценарий 1
# создадим ненужные файлы
touch some_binary_file{1..9}.bin
ls

# посмотрим их статус
git status

# очистим Git от этих файлов
git clean -f
ls
git status

# сценарий 2
# создадим пустые папки
mkdir bin
mkdir tmp
ls

# посмотрим их статус
git status

# очистим Git от этих пустых каталогов
git clean -d -f
ls
git status

# ключ -n -- 'холостой прогон команды'
# покажет, что будет происходить при выполнении команды
git clean -f -n
git clean -f -d -n

# ключ -q -- тихое выполнение команды
# не выводит комментарии о ходе своего выполнения
git clean -f -d -q

# переименование файла в терминале
mv page1.html index.html

# набор команд для корректного переименования в Git
mv page1.html index.html
git add index.html
git rm page1.html

# переименование/перемещение файла в Git одной командой
git mv page1.html index.html

# вызов справки
git mv --help

# создаем папку styles
mkdir styles

# перемещаем файл с CSS-стилями в новую папку
git mv styles.css styles

# делаем коммит
git commit -m "create folder for css styles"

# переименование папки в Git
git mv styles css

# создаем папку web_pages
mkdir web_pages

# перемещение набора файлов
git mv *.html web_pages

# вызов локальной справки по команде git diff
git diff --help

# вывод изменений после последнего коммита (не добавленных в индекс)
git diff

# вывод изменений после последнего коммита (включая добавленные в индекс)
git diff HEAD

# вывод изменений, добавленных в индекс
git diff --staged
git diff --cached

# фоматирование изменений по словам (а не по строкам)
git diff --word-diff

# исключение пустых строк из вывода
git diff -w

# вывод изменений после HEAD~1 (и до HEAD)
git diff HEAD~1


# указание хэша коммита для вывода изменений после него
git diff 8a8b14c

# вывод разницы между двумя указанными коммитами
git diff 8a8b14c b0272be

# вывод изменений в конкретном файле после указанного коммита
git diff HEAD~1 web_pages/index.html

# сравнение двух произвольных файлов (даже вне git-репозитория)
git diff index.html page2.html

# вызов локальной справки по команде git difftool
git difftool --help

# указание хэша коммита для вывода изменений после него с помощью утилиты difftool
git difftool 8a8b14c

# просмотр коммита (одно и то же)
git show
git diff HEAD~1

# вывести все накопленные изменения между текущим состоянием и состоянием на момент указанного коммита
git diff bea5ea0

# вывести только изменения, выполненные в указанном коммите
git show bea5ea0

# вывести все коммиты с изменениями между двумя коммитами
git show 0e47d61..ca3a6b1

# вывести все накопленные изменения в файлах между двумя коммитами
git diff 0e47d61..ca3a6b1
git diff 0e47d61 ca3a6b1

# аналогичные команды - просмотр изменений файла в определённом коммите
git show HEAD~1:styles/styles.css
git diff HEAD~1 css/styles.css

# вывести только список файлов, измененных в указанном коммите
git show 4b2413e --name-only
git show 55f77dc --name-only

# вывести только список файлов, измененных с указанного коммита и до текущего состояния репозитория
git diff 55f77dc --name-only

# базовое использование команды просмотра логов
git log

# просмотр логов в кратком формате
git log --oneline

# вызов справки по команде
git log --help

# вывод статистики по коммитам
git log --stat

# просмотр патчей (деталей каждого изменения) по коммитам
git log -p

# ограничение количества комитов в выводе
git log -4

# опции можно сочетать в одной команде
git log –-stat -p
git log -4 --stat -p

# отображение веток в истории коммитов
git log --graph

# клонирование нового репозитория в отдельной папке
cd ..
git clone https://github.com/githubtraining/hellogitworld
cd hellogitworld
ls –a

# использование изученных команд в новом репозитории
git status
git log
git log --oneline
git log --oneline README.txt
git log --stat
git log --graph

# фильтр коммитов по автору
git log --author="Jordan McCullough" –-oneline

# форматирование: дата, автор, время, сообщение
git log -5 --pretty=format:"%h - %an - %as - %s"
git log -5 --pretty=format:"%h - %an - %as %n >> %s"

# читабельное предложение с помощью форматирования
git log --pretty=format:"This guy:%cn committed with hash '%h' on %cd"


# компактный отчёт о коммитах в репозитории группирует коммиты по авторам и выводит список их имён вместе с количеством сделанных ими коммитов и краткими описаниями этих коммитов
git shortlog

# показывает электронную почту автора рядом с его именем
git shortlog -e

# сортирует вывод по количеству коммитов, от большего к меньшему
git shortlog -n

# выводит только статистику (количество коммитов) без списка сообщений коммитов
git shortlog -s

# фильтрация коммитов по датам "до" и "после"
git shortlog --since="2012-01-01" --until="2012-12-31"

Полезные опции для git log --pretty=format

Опция	Описания вывода
%H Хеш коммита

%h Сокращённый хеш коммита

%T Хеш дерева

%t Сокращённый хеш дерева

%P Хеш родителей

%p Сокращённый хеш родителей

%an Имя автора

%ae Электронная почта автора

%ad Дата автора (формат даты можно задать опцией --date=option)

%ar Относительная дата автора

%cn Имя коммитера

%ce Электронная почта коммитера

%cd Дата коммитера

%cr Относительная дата коммитера

%s Содержание

# вывод reference log
# отображает только локальную историю
git reflog

# перемещение в другой репозиторий и вывод аналогичной информации о нем
cd ../hellogitworld
pwd
git reflog

# Сценарий использования: Восстановление удаленного коммита
#
git reflog
git log --oneline
git reset --hard HEAD~1
git log --oneline
git reflog
git reset --hard 10f7044
git log –oneline

# Сценарий использования: Удаление старых записей
#
git reflog
git reflog expire --expire=7.days --all --verbose
git reflog

git reflog expire --expire=1.minutes --all –-verbose
git reflog

# запуск сборщика мусора Git
git gc

# Сравнительная таблица

Характеристика	        git log	                    git reflog
Что показывает	        Коммиты	                    Перемещения HEAD
Объем данных	        Только достижимые коммиты	Все операции
Время хранения	        Бессрочно	                90 дней (по умолчанию)
Для чего использовать	Анализ истории	            Восстановление данных
Порядок вывода	        От новых к старым	        От новых к старым
Показывает мержи	    Да	                        Да
Покажает reset	        Нет	                        Да

## простой пример
# вернемся в каталог с репозиторием first_project
cd ../first_project

# создадим лог-файл
touch events.log
# проверим статус файлов
git status
# создадим файл для настроек игнора
nano .gitignore
# добавим в этот файл имя игнорируемого файла
 events.log

# снова проверим статус файлов
git status
# добавим все изменения в индекс
git add .
# снова проверим статус файлов
git status

# сделаем новый коммит
git commit -m "add .gitignore file"
# проверим список коммитов
git log --oneline


##	шаблоны (*, ?)
# создадим еще пару файлов с логами
touch events_123.log e_123123.log
# проверим, что они появились
ls
# проверим гит-статус
git status
# откроем файл .gitignore, чтобы добавить в него новый шаблон
nano .gitignore
 *.log

# снова проверим гит-статус
git status
# добавим все изменения в индекс
git add .
git status
# добавим новые изменения в прошлый коммит
git commit --amend --no-edit
git status
git log --oneline


## игнор папки
# создадим новую папку с указанным именем
mkdir logs
# переместим все файлы с расширением 'log' в эту папку
mv *.log logs
ls
ls logs/
git status
# откроем файл .gitignore, чтобы добавить в него новый шаблон
nano .gitignore
  logs/*

git status
git add .
git status
git commit --amend --no-edit
git log --oneline
git status
ls


## отмена игнора (“!”)
#
touch rare_critical_errors.log
ls
git status
nano .gitignore
  !rare_critical_errors.log

git status
git add .
git status
git commit --amend --no-edit
git status
git log –-oneline
git log --stat -1

## форсированное добавление
## (это редкий сценарий)

touch debug.log
ls
git status
# принудительно добавляем в индекс файл debug.log
git add -f debug.log
git status
git commit -m "force adding debug.log"
git status
git log --oneline


## глобальные настройки
# указываем глобальную настройку для пути к файлу .gitignore
git config --global core.excludesfile ~/.gitignore_global
# создаем сам файл по указанному пути
touch ~/.gitignore_global
nano ~/.gitignore_global
  *.tmp

ls
git status
# создаем тестовый файл (должен игнорироваться)
touch tempfile.tmp
git status

# добавляем новые изменения в файловой системе локального репозитория
touch somefile.txt

# добавляем изменения в индекс
git add .

# делаем новый коммит
git commit

# проверяем, что коммит появился
git status

# отправляем наш коммит на удаленный репозиторий
git push
