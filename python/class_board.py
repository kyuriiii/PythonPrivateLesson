class Board:
    articles = []
     
    def print_welcome_message(self):
        print("-------------------- Python 게시판 ---------------------")
     
    def print_menu(self):
        print("""--------------------\n 1. List # 2. Search # 3. Read # 4. Delete # 5. Write # 0. Quit \n--------------------""")  
     
    def input_menu(self):
        id = input("Menu : ")
        return int(id)
         
    def print_all_articles(self):
        if len(self.articles) == 0:
            print("게시판 목록이 없습니다.")
            return
         
        for artcl in self.articles:
            self.print_article(artcl)
     
    def print_article(self, article):
        print()
        print("Title : " + article["title"] + ", Read : " + str(article["read"]))
     
    def search_article(self):
        search_keyword = input("Input search keyword : ")
         
        for artcl in self.articles:
            if search_keyword in artcl["title"]:
                self.print_article(artcl)
                     
    def read_article(self):
        id = input("게시글 Index : ")
        id = int(id)
         
        if len(self.articles) - 1 < id:
            print(id, " 의 글이 없습니다.'")
        else:
            self.articles[id]["read"] += 1
            self.print_article(self.articles[id])
     
    def delete_article(self):
        id = input("삭제할 게시글  Index : ")
        id = int(id)
         
        if len(self.articles) - 1 < id:
            print(id, " 의 글이 없습니다'")
        else:
            self.articles.pop(id)
     
    def write_article(self):
        title = input("제목 : ")
        article = {
            "title": title,
            "read": 0
        }
         
        self.articles.append(article)
     
    def run(self):
        self.print_welcome_message()
         
        while(True):
            self.print_menu()
            id = self.input_menu()
             
            if id == 1:
                self.print_all_articles()
            elif id == 2:
                self.search_article()
            elif id == 3:
                self.read_article()
            elif id == 4:
                self.delete_article()
            elif id == 5:
                self.write_article()
            elif id == 0:
                print("종료!")
                break
            print("")
             
def start_board_app():
    board = Board()
    board.run()
     
if __name__ == "__main__":
    start_board_app()
