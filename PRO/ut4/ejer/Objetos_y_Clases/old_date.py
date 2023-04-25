FIRST_YEAR_VALID = 1900
LAST_YEAR_VALID = 2050
WEEKDAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
WEEKEND = [WEEKDAYS.index("sábado"), WEEKDAYS.index("domingo")]
MONTHS = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}


class Date:
    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.year = (
            year if FIRST_YEAR_VALID < year < LAST_YEAR_VALID else FIRST_YEAR_VALID
        )
        self.month = month if month in MONTHS else 1
        self.day = day if self.days_in_month(self.year, self.month) >= day > 0 else 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        if month == 2:
            return 28 + Date.is_leap_year(year)
        DAYS_IN_MONTH_ODD_EVEN = [30, 31]
        is_month_second_part = month > 7
        if is_month_second_part:
            return DAYS_IN_MONTH_ODD_EVEN[(month - 7) % 2]
        return DAYS_IN_MONTH_ODD_EVEN[month % 2]

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        total_days = 0
        for i in range(FIRST_YEAR_VALID, self.year):
            if self.is_leap_year(i):
                total_days += 366
            else:
                total_days += 365
        for i in range(1, self.month):
            total_days += self.days_in_month(self.year, i)
        total_days += (
            self.day - 1
        )  # Se tiene que restar 1 porque si no se contaría a sí mismo y tendríamos un día de más
        return total_days

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue lunes."""
        return self.delta_days() % 7 + WEEKDAYS.index("lunes")

    def is_weekend(self) -> bool:
        return self.weekday() in WEEKEND

    def short_date(self) -> str:
        """02/09/2003"""
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        weekday = WEEKDAYS[self.weekday()]
        month = MONTHS[self.month]
        return f"{weekday} {self.day} de {month} de {self.year}"

    def __add__(self, days: int):
        """ """
        new_year = self.year
        new_month = self.month
        new_day = self.day

        # leap_year = self.year
        # if self.month > 2:
        #     leap_year += 1
        # if self.is_leap_year(leap_year):
        #     days -= 1
        #     if days < 365:
        #         new_day += 1
        # while leap_year < (self.year + 9) or days >= 365:
        #     if self.is_leap_year(leap_year):
        #         break
        #     days-= 365
        #     new_year += 1
        #     leap_year += 1
        # years_to_add,days = divmod(days,365)
        # days -= years_to_add // 4
        # new_year += years_to_add

        if self.month > 2:
            target_year = new_year + 1
        else:
            target_year = new_year
        while days >= 365 + self.is_leap_year(target_year):
            days_in_current_year = 365 + self.is_leap_year(target_year)
            days -= days_in_current_year
            new_year += 1
            target_year += 1

        while days > (self.days_in_month(new_year, new_month) - new_day):
            days -= self.days_in_month(new_year, new_month)
            new_month += 1
            if new_month == 13:
                new_month = 1
                new_year += 1
        new_day += days
        return Date(new_day, new_month, new_year)

    def __sub__(self, other):
        if isinstance(other, Date):
            return abs(self.delta_days() - other.delta_days())
        if isinstance(other, int):  # ó else
            new_year = self.year
            if self.month <= 2:
                target_year = new_year - 1
            else:
                target_year = new_year
            while other >= 365 + self.is_leap_year(target_year):
                other -= 365 + self.is_leap_year(target_year)
                new_year -= 1
                target_year -= 1

            new_month = self.month
            target_month = new_month - 1
            target_year = new_year
            if target_month <= 0:
                target_month = 12
                target_year = new_year - 1
            while other >= self.days_in_month(target_year, target_month):
                other -= self.days_in_month(target_year, target_month)
                new_month -= 1
                target_month -= 1
                if new_month <= 0:
                    new_month = 12
                    new_year -= 1
                if target_month <= 0:
                    target_month = 12
                    target_year -= 1

            new_day = self.day - other
            if new_day <= 0 and new_year > FIRST_YEAR_VALID:
                new_day = self.days_in_month(target_year, target_month) + new_day
                new_month = target_month
                if new_month == 12:
                    new_year = target_year
            return Date(new_day, new_month, new_year)

    def __eq__(self, other) -> bool:
        are_years_eq = self.year == other.year
        are_months_eq = self.month == other.month
        are_days_eq = self.day == other.day
        return all([are_years_eq, are_months_eq, are_days_eq])

    def __gt__(self, other) -> bool:
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    def __ge__(self, other) -> bool:
        if self > other or self == other:
            return True
        return False

    

    def __lt__(self, other) -> bool:
        if self >= other:
            return False
        return True

    def __le__(self, other) -> bool:
        if self < other or self == other:
            return True
        return False

    # operador + suma días a la fecha
    # operador - resta días a la fecha o calcula la diferencia entre dos fechas
    # operador == dice si dos fechas son iguales
    # operador > dice si una fecha es mayor que otra
    # operador < dice si una fecha es menor que otra


fecha1 = Date(1, 1, 1904)
print(fecha1)
fecha2 = Date(1, 2, 1903)
print(fecha2)
fecha4 = Date(9999, 9999, 99999)
print(fecha4)
print(Date.is_leap_year(fecha1.year), Date.is_leap_year(fecha2.year))
print(fecha1.delta_days(), fecha2.delta_days())
print(fecha1 - fecha2)
fecha3 = fecha1 + 365
print(fecha3)
print(fecha1.weekday())
print(fecha1 - 365)
print(fecha2 > fecha4)
print(fecha2 >= fecha4)
print(fecha2 < fecha4)
print(fecha2 <= fecha4)
print(fecha1.short_date())
