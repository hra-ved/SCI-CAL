from PyQt6.QtCore import QSettings, QCoreApplication


class Settings(QSettings):
    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

        # settings identification
        QCoreApplication.setApplicationName("SCI-CAL X-PRO") # name
        QCoreApplication.setOrganizationName("MIOC") # WIN / Linux
        QCoreApplication.setOrganizationDomain("mioc.hr") # macOS / iOS
        QCoreApplication.setApplicationName("SCI-CAL X-PRO")  # name
        QCoreApplication.setOrganizationName("MIOC")  # WIN / Linux
        QCoreApplication.setOrganizationDomain("mioc.hr")  # macOS / iOS
        if self.read_settings("Language", "Language") is None or self.read_settings("Language", "Language") == "None":
            settings = QSettings()
            settings.beginGroup("Language")
            settings.setValue("language", "en")
            settings.endGroup()

    @staticmethod
    def store_setting(group, setting, value):
        settings = QSettings()
        settings.beginGroup(group)
        settings.setValue(setting, value)
        settings.endGroup()

    @staticmethod
    def read_settings(group, setting):
        settings = QSettings()
        settings.beginGroup(group)
        try:
            s_value = settings.value(setting).toString()
        except AttributeError:
            s_value = settings.value(setting)
        settings.endGroup()
        return str(s_value)
