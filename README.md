### Домашняя работa 19.2
#### Задание 1
Для начала работы над задачей выполните первые шаги:

 Настройте виртуальное окружение.
 Создайте новый Django-проект.
#### Задание 2
После успешного создания проекта сделайте первую настройку. Для этого:
Создайте первое приложение с названием catalog.
Внесите начальные настройки проекта.
Сделайте настройку урлов (URL-файлов) для нового приложения.
#### Задание 3
Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.
Для создания шаблонов лучше использовать UIkit Bootstrap. Это удобный набор элементов, которые уже стилизованы и готовы к использованию. UIkit Bootstrap помогает избежать самостоятельной верстки макетов.
Если возникнут проблемы при создании собственного интерфейса, возьмите за основу данный шаблон: https://github.com/oscarbotru/.

#### Задание 4
В приложении в контроллере реализуйте два контроллера:
 Контроллер, который отвечает за отображение домашней страницы.
 Контроллер, который отвечает за отображение контактной информации.

### Домашняя работa 21.1
#### Задание 1
Переведите имеющиеся контроллеры с FBV на CBV.

#### Задание 2
Создайте новую модель блоговой записи со следующими полями:

заголовок;
slug (реализовать через CharField);
содержимое;
превью (изображение);
дата создания;
признак публикации;
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

#### Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

При открытии отдельной статьи увеличивать счетчик просмотров.
Для решения этой задачи можно воспользоваться переопределением метода 
get_object() в DetailView

Отфильтруйте статьи блога с помощью ORM-запроса.

При создании динамически формировать slug name для заголовка.
Для решения этой задачи можно воспользоваться переопределением метода 
form_valid() в CreateView

После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
Для решения этой задачи можно воспользоваться переопределением метода 
get_success_url() в UpdateView

### Домашняя работa 22.1
#### Задание 1
Для модели продуктов реализуйте механизм CRUD, задействовав модуль django.forms
Условия для пользователей:
могут создавать новые продукты,
не могут создавать продукты с запрещенными словами в названии и описании.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

#### Задание 2
Добавьте новую модель «Версия», которая должна содержать следующие поля:
продукт,
номер версии,
название версии,
признак текущей версии.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

#### Задание 3
Добавьте реализацию работы с формами для версий продукта.
В один момент может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, что пользователь в качестве активной версии указал только одну
