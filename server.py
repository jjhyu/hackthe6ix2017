import tornado.ioloop
import tornado.web
import processRecipe
import json

db = [
    { }
]

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class FetchAllRecipesHandler(tornado.web.RequestHandler):
    def get(self):
        for recipe_id in ["1","2","3"]:
            print(recipe_id)
            self.write(processRecipe.processRecipe("testing_examples/recipe" + recipe_id +".txt"))
            self.write("\n")

def make_app():
    return tornado.web.Application([(r"/", MainHandler),
                                    (r"/recipes", FetchAllRecipesHandler),])

if __name__=="__main__":
    app = make_app()
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()