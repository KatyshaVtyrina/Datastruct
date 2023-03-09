Библиотека Datastruct - разработка пакета, который позволит другим программистам “из коробки” использовать различные структуры данных для эффективной организации работы с данными: их добавления, удаления, хранения и поиска.

 Класс узла `Node` содержит два атрибута:
    - данные 
    (сюда будут записываться любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел

Класс `Stack` одноименная структура данных. 
Экземпляр класса `Stack` инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стеке) узел. Для пустого стека этот атрибут будет содержать `None`.
Метод `push` добавляет данные в стек. 
Метод `pop` удаляет данные из стека.


Класс `Queue` одноименная структура данных. 
Экземпляр класса `Queue` инициализируется двумя атрибутами, хранящими ссылки на начало и конец очереди. Для пустой очереди оба эти атрибута равны `None`.
Метод `enqueue` добавляет данные в очередь. 
Метод `dequeue` удаляет данные из очереди.


Класс `LinkedList` односвязный список.
Инициализируется пустым. Хранит ссылки на начало (head) и конец(tail) списка. Могут храниться только словари, в который есть ключ 'id'.
Метод `insert_beginning` добавляет элемент в начало списка.
Метод `insert_at_end` добавляет элемент в конец списка.
Метод `print_ll_` выводит данные односвязного списка.
Метод `to_list` - возвращает список с данными, содержащимися в односвязном списке.
Метод `get_data_by_id(<значение id>)` - возвращает первый найденный в LinkedList словарь с ключом id, значение которого равно переданному в метод значению. 