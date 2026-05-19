# API 参考

## calculator.core

### add(a, b)

加法运算，返回 `a + b`。

### subtract(a, b)

减法运算，返回 `a - b`。

### multiply(a, b)

乘法运算，返回 `a * b`。

### divide(a, b)

除法运算，返回 `a / b`。当 `b == 0` 时抛出 `ValueError`。

### power(base, exponent)

幂运算，返回 `base ** exponent`。当底数为 0 且指数为负数时抛出 `ValueError`。
