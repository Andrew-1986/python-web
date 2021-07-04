class Meta(type):
    class_number = 0

    def __new__(cls, *args):
        instance = type.__new__(cls, *args)
        instance.class_number = cls.class_number
        cls.class_number += 1
        return instance


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


def main():
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)

    for i in range(10):
        my_cls = Meta(f'{i}', (), {})
        print(my_cls.class_number)


if __name__ == '__main__':
    main()