#!/usr/bin/env python3
"""Illustrative, read-only AKE EP02 financial arithmetic; no real creator revenue verified."""
from decimal import Decimal as D

def model(gross=D('10000'),price=D('50'),days=D('30'),minutes=D('10'),rate=D('.029'),fixed=D('.30'),subscription=D('29')):
    assert gross >= 0 and price > 0 and gross % price == 0 and days > 0 and minutes > 0
    orders = int(gross / price)
    hours = days * minutes / D('60')
    processing = gross * rate + orders * fixed
    return {'hours': hours,'gross_per_claimed_hour': gross/hours,'orders':orders,
            'processing':processing,'subscription':subscription,
            'before_other_costs':gross-processing-subscription,
            'is_real_income_evidence':False}

def test():
    x=model()
    assert x['hours']==5
    assert x['gross_per_claimed_hour']==2000
    assert x['orders']==200
    assert x['processing']==350
    assert x['subscription']==29
    assert x['before_other_costs']==9621
    assert not x['is_real_income_evidence']
    assert model(price=D('25'))['processing']==410
    print('8 checks passed; all figures illustrative')

if __name__=='__main__':
    test()
    print(model())
