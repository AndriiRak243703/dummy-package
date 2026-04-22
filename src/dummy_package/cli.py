import typer
from .smart_predict import predict_next

app = typer.Typer()

@app.command()
def predict(numbers: str):
    number_list = [float(n) for n in numbers.split(",")]
    result = predict_next(number_list)
    typer.echo(f"Next predicted value: {result}")

if __name__ == "__main__":
    app()