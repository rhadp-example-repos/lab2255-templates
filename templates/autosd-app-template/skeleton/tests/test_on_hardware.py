import logging
import sys

from jumpstarter_testing.pytest import JumpstarterTest


log = logging.getLogger(__name__)


class TestOnHardware(JumpstarterTest):
    selector = "type=virtual"

    def test_boot(self, client):
        """Test the boot process of the device."""
        log.info("Testing boot process")
        client.power.cycle()
        with client.console.pexpect() as console:
            console.logfile_read = sys.stdout.buffer
            console.expect_exact("login:", timeout=120)
            console.sendline("root")
            console.expect_exact("Password:", timeout=10)
            console.sendline("password")
            console.expect_exact("]#", timeout=10)
            console.sendline("uname -a")
            console.expect_exact("]#", timeout=10)
            print(console.before.decode())

            console.sendline("podman images")
            console.expect_exact("]#", timeout=10)
            assert "localhost/app" in console.before.decode()

            console.sendline("systemctl status --no-pager radio.service")
            console.expect_exact("]#", timeout=10)

            console.sendline("podman exec -i systemd-radio radio-client")
            console.expect_exact("Connecting to radio service", timeout=10)

            # test changing volume
            console.sendline("+" * 10)
            console.expect_exact("Volume:  [#####################]", timeout=10)
            console.sendline("-" * 10)
            console.expect_exact("Volume:  [                     ]", timeout=10)
            console.sendline("+" * 5)
            console.expect_exact("Volume:  [##########           ]", timeout=10)

            console.sendline("q")
            console.expect_exact("]#", timeout=10)
