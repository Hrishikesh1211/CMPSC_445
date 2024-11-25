import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QFrame
)
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class StockPredictorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Predictor")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Chart section
        chart_layout = QVBoxLayout()
        chart_label = QLabel("This Month's Prediction (Stock: AAPL)")
        chart_label.setAlignment(Qt.AlignCenter)
        chart_layout.addWidget(chart_label)

        # Create a line chart
        chart = QChart()
        chart.setTitle("Stock Prediction Chart")
        line_series = QLineSeries()
        data_points = [(1, 800), (2, 900), (3, 1200), (4, 1000), (5, 700), (6, 900)]
        for x, y in data_points:
            line_series.append(x, y)
        chart.addSeries(line_series)
        chart.createDefaultAxes()
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_layout.addWidget(chart_view)

        main_layout.addLayout(chart_layout)

        # Prediction data
        prediction_layout = QHBoxLayout()
        peak_label = QLabel("Time of Peak: 12/15/2024\nValue of Peak: $1219.87")
        valley_label = QLabel("Time of Valley: 12/28/2024\nValue of Valley: $683.51")
        avg_label = QLabel("Predicted Average: $922.21")
        prediction_layout.addWidget(peak_label)
        prediction_layout.addWidget(valley_label)
        prediction_layout.addWidget(avg_label)

        main_layout.addLayout(prediction_layout)

        # News and sentiment section
        news_layout = QVBoxLayout()
        news_label = QLabel("Today's News (Average Sentiment Value: +89%)")
        news_label.setAlignment(Qt.AlignCenter)
        news_layout.addWidget(news_label)

        news_table = QTableWidget(2, 2)
        news_table.setHorizontalHeaderLabels(["Article Title", "Sentiment Score"])
        news_table.setItem(0, 0, QTableWidgetItem("Steve Jobs hires 100,000 new employees"))
        news_table.setItem(0, 1, QTableWidgetItem("+93%"))
        news_table.setItem(1, 0, QTableWidgetItem("Customer outrage at iPhone 19 not having 3D cameras"))
        news_table.setItem(1, 1, QTableWidgetItem("-5%"))
        news_layout.addWidget(news_table)

        main_layout.addLayout(news_layout)

        # Finalize layout
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockPredictorUI()
    window.show()
    sys.exit(app.exec_())
