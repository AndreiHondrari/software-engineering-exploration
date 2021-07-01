import abc


class Element(abc.ABC):

    @abc.abstractmethod
    def accept(self, visitor: 'Visitor') -> None:
        raise NotImplementedError


class Visitor:

    @abc.abstractmethod
    def visit_element_a(self, element: 'ElementA') -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def visit_element_b(self, element: 'ElementB') -> None:
        raise NotImplementedError


class ElementA(Element):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element_a(self)

    def operation_a(self) -> None:
        print("ElementA operating")


class ElementB(Element):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element_b(self)

    def operation_b(self) -> None:
        print("ElementB operating")


class VisitorX(Visitor):

    def visit_element_a(self, element: ElementA) -> None:
        print("VisitorX visits ElementA")
        element.operation_a()

    def visit_element_b(self, element: ElementB) -> None:
        print("VisitorX visits ElementB")
        element.operation_b()


if __name__ == '__main__':
    visitor = VisitorX()

    element_1 = ElementA()
    element_2 = ElementB()

    element_1.accept(visitor)
    element_2.accept(visitor)
