
# install ipdb
# python -m unittest discover -s tests
# verbose python -m unittest discover -s tests -v



class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second == 0:
            return "0으로 나눌 수 없습니다."
        return self.first / self.second
    
    def mod(self):
        return self.first % self.second