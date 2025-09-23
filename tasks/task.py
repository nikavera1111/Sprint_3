import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items  
    
    @number_items.setter
    def number_items(self, value):
        self.__number_items = value

    @property
    def item_price(self):
        return self.__item_price
    
    @property
    def tax_rate(self):
        return self.__tax_rate

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name)>40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.item_price.keys():
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.name_items.append(name)
            self.number_items = self.number_items + 1

    def delete_item_from_check(self, name):
        if name not in self.name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.name_items.remove(name)
            self.number_items = self.number_items - 1

    def check_amount(self):
        total = [] 
        for item in self.name_items:
            item_price = self.item_price.get(item)
            if item_price:
                total.append(item_price)
        total_price = sum(total)
        if len(total) > 10:
            total_price = total_price * 0.9
        return total_price
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.name_items:
            if self.tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                total.append(self.item_price.get(item))
        total_tax = sum(total) * 0.2
        if len(self.name_items) > 10:
            total_tax = total_tax * 0.9
        return total_tax
        

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.name_items:
            if  self.tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
                total.append(self.item_price.get(item))
        total_tax = sum(total) * 0.1
        if len(self.name_items) > 10:
            total_tax = total_tax * 0.9
        return total_tax
    
    def total_tax(self):
        total_tax = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return total_tax
    
    @staticmethod
    def get_telephone_number(telephone_number):
        telephone_number = str(telephone_number)
        try:
            int(telephone_number)
        except Exception:
            raise ValueError ('Необходимо ввести цифры')
        if len(telephone_number) > 10:
                raise ValueError ('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'
    