import logging
from sqlalchemy import create_engine, select
from core.models.base import Base
from core.models import Profession, Tag, Course, course_tags, Competence, competence_tags, create_session, Session, database, discipline_courses, Discipline, Teacher, course_teachers



professions_tags = {
    "Программист высокопроизводительных вычислительных систем": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "Pandas", "NumPy", "SciPy",
        "Линейная алгебра", "Теория вероятностей и математическая статистика",
        "Многослойный персептрон", "Сверточные нейронные сети (CNN)", "Автоэнкодеры",
        "C/C++", "Python"
    ],
    "Специалист по искусственному интеллекту": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "Caffe", "Многослойный персептрон",
        "Сверточные нейронные сети", "Рекуррентные нейронные сети", "Долгая краткосрочная память",
        "OpenCV", "Scikit-image", "Dlib", "Оптический поток", "Детектирование объектов",
        "Классификация изображений"
    ],
    "Системный программист": [
        "Bash", "C/C++", "Linux", "Docker", "Kubernetes", "POSIX", "Системные вызовы",
        "Работа с процессами и потоками", "Database", "SQL", "NoSQL", "Операционные системы",
        "Администрирование"
    ],
    "Разработчик интеллектуальных систем управления динамической диспетчеризацией": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "Matplotlib",
        "Сверточные нейронные сети (CNN)", "Рекуррентные нейронные сети (RNN)",
        "Системы линейных уравнений и матрицы", "Математическая статистика", "Python",
        "SQL", "Docker"
    ],
    "Системный аналитик": [
        "BPMN", "UML", "DFD", "Бизнес-планировние", "Системы управления", "Риск-менеджмент"
    ],
    "Ментор стартапов": [
        "Технологии продаж", "Социальные коммуникации", "Эмоциональный интеллект",
        "Деловой этикет", "Бизнес-планирование", "Маркетинг", "Риск-менеджмент"
    ],
    "Специалист по администрированию сети": [
        "Linux", "Ubuntu", "Linux Mint", "Debian", "Fedora", "openSUSE", "CentOS", "FreeBSD",
        "Solaris", "Arch Linux", "Apache", "Nginx", "IIS", "HTTP/HTTPS", "TCP/IP", "SMTP/POP/IMAP",
        "FTP/SFTP", "DNS", "WebSocket", "CDN", "Server Security", "Content Security Policy", "CSP",
        "CORS", "IPC", "OWASP", "Memcached", "Hazelcast", "Apache Ignite", "Bash",
        "Basic Terminal Commands", "Zsh", "PowerShell", "Docker", "Kubernetes", "LXC",
        "Server Sent Events (SSE)", "Service Workers", "Shadow DOM", "Web Sockets", "Service mesh",
        "Storage", "Брокеры сообщений", "Kafka", "RabbitMQ", "ActiveMQ"
    ],
    "Специалист по автоматизации банковского дела": [
        "SQL", "PostgreSQL", "Kafka", "Docker", "Hibernate"
    ],
    "Руководитель проектов в области информационных технологий": [
        "Canvas", "Cawemo", "Jira", "Trello", "SmartService", "Asana", "Мегаплан",
        "Битрикс24", "Basecamp", "Яндекс.Трекер", "GanttPro", "Worksection", "MeisterTask",
        "Wrike"
    ],
    "Проектировщик промышленной робототехники": [
        "PIC (Peripheral Interface Controller)", "AVR", "ARM", "Raspberry Pi", "LoRa", "MCS51",
        "ESP32", "MSP430", "STM32", "Raspberry Pi", "BeagleBone", "Odroid", "C/C++", "ассемблер",
        "Arduino"
    ],
}


courses_tags = {
    "Нейронные сети и компьютерное зрение": [
        "Нейронные сети", "OpenCV", "TensorFlow", "Keras", "Caffe", "PyTorch", 
        "scikit-image", "Dlib", "TorchVision", "PIL"
    ],
    "UX/UI дизайн": [
        "УЦСБ", "RUS", "ТK"
    ],
    "Программирование сложных приложений на Python": [
        "Python", "SQLAlchemy", "PyMySQL", "RESTAPI", "Pandas", "Numpy", 
        "Matplotlib", "Seaborn", "Caffe"
    ],
    "JavaScript углублённый курс": [
        "JavaScript", "React", "Angular", "Vue.js", "Ember.js", "Backbone.js", 
        "Svelte", "Aurelia", "Preact"
    ],
    "Python для интеллектуального анализа данных": [
        "Python", "Data Science", "Jupyter Notebook", "Google Colaboratory", 
        "Kaggle Kernel", "Pandas", "Numpy", "Scikit-Learn", "Scipy", "Seaborn", 
        "Matplotlib", "Plotly", "Математическая Статистика", "Линейная Алгебра", "Git"
    ],
    "Основы тестирования программного обеспечения": [
        "Java", "SQL", "MySQL", "MariaDB", "Amazon Aurora", "Microsoft SQL Server", 
        "MS SQL", "Oracle", "PostgreSQL", "SAP HANA", "SQLite", "T-SQL", "Teradata", 
        "DevTools", "Lighthouse", "Postman"
    ],
    "Базы данных. Углубленный курс": [
        "SQL", "MySQL", "MariaDB", "Amazon Aurora", "Microsoft SQL Server", "MS SQL", 
        "Oracle", "PostgreSQL", "SAP HANA", "SQLite", "T-SQL", "Teradata"
    ],
    "Анализ естественного языка (Онлайн, SkillFactory)": [
        "NLP", "НейронныеСети"
    ],
    "Тестирование программного обеспечения": [
        "SQL", "MySQL", "MariaDB", "Amazon Aurora", "Microsoft SQL Server",
        "MS SQL", "Oracle", "PostgreSQL", "SAP HANA", "SQLite", "T-SQL", "Teradata",
        "DevTools", "Lighthouse", "Postman"
    ],
    "Курс по разработке мобильных приложений (Android)": [
        "Android", "Java", "Kotlin", "XML", "Android Studio", "Firebase", "SQLite", "REST API"
    ],
    "Веб-разработка с использованием Django (Python)": [
        "Python", "Django", "HTML", "CSS", "JavaScript", "Bootstrap", "PostgreSQL", "SQLite", "Git"
    ],
    "Машинное обучение в бизнесе (Coursera)": [
        "Machine Learning", "Data Science", "Python", "Scikit-Learn", "Pandas", "NumPy", 
        "Matplotlib", "Seaborn", "Jupyter Notebook", "Google Colaboratory"
    ],
}


competences_tags = {
    "Умение работать с нейронными сетями": [
        "Нейронные сети", "OpenCV", "TensorFlow", "Keras", "Caffe", "PyTorch", 
        "scikit-image", "Dlib", "TorchVision", "PIL"
    ],
    "Применение современных средств автоматизации в производстве": [
        "PowerMill"
    ],
    "Разработка приложений для iOS": [
        "SwiftUI", "Xcode", "Core Data", "Combine", "Storyboards"
    ],
    "Проведение тестирования на проникновение": [
        "CDN", "Server Security", "Content Security Policy", "CSP", "CORS", 
        "IPC", "OWASP"
    ],
    "Умение создавать удобные и эстетичные интерфейсы": [
        "Sketch", "Adobe XD", "Figma", "InVision", "Axure RP", "Balsamiq", 
        "UsabilityHub", "Crazy Egg", "Hotjar", "Optimal Workshop", 
        "Adobe After Effects", "Zeplin"
    ],
    "Написание автоматизированных тестов для WEB и API с использованием Java": [
        "Java", "SQL", "MySQL", "MariaDB", "Amazon Aurora", "Microsoft SQL Server", 
        "MS SQL", "Oracle", "PostgreSQL", "SAP HANA"
    ],
    "Эффективное управление ИТ-проектами": [
        "Проектное Управление"
    ],
    "Умение кодировать информацию": [
        "SSL/TLS", "IPsec", "SSH", "VPN", "WPA/WPA2", "Kerberos", "S/MIME", "PGP"
    ],
    "Умение анализировать и решать задачи, возникающие при разработке решений на современных системах управления базами данными": [
        "SQL", "MySQL", "MariaDB", "Amazon Aurora", "Microsoft SQL Server", "MS SQL", 
        "Oracle", "PostgreSQL", "SAP HANA", "SQLite", "T-SQL", "Teradata"
    ],
    "Формирование требований по безопасности при разработке ПО": [
        "Authentication Strategies", "Credentials", "JWT", "Notifications", "Payments", 
        "Session Auth", "SSO", "DevTools", "Lighthouse", "Postman"
    ],
    "Способность анализировать архитектуру компьютерных систем": [
        "GitHub", "GitLab", "Bitbucket", "Netify", "Google"
    ],
    "Безопасное и эффективное использование компьютеров и интернет-ресурсов": [
        "GitHub", "GitLab", "Bitbucket", "Netify", "Google"
    ],
}
discipline_courses = { 
    "Программирование": [
        "Анализ естественного языка (Онлайн, SkillFactory)", "UX/UI дизайн"
    ],
    "Анализ данных и искусственный интеллект": [
        "Нейронные сети и компьютерное зрение", "Тестирование программного обеспечения"
    ],   
}
course_teachers = {
    "Васильев Ростислав Вадимович": [
        "Тестирование программного обеспечения", "UX/UI дизайн"
    ],
    "Чернышев Лев Максимович": [
        "Нейронные сети и компьютерное зрение", "Базы данных. Углубленный курс"
    ],
  
}

