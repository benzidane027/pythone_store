class support():
    def __init__(self):
        self.update_Status=None
        self.aboutUs=""
        self.version="V 1.0"
    def check_for_update(self):
        self.update_Status=False
        return False
    def about(self):
        return "hell this program create by \nbenzidane27@gmail.com don't copy or \nshare this softwar without permition"
if __name__ == "__main__":
    a=support()
    print(a.version)
            