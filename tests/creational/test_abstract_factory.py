from patterns.creational import IGUIFactory, WindowsFactory, MacOSFactory, LinuxFactory
from patterns.creational.abstract_factory import WindowsButton, WindowsTextBox, WindowsScreen

def test_windows_factory_creates_expected_components():
    factory = WindowsFactory()
    screen = factory.create_screen()
    button = factory.create_button()
    textbox = factory.create_textbox()

    assert isinstance(screen, WindowsScreen)
    assert isinstance(button, WindowsButton)
    assert isinstance(textbox, WindowsTextBox)