from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QImage,
    QRadialGradient)
from PyQt5.QtWidgets import *
import sys
import webbrowser
from googleapiclient.discovery import build
import csv
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(631, 625)
        MainWindow.setStyleSheet(u"background-color:#383838; border-radius:10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(20,150,575,450)
        scroll_stylesheet = """
        QScrollBar:vertical{
        background:#383838;
        width:15px;
        border:1px transparent #383838;
        border-radius:4px;}
        QScrollBar::handle:vertical{
        background: #e0dcdc;
        min-height:5px;
        border-radius:6px;}
        QScrollBar::sub-line:vertical{
        height:10px;
        width:10px;}
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
        background:#383838;}
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{
        background:#383838;}"""
        self.scrollArea.setStyleSheet(scroll_stylesheet)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 549, 459))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 531, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        font = QFont()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.search_frame = QFrame(self.centralwidget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setGeometry(QRect(130, 40, 361, 61))
        self.search_frame.setStyleSheet(u"#search_frame{\n"
        "border: 6px solid white;\n"
        "border-radius: 30px;\n"
        "background: #D9D9D9;\n"
        "}\n"
        "#search_frame QPushButton{\n"
        "padding: 5px 5px;\n"
        "border:none;\n"
        "background: #D9D9D9;\n"
        "}\n"
        "#search_frame QPushButton::pressed{\n"
        "padding-top:10px;\n"
        "padding-right:10px;}\n"
        "#search_frame QLineEdit{\n"
        "border:none;\n"
        "background: #D9D9D9;}\n"
        "")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.search_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.search_frame)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(r'search.png')
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.clicked.connect(self.search_clicked)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 631, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.horizontalLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.pushButton_13 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setMinimumSize(QSize(10, 0))
        self.pushButton_13.setMaximumSize(QSize(40, 16777215))
        font2 = QFont()
        font2.setFamily(u"Arial Rounded MT Bold")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"color:white;}\n"
"QPushButton::pressed{\n"
"padding-bottom:4px;\n"
"padding-right:2px;}")
        self.horizontalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_12 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(40, 16777215))
        font3 = QFont()
        font3.setFamily(u"Arial ")
        font3.setBold(False)
        font3.setPointSize(10)
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setStyleSheet(u"QPushButton{border:none;\n"
"color:white;\n"
"padding-top:4px;}\n"
"QPushButton::pressed{\n"
"padding-bottom:2px;\n"
"padding-right:2px;}")

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton.setText("")
        self.label_21.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"X", None))
    def search_clicked(self):
        search_text = self.lineEdit.text()
        sia = SentimentIntensityAnalyzer()
        api_key = '' #Mention Your own Google API Key
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_details = {}
        request = youtube.search().list(                              
        part = 'Id, snippet',
        type = 'video',
        q = str(search_text),
        videoDuration='long',
        videoDefinition = 'high',
        maxResults = 5,
        fields = "nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description,thumbnails))")
        response = request.execute()
        data = [['id', 'VideoId','Title', 'Description', 'Emotion scale']]
        for i in range(5):
            text = ""
            text += 'Title: ' + str(response['items'][i]['snippet']['title']) + '. Description: ' + str(response['items'][i]['snippet']['description'])
            translated = GoogleTranslator(source = 'auto', target = 'en').translate(str(text))
            sentiment = sia.polarity_scores(translated)
            compound = sentiment['compound']
            if(compound>=0.05): sentiment_type = 'Positive'
            elif(compound<=-0.05): sentiment_type = 'Negative'
            else: sentiment_type = 'Neutral'
            if(compound >= 0.05 or compound <= -0.05):
                a = abs(compound) - 0.0499
                res = int((a/0.96)*100)
                sentiment_type += '\n' + str(res) + '%'
            temp = [(i+1),response['items'][i]['id']['videoId'],response['items'][i]['snippet']['title'],response['items'][i]['snippet']['description'],response['items'][i]['snippet']['thumbnails']['high']['url'], sentiment_type]
            data.append(temp)
        with open(r'data1.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        with open(r'data1.csv', 'r',encoding='utf-8' ) as csv_f:
            reader = csv.reader(csv_f)
            csv_list = list(reader)
            self.pushbutton_det = {}
            for i in range(1,4):
                self.frame_4 = QFrame(self.verticalLayoutWidget)
                self.frame_4.setObjectName(u"frame_4")
                self.frame_4.setFixedSize(QSize(521, 121))
                self.frame_4.setFixedHeight(121)
                self.frame_4.setStyleSheet(u"QFrame{\n"
        "background-color: #1E1D1D;\n"
        "border-radius: 5px;}")
                self.frame_4.setFrameShape(QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QFrame.Raised)
                self.label_17 = QLabel(self.frame_4)
                self.label_17.setObjectName(u"label_17")
                self.label_17.setGeometry(QRect(20, 20, 111, 81))
                self.label_17.setStyleSheet(u"QLabel{\n"
                "background: #ffffff;\n"
                "border-radius: 5px;}")
                url_image = str(csv_list[i][4])
                image = QImage()
                image.loadFromData(requests.get(url_image).content)
                self.label_17.setPixmap(QPixmap(image))
                self.label_17.setScaledContents(True)
                self.label_17.setStyleSheet('border-radius:5px;')
                self.pushbutton_det['button' + str(i)] = QPushButton(self.frame_4)
                title_str = str(csv_list[i][2])
                self.pushbutton_det['button' + str(i)].setText(str(title_str[:28]) + ' \n'+ title_str[28:56]+ '\n' + title_str[56:])
                print(str(csv_list[i][2]))
                self.pushbutton_det['button' + str(i)].setObjectName(u"pushButton_10")
                self.pushbutton_det['button' + str(i)].setGeometry(QRect(150, 20, 281, 71))
                self.pushbutton_det['button' + str(i)].clicked.connect(lambda: self.on_button(i))
                self.video_id = str(csv_list[i][1])
                font = QFont()
                font.setFamily(u"Segoe UI")
                font.setBold(True)
                font.setWeight(75)
                self.pushbutton_det['button' + str(i)].setFont(font)
                self.pushbutton_det['button' + str(i)].setStyleSheet(u"background-color: #1E1D1D;\n"
                "border:none;\n"
                "color:white;\n"
                "font-size:15px;\n"
                "text-align:left;")
                self.label_18 = QLabel(self.frame_4)
                self.label_18.setText(str(csv_list[i][5]))
                self.label_18.setObjectName(u"label_18")
                self.label_18.setGeometry(QRect(420, 10, 91, 71))
                self.label_18.setFont(font)
                self.label_18.setStyleSheet(u"color:yellow;\n"
                "font-size: 15px;\n"
                "text-align: center;")
                if('Positive' in str(csv_list[i][5])): self.label_18.setStyleSheet("color:green;")
                elif('Negative' in str(csv_list[i][5])): self.label_18.setStyleSheet("color:red;")
                self.label_18.setAlignment(Qt.AlignCenter)
                self.verticalLayout.addWidget(self.frame_4)
    def on_button(self, i):
        url = 'https://www.youtube.com/watch?v=' + self.video_id
        webbrowser.open(url)
        print(str(i))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())