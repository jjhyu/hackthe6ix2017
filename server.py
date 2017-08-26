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
        recipe_id = self.get_arguments("rid")
        print(recipe_id)
        array = [{"recipe" : "1"},{"recipe" : 2.5}]
        json_array = json.dumps(array)
        self.write(json_array)

def make_app():
    return tornado.web.Application([(r"/", MainHandler),
                                    (r"/recipes", FetchAllRecipesHandler),])

if __name__=="__main__":
    app = make_app()
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()