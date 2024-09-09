from django.shortcuts import render
from django.http import JsonResponse

def candlestick_data(request):
    data = {
        "data": [
            {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
            {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
            # Add more data as needed
        ]
    }
    return JsonResponse(data)

def line_chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [12, 11, 25, 35, 14, 13, 10, 15, 16, 10, 18, 9],
    }
    return JsonResponse(data)


def bar_chart_data(request):
    data = {
        "labels": ["Product A", "Product B", "Product C", "Product D"],
        "data": [100, 150, 200, 125]
    }
    return JsonResponse(data)

def pie_chart_data(request):
    data = {
        "labels": ["linkedin", "facebook", "instagram"],
        "data": [20, 50, 30]
    }
    return JsonResponse(data)