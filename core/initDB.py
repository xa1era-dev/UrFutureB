import logging
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Profession, Tag, Course, course_tags, Competence, competence_tags, create_session



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
logging.basicConfig(level=logging.DEBUG)

session = create_session("postgresql://postgres:postgres@localhost/postgres")

def insert_data(data, Model, session):
    try:
        for name, tags in data.items():
            obj = Model(name=name)
            session.add(obj)
            for tag_name in tags:
                tag = session.query(Tag).filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    session.add(tag)
                obj.tags.append(tag)
        session.commit()
        print(f"Данные успешно добавлены в таблицу {Model.__tablename__}")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении данных в таблицу {Model.__tablename__}: {e}")
        raise e
    finally:
        session.close()

if __name__ == "__main__":
    try:
        insert_data(professions_tags, Profession, session)
        insert_data(courses_tags, Course, session)
        insert_data(competences_tags, Competence, session)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

