"""
Abstract Factory:

Provides an interface for creating families of related UI objects (e.g., Screen, Button, TextBox) without specifying
their concrete classes.

Common uses: when you need to support multiple platforms/themes ensure components stay consistent
within the same family, and swap implementations by changing only the factory.
"""


from abc import ABC, abstractmethod


class IScreen(ABC):
    @abstractmethod
    def render_screen(self):
        pass


class IButton(ABC):
    @abstractmethod
    def render_button(self):
        pass


class ITextBox(ABC):
    @abstractmethod
    def render_textbox(self):
        pass


class IGUIFactory(ABC):
    @abstractmethod
    def create_screen(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass


# Concrete Products: Windows

class WindowsScreen(IScreen):
    def render_screen(self):
        print("Rendering Windows screen")


class WindowsButton(IButton):
    def render_button(self):
        print("Rendering Windows button")


class WindowsTextBox(ITextBox):
    def render_textbox(self):
        print("Rendering Windows textbox")


# Concrete Products: MacOS

class MacOSScreen(IScreen):
    def render_screen(self):
        print("Rendering MacOS screen")


class MacOSButton(IButton):
    def render_button(self):
        print("Rendering MacOS button")


class MacOSTextBox(ITextBox):
    def render_textbox(self):
        print("Rendering MacOS textbox")


# Concrete Products: Linux

class LinuxScreen(IScreen):
    def render_screen(self):
        print("Rendering Linux screen")


class LinuxButton(IButton):
    def render_button(self):
        print("Rendering Linux button")


class LinuxTextBox(ITextBox):
    def render_textbox(self):
        print("Rendering Linux textbox")


# Concrete Factories

class WindowsFactory(IGUIFactory):
    def create_screen(self):
        return WindowsScreen()

    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()


class MacOSFactory(IGUIFactory):
    def create_screen(self):
        return MacOSScreen()

    def create_button(self):
        return MacOSButton()

    def create_textbox(self):
        return MacOSTextBox()


class LinuxFactory(IGUIFactory):
    def create_screen(self):
        return LinuxScreen()

    def create_button(self):
        return LinuxButton()

    def create_textbox(self):
        return LinuxTextBox()


if __name__ == "__main__":

    windows_factory = WindowsFactory()
    windows_screen = windows_factory.create_screen()
    windows_button = windows_factory.create_button()
    windows_textbox = windows_factory.create_textbox()

    windows_screen.render_screen()
    windows_button.render_button()
    windows_textbox.render_textbox()

    macos_factory = MacOSFactory()
    macos_screen = macos_factory.create_screen()
    macos_button = macos_factory.create_button()
    macos_textbox = macos_factory.create_textbox()

    macos_screen.render_screen()
    macos_button.render_button()
    macos_textbox.render_textbox()

    linux_factory = LinuxFactory()
    linux_screen = linux_factory.create_screen()
    linux_button = linux_factory.create_button()
    linux_textbox = linux_factory.create_textbox()

    linux_screen.render_screen()
    linux_button.render_button()
    linux_textbox.render_textbox()
