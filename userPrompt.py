# from datetime import datetime
#
#
# # prompt user for symbol
# def get_symbol():
#     symbol = input("Please enter a stock symbol: ").upper()
#     return symbol
#
#
# # prompt user for chart type
# def chart_type():
#     print("1. Bar")
#     print("2. Line")
#     try:
#         choice = int(input("Select a chart type: "))
#         if choice < 1 or choice > 2:
#             print("Please only select (1 or 2)")
#             return chart_type()
#         return choice
#     except ValueError:
#         print("Please enter the valid number")
#         return chart_type()
#
#
# def chart_type_selection():
#     chart_type_choice = chart_type()
#     if chart_type_choice == 1:
#         return "this is bar type"
#     elif chart_type_choice == 2:
#         return "this is line type"
#
#
# # prompt user for time series
# def time_series():
#     print("1. Intraday")
#     print("2. Daily")
#     print("3. Weekly")
#     print("4. Monthly")
#
#     try:
#         choice = int(input("Please choose a time series (1-4): "))
#         if choice < 1 or choice > 4:
#             print("Please only select from 1-4")
#             return time_series()
#         return choice
#     except ValueError:
#         print("Please enter the valid number")
#         return time_series()
#
#
# def time_series_selection():
#     choice = time_series()
#
#     if choice == 1:
#         return "TIME_SERIES_INTRADAY"
#     elif choice == 2:
#         return "TIME_SERIES_DAILY"
#     elif choice == 3:
#         return "TIME_SERIES_Weekly"
#     elif choice == 4:
#         return "TIME_SERIES_Monthly"
#
#
# # prompt user for start date
# def get_start_date():
#     start_date = str(input("Enter the start date(YYYY-MM-DD): "))
#     valid_date = check_date_format(start_date)
#     if not valid_date:
#         print("Please enter the date in valid format(YYYY-MM-DD)")
#         return get_start_date()
#     return start_date
#
#
# # prompt user for end date and check if end date is less than start date
# def get_end_date(start_date):
#     end_date = str(input("Enter the end date(YYYY-MM-DD): "))
#     valid_date = check_date_format(end_date)
#     if valid_date:
#         if end_date < start_date:
#             print("End date cannot be less than start date")
#             return get_end_date(start_date)
#         return end_date
#     else:
#         print("Please enter the date in valid format(YYYY-MM-DD)")
#         return get_end_date(start_date)
#
#
# # check date format
# def check_date_format(date):
#     try:
#         if len(date) == 10:
#             datetime.strptime(date, "%Y-%m-%d")
#             return True
#         return False
#     except ValueError:
#         return False
