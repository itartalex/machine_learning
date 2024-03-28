# Lesson 7
# Домашнее задание
# Проектируем иерархию классов для работы с файлами
#
# Цель:
#  В этом ДЗ вы напишите базовые и конкретные классы для предметной области.
#  И оцените перспективы добавления нового функционала в полученную иерархию.
#
# В проекте мы работаем с медиа-файлами (аудио, видео, фото)
# есть некоторый общий набор данных о файле, необходимый для реализации бизнес-логики
# (имя, размер, дата создания, владелец...)
# Для каждого типа медиа-фалов есть свой набор мета-данных
# попробуйте написать классы для работы с медиа-файлами (они будут основой для пользовательского кода остальных команд)
# Приведите примеры кода - как можно создать, обновить, удалить или провести какое-нибудь действие
# (конвертация, извлечение фич) над файлом (можно без реализации деталей)
# Попробуйте дописать классы для работы с файлами, расположенными не на локальном диске
# (облако, удаленный сервер, s3-like storage)
# Попробуйте ответить на вопросы: много ли кода придется дописать / переписать при добавлении новых типов файлов
# и способов их хранения?
# Суть задания - именно проектирование классовой иерархии, а не реализация самой логики, поэтому достаточно, например,
# просто объявить метод .save(...) и в комментарии уточнить - что он должен делать, без конкретной релаизации

class BaseMedia:
    """
    This is base class for media files
    """

    def __init__(self):
        self.name = None
        self.path = None
        self.size = None
        self.create_date = None
        self.owner = None

    def create_file(self, name, path, size, create_date, owner):
        """ Creating a file """
        self.name = name
        self.path = path
        self.size = size
        self.create_date = create_date
        self.owner = owner
        raise NotImplementedError

    def save_file(self, name, path):
        """ Saving a file """
        self.name = name
        self.path = path
        raise NotImplementedError

    def delete_file(self, name, path):
        """ Deleting a file """
        self.name = name
        self.path = path
        raise NotImplementedError

    def open_file(self, name, path):
        """ Opening a file """
        self.name = name
        self.path = path
        raise NotImplementedError

    def __str__(self):
        return f"name: {self.name} path: {self.path} size: {self.size} create date: {self.create_date} owner: {self.owner}"


class FileAudio(BaseMedia):
    """
    This is a class for local and cloud audio files
    """

    def __init__(self):
        super.__init__()
        self.path_cloud = None

    def create_file(self, name, path, size, create_date, owner):
        """ Creating a local audio file """
        self.name = name
        self.path = path
        self.size = size
        self.create_date = create_date
        self.owner = owner
        print(f'Create a audio file {self.name} on local path {self.path}')

    def create_file_cloud(self, name, path_cloud, size, create_date, owner):
        """ Creating a cloud audio file """
        self.name = name
        self.path_cloud = path_cloud
        self.size = size
        self.create_date = create_date
        self.owner = owner
        print(f'Create a audio file {self.name} on cloud path {self.path_cloud}')


class FileVideo(BaseMedia):
    """
    This is class for video file
    """

    def open_file(self, name, path):
        """ Opening a video file """
        self.name = name
        self.path = path
        print(f'Open a video file {self.name}')


class FilePhoto(BaseMedia):
    """
    This is class for photo
    """

    def delete_file(self, name, path):
        """ Deleting a photo file """
        self.name = name
        self.path = path
        print(f'Delete a photo file {self.name}')
