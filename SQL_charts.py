from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QComboBox, QFrame, QListWidget, QHBoxLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextEdit, QLineEdit
from PyQt5 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import sqlite3


class IronMan(QMainWindow):
    def __init__(self):
        super(IronMan, self).__init__()
        uic.loadUi("extract.ui", self)

        # define content:
        self.head_label = self.findChild(QLabel, "head_label")
        self.label_3 = self.findChild(QLabel, "label_3")
        self.label_4 = self.findChild(QLabel, "label_4")
        self.label_5 = self.findChild(QLabel, "label_5")
        self.chart_label = self.findChild(QLabel, "chart_label")
        self.color_label = self.findChild(QLabel, "color_label")
        self.x_label = self.findChild(QLabel, "x_label")
        self.y_label = self.findChild(QLabel, "y_label")

        self.run_button = self.findChild(QPushButton, "run_button")
        self.display_button = self.findChild(QPushButton, "display_button")
        self.close_button = self.findChild(QPushButton, "close_button")
        self.show_button = self.findChild(QPushButton, "show_button")

        self.first_frame = self.findChild(QFrame, "first_frame")
        self.second_frame = self.findChild(QFrame, "second_frame")
        self.button_frame = self.findChild(QFrame, "button_frame")

        self.box_2 = self.findChild(QComboBox, "box_2")
        self.box_3 = self.findChild(QComboBox, "box_3")

        self.main_table = self.findChild(QTableWidget, "main_table")
        self.list_widget = self.findChild(QListWidget, "list_widget")

        self.text_edit = self.findChild(QTextEdit, "text_edit")
        self.x_line = self.findChild(QLineEdit, "x_line")
        self.y_line = self.findChild(QLineEdit, "y_line")

        # define chart layout:
        self.First_Layout = QHBoxLayout(self.second_frame)
        self.First_Layout.setObjectName("First_Layout")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.First_Layout.addWidget(self.diagramm)

        # variables:
        self.table_list = ["customers", "orders", "orderdetails", "products", "employees"]

        # call defined methods:
        self.close_button.clicked.connect(lambda: self.close())
        self.run_button.clicked.connect(self.Execute_Query)
        self.show_button.clicked.connect(self.show_tables)
        self.display_button.clicked.connect(self.draw_charts)
        
        self.show()

# ----------------------------------- logic ------------------------------------ #
    def Execute_Query(self):
        sql_query = self.text_edit.toPlainText()
        conn = sqlite3.connect("sales.db")
        curr = conn.cursor()

        try:
            main_list = []
            for item in curr.execute(f'''{sql_query}'''):
                main_list.append(list(item))
        except sqlite3.OperationalError:
            pass

        conn.commit()
        conn.close()
        
        # define columns: step_1
        start_position = sql_query.find("T") + 1
        end_position = sql_query.find("FROM")
        answer_1 = sql_query[start_position:end_position]
        # step_2
        answer_1 = answer_1.replace("\n", "")
        answer_2 = answer_1.split(",")
        for item in range(len(answer_2)):
            answer_2[item] = answer_2[item].split()
        # step_3
        table_columns = []
        for item in answer_2:
            table_columns.append(item[-1])

        # create DataFrame
        main_data = pd.DataFrame(main_list, columns = table_columns)

        RowNumber = len(main_data.index)
        ColumnNumber = len(main_data.columns)

        self.main_table.setColumnCount(ColumnNumber)
        self.main_table.setRowCount(RowNumber)
        self.main_table.setHorizontalHeaderLabels(main_data.columns)

        for rows in range(RowNumber):
            for columns in range(ColumnNumber):
                self.main_table.setItem(rows, columns, QTableWidgetItem(str(main_data.iat[rows, columns])))
        
        main_data.to_csv("yep.csv", index=False)
    
    # define method for show tables button:
    def show_tables(self):
        for item in self.table_list:
            self.list_widget.addItem(f"{item}")
        self.show_button.setEnabled(False)
    
    # define method to draw charts:
    def draw_charts(self):
        chart = self.box_2.currentText()
        x_column = self.x_line.text()
        y_column = self.y_line.text()
        color_type = self.box_3.currentText()
        self.figure.clear()
        df = pd.read_csv("yep.csv")
        # draw: scatter
        if chart == "Scatter":
            if x_column in df.columns and y_column in df.columns:
                sizes = pd.Series(df[f"{y_column}"]).to_numpy()
                colors_1 = sizes
                sizes_1 = sizes * 25
                plt.scatter(df[f"{x_column}"], df[f"{y_column}"], c=colors_1, s = sizes_1, alpha=0.7, cmap='nipy_spectral')
                plt.grid()
                plt.colorbar()
                self.diagramm.draw()
            else:
                None
        # draw: bar
        elif chart == "Bar":
            if x_column in df.columns and y_column in df.columns:
                plt.bar(df[f"{x_column}"], df[f"{y_column}"], color = f"{color_type}")
                plt.grid()
                self.figure.autofmt_xdate()
                self.diagramm.draw()
            else:
                None
        # draw: pie
        elif chart == "Pie":
            if x_column in df.columns and y_column in df.columns:
                my_labels = pd.Series(df[f"{x_column}"]).to_numpy()
                plt.pie(df[f"{y_column}"], labels = my_labels, startangle=90, shadow=True)
                self.diagramm.draw()
            else:
                None
        # draw: line
        elif chart == "Line":
            if x_column in df.columns and y_column in df.columns:
                first = pd.Series(df[f"{x_column}"])
                second = pd.Series(df[f"{y_column}"])
                plt.plot(first, color = "DarkSlateGray", marker = "^")
                plt.plot(second, color = "FireBrick", marker = "D")
                plt.grid()
                self.diagramm.draw()
                
            else:
                None
        

# ------------------------------------ end ------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    iron = IronMan()
    sys.exit(app.exec_())