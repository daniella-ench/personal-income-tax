# NAME: ENE CHIAMAKA DANIELLA
# MATRIC NO: BU24SEN1037
# COURSE: COS201
# PROGRAM: PERSONAL INCOME TAX CALCULATOR (2009)

while True:
    try:
        status = int(input(
            "Choose filing status:\n"
            "0 - Single\n"
            "1 - Married Filing Jointly / Widow(er)\n"
            "2 - Married Filing Separately\n"
            "3 - Head of Household\n"
            "Enter choice: "
        ))

        income = float(input("Enter taxable income: "))

        if income < 0:
            print("Error: income cannot be negative.\n")
            continue

        if status not in (0, 1, 2, 3):
            print("Error: invalid filing status.\n")
            continue

        tax_due = 0.0
        remaining_income = income

        # ---------- SINGLE ----------
        if status == 0:
            if remaining_income > 372950:
                tax_due += (remaining_income - 372950) * 0.35
                remaining_income = 372950
            if remaining_income > 171550:
                tax_due += (remaining_income - 171550) * 0.33
                remaining_income = 171550
            if remaining_income > 82250:
                tax_due += (remaining_income - 82250) * 0.28
                remaining_income = 82250
            if remaining_income > 33950:
                tax_due += (remaining_income - 33950) * 0.25
                remaining_income = 33950
            if remaining_income > 8350:
                tax_due += (remaining_income - 8350) * 0.15
                remaining_income = 8350
            tax_due += remaining_income * 0.10

        # ---------- MARRIED JOINT ----------
        elif status == 1:
            if remaining_income > 372950:
                tax_due += (remaining_income - 372950) * 0.35
                remaining_income = 372950
            if remaining_income > 208850:
                tax_due += (remaining_income - 208850) * 0.33
                remaining_income = 208850
            if remaining_income > 137050:
                tax_due += (remaining_income - 137050) * 0.28
                remaining_income = 137050
            if remaining_income > 67900:
                tax_due += (remaining_income - 67900) * 0.25
                remaining_income = 67900
            if remaining_income > 16700:
                tax_due += (remaining_income - 16700) * 0.15
                remaining_income = 16700
            tax_due += remaining_income * 0.10

        # ---------- MARRIED SEPARATE ----------
        elif status == 2:
            if remaining_income > 186475:
                tax_due += (remaining_income - 186475) * 0.35
                remaining_income = 186475
            if remaining_income > 104425:
                tax_due += (remaining_income - 104425) * 0.33
                remaining_income = 104425
            if remaining_income > 68525:
                tax_due += (remaining_income - 68525) * 0.28
                remaining_income = 68525
            if remaining_income > 33950:
                tax_due += (remaining_income - 33950) * 0.25
                remaining_income = 33950
            if remaining_income > 8350:
                tax_due += (remaining_income - 8350) * 0.15
                remaining_income = 8350
            tax_due += remaining_income * 0.10

        # ---------- HEAD OF HOUSEHOLD ----------
        elif status == 3:
            if remaining_income > 372950:
                tax_due += (remaining_income - 372950) * 0.35
                remaining_income = 372950
            if remaining_income > 190200:
                tax_due += (remaining_income - 190200) * 0.33
                remaining_income = 190200
            if remaining_income > 117450:
                tax_due += (remaining_income - 117450) * 0.28
                remaining_income = 117450
            if remaining_income > 45500:
                tax_due += (remaining_income - 45500) * 0.25
                remaining_income = 45500
            if remaining_income > 11950:
                tax_due += (remaining_income - 11950) * 0.15
                remaining_income = 11950
            tax_due += remaining_income * 0.10

        print(f"\nTotal tax owed: ${tax_due:.2f}")
        break

    except ValueError:
        print("Error: please enter valid numeric values.\n")
