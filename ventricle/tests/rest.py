from ventricle import Ventricle

if __name__ == '__main__':
    app = Ventricle()

    @app.worker.task
    async def worker():
        print("hello from the task")

    @app.rest.get("/test")
    async def test():
        await worker()
        return {"hello": "world"}

    app.start(rest=True, schedular=True, worker=True)
