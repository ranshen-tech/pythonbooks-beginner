# 小数基础知识
print(0.1 + 0.1 + 0.1 - 0.3)
import decimal
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))

print(Decimal("0.1") + Decimal("0.10") + Decimal("0.10") - Decimal("0.30"))

print(Decimal("0.1") * 3 - Decimal("0.3"))
print(Decimal("0.1") * 3)

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(Decimal.from_float(1.25) - Decimal.from_float(1.25))


# 设置全局小数精度
print(Decimal(1) / Decimal(7))

decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))
