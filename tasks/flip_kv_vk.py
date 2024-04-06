from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.
    Например,
    flip_kv_vk({
        'tokyo': 'Токио',
        'moscow': 'Москва',
    }) == {
        'Токио': 'tokyo',
        'Москва': 'moscow',
    }
    """
    ans = dict()

    for key, value in d.items():
        ans[value] = key

    return ans


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - массив ключей конфликтующих
    значений.
    Например,
    flip_kv_vk({
        'Санкт-Петербург': '+3',
        'Москва': '+3',
    }) == {
        '+3': ['Москва', 'Санкт-Петербург'],
    }
    """
    ans = dict()
    anss = dict()

    for key, value in d.items():
        ans[value] = list()
            
    for key, value in d.items():
        ans[value].append(key)

    for key, value in ans.items():
        if len(value) > 1:
            anss[key] = value
    if len(anss) == 0:  
        return ans
    return anss
