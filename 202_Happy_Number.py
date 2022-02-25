"""
Проверка, является ли число счастливым. Счастливое число, это число, определённое следующим процессом: 
начиная с любого положительного целого числа, мы заменяем это число суммой квадратов его цифр в десятичной
системе счисления и повторяем данный процесс, пока число либо не станет равно 1 (где весь процесс остановится),
или попадёт в бесконечный цикл, не содержащий 1.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Решение "в лоб".
        """
        sq_sum, it = 0, 0
        while n != 1:
            while n > 0:
                sq_sum += (n % 10)**2
                n //= 10
            n = sq_sum
            sq_sum = 0
            it += 1
            if it == 8:
                return False
        return True
      
    def isHappy(self, n: int) -> bool:
        """
        Классическое для подобного класса задач решение черепашкой.
        Берём быстрый и медленный указатель и если в какой-то момент они совпадут,
        значит мы попали в цикл и это число не является счастливым.
         s     f
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
               s           f
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
                     s                f
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
                           s                       f
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
         f                       s               
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
                     f                 s               
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
                                f            s               
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
                                             f     s               
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
                                                        f/s               
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        """
        def squared(n):
            result = 0
            while n > 0:
                last = n % 0
                result += last * last
                n = n // 10
            return result
        slow = squared(n)
        fast = squared(squared(n))
        while slow!=fast and fast!=1:
            slow = squared(slow)
            fast = squared(squared(fast))
        return fast==1
