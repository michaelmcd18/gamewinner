from _pytest.python import Metafunc

from gamewinner.games.bracket import Bracket
from gamewinner.printers import Printer, available_printers


def pytest_generate_tests(metafunc: Metafunc) -> None:
    fixture = "printer"
    if fixture in metafunc.fixturenames:
        metafunc.parametrize(fixture, available_printers, scope="function")


class TestPrinters:
    def test_print(self, strategized_bracket: Bracket, printer: Printer) -> None:
        bracket = strategized_bracket
        bracket.play()
        printer.print(bracket)
