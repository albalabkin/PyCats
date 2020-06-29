import os

from common._libs.config_parser.config_dto import APIValidationDTO, WebDriverSettingsDTO
from common._libs.config_parser.config_parser import ParseConfig
from common._libs.helpers.singleton import Singleton


class ConfigManager(metaclass=Singleton):
    DEFAULT_CONFIG_PATH = f"{os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../config/config.ini')}"

    def __init__(self, path_to_config=None):
        self.path_to_config = path_to_config or self.DEFAULT_CONFIG_PATH
        self.config = ParseConfig(self.path_to_config)
        self.cli_update = None

    def get_config(self):
        return self.config

    def update_config(self, custom_args):
        self.config = ParseConfig(self.path_to_config, custom_args)

    def get_api_validations(self) -> APIValidationDTO:
        settings = self.config.api_settings.api_validation_settings
        return APIValidationDTO(settings.validate_status_code, settings.validate_headers,
                                settings.validate_body, settings.validate_is_field_missing)

    def get_webdriver_settings(self) -> WebDriverSettingsDTO:
        settings = self.config.web_settings
        return WebDriverSettingsDTO(settings.webdriver_folder, settings.webdriver_default_wait_time,
                                    settings.webdriver_implicit_wait_time, settings.selenium_server_executable,
                                    settings.chrome_driver_name, settings.firefox_driver_name, settings.browser,
                                    settings.driver_path)