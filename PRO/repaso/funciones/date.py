from __future__ import annotations


class Date:
    FIRST_YEAR = 1900
    LAST_YEAR = 2050
    WEEKDAYS = ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado']
    WEEKEND_DAYS = ['Sábado','Domingo']
    MONTH_DAYS = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    MONTHS_NAMES = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        self.year = year if Date.FIRST_YEAR <= year <= Date.LAST_YEAR else Date.FIRST_YEAR       
        self.month = month if month in Date.MONTH_DAYS else 1
        self.day = day if 1 <= day <= Date.days_in_month(self.month,self.year) else 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        return Date.MONTH_DAYS[month] if month != 2 else Date.MONTH_DAYS[month] + Date.is_leap_year(year)

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        total_days = self.day -1
        for year in range(Date.FIRST_YEAR,self.year):
            total_days += 365 + Date.is_leap_year(year)
        for month in range(1,self.month):
            total_days += Date.days_in_month(month,self.year)
        return total_days

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        return (self.get_delta_days() + Date.WEEKDAYS.index('Lunes')) % 7

    @property
    def is_weekend(self) -> bool:
        return  Date.WEEKDAYS[self.weekday] in Date.WEEKEND_DAYS

    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        return f'{self.day:02.0f}/{self.month:02.0f}/{self.year}'

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        weekday = self.weekday
        return f'{Date.WEEKDAYS[weekday]} {self.day} DE {Date.MONTHS_NAMES[self.month-1]} DE {self.year}'.upper()

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        current_year = self.year
        while days >= 365 + Date.is_leap_year(current_year):
            days -= 365 + Date.is_leap_year(current_year)
            current_year += 1
        new_year = current_year

        current_month = self.month
        while days >= Date.days_in_month(current_month,new_year):
            days-= Date.days_in_month(current_month,new_year)
            current_month += 1
            if current_month > 12:
                current_month = 1
                new_year += 1
        new_month = current_month

        new_day = self.day + days
        if new_day > Date.days_in_month(new_month,new_year):
            new_day -= Date.days_in_month(new_month,new_year) 
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        return Date(new_day,new_month,new_year)



    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        if isinstance(other,int):
            current_year = self.year
            while other >= 365 + Date.is_leap_year(current_year):
                other -= 365 + Date.is_leap_year(current_year)
                current_year -= 1
            new_year = current_year

            current_month = self.month
            while other >= Date.days_in_month(current_month,new_year):
                other-= Date.days_in_month(current_month,new_year)
                current_month -= 1
                if current_month < 1:
                    current_month = 12
                    new_year -= 1
            new_month = current_month

            new_day = self.day - other
            if new_day < 1:
                new_month -= 1
                new_day += Date.days_in_month(new_month,new_year)                
                if new_month < 1:
                    new_month = 12
                    new_year -= 1
            return Date(new_day,new_month,new_year)
        else:
            return self.get_delta_days() - other.get_delta_days()

    def __lt__(self, other) -> bool:
        return self.get_delta_days() < other.get_delta_days()

    def __gt__(self, other) -> bool:
        return self.get_delta_days() > other.get_delta_days()

    def __eq__(self, other) -> bool:
        return self.get_delta_days() == other.get_delta_days()
