import config 
from  app import app

if __name == "__main__":
	app.run(host=config.url['HOST'], port=config.url['PORT'])
