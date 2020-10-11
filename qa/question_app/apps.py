from django.apps import AppConfig


class QuestionAppConfig(AppConfig):
    name = 'question_app'
    def ready(self):
        import question_app.signals

