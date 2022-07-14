
import pygal
import datetime

class ChartMaker:

    """
    Class Maker Handles The Creation Of The Chart
    @params
    opens = array of every opening stock value
    closes= array of every ending stock value
    highs = array of highest values for each day
    lows = array of lowest values for each day
    dates = array of date objects 

    
    """
    def __init__(self, opens, closes, highs, lows, company_name, dates, end_date):
        self.opens = opens
        self.closes = closes
        self.highs = highs
        self.lows = lows
        self.company_name = company_name
        self.dates = dates
    def render_chart(self):
        line_chart = pygal.Line()
        line_chart.title = f"Stock data for {self.company_name} from {self.get_start_date} to {self.get_end_date} "
        line_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), self.dates)
        line_chart.add("Highs", self.highs)
        line_chart.add("Lows", self.lows)
        line_chart.add("Close", self.closes)
        line_chart.add("Open", self.opens)
        line_chart.render()
    def get_start_date(self):
        return self.dates[0].strftime('%Y-%m-%d')
    def get_end_date(self):
        return self.dates[len(self.dates) - 1].strftime('%Y-%m-%d')