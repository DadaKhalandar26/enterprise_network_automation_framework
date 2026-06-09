import os
from datetime import datetime
from ..core.connection import DeviceConnectionHandler
from ..config.settings import Env_Setting
from ..utils import logger

log = logger.get_logger("Services_Back-UP_Logger")

class BackUp:
    """Service for collecting and storing device backups."""

    def __init__(
        self,
        Netbox_url,
        Netbox_token,
        user_name,
        Password,
        enbable_password: str | None
    ):
        """Initialize backup service dependencies and backup storage settings."""
        self.Netbox_url = Netbox_url
        self.Netbox_token = Netbox_token
        self.user_name = user_name
        self.password = Password
        self.enable_password = enbable_password
        self.Connect_to = DeviceConnectionHandler(
            Netbox_url=self.Netbox_url,
            Netbox_token=self.Netbox_token,
            user_name=self.user_name,
            Password=self.password,
            enbable_password=self.enable_password
        )
        self.Root_Device_BackUP_Folder = "reports/backups/devices"
        log.info(
            f"Initialized backup service for device backups with NetBox URL '{self.Netbox_url}'."
        )

    def device_back_up_by_name(self, device) -> bool:
        """Perform the backup for the specified device and persist it to disk."""
        log.info(f"Starting backup run for device '{device}'.")

        try:
            # Run the configured connection handler to retrieve backup output.
            backup_output = self.Connect_to.execute_command(command="show run", device_name=device)
            execution_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            if backup_output:
                log.info("Backup output received from the connection handler.")
                device_back_up_folder = f"{self.Root_Device_BackUP_Folder}/{device}"
                if os.path.exists(device_back_up_folder):
                    log.info(
                        f"Device backup folder already exists for '{device}'; reusing existing folder."
                    )
                    with open(f"{device_back_up_folder}/{device}-{execution_time}.txt", 'w') as f:
                        f.write(backup_output)
                else:
                    log.info(
                        f"Device backup folder does not exist for '{device}'; creating new folder."
                    )
                    os.makedirs(device_back_up_folder, exist_ok=True)
                    with open(f"{device_back_up_folder}/{device}-{execution_time}.txt", 'w') as f:
                        f.write(backup_output)
                log.info(f"Backup completed successfully for device '{device}'.")
                return True

            log.warning(
                f"No backup output available for device '{device}'; backup not persisted."
            )
            return False
        except TypeError as e:
            log.error(f"TypeError during backup for device '{device}': {e}")
        except AttributeError as e:
            log.error(f"AttributeError during backup for device '{device}': {e}")
        except Exception as e:
            log.error(f"Unexpected error during backup for device '{device}': {e}")


if __name__ == "__main__":
    Setting = Env_Setting()
    get = BackUp(Netbox_url=Setting.NETBOX_DEV_URL, Netbox_token=Setting.NETBOX_DEV_TOKEN_RW.get_secret_value(), user_name=Setting.DEVICE_USERNAME, Password=Setting.DEVICE_PASSWORD.get_secret_value(), enbable_password=None)
    do_back = get.device_back_up_by_name(device="IN-HYD-LAB1-ACC-01")
    if do_back:
        print("Back-UP Successfull.")

