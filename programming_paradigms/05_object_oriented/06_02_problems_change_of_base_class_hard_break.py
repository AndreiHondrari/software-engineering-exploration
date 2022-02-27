"""
Proof that if a subclass depends on members of the superclass,
the superclass becomes inflexible due to subclasses that depend on its members.
Any change in the superclass could result in some hard errors for the user of
that class.
"""

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
    hard breaking error
    """

    def __init__(self) -> None:
        self._messages: List[str] = []
        self._last_flushed_index: int = 0

    def flush_to_file(self) -> None:
        print("flushing to file ...")
        for i in range(self._last_flushed_index, len(self._messages)):
            print("to file:", self._messages[i])

        self._last_flushed_index = len(self._messages)

    def report(self, message: str) -> None:
        print("reporting:", message)
        self._messages.append(message)


class EventLogger(FileLogger):

    def report_event(self, event: Event) -> None:
        """
        Here we assume that we have a flush_to_file function at our
        disposal
        """
        self.report(f"[{event.code.name}] {event.description}")

        # We are using it in the subclass.
        # The superclass reimplementation will remove this function
        # resulting in this call to be illegal
        self.flush_to_file()


def alter_class(klass: type) -> None:

    def new_report(self, message: str) -> None:
        # Message reporting part
        print("reporting:", message)
        self._messages.append(message)

        # File flushing part (now incorporated in the report method)
        print("flushing to file ...")
        for i in range(self._last_flushed_index, len(self._messages)):
            print("to file:", self._messages[i])

        self._last_flushed_index = len(self._messages)

    del klass.flush_to_file
    klass.report = new_report


def main() -> None:
    hprint("Non-altered event logger test")
    elogger1 = EventLogger()
    elogger1.report_event(Event(EventCode.DEFCON_1, "giovanni georgio"))
    elogger1.report_event(Event(EventCode.DEFCON_3, "salvatore ganacci"))

    hprint("Altered event logger test")

    """
    Let's change the implementation of the FileLogger class, so that
    flush_to_file is removed and the code of the method is incorporated
    instead in the report method.
    """
    alter_class(FileLogger)

    elogger2 = EventLogger()
    try:
        elogger2.report_event(Event(EventCode.DEFCON_2, "gandalf"))
    except AttributeError as aerr:
        print("AttributeError caught:", str(aerr))

    try:
        elogger2.report_event(Event(EventCode.DEFCON_3, "wizard of oz"))
    except AttributeError as aerr:
        print("AttributeError caught:", str(aerr))

    try:
        elogger2.report_event(Event(EventCode.DEFCON_1, "john cena"))
    except AttributeError as aerr:
        print("AttributeError caught:", str(aerr))


if __name__ == "__main__":
    main()
