from webnetlab import init_app


app = init_app()


if __name__ == "__main__":
    app.run(
        host=app.config.server_ip,
        port=app.config.server_port,
        debug=app.config.debug_mode,
    )