logging.basicConfig(level=logging.DEBUG)

def insert_data(data: dict[str, list[str]], Model: Profession | Teacher | Competence):
    with create_session(database.DB_URL) as sess:
        sess.insert(map(lambda n: Model(name=n), data.keys()))
        for name, tags in data.items():
            try:
                obj = Model(name=name)
                tags_ = []
                all_tags = []
                alive_tags = sess.query(Tag).where(Tag.name.in_(tags)).all()
                for tag_name in tags:
                    tag = Tag(name=tag_name)
                    if tag not in alive_tags:
                        tags_.append(tag)
                    all_tags.append(tag)
                sess.insert(tags_)
                obj.tags.extend(all_tags)
                sess.commit()
                print(f"Данные успешно добавлены в таблицу {Model.__tablename__}")
            except Exception as e:
                print(f"Ошибка при добавлении данных в таблицу {Model.__tablename__}: {e}")

def insert_disciplines_and_courses(discipline_courses_data: dict):
    with create_session(database.DB_URL) as sess:
        try:
            for discipline_name, course_names in discipline_courses_data.items():
                discipline = Discipline(name=discipline_name)
                for course_name in course_names:
                    course = sess.query(Course).filter_by(name=course_name).first()
                    if course:
                        discipline.courses.append(course)
                    else:
                        print(f"Course '{course_name}' not found")
                sess.add(discipline)
                sess.commit()
                print(f"Discipline '{discipline_name}' successfully added")
        except Exception as e:
            print(f"Error inserting discipline '{discipline_name}': {e}")



def insert_courses_and_teachers(course_teachers_data: dict):
    with create_session(database.DB_URL) as sess:
        try:
            for teacher_name, course_names in course_teachers_data.items():
                teacher = Teacher(name=teacher_name)
                for course_name in course_names:
                    course = sess.query(Course).filter_by(name=course_name).first()
                    if course:
                        teacher.courses.append(course)
                    else:
                        print(f"Course '{course_name}' not found")
                sess.add(teacher)
                sess.commit()
                print(f"Teacher '{teacher_name}' successfully added")
        except Exception as e:
            print(f"Error inserting teacher '{teacher_name}': {e}")


if __name__ == "__main__":
    try:
        engine = create_engine(database.DB_URL)
        Base.metadata.drop_all(engine) 
        Base.metadata.create_all(engine)
        insert_data(professions_tags, Profession)
        insert_data(courses_tags, Course)
        insert_data(competences_tags, Competence)
        insert_disciplines_and_courses(discipline_courses)
        insert_courses_and_teachers(course_teachers)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

