from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar


class Sized(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f"{self.name}"

    def array(self, len: int) -> "Sized":
        return Sized(f"{self.name}[{len}]", self.size * len)


qword = Sized("QWORD", 8)
dword = Sized("DWORD", 4)
word = Sized("WORD", 2)
byte = Sized("BYTE", 1)
char = Sized("char", 1)


STACK_FRAME = [
    ("input", char.array(64)),
    ("cypher_key", char.array(51)),
    ("<undef>", byte.array(9)),
    ("random2", dword),
    ("random1", dword),
    ("<undef>", byte),
    ("<undef>", byte),
    ("<undef>", byte),
    ("fix", char),
    ("secret3", dword),
    ("secret2", dword),
    ("secret1", dword),
    ("len", dword),
    ("j", dword),
    ("i", dword),
    ("<undef>", qword),
    ("saved_rbp", qword),
    ("ret_addr", qword),
]
