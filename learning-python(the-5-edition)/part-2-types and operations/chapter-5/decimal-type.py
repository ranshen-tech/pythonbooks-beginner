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
print(Decimal("1") / Decimal("7"))
# decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))

print(1999 + 1.333)
print(Decimal("1") / Decimal("7"))
# decimal.getcontext().prec = 2
print(Decimal(1999) + Decimal(1.333))
pay = Decimal(str(1999 + 1.333))
print(pay)


# 小数上下文管理器
print(Decimal("1.00") / Decimal("3.00"))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal("1.00") / Decimal("3.00"))

print(Decimal("1.00") / Decimal("3.00"))
