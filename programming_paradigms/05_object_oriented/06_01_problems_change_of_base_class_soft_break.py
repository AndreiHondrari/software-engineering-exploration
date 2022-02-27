import enum
import functools

from typing import List
from collections import namedtuple

hprint = functools.partial(print, "\n#")

Event = namedtuple('Event', ['code', 'description'])


@enum.unique
class EventCode(enum.IntEnum):
    DEFCON_1 = enum.auto()
    DEFCON_2 = enum.auto()
    DEFCON_3 = enum.auto()


class FileLogger:
    """
    Technically the code handling the file flushing should be
    outside of this class, but we are just trying to make a point on
    soft error breaking
    """

    def __init__(self) -> None:
        self._messages: List[str] = []

    def flush_to_file(self) -> None:
        print("flushing to file ...")
        try:
            last_message = self._messages[-1:][0]
            print("to file:", last_message)
        except IndexError:
            pass

    def report(self, message: str) -> None:
        print("reporting:", message)
        self._messages.append(message)
        self.flush_to_file()  # also flushing


class EventLogger(FileLogger):

    def report_event(self, event: Event) -> None:
        """
        Here we assume that reporting will also flush to file immediately
        """
        self.report(f"[{event.code.name}] {event.description}")


def alter_class(klass: type) -> None:

    def new_init(self) -> None:
        self._messages: List[str] = []
        self._last_flushed_index: int = 0

    def new_flush_to_file(self) -> None:
        print("flushing to file ...")
        for i in range(self._last_flushed_index, len(self._messages)):
            print("to file:", self._messages[i])

        self._last_flushed_index = len(self._messages)

    def new_report(self, message: str) -> None:
        print("reporting:", message)
        self._messages.append(message)

    klass.__init__ = new_init
    klass.flush_to_file = new_flush_to_file
    klass.report = new_report


def main() -> None:
    hprint("Non-altered event logger test")
    elogger1 = EventLogger()
    elogger1.report_event(Event(EventCode.DEFCON_1, "giovanni georgio"))
    elogger1.report_event(Event(EventCode.DEFCON_3, "salvatore ganacci"))

    hprint("Altered event logger test")

    """
    Let's change the FileLogger class so that whenever the report is called,
    the flush_to_file is no longer automatically called, but leaving it
    as an option to the user of the class to manually trigger the function.

    This breaks the subclass because, the subclass made an assumption that
    whenever it reports, it will automatically flush to file.
    """

    alter_class(FileLogger)
    elogger2 = EventLogger()
    elogger2.report_event(Event(EventCode.DEFCON_2, "gandalf"))
    elogger2.report_event(Event(EventCode.DEFCON_3, "wizard of oz"))
    elogger2.report_event(Event(EventCode.DEFCON_1, "john cena"))

    print("\nmanually flushing ...")
    elogger2.flush_to_file()


if __name__ == "__main__":
    main()
