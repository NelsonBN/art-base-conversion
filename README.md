# Base conversion

In the [previous publication](https://github.com/NelsonBN/art-binary-numbers), I talked about binary numbers and how we can convert from binary to decimal and vice versa. But in computer science, it is common to encounter numbers in other bases, like hexadecimal, octal, etc. So, in this publication, I am going to discuss how we can convert from one base to another.


## Numeric systems

* **Binary (Base 2):** Uses only two digits: 0 and 1. It is the fundamental language of computers and digital systems.
  * `0`, `1`
* **Octal (Base 8):** Uses digits from 0 to 7. Although less common nowadays, it was used in older systems.
  * `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`
* **Decimal (Base 10):** The system we use in our daily lives. This is the system most people are familiar with. Contains digits from 0 to 9.
  * `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
* **Hexadecimal (Base 16):** Uses digits from 0 to 9 and letters from A to F. It is widely used in programming and system design.
  * `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `A`, `B`, `C`, `D`, `E`, `F`


## Conversions from decimal to another base

First, we are going to convert from decimal to another base to understand the process.

To convert from decimal to another base, we have to divide the decimal number by the base and get the remainder. Then, we have to divide the result by the base again and get the remainder. We have to repeat this process until the quotient is 0. Then, we have to write the remainders in reverse order.


### From decimal to binary

| Dividend | Divisor | Quotient | Remainder | Position |
|----------|---------|----------|-----------|----------|
| 13       | 2       | 6        | 1         | 4        |
| 6        | 2       | 3        | 0         | 3        |
| 3        | 2       | 1        | 1         | 2        |
| 1        | 2       | 0        | 1         | 1        |

13<sub>(10)</sub> = 1101<sub>(2)</sub>

**Python example**
```python
print(bin(13)) # 0b1101
```


### From decimal to octal

| Dividend | Divisor | Quotient | Remainder | Position |
|----------|---------|----------|-----------|----------|
| 541      | 8       | 67       | 5         | 4        |
| 67       | 8       | 8        | 3         | 3        |
| 8        | 8       | 1        | 0         | 2        |
| 1        | 8       | 0        | 1         | 1        |

541<sub>(10)</sub> = 1035<sub>(8)</sub>

**Python example**
```python
print(oct(541)) # 0o1035
```


### From decimal to hexadecimal

| Dividend | Divisor | Quotient | Remainder | Symbol | Position |
|----------|---------|----------|-----------|--------|----------|
| 3709     | 16      | 231      | 13        | D      | 3        |
| 231      | 16      | 14       | 7         | 7      | 2        |
| 14       | 16      | 0        | 14        | E      | 1        |

3709<sub>(10)</sub> = E7D<sub>(16)</sub>

**Python example**
```python
print(hex(3709)) # 0xe7d
```


### Algorithm

```python
def fromDecimalTo(num: int, base: int) -> str:
    result = ""

    while num > 0:
        remainder = num % base

        if(remainder > 9):
            result = chr(ord('A') + remainder - 10) + result
        else:
            result = str(remainder) + result

        num //= base

    return result
```


## Conversions from another base to decimal

Now, we are going to convert from another base to decimal to understand the process. To convert from another base to decimal, we have to multiply each digit by the base raised to the power of the position of the digit. Then, we have to add all the results.


### From binary to decimal

1101<sub>(2)</sub> = <br>
1 * 2<sup>3</sup> + 1 * 2<sup>2</sup> + 0 * 2<sup>1</sup> + 1 * 2<sup>0</sup> = <br>
8 + 4 + 0 + 1 = <br>
13<sub>(10)</sub>


**Python example**
```python
print(int('1101', 2)) # 13
```


### From octal to decimal

723<sub>(8)</sub> = <br>
7 * 8<sup>2</sup> + 2 * 8<sup>1</sup> + 3 * 8<sup>0</sup> = <br>
448 + 16 + 3 = <br>
467<sub>(10)</sub>

**Python example**
```python
print(int('723', 8)) # 467
```


### From hexadecimal to decimal

Before we convert from hexadecimal to decimal, we have to convert the letters to numbers. Here is the table with equivalences.

| Symbol | Value |
|--------|-------|
| 0      | 0     |
| 1      | 1     |
| 2      | 2     |
| 3      | 3     |
| 4      | 4     |
| 5      | 5     |
| 6      | 6     |
| 7      | 7     |
| 8      | 8     |
| 9      | 9     |
| A      | 10    |
| B      | 11    |
| C      | 12    |
| D      | 13    |
| E      | 14    |
| F      | 15    |

EB9<sub>(16)</sub> = <br>
14 * 16<sup>2</sup> + 11 * 16<sup>1</sup> + 9 * 16<sup>0</sup> = <br>
3584 + 176 + 9 = <br>
3769<sub>(10)</sub>

> NOTE: When a letter appears, we overwrite it with the equivalent number. E.g., E = 14 and B = 11.

Whit this, we can understand the mathematical formula to convert from another base to decimal is `Decimal value = digit_n * b^n + ... + digit_1 * b^1 + digit_0 * b^0`

**Python example**
```python
print(int('EB9', 16)) # 3769
```


### Algorithm

```python
def toDecimal(num: str, base: int) -> int:
    result = 0
    power = 0

    for i in range(len(num) - 1, -1, -1):
        if num[i].isdigit():
            result += int(num[i]) * base ** power
        else:
            result += (ord(num[i]) - ord('A') + 10) * base ** power

        power += 1

    return result
```



## Conclusion

Understanding the conversion between different numerical bases is fundamental in computer science. This knowledge not only allows us to comprehend how computers interpret and manipulate data, but it is also crucial for those who wish to delve deeper into algorithms and data structures, enabling the perception of optimization opportunities that are not possible with more conventional algorithms.


[Blog Post](https://nelsonbn.com/blog/base-conversion)