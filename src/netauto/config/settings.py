from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Env_Setting(BaseSettings):
    '''
    Load Envernment variables
    '''
    NETBOX_PROD_URL: str = "Netbox prod url did not loaded from env"
    NETBOX_PROD_TOKEN_RW: SecretStr = "Netbox prod token did not loaded from env"

    NETBOX_DEV_URL: str = "Netbox dev url did not loaded from env"
    NETBOX_DEV_TOKEN_RW: SecretStr = "Netbox dev token did not loaded from env"

    DEVICE_USERNAME: str = "Device username did not loaded from env"
    DEVICE_PASSWORD: SecretStr = "Device password did not loaded from env"
    DEVICE_ENABLE_PASSWORD: SecretStr = "Device enable secrate did not loaded from env"

    # Configuration for loading .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


if __name__ == "__main__":
    settings = Env_Setting()

    print("PROD URL:", settings.NETBOX_PROD_URL)
    print("PROD TOKEN:", settings.NETBOX_PROD_TOKEN_RW)
    print("DEV URL:", settings.NETBOX_DEV_URL)
    print("DEV TOKEN:", settings.NETBOX_DEV_TOKEN_RW)

    print("DEVICE USERNAME:", settings.DEVICE_USERNAME)
    print("DEVICE PASSWORD:", settings.DEVICE_PASSWORD)
    print("DEVICE ENABLE SECRATE:", settings.DEVICE_ENABLE_PASSWORD)