from PyQt4 import QtGui
from models.Data import list_of_subjects
from customWidgets.TestWidget import TestWidget
import interfaces.TakeTestScreen as TakeTestScreen

class Screen(QtGui.QWidget):
    def __init__(self, callScreen, subject):
        super(Screen, self).__init__()
        self.callScreen = callScreen 
        self.subject = subject 
        self.initUI()
    
    def initUI(self):
        
        while (self.callScreen.layout.count()>0):
            widget = self.callScreen.layout.itemAt(0).widget()
            if(widget):
                self.callScreen.layout.removeWidget(widget)
                widget.setParent(None)
                widget.deleteLater()
        self.callScreen.layout.insertWidget(0, self)
        
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.ScrollArea = QtGui.QScrollArea()
        self.layout.addWidget(self.ScrollArea)
        self.Wrapper = QtGui.QWidget()
        self.Wrapper.layout = QtGui.QVBoxLayout()
        self.Wrapper.setLayout(self.Wrapper.layout)
        self.Wrapper.layout.setContentsMargins(10, 5, 5, 5)

        self.Wrapper.Label = QtGui.QLabel("User Account")
        self.Wrapper.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: #2A7640; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.Label)
        self.Wrapper.welcome = QtGui.QLabel("WELCOME " + str(self.callScreen.user.userName) + " !")
        self.Wrapper.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: #6648B0; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.welcome)
        self.Wrapper.subject = QtGui.QLabel(str(self.subject.subjectName))
        self.Wrapper.subject.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: #6648B0; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.subject)

        self.Wrapper.Label1 = QtGui.QLabel("List Of Tests : ")
        self.Wrapper.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                    color : #9A48B0;
                    font-weight: bold;
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.Label1)

        for test in self.subject.tests :
            widget = TestWidget(test, self.onTestWidgetNotification)
            self.Wrapper.layout.addWidget(widget)


        self.ScrollArea.setWidget(self.Wrapper)

    def onTestWidgetNotification(self, subject):
        TakeTestScreen.Screen(self, subject)