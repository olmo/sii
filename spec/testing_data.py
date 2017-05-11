# -*- coding: utf-8 -*-


class Period:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self, partner_id):
        self.partner_id = partner_id


class Partner:
    def __init__(self, name, nif):
        self.name = name
        self.vat = nif


class Tax:
    def __init__(self, amount):
        self.amount = amount


class InvoiceLineTaxes:
    def __init__(self, name, base, tax_amount, tax_id):
        self.name = name
        self.base = base  # base imponible
        self.tax_amount = tax_amount
        self.tax_id = tax_id


class Invoice:

    def __init__(self, description, number, type, partner_id, company_id,
                 amount_total, period_id, date_invoice, tax_line):
        self.name = description
        self.number = number
        self.type = type
        self.partner_id = partner_id
        self.company_id = company_id
        self.period_id = period_id
        self.amount_total = amount_total
        self.date_invoice = date_invoice
        self.tax_line = tax_line


class DataGenerator:
    def __init__(self):
        self.period = Period(name='03/2016')
        self.tax_ibi = Tax(amount=0.15)
        self.tax_iva = Tax(amount=0.21)
        self.tax_line = [
            InvoiceLineTaxes(
                name='IVA 21%', base=1000, tax_amount=210, tax_id=self.tax_iva
            ),
            InvoiceLineTaxes(
                name='IBI 15%', base=1000, tax_amount=150, tax_id=self.tax_ibi
            )
        ]
        self.partner_invoice = Partner(name='Francisco García', nif='12345678T')
        self.partner_company = Partner(
            name='Compañía Eléctrica S.A.', nif='55555555T'
        )
        self.company = Company(partner_id=self.partner_company)

        self.invoice_number = 'F012345'
        self.date_invoice = '2016-03-25'
        self.amount_total = 15

    def get_in_invoice(self):
        invoice = Invoice(
            type='in_invoice',
            description='Factura recibida',
            number=self.invoice_number,
            partner_id=self.partner_invoice,
            company_id=self.company,
            amount_total=self.amount_total,
            period_id=self.period,
            date_invoice=self.date_invoice,
            tax_line=self.tax_line
        )
        return invoice

    def get_out_invoice(self):
        invoice = Invoice(
            type='out_invoice',
            description='Factura emitida',
            number=self.invoice_number,
            partner_id=self.partner_invoice,
            company_id=self.company,
            amount_total=self.amount_total,
            period_id=self.period,
            date_invoice=self.date_invoice,
            tax_line=self.tax_line
        )
        return invoice

    def get_in_refund_invoice(self):
        invoice = Invoice(
            type='in_refund',
            description='Factura rectificativa recibida',
            number=self.invoice_number,
            partner_id=self.partner_invoice,
            company_id=self.company,
            amount_total=self.amount_total,
            period_id=self.period,
            date_invoice=self.date_invoice,
            tax_line=self.tax_line
        )
        return invoice

    def get_out_refund_invoice(self):
        invoice = Invoice(
            type='out_refund',
            description='Factura rectificativa emitida',
            number=self.invoice_number,
            partner_id=self.partner_invoice,
            company_id=self.company,
            amount_total=self.amount_total,
            period_id=self.period,
            date_invoice=self.date_invoice,
            tax_line=self.tax_line
        )
        return invoice