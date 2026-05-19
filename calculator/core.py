"""计算器核心模块。

提供基础的加减乘除运算，所有函数均带有类型注解和文档字符串。
"""


def add(a: float, b: float) -> float:
    """加法运算。

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两数之和
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """减法运算。

    Args:
        a: 被减数
        b: 减数

    Returns:
        两数之差
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """乘法运算。

    Args:
        a: 第一个因数
        b: 第二个因数

    Returns:
        两数之积
    """
    return a * b


def divide(a: float, b: float) -> float:
    """除法运算。

    Args:
        a: 被除数
        b: 除数

    Returns:
        商

    Raises:
        ValueError: 当除数为零时
    """
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(base: float, exponent: float) -> float:
    """幂运算。

    Args:
        base: 底数
        exponent: 指数

    Returns:
        base 的 exponent 次方

    Raises:
        ValueError: 当底数为 0 且指数为负数时
    """
    if base == 0 and exponent < 0:
        raise ValueError("零不能取负数次幂")
    return base**exponent
