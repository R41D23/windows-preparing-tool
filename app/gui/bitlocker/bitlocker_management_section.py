from app.gui.inputs.button import DefaultRadioButton
from app.logic.bitlocker.bitlocker_management import BitlockerManagement


class CreateBitlockerManagementSection:
    def __init__(self, root):

        self.root = root

        self.bitlocker_management = BitlockerManagement(self.root)

        self.bitlocker_management.check_on_startup()

        self.deactivate_bitl = DefaultRadioButton(
            self.root,
            text="Deaktywacja Bitlockera",
            variable=self.bitlocker_management.bitl_set_state,
            value="deactivate",
            x=30,
            y=430,
        )

        self.activate_bitl = DefaultRadioButton(
            self.root,
            text="Aktywacja Bitlockera",
            variable=self.bitlocker_management.bitl_set_state,
            value="activate",
            x=30,
            y=460,
        )

        self.activate_bitl_fast = DefaultRadioButton(
            self.root,
            text="Szybka aktywacja Bitlockera (szybkie on/off)",
            variable=self.bitlocker_management.bitl_set_state,
            value="fastactivate",
            x=30,
            y=490,
        )
