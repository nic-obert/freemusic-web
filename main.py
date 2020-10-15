from frontend import api


if __name__ == "__main__":

    # start web app
    api.app.run(debug=True, host='127.0.0.1')
