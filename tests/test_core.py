"""计算器核心模块测试。

覆盖加减乘除和幂运算的正常路径与边界情况。
"""

import pytest

from calculator.core import add, subtract, multiply, divide, power

# ==================== 加法测试 ====================


class TestAdd:
    """加法测试。"""

    def test_positive_numbers(self) -> None:
        assert add(2, 3) == 5

    def test_negative_numbers(self) -> None:
        assert add(-1, -2) == -3

    def test_mixed_numbers(self) -> None:
        assert add(-1, 1) == 0

    def test_float(self) -> None:
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_zero(self) -> None:
        assert add(0, 0) == 0


# ==================== 减法测试 ====================


class TestSubtract:
    """减法测试。"""

    def test_positive_result(self) -> None:
        assert subtract(5, 3) == 2

    def test_negative_result(self) -> None:
        assert subtract(3, 5) == -2

    def test_same_numbers(self) -> None:
        assert subtract(7, 7) == 0

    def test_float(self) -> None:
        assert subtract(0.5, 0.3) == pytest.approx(0.2)


# ==================== 乘法测试 ====================


class TestMultiply:
    """乘法测试。"""

    def test_positive_numbers(self) -> None:
        assert multiply(3, 4) == 12

    def test_negative_numbers(self) -> None:
        assert multiply(-2, -3) == 6

    def test_mixed_signs(self) -> None:
        assert multiply(-2, 3) == -6

    def test_by_zero(self) -> None:
        assert multiply(5, 0) == 0

    def test_float(self) -> None:
        assert multiply(0.1, 0.2) == pytest.approx(0.02)


# ==================== 除法测试 ====================


class TestDivide:
    """除法测试。"""

    def test_normal_division(self) -> None:
        assert divide(10, 2) == 5

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="除数不能为零"):
            divide(10, 0)

    def test_negative_division(self) -> None:
        assert divide(-6, 3) == -2

    def test_float_result(self) -> None:
        assert divide(7, 2) == 3.5

    def test_integer_result(self) -> None:
        assert divide(9, 3) == 3.0


# ==================== 幂运算测试 ====================


class TestPower:
    """幂运算测试。"""

    def test_positive_exponent(self) -> None:
        assert power(2, 3) == 8

    def test_zero_exponent(self) -> None:
        assert power(5, 0) == 1

    def test_negative_exponent(self) -> None:
        assert power(2, -1) == pytest.approx(0.5)

    def test_float_base(self) -> None:
        assert power(1.5, 2) == pytest.approx(2.25)

    def test_zero_base_negative_exponent(self) -> None:
        with pytest.raises(ValueError, match="零不能取负数次幂"):
            power(0, -1)
