def close_btn(self):
    """ 
    Quits the application

    Also closes all the file descriptors that remain open
    """
    quitButton = QPushButton("Quit")
    quitButton.clicked.connect(app.quit)

    def open_btn(self):
        pass

    def saveAs_btn(self):
        #dir = "."

        #fileObj = QFileDialog.getSaveFileName(self, self.__appname__, \
                #dir=dir)

        ##self.plainTextEdit.selectAll()
        ##contents = self.plainTextEdit.copy()

        #fileName = fileObj[0]
        #self.fd1 = open(fileName, mode="w")
        #self.fd1.write(contents)
        ##self.fd1.close()

        #print "finished the save_btn function"
        pass

    def save_btn(self):
        # Checks weather a file descriptor is already open
        try: 
            self.plainTextEdit.selectAll()
            contents = self.plainTextEdit.copy()
            self.fd1.write(contents)
        except NameError:
            self.saveAs_btn()

