import config 
from  app import app

if __name__ == "__main__":
	app.run(host=config.url['HOST'], port=config.url['PORT'])
