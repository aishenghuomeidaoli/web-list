# _*_ coding: utf-8 _*_
from weblist import create_app, config

app = create_app()

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
