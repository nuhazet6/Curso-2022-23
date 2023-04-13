FIRST_YEAR = 1900
LAST_YEAR = 2050


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.day = day
        self.month = month
        self.year = year
        if FIRST_YEAR > year > LAST_YEAR:
            self.year = FIRST_YEAR
        if 0 > self.month > 12:
            self.month = 1

    @staticmethod
    def is_leap_year(year) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @property
    def days_in_month(self) -> int:
        if self.month == 2:
            return 28 + self.is_leap_year(self.year)
        DAYS_IN_MONTH_ODD_EVEN = [30, 31]
        is_month_second_part = self.month > 7
        if is_month_second_part:
            return DAYS_IN_MONTH_ODD_EVEN[(self.month - 7) % 2]
        return DAYS_IN_MONTH_ODD_EVEN[self.month % 2]

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        total_days = 0
        for i in range(FIRST_YEAR, self.year):
            if self.is_leap_year(i):
                total_days += 366
            else:
                total_days += 365

        return total_days

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        pass

    def is_weekend(self) -> bool:
        pass

    def short_date(self) -> str:
        """02/09/2003"""
        pass

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        pass

    def __sub__(self, other):
        if self.year > other.year:
            lower = other
            upper = self
        else:
            lower = self
            upper = other
        new_year = upper.year - lower.year
        new_month = 12 - lower.month + upper.month
        new_days = lower.days_in_month() - lower.days + upper.days_in_month
        return

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


fecha1 = Date(1, 1, 1901)
fecha2 = Date(30, 2, 2020)
print(Date.is_leap_year(fecha1.year), Date.is_leap_year(fecha2.year))
print(fecha1.delta_days())
