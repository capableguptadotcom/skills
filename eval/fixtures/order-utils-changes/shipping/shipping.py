"""Shipping prices, in cents."""

import math
import os


DOMESTIC = "US"


def _is_domestic(country):
    if country == DOMESTIC:
        return True
    else:
        return False


def _round_up_kg(weight_kg):
    return math.ceil(weight_kg)


def shipping_cost(weight_kg, express=False, country="US"):
    """Price of one parcel. Express doubles the price."""
    cost = 0
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if _is_domestic(country) == True:
        if weight_kg <= 1:
            cost = 500
        else:
            if weight_kg <= 5:
                cost = 900
            else:
                cost = 900 + math.ceil(weight_kg - 5) * 150
    else:
        if weight_kg <= 1:
            cost = 1500
        else:
            if weight_kg <= 5:
                cost = 2500
            else:
                cost = 2500 + math.ceil(weight_kg - 5) * 400
    if express:
        cost = cost * 2
    else:
        cost = cost
    return cost
