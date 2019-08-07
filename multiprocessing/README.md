# Процесси та потоки в Python

## Процес

 - Що таке процесс 
    https://habr.com/ru/post/423049/
    https://www.tecmint.com/linux-process-management/
    
 - подивитися запущені python процесси 
 `ps -aux | grep python` 
 - порахувати кількість python процессів
 `ps -aux | grep python |  wc -l`

 створити процесс демон 
 https://dpbl.wordpress.com/2017/02/12/a-tutorial-on-python-daemon/
## Поток
  - Що таке поток
  - Порахувати кількість потоків для процессу  
 `ps hH p <pid> | wc -l`

## Асинхронність

    https://habr.com/ru/post/337420/
    
    
## I\O bound and CPU bound 
    https://www.quora.com/How-do-you-know-if-a-web-app-is-IO-bound-or-CPU-bound-For-example-what-are-the-instance-types-of-Amazon-and-Dropbox